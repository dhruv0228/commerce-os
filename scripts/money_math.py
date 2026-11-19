#!/usr/bin/env python3
"""Money math for the hero kit: where each dollar of a $149 order goes, per supply route.

Built on scripts/fee_breakdown.py (which checks itself against scripts/channels.py).
Inputs:  research/money-math-2026-11-19/inputs.json (every number labeled)
Output:  research/money-math-2026-11-19/outputs.json and a printed summary.

Definitions follow CLAUDE.md section 4: pre-ad contribution, break-even CAC = pre-ad contribution,
target CAC = 75% of break-even, break-even ROAS = price / pre-ad contribution, tough case = Meta CPA x 1.3.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import channels as ch  # noqa: E402
import fee_breakdown as fb  # noqa: E402

ROOT = os.path.dirname(HERE)
DIR = os.path.join(ROOT, "research", "money-math-2026-11-19")


def main():
    params = ch.load_params()
    cfg = json.load(open(os.path.join(DIR, "inputs.json")))
    box = cfg["box"]
    out = {"scenarios": [], "inputs": "research/money-math-2026-11-19/inputs.json"}
    for s in cfg["scenarios"]:
        w = s.get("weight_lb", box["weight_lb"])
        dims = tuple(s.get("dims_in", box["dims_in"]))
        r = fb.breakdown(params, s["price"], s["unit_cost"], w, dims, "pets", s["stage"], s["ship_cost"])["dtc_meta"]
        pre = r["pre_acq"]
        row = {"id": s["id"], "name": s["name"], "price": s["price"], "stage": s["stage"], "lines": r["lines"],
               "pre_ad": round(pre, 2), "break_even_cac": round(pre, 2), "target_cac": round(pre * 0.75, 2),
               "break_even_roas": round(s["price"] / pre, 2) if pre > 0 else None,
               "meta_cpa_benchmark": round(r["lines"][-1]["usd"], 2),
               "profit_after_ads": r["profit"], "profit_after_ads_tough": r["profit_tough"],
               "passes_cushion": r["lines"][-1]["usd"] <= pre * 0.75, "label": s["label"], "source": s["source"]}
        out["scenarios"].append(row)
    by = {r["id"]: r for r in out["scenarios"]}

    t = cfg["trial"]
    tr = by["trial_express"]
    sold = t["kits_bought"] - t["kits_kept_as_sample"]
    unit = next(x for x in cfg["scenarios"] if x["id"] == "trial_express")["unit_cost"]
    cash_in_kits = t["kits_bought"] * unit
    contribution = sold * tr["pre_ad"]
    out["trial"] = {"kits_bought": t["kits_bought"], "kits_sold": sold, "cash_for_kits": round(cash_in_kits, 2),
                    "revenue_if_all_sold": sold * tr["price"],
                    "pre_ad_contribution_if_all_sold": round(contribution, 2),
                    "ad_budget": t["ad_budget_usd"],
                    "sample_kit_cost": round(unit * t["kits_kept_as_sample"], 2),
                    "ads_to_sell_them_at_benchmark": round(sold * tr["meta_cpa_benchmark"], 2),
                    "net_at_benchmark_ads": round(contribution - sold * tr["meta_cpa_benchmark"] - unit * t["kits_kept_as_sample"], 2),
                    "net_at_tough_ads": round(contribution - sold * tr["meta_cpa_benchmark"] * ch.HOUSE["new_store_cpa_mult"] - unit * t["kits_kept_as_sample"], 2),
                    "ad_spend_per_sale_to_break_even": tr["break_even_cac"],
                    "note": "Each sale's pre-ad contribution is after its own kit cost; the sample kit is an extra cost. Ads stop once the kits are sold."}

    g = cfg["goal"]
    sc = by["bulk_sea"]
    per = sc["profit_after_ads"]
    orders = (g["monthly_profit_usd"] + g["fixed_monthly_usd"]) / per
    unit_scale = next(x for x in cfg["scenarios"] if x["id"] == "bulk_sea")["unit_cost"]
    out["goal"] = {"monthly_profit_target": g["monthly_profit_usd"], "profit_per_order_at_scale": per,
                   "orders_per_month": round(orders), "orders_per_day": round(orders / 30, 1),
                   "revenue_per_month": round(orders * sc["price"]),
                   "ad_spend_per_month": round(orders * sc["meta_cpa_benchmark"]),
                   "inventory_cash_for_one_month": round(orders * unit_scale),
                   "cash_for_first_bulk_order_150": round(150 * unit_scale),
                   "orders_per_month_tough": round((g["monthly_profit_usd"] + g["fixed_monthly_usd"]) / sc["profit_after_ads_tough"])}
    json.dump(out, open(os.path.join(DIR, "outputs.json"), "w"), indent=1)

    for r in out["scenarios"]:
        print(f"\n{r['name']}  (${r['price']}, {r['stage']})")
        for ln in r["lines"]:
            print(f"  {ln['item']:<44}${ln['usd']:>8.2f}")
        print(f"  pre-ad ${r['pre_ad']:.2f} | target CAC ${r['target_cac']:.2f} | break-even ROAS {r['break_even_roas']} | "
              f"profit after ads ${r['profit_after_ads']:.2f} (tough ${r['profit_after_ads_tough']:.2f}) | cushion {'PASS' if r['passes_cushion'] else 'FAIL'}")
    print("\nTrial:", json.dumps(out["trial"]))
    print("Goal:", json.dumps(out["goal"]))


if __name__ == "__main__":
    main()
