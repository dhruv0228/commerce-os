#!/usr/bin/env python3
"""Unit economics for every product scenario.

All margin, CAC and ROAS math for the business lives here. Agents write cost
inputs to data/economics_inputs.csv (one row per field, with a label and a
source) and run this script. They never do this arithmetic in prose.

Usage:
    python3 scripts/economics.py
    python3 scripts/economics.py --inputs examples/economics_example.csv --out /tmp/out.csv
"""
import argparse
import csv
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_IN = ROOT / "data" / "economics_inputs.csv"
DEFAULT_OUT = ROOT / "data" / "economics_outputs.csv"

LABELS = {"VERIFIED", "ESTIMATED", "ASSUMED", "UNKNOWN"}

# Every scenario needs all of these. Percentages are written as decimals (0.029 = 2.9%).
REQUIRED = [
    "price",             # retail price per order, before discount
    "discount_pct",      # average discount given, 0 if none
    "product_cost",      # unit cost from the supplier
    "supplier_shipping", # supplier's shipping charge to a US customer
    "duties_other",      # duties, tariffs and other landed costs, 0 if none
    "packaging",         # inserts or branded packaging per order, 0 if none
    "fulfillment_fee",   # per-order fee charged by the supplier or 3PL, 0 if none
    "payment_pct",       # payment processing rate
    "payment_fixed",     # payment processing fixed fee per order
    "refund_pct",        # refund and return allowance as a share of revenue
    "benchmark_cpa",     # sourced category cost per purchase, for the cushion test
]

TARGET_SHARE = 0.75          # target CAC = 75% of break-even CAC (house rule)
CPA_MULTIPLIERS = {"good": 0.75, "benchmark": 1.0, "tough": 1.3}


def load_inputs(path):
    """Read long-format rows into {(product_id, scenario): {field: row}}."""
    data = {}
    with open(path, newline="", encoding="utf-8") as f:
        for i, row in enumerate(csv.DictReader(f), start=2):
            if not row.get("product_id"):
                continue
            label = (row.get("label") or "").strip().upper()
            if label not in LABELS:
                sys.exit(f"{path}:{i}: label must be one of {sorted(LABELS)}, got {label!r}")
            field = row["field"].strip()
            if field not in REQUIRED:
                sys.exit(f"{path}:{i}: unknown field {field!r}. Allowed: {REQUIRED}")
            key = (row["product_id"].strip(), row["scenario"].strip().lower())
            data.setdefault(key, {})[field] = {
                "value": row.get("value", "").strip(),
                "label": label,
                "source": row.get("source", "").strip(),
            }
    return data


def compute(fields):
    """Return the economics for one scenario. fields maps name -> {value, label}."""
    missing = [f for f in REQUIRED if f not in fields or fields[f]["label"] == "UNKNOWN"
               or fields[f]["value"] == ""]
    labels = {fields[f]["label"] for f in fields}
    if missing:
        return {"status": "blocked", "missing_or_unknown": ";".join(missing)}

    v = {f: float(fields[f]["value"]) for f in REQUIRED}
    net_revenue = v["price"] * (1 - v["discount_pct"])
    payment = net_revenue * v["payment_pct"] + v["payment_fixed"]
    refund_cost = net_revenue * v["refund_pct"]
    variable_costs = (v["product_cost"] + v["supplier_shipping"] + v["duties_other"]
                      + v["packaging"] + v["fulfillment_fee"] + payment + refund_cost)
    pre_ad = net_revenue - variable_costs
    be_cac = pre_ad
    be_roas = net_revenue / pre_ad if pre_ad > 0 else float("inf")
    target_cac = TARGET_SHARE * be_cac if be_cac > 0 else 0.0
    bench = v["benchmark_cpa"]
    ratio = target_cac / bench if bench > 0 else 0.0
    # Margin points (0 to 25) for the Scout's score: 0 at a ratio of 0.7 or less, 25 at 1.3 or more.
    margin_points = max(0, min(25, round(25 * (ratio - 0.7) / 0.6)))

    status = "verified" if labels == {"VERIFIED"} else "preliminary"
    out = {
        "status": status,
        "net_revenue": net_revenue,
        "variable_costs": variable_costs,
        "pre_ad_contribution": pre_ad,
        "pre_ad_margin_pct": pre_ad / net_revenue if net_revenue else 0.0,
        "breakeven_cac": be_cac,
        "breakeven_roas": be_roas,
        "target_cac": target_cac,
        "benchmark_cpa": bench,
        "cushion_ratio": ratio,
        "cushion_pass": "yes" if pre_ad > 0 and bench <= target_cac else "no",
        "margin_points": margin_points,
        "missing_or_unknown": "",
    }
    for name, mult in CPA_MULTIPLIERS.items():
        out[f"contribution_after_ads_{name}"] = pre_ad - bench * mult
    return out


COLUMNS = ["product_id", "scenario", "status", "net_revenue", "variable_costs",
           "pre_ad_contribution", "pre_ad_margin_pct", "breakeven_cac", "breakeven_roas",
           "target_cac", "benchmark_cpa", "cushion_ratio", "cushion_pass", "margin_points",
           "contribution_after_ads_good", "contribution_after_ads_benchmark",
           "contribution_after_ads_tough", "missing_or_unknown"]


def fmt(value):
    if isinstance(value, float):
        return "inf" if value == float("inf") else f"{value:.4f}" if abs(value) < 1 else f"{value:.2f}"
    return value


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--inputs", default=str(DEFAULT_IN))
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    args = ap.parse_args(argv)

    data = load_inputs(args.inputs)
    rows = []
    for (pid, scenario), fields in sorted(data.items()):
        row = {"product_id": pid, "scenario": scenario}
        row.update(compute(fields))
        rows.append(row)

    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: fmt(r.get(k, "")) for k in COLUMNS})

    if not rows:
        print(f"No inputs found in {args.inputs}.")
        return 0
    print(f"{'product':<22}{'scen':<6}{'status':<12}{'pre-ad':>9}{'BE CAC':>9}{'BE ROAS':>9}"
          f"{'target':>9}{'bench':>8}{'cushion':>9}")
    for r in rows:
        if r["status"] == "blocked":
            print(f"{r['product_id']:<22}{r['scenario']:<6}{'blocked':<12}  missing: {r['missing_or_unknown']}")
            continue
        print(f"{r['product_id']:<22}{r['scenario']:<6}{r['status']:<12}{r['pre_ad_contribution']:>9.2f}"
              f"{r['breakeven_cac']:>9.2f}{r['breakeven_roas']:>8.2f}x{r['target_cac']:>9.2f}"
              f"{r['benchmark_cpa']:>8.2f}{r['cushion_pass']:>9}")
    print(f"\nWrote {len(rows)} rows to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
