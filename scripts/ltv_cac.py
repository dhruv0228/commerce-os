#!/usr/bin/env python3
"""LTV to CAC check: how our own options score against the "LTV must be 3x CAC" rule.

Uses only numbers the other scripts already produced (no new product facts):
- research/money-math-2026-11-19/outputs.json     Barkfare routes (what is left before ads)
- research/models-2026-11-19/outputs.json         nine models, first order and 12 months per customer
- research/fast-test-2026-11-21/ranked.json       fast-test products
- research/fast-test-2026-11-21/pod_price_sweep_outputs.csv   print-on-demand bundle
- research/fast-test-2026-11-21/rank_inputs.json  current Meta cost-per-purchase benchmarks

Definitions (contribution basis, the strict one):
- LTV = money left per customer after product, shipping, fees and refunds, before ads.
  "first order" counts one order; "12 months" adds the reorders the model assumed.
- CAC = the category benchmark cost per purchase on Meta (or Amazon PPC where stated).
- Ratio = LTV / CAC. The reel's rule asks for 3.0. The house cushion rule (target CAC = 75% of
  break-even CAC) is the same thing as a first-order ratio of 1.33.

Usage:
    python3 scripts/ltv_cac.py research/reel-check-2026-11-22
"""
import csv
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
RULE = 3.0            # the reel's rule (ESTIMATED: a common venture rule of thumb)
HOUSE = 1 / 0.75      # CLAUDE.md section 4: target CAC is 75% of break-even CAC

# Which benchmark each earlier model row should be read against today (ASSUMED mapping by category).
MODEL_BENCH = {"skin_resell": "beauty", "skin_pl": "beauty", "skin_pl_bundle": "beauty", "affiliate": "beauty", "supp_pl": "all"}


def row(rid, name, group, first, cac, cac_note, src, ltv12=None, ltv12_strong=None, note=""):
    best = max(x for x in (first, ltv12, ltv12_strong) if x is not None)
    return {
        "id": rid, "name": name, "group": group, "source": src, "note": note,
        "ltv_first_order": first, "ltv_12mo": ltv12, "ltv_12mo_strong": ltv12_strong,
        "cac": cac, "cac_note": cac_note,
        "ratio_first_order": first / cac,
        "ratio_12mo": (ltv12 / cac) if ltv12 is not None else None,
        "ratio_12mo_strong": (ltv12_strong / cac) if ltv12_strong is not None else None,
        "ratio_best_case": best / cac,
        "passes_house_rule_first_order": first / cac >= HOUSE,
        "passes_3_to_1_best_case": best / cac >= RULE,
        # What would have to change to reach 3 to 1:
        "ltv_needed_for_3_to_1": RULE * cac,
        "extra_ltv_needed": max(0.0, RULE * cac - best),
        "cac_needed_for_3_to_1": best / RULE,
    }


