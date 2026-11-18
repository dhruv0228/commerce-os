#!/usr/bin/env python3
"""Profit per order for offer tiers, bundles and checkout add-ons (built on scripts/fee_breakdown.py).

Inputs: research/offers-2026-11-18/offer_inputs.json (every cost labeled).
Output: research/offers-2026-11-18/offer_economics.json and a printed table.

Tiers are full orders: they pay acquisition (Meta CPA or TikTok commission) like any order.
Add-ons are extra items added to an order that already happened: no extra acquisition cost,
only their own cost, the extra postage, card and platform fees, and a refund allowance.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import channels as ch  # noqa: E402
import fee_breakdown as fb  # noqa: E402

ROOT = os.path.dirname(HERE)
IN = os.path.join(ROOT, "research", "offers-2026-11-18", "offer_inputs.json")
OUT = os.path.join(ROOT, "research", "offers-2026-11-18", "offer_economics.json")


def ship_for(params, boxes, stage):
    """Postage plus packaging for a list of (weight_lb, dims) boxes, from home (test) or 3PL rates (scale)."""
    mult = ch.HOUSE["scale_ship_mult"] if stage == "scale" else 1.0
    pack = ch.HOUSE["scale_packaging"] if stage == "scale" else ch.HOUSE["packaging"]
    return sum(ch.ship_from_home(params, w, tuple(d)) * mult + pack for w, d in boxes)


def main():
    params = ch.load_params()
    cfg = json.load(open(IN))
    comp = cfg["components"]
    out = {"tiers": [], "addons": []}
    for t in cfg["tiers"]:
        for stage in ("test", "scale"):
            cost = sum(comp[c][f"landed_{stage}"] * n for c, n in t["items"].items())
            ship = ship_for(params, t["boxes"], stage)
            r = fb.breakdown(params, t["price"], cost, t["boxes"][0][0], tuple(t["boxes"][0][1]), "pets", stage, ship_cost=ship)
            row = {"offer": t["offer"], "tier": t["name"], "stage": stage, "price": t["price"], "landed_cost": round(cost, 2),
                   "ship_and_pack": round(ship, 2)}
            for k in ("dtc_meta", "tiktok_aff"):
                row[k] = r[k]["profit"]
                row[k + "_tough"] = r[k]["profit_tough"]
                row[k + "_pre_ad"] = r[k]["pre_acq"]
            out["tiers"].append(row)
    meta = params["dtc_meta"]
    pay_pct = ch.v(meta["payment_pct_combined_for_economics_py"])
    for a in cfg["addons"]:
        for stage in ("test", "scale"):
            cost = comp[a["item"]][f"landed_{stage}"]
            extra_ship = a["extra_ship_usd"]
            fees = a["price"] * pay_pct
            refunds = a["price"] * ch.HOUSE["refund_pct_dtc"]
            profit = a["price"] - cost - extra_ship - fees - refunds
            out["addons"].append({"addon": a["name"], "stage": stage, "price": a["price"], "landed_cost": cost,
                                  "extra_ship": extra_ship, "fees": round(fees, 2), "refunds": round(refunds, 2),
                                  "profit_per_addon": round(profit, 2)})
    json.dump(out, open(OUT, "w"), indent=1)
    print(f"{'offer':<10}{'tier':<34}{'stage':<7}{'price':>7}{'cost':>8}{'ship':>7}{'DTC':>9}{'DTC tough':>11}{'TikTok':>9}")
    for r in out["tiers"]:
        print(f"{r['offer']:<10}{r['tier']:<34}{r['stage']:<7}{r['price']:>7.0f}{r['landed_cost']:>8.2f}{r['ship_and_pack']:>7.2f}"
              f"{r['dtc_meta']:>9.2f}{r['dtc_meta_tough']:>11.2f}{r['tiktok_aff']:>9.2f}")
    print()
    for a in out["addons"]:
        print(f"add-on {a['addon']:<40}{a['stage']:<7} price {a['price']:>6.2f}  profit {a['profit_per_addon']:>6.2f}")


if __name__ == "__main__":
    main()
