#!/usr/bin/env python3
"""Rank suppliers for the fastest credible first order, out of 100.

Dhruv's factors (Nov 17, 2026), in his order of importance:
    speed to a sellable unit   35   days until 5 sellable kits are in Florida or with a US customer
    cost                       25   100 x cheapest unit cost / this unit cost
    reliability                25   judged 0-100 from audits, years trading, consistency of claims, return terms
    used by other buyers       15   judged 0-100 from reviews, transactions or known brand customers

Speed score: 100 at 5 days or less, 0 at 60 days or more, straight line between.
Gate: if the minimum order is above the first order we want (5 kits), the total is capped at 60,
because the supplier cannot do the fast first order. Our own brand (private label) is required for the
hero; a source that only sells another brand is capped at 70 and flagged.

Inputs: data/supplier_rank_inputs.csv (every judged number has a note and a label).
Output: reports/ranked_suppliers_speed_<date>.md and stdout.
"""
import csv
import pathlib
import sys
from datetime import date

ROOT = pathlib.Path(__file__).resolve().parent.parent
INPUTS = ROOT / "data" / "supplier_rank_inputs.csv"
WEIGHTS = {"speed": 35, "cost": 25, "reliability": 25, "used_by_others": 15}
FIRST_ORDER = 5


def speed_score(days):
    d = float(days)
    if d <= 5:
        return 100.0
    if d >= 60:
        return 0.0
    return 100.0 * (60 - d) / 55


def main():
    rows = [r for r in csv.DictReader(open(INPUTS, newline="", encoding="utf-8")) if r.get("id")]
    cheapest = min(float(r["unit_cost_usd"]) for r in rows)
    out = []
    for r in rows:
        parts = {
            "speed": speed_score(r["days_to_5_sellable"]),
            "cost": 100.0 * cheapest / float(r["unit_cost_usd"]),
            "reliability": float(r["reliability_0_100"]),
            "used_by_others": float(r["used_by_others_0_100"]),
        }
        total = sum(parts[k] * WEIGHTS[k] / 100 for k in WEIGHTS)
        caps = []
        if int(r["moq"]) > FIRST_ORDER:
            total = min(total, 60.0)
            caps.append(f"MOQ {r['moq']} > {FIRST_ORDER}")
        if r["own_brand_possible"].strip().lower() != "yes":
            total = min(total, 70.0)
            caps.append("other brand only")
        out.append({**r, **{k + "_score": round(v, 1) for k, v in parts.items()},
                    "total": round(total, 1), "caps": "; ".join(caps) or "none"})
    out.sort(key=lambda x: -x["total"])
    today = date.today().isoformat()
    lines = [f"# Suppliers ranked for a fast first order ({today})", "",
             "Weights: speed 35, cost 25, reliability 25, used by other buyers 15. Computed by `scripts/supplier_rank.py` "
             "from `data/supplier_rank_inputs.csv`. Judged inputs are labeled there; none are verified until suppliers reply.", "",
             "| Rank | Supplier | Total /100 | Speed | Cost | Reliability | Used by others | Days to 5 kits | Unit cost | MOQ | US stock | Caps |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(out, 1):
        lines.append(f"| {i} | {r['name']} | **{r['total']}** | {r['speed_score']} | {r['cost_score']} | {r['reliability_score']} | "
                     f"{r['used_by_others_score']} | {r['days_to_5_sellable']} | ${float(r['unit_cost_usd']):.2f} | {r['moq']} | {r['us_stock']} | {r['caps']} |")
    path = ROOT / "reports" / f"ranked_suppliers_speed_{today}.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    for l in lines[4:]:
        print(l)
    print(f"-> {path.relative_to(ROOT)}")


if __name__ == "__main__":
    sys.exit(main())
