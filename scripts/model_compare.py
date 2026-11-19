#!/usr/bin/env python3
"""Compare business models: profit on the first order and over a customer's first 12 months.

Built on scripts/fee_breakdown.py (checked against scripts/channels.py).
Inputs:  research/models-2026-11-19/inputs.json   Output: research/models-2026-11-19/outputs.json

First order: price minus product, shipping, fees, refunds and the Meta ad cost to win the customer.
Reorders: same order without the ad cost (email and SMS bring them back), times the expected reorders.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import channels as ch  # noqa: E402
import fee_breakdown as fb  # noqa: E402

DIR = os.path.join(os.path.dirname(HERE), "research", "models-2026-11-19")
# beauty is not in channels.CATEGORY_MAP; add it locally (Meta beauty median, ESTIMATED in data/channel_params.json)
ch.CATEGORY_MAP.setdefault("beauty", dict(ch.CATEGORY_MAP["auto"], meta="meta_cpa_beauty_usd"))
ch.CATEGORY_MAP.setdefault("all", ch.CATEGORY_MAP["auto"])


def main():
    params = ch.load_params()
    cfg = json.load(open(os.path.join(DIR, "inputs.json")))
    rep = {k: v["value"] for k, v in cfg["repeat"].items()}
    rows = []
    for m in cfg["models"]:
        dims = tuple(m["dims"]) if m.get("dims") else None
        w = m.get("weight_lb", 0.5)
        r = fb.breakdown(params, m["price"], m["unit_cost"], w, dims, m["category"], m["stage"], m["ship_cost"])
        key = m.get("channel", "dtc_meta")
        d = r[key]
        pre, first = d["pre_acq"], d["profit"]
        ads = d["lines"][-1]["usd"]
        out = {"id": m["id"], "group": m["group"], "name": m["name"], "brand": m["brand"], "who_ships": m["who_ships"],
               "price": m["price"], "lines": d["lines"], "pre_ad": pre, "ad_cost": round(ads, 2),
               "first_order_profit": first, "first_order_profit_tough": d["profit_tough"],
               "cash_up_front": m["cash_up_front"], "cash_label": m["cash_label"], "source": m["source"],
               "out_of_scope": m.get("out_of_scope")}
        for label, rk in (("12mo", m["reorders"]), ("12mo_strong", "consumable_reorders_strong" if "consumable" in m["reorders"] else m["reorders"])):
            out[f"profit_per_customer_{label}"] = round(first + rep[rk] * pre, 2)
            out[f"reorders_{label}"] = rep[rk]
        out["reorders_to_cover_ads"] = round(-first / pre, 2) if first < 0 and pre > 0 else 0
        rows.append(out)
    a = cfg["affiliate"]
    comm = a["price"] * a["commission_pct"]["value"]
    cpa = ch.v(params["dtc_meta"]["meta_cpa_beauty_usd"])
    rows.append({"id": "affiliate", "group": "Skincare / repeat products", "name": "Affiliate: promote another brand for a commission",
                 "brand": "theirs", "who_ships": "the brand", "price": a["price"], "pre_ad": round(comm, 2), "ad_cost": cpa,
                 "first_order_profit": round(comm - cpa, 2), "first_order_profit_tough": round(comm - cpa * ch.HOUSE["new_store_cpa_mult"], 2),
                 "profit_per_customer_12mo": round(comm - cpa, 2), "profit_per_customer_12mo_strong": round(comm - cpa, 2),
                 "reorders_12mo": 0, "cash_up_front": 0, "cash_label": "none",
                 "note": "Reorders usually go to the brand, not to you. Affiliates live on free content, not paid ads.",
                 "source": a["commission_pct"]["source"]})
    json.dump(rows, open(os.path.join(DIR, "outputs.json"), "w"), indent=1)
    print(f"{'model':<62}{'price':>6}{'pre-ad':>8}{'ads':>7}{'1st order':>10}{'12mo/cust':>10}{'strong':>8}{'cash':>8}")
    for o in rows:
        print(f"{o['name'][:61]:<62}{o['price']:>6}{o['pre_ad']:>8.2f}{o['ad_cost']:>7.2f}{o['first_order_profit']:>10.2f}"
              f"{o['profit_per_customer_12mo']:>10.2f}{o['profit_per_customer_12mo_strong']:>8.2f}{o['cash_up_front']:>8}")


if __name__ == "__main__":
    main()