def main():
    out_dir = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "research/reel-check-2026-11-22")
    out_dir.mkdir(parents=True, exist_ok=True)
    bench = json.loads((ROOT / "research/fast-test-2026-11-21/rank_inputs.json").read_text())["meta_cpa_benchmark_usd"]
    rows = []

    # Barkfare routes (pets benchmark)
    mm = json.loads((ROOT / "research/money-math-2026-11-19/outputs.json").read_text())["scenarios"]
    names = {"fast_lane": "Barkfare extender, US-stock fast lane", "trial_express": "Barkfare extender, 5-kit trial shipped from home",
             "bulk_sea": "Barkfare extender, bulk stock in a US warehouse", "bulk_sea_bundle": "Barkfare $189 bundle, bulk stock in a US warehouse"}
    for s in mm:
        if s["id"] in names:
            rows.append(row(s["id"], names[s["id"]], "Barkfare (one-time purchase)", s["pre_ad"], bench["pets"], "Meta, pets benchmark",
                            "research/money-math-2026-11-19/outputs.json"))

    models = json.loads((ROOT / "research/models-2026-11-19/outputs.json").read_text())
    for mo in models:
        if mo["id"] == "ext_fba":
            rows.append(row("ext_fba", "Barkfare extender on Amazon (FBA), bulk stock", "Barkfare (one-time purchase)", mo["pre_ad"], mo["ad_cost"],
                            "Amazon pay-per-click, from channels.py", "research/models-2026-11-19/outputs.json",
                            note="Cheaper acquisition, not more lifetime value. Needs stock in hand."))
        if mo["id"] in MODEL_BENCH:
            cac = bench[MODEL_BENCH[mo["id"]]]
            # 12-month contribution = 12-month profit + the ad cost that run subtracted
            l12 = mo["profit_per_customer_12mo"] + mo["ad_cost"]
            l12s = mo["profit_per_customer_12mo_strong"] + mo["ad_cost"]
            rows.append(row(mo["id"], mo["name"], "Repeat-purchase models (Nov 19 math)", mo["pre_ad"], cac, f"Meta, {MODEL_BENCH[mo['id']]} benchmark",
                            "research/models-2026-11-19/outputs.json", l12, l12s,
                            note=(mo.get("out_of_scope") or "") + f" Reorders assumed: {mo.get('reorders_12mo', 0)} to {mo.get('reorders_12mo_strong', mo.get('reorders_12mo', 0))} in 12 months (ASSUMED)."))

    # Print-on-demand bundle at $149
    for r in csv.DictReader(open(ROOT / "research/fast-test-2026-11-21/pod_price_sweep_outputs.csv")):
        if r["product_id"].endswith("-149"):
            rows.append(row("pod_149", "Dog portrait blanket and canvas at $149, print-on-demand", "Fast-test options", float(r["pre_ad_contribution"]), bench["pets"],
                            "Meta, pets benchmark", "research/fast-test-2026-11-21/pod_price_sweep_outputs.csv"))

    # Best scouted fast-test products
    ranked = json.loads((ROOT / "research/fast-test-2026-11-21/ranked.json").read_text())["rows"]
    for r in ranked:
        if r.get("shortlist") and r["id"] != "barkfare-extender-us-stock":
            u = r["us"]
            rows.append(row(r["id"], r["id"].replace("-", " "), "Fast-test options", u["pre_ad_contribution"], u["benchmark_cpa"],
                            f"Meta, {r['benchmark_used']} benchmark", "research/fast-test-2026-11-21/ranked.json"))

    # The cheaper extender listing found on Nov 22 (a lead), if the launch-plan ranking exists.
    lp = ROOT / "research/launch-plan-2026-11-22/ranked.json"
    if lp.exists():
        for r in json.loads(lp.read_text())["rows"]:
            if r["id"] == "barkfare-extender-cheaper-listing" and r.get("us"):
                u = r["us"]
                rows.append(row(r["id"], "Barkfare extender, cheaper US listing seen Nov 22 (lead)", "Barkfare (one-time purchase)", u["pre_ad_contribution"],
                                u["benchmark_cpa"], "Meta, pets benchmark", "research/launch-plan-2026-11-22/ranked.json",
                                note="A $47.31 US-stock card price, not yet checked against the hero spec."))
    rows.sort(key=lambda x: -x["ratio_best_case"])
    summary = {
        "rule": RULE, "house_rule_first_order_ratio": HOUSE,
        "rows": len(rows),
        "pass_3_to_1": [r["id"] for r in rows if r["passes_3_to_1_best_case"]],
        "pass_house_rule": [r["id"] for r in rows if r["passes_house_rule_first_order"]],
        "labels": "Benchmarks ESTIMATED (Triple Whale medians, established brands). Costs behind each row are ESTIMATED or ASSUMED in their own files. Reorder counts are ASSUMED. Nothing here is measured from our own store.",
    }
    (out_dir / "ltv_cac_outputs.json").write_text(json.dumps({"summary": summary, "rows": rows}, indent=1))

    def m(x):
        return "n/a" if x is None else (f"-${abs(x):,.2f}" if x < 0 else f"${x:,.2f}")

    def x_(v):
        return "n/a" if v is None else f"{v:.2f}"

    md = ["# LTV to CAC check (scripts/ltv_cac.py)", "",
          "LTV here is what is left per customer after product, shipping, fees and refunds, before ads. CAC is the benchmark ad cost per purchase.",
          f"The reel's rule asks for a ratio of {RULE:.0f}. The house cushion rule equals a first-order ratio of {HOUSE:.2f}.", "",
          "| Option | Left per customer, first order | Left per customer, 12 months (base to strong) | Ad cost per customer | Ratio, first order | Ratio, 12 months (base to strong) | Ad cost needed for 3 to 1 | Extra money per customer needed for 3 to 1 |",
          "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        l12 = f"{m(r['ltv_12mo'])} to {m(r['ltv_12mo_strong'])}" if r["ltv_12mo"] is not None else "no reorders modelled"
        r12 = f"{x_(r['ratio_12mo'])} to {x_(r['ratio_12mo_strong'])}" if r["ratio_12mo"] is not None else "same as first order"
        md.append(f"| {r['name']} | {m(r['ltv_first_order'])} | {l12} | {m(r['cac'])} ({r['cac_note']}) | {x_(r['ratio_first_order'])} | {r12} | {m(r['cac_needed_for_3_to_1'])} | {m(r['extra_ltv_needed'])} |")
    md += ["", f"Options that reach 3 to 1 in their best case: {', '.join(summary['pass_3_to_1']) or 'none'}.",
           f"Options that pass the house rule on the first order: {', '.join(summary['pass_house_rule']) or 'none'}.", "", summary["labels"]]
    (out_dir / "ltv_cac.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main()
