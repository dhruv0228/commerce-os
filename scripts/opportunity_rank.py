#!/usr/bin/env python3
"""Rank opportunities out of 100 for a founder starting with $2,000 or less.

Scores (100):
  cash fit 20        computed: cash needed to reach a first real test vs the budget
  unit profit 20     computed: profit per order (consumables: per customer over 12 months) after ads,
                     new-store tough case (ad cost x 1.3), as % of price; 15% or more earns full points
  demand 15          computed: log scale of US Google search volume for the main keyword (DataForSEO)
  supplier access 15 judged, with reasons in rank_inputs.json
  risk 15            judged (15 = lowest freight, return, safety and regulatory risk)
  long-term 10       judged (own brand, repeat, path to $10k/month)

Inputs: research/high-ticket-2026-11-19/{rank_inputs,niches,consumables,consumables_keywords}.json,
        research/models-2026-11-19/outputs.json, data/channel_params.json
Output: research/high-ticket-2026-11-19/rank_outputs.json
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import channels as ch  # noqa: E402

ROOT = os.path.dirname(HERE)
D = os.path.join(ROOT, "research", "high-ticket-2026-11-19")
load = lambda p: json.load(open(p))


def clamp(x, lo=0.0, hi=1.0):
    return max(lo, min(hi, x))


def demand_pts(vol):
    return round(15 * clamp((math.log10(max(vol, 1)) - 2) / 4), 1)  # 100 -> 0, 1,000,000 -> 15


def cash_pts(cash, budget):
    return round(20 * clamp((1.25 - cash / budget) / 0.75), 1)  # <=50% of budget -> 20, >=125% -> 0


def unit_pts(profit_tough, price):
    return round(20 * clamp((profit_tough / price) / 0.15), 1) if price else 0.0


def main():
    params = ch.load_params()
    meta = params["dtc_meta"]
    pay_pct, pay_fix = ch.v(meta["payment_pct"]), ch.v(meta["payment_fixed_usd"])
    shop_month = ch.v(meta["platform_monthly_usd"])
    tough = ch.HOUSE["new_store_cpa_mult"]
    cfg = load(os.path.join(D, "rank_inputs.json"))
    budget, setup = cfg["budget_usd"]["value"], cfg["setup_usd"]["value"]
    H = {k: v["value"] for k, v in cfg["high_ticket_assumptions"].items()}
    C = {k: v["value"] for k, v in cfg["consumable_assumptions"].items()}
    kw = {r["keyword"]: r for r in load(os.path.join(D, "consumables_keywords.json"))["rows"]}
    rows = []

    # High-ticket authorized-dealer dropshipping
    for n in load(os.path.join(D, "niches.json")):
        j = cfg["judged"][n["id"]]
        price = n["typical_aov"]
        margin = (j["margin_pct"] if j["margin_pct"] is not None else H["margin_if_unknown_pct"]) / 100
        cost = price * (1 - margin)
        conv = next(c for cap, c in H["conversion_by_aov"] if price < cap)
        cpa = n["cpc"] / conv
        refund = price * (H["refund_damage_pct_ltl"] if n["freight"] == "ltl" else H["refund_damage_pct_parcel"])
        fees = price * pay_pct + pay_fix
        pre = price - cost - H["dropship_fee_usd"] - fees - refund
        profit, profit_t = pre - cpa, pre - cpa * tough
        profit_opt = pre - cpa / 2  # optimistic: conversion rate twice the assumed one
        cash = setup + cost + 2 * cpa
        fixed = shop_month
        rows.append({"id": n["id"], "group": "high", "name": n["name"], "price": price, "price_label": n["aov_label"],
                     "lines": {"product": round(cost, 2), "shipping": 0.0, "supplier_fee": H["dropship_fee_usd"], "card_fees": round(fees, 2),
                               "refunds_damage": round(refund, 2), "ads": round(cpa, 2)},
                     "margin_pct_used": round(margin * 100), "margin_label": "ASSUMED floor" if j["margin_pct"] is None else n["margin_label"],
                     "conversion_used": conv, "cpc": n["cpc"], "keyword": n["keyword"], "search_volume": n["search_volume"],
                     "pre_ad": round(pre, 2), "profit": round(profit, 2), "profit_tough": round(profit_t, 2), "profit_if_conversion_doubles": round(profit_opt, 2),
                     "cash_needed": round(cash), "cash_note": "setup + paying the supplier for 1 order before payout + ads for 2 sales",
                     "orders_per_month_10k": round((10000 + fixed) / profit) if profit > 0 else None,
                     "judged": j, "flag": "Reselling other brands as the hero breaks CLAUDE.md section 1"})

    cons = {c["id"]: c for c in load(os.path.join(D, "consumables.json"))}
    models = {m["id"]: m for m in load(os.path.join(ROOT, "research", "models-2026-11-19", "outputs.json"))}
    for o in cfg["others"]:
        if o["id"] == "ext_own":
            s, t = models["ext_3pl"], models["ext_home"]
            price = s["price"]
            L = {l["item"]: l["usd"] for l in s["lines"]}
            lines = {"product": L["Product (landed)"], "shipping": round(L["Shipping to customer"] + L["Packaging"], 2), "supplier_fee": 0.0,
                     "card_fees": L["Card processing 2.9% + $0.30"], "refunds_damage": L["Refund allowance 6%"], "ads": s["ad_cost"]}
            pre, profit, profit_t = s["pre_ad"], s["first_order_profit"], s["first_order_profit_tough"]
            cash = setup + t["cash_up_front"] + 4 * t["ad_cost"]
            vol = kw[o["keyword"]]["search_volume"]
            rows.append({"id": o["id"], "group": "mid", "name": o["name"], "price": price, "price_label": "ASSUMED Offer B kit price",
                         "lines": lines, "pre_ad": pre, "profit": profit, "profit_tough": profit_t, "keyword": o["keyword"], "search_volume": vol,
                         "cash_needed": round(cash), "cash_note": "setup + 5-kit trial + ads for 4 sales; profit per order shown at bulk (3PL) costs, funded from trial profits",
                         "start_profit": t["first_order_profit"], "orders_per_month_10k": round((10000 + shop_month) / profit),
                         "judged": {k: o[k] for k in ("supplier", "risk", "longterm", "why")}, "flag": None})
            continue
        c = cons.get(o.get("src"), {})
        price = o.get("price") or (c.get("amazon_price") if o.get("use_amazon_price") else c.get("price"))
        cost = o.get("unit_cost") if "unit_cost" in o else c["unit_cost"]
        ship = o.get("ship") if "ship" in o else c["ship_or_fulfil_cost"]
        monthly = o.get("monthly_fee") if "monthly_fee" in o else (c.get("monthly_fee") or 0)
        cpa = o.get("cpa") or c["cpa_benchmark"]
        rep = o.get("repeat") if "repeat" in o else c["repeat_rate_12mo"]
        sup_fee = 0.0
        scf = c.get("supplier_card_fee")
        if isinstance(scf, str) and "%" in scf:  # e.g. "3.45% + $0.25 of order cost" (Rocktomic)
            pct = float(scf.split("%")[0]) / 100
            fixed_part = float(scf.split("$")[1].split()[0]) if "$" in scf else 0.0
            sup_fee = (cost + ship) * pct + fixed_part
        fees = price * pay_pct + pay_fix
        refund = price * C["refund_pct"]
        pre = price - cost - ship - sup_fee - fees - refund
        reorders = rep * C["reorders_per_repeat_buyer"]
        first, first_t = pre - cpa, pre - cpa * tough
        year, year_t = first + reorders * pre, first_t + reorders * pre
        cash = setup + monthly + (C["test_customers"] * max(0.0, -first) if first < 0 else cpa)
        fixed = shop_month + monthly
        vol = kw[o["keyword"]]["search_volume"]
        rows.append({"id": o["id"], "group": "small", "name": o["name"], "price": price,
                     "price_label": o.get("price_label") or ("Amazon price (the real ceiling)" if o.get("use_amazon_price") else c.get("price_source", "")),
                     "lines": {"product": round(cost, 2), "shipping": round(ship, 2), "supplier_fee": round(sup_fee, 2), "card_fees": round(fees, 2),
                               "refunds_damage": round(refund, 2), "ads": round(cpa, 2)},
                     "pre_ad": round(pre, 2), "profit": round(first, 2), "profit_tough": round(first_t, 2),
                     "reorders_12mo": round(reorders, 2), "profit_12mo": round(year, 2), "profit_12mo_tough": round(year_t, 2),
                     "keyword": o["keyword"], "search_volume": vol, "monthly_fee": monthly,
                     "cash_needed": round(cash), "cash_note": f"setup + first month's fees + ad losses on the first {C['test_customers']} customers",
                     "orders_per_month_10k": round((10000 + fixed) / year) if year > 0 else None,
                     "judged": {k: o[k] for k in ("supplier", "risk", "longterm", "why")},
                     "flag": "Supplements are out of scope in CLAUDE.md section 2" if o["id"].startswith("supp") else
                             ("Reselling other brands as the hero breaks CLAUDE.md section 1" if o["id"].startswith("kb") else None)})

    for r in rows:
        steady_t = r.get("profit_12mo_tough", r["profit_tough"])
        j = r["judged"]
        pts = {"cash": cash_pts(r["cash_needed"], budget), "unit": unit_pts(steady_t, r["price"]), "demand": demand_pts(r["search_volume"]),
               "supplier": j["supplier"], "risk": j["risk"], "longterm": j["longterm"]}
        r["points"] = pts
        r["score"] = round(sum(pts.values()))
    rows.sort(key=lambda r: -r["score"])
    json.dump({"budget": budget, "setup": setup, "rows": rows}, open(os.path.join(D, "rank_outputs.json"), "w"), indent=1)
    print(f"{'#':>2} {'opportunity':<46}{'score':>6}{'price':>8}{'profit':>9}{'tough':>9}{'12mo':>9}{'cash':>7}  pts cash/unit/demand/sup/risk/long")
    for i, r in enumerate(rows, 1):
        p = r["points"]
        print(f"{i:>2} {r['name'][:45]:<46}{r['score']:>6}{r['price']:>8.0f}{r['profit']:>9.2f}{r['profit_tough']:>9.2f}{r.get('profit_12mo', r['profit']):>9.2f}{r['cash_needed']:>7}"
              f"  {p['cash']}/{p['unit']}/{p['demand']}/{p['supplier']}/{p['risk']}/{p['longterm']}")


if __name__ == "__main__":
    main()
