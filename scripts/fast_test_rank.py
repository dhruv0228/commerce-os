#!/usr/bin/env python3
"""Rank fast-test product candidates per category and overall.

Reads research/<folder>/candidates_*.json (written by the product scouts) and
rank_inputs.json, runs each product through own-store + Meta-ads dropship economics
(supplier ships to the customer, so no postage or packaging on our side), and scores
each product out of 100 for a one-week test on a small budget.

All numbers the report quotes come from this script (CLAUDE.md section 4).
Card fees come from data/channel_params.json through scripts/channels.py.

Usage:
    python3 scripts/fast_test_rank.py research/fast-test-2026-11-21
    python3 scripts/fast_test_rank.py research/launch-plan-2026-11-22 --include=research/fast-test-2026-11-21
"""
import glob
import json
import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import channels as ch  # noqa: E402


def val(node):
    return node["value"] if isinstance(node, dict) and "value" in node else node


def benchmark_key(category, file_key, rules, bench):
    """Pick the Meta benchmark for a product: the scout file's default, or in mixed files the keyword match.
    If more than one keyword benchmark matches, use the more expensive one."""
    text = (category or "").lower()
    keys = {key for word, key in rules.get("file_keywords", {}).get(file_key, []) if word in text}
    if not keys:
        return rules["file_default"].get(file_key, "all")
    return max(keys, key=lambda k: bench[k])


def economics(price, landed, cpa, refund_pct, pay_pct, pay_fixed, tough_mult):
    """Per-order money for a dropshipped order. landed = product + shipping to the customer."""
    pay = price * pay_pct + pay_fixed
    refunds = price * refund_pct
    pre = price - landed - pay - refunds
    target_cac = pre * 0.75
    return {
        "price": price, "landed": landed, "card_fee": pay, "refund_allowance": refunds,
        "pre_ad_contribution": pre, "break_even_cac": pre,
        "break_even_roas": (price / pre) if pre > 0 else None,
        "target_cac": target_cac, "benchmark_cpa": cpa, "tough_cpa": cpa * tough_mult,
        "cushion_pass": cpa <= target_cac,
        "profit_benchmark": pre - cpa, "profit_tough": pre - cpa * tough_mult,
        # Highest supplier cost at which the cushion rule still passes (benchmark ad cost = 75% of what is left before ads).
        "max_cost_for_cushion": price - pay - refunds - cpa / 0.75,
    }


def clamp(x, lo=0.0, hi=1.0):
    return max(lo, min(hi, x))


def score(c, us, n_us_sources):
    """Score out of 100. Weights are house choices (ASSUMED)."""
    parts = {}
    # 1. Profit per order in the tough case (30): -$15 or worse = 0, +$15 or better = 30
    parts["profit_tough_30"] = 30 * clamp((us["profit_tough"] + 15) / 30) if us else 0.0
    # 2. Demand proof (20): Amazon "bought in past month" across top listings, log scale 2,000 -> 50,000
    bpm = (c.get("amazon") or {}).get("bought_past_month_top_listings") or 0
    parts["demand_20"] = 20 * clamp((math.log10(bpm) - math.log10(2000)) / (math.log10(50000) - math.log10(2000))) if bpm > 0 else 0.0
    # 3. Supply ready this week (20): a US-stock cost exists (14), two or more US sources (20)
    parts["supply_20"] = 0.0 if not us else (20.0 if n_us_sources >= 2 else 14.0)
    # 4. Price holds up against Amazon (10): our price / typical Amazon price, 1.0 or less = 10, 1.5 or more = 0
    amz = (c.get("amazon") or {}).get("typical_price")
    parts["price_vs_amazon_10"] = 10 * clamp((1.5 - c["sell_price"] / amz) / 0.5) if amz else 5.0
    # 5. Films well (10)
    parts["demo_10"] = 2.0 * (c.get("demo_score_1to5") or 0)
    # 6. No giant competitor (5)
    whales = sum(1 for d in (c.get("dtc_competitors") or []) if d.get("is_whale"))
    parts["no_whale_5"] = {0: 5.0, 1: 2.5}.get(whales, 0.0)
    # 7. Light and simple to ship and return (5)
    w = c.get("weight_lb")
    parts["light_5"] = 2.0 if w is None else (5.0 if w <= 3 else 3.0 if w <= 6 else 1.0 if w <= 10 else 0.0)
    return round(sum(parts.values()), 1), {k: round(v, 1) for k, v in parts.items()}


def week1(us, budget, setup_fixed, goal):
    """Cash-limited first week: no Shopify payout arrives, so each order needs ad cost + supplier cost in cash."""
    fixed = setup_fixed + us["landed"]  # setup plus one sample unit ordered to Dhruv
    cash = budget - fixed
    per_order_cash = us["tough_cpa"] + us["landed"]
    orders = max(0, math.floor(cash / per_order_cash))
    return {
        "budget": budget, "fixed_setup_and_sample": fixed, "cash_per_order_before_payout": per_order_cash,
        "orders": orders, "sales": orders * us["price"],
        "ad_spend": orders * us["tough_cpa"], "supplier_spend": orders * us["landed"],
        "profit_after_everything": orders * us["profit_tough"] - fixed,
        "orders_needed_for_goal": math.ceil(goal / us["price"]),
        "cash_needed_for_goal": fixed + math.ceil(goal / us["price"]) * per_order_cash,
    }


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--include=")]
    folder = pathlib.Path(args[0] if args else "research/fast-test-2026-11-21")
    # --include=<folder> adds the candidate files of another research folder (repeatable).
    extra = [pathlib.Path(a.split("=", 1)[1]) for a in sys.argv[1:] if a.startswith("--include=")]
    inp = json.loads((folder / "rank_inputs.json").read_text())
    params = ch.load_params()
    pay_pct = ch.v(params["dtc_meta"]["payment_pct_combined_for_economics_py"])
    pay_fixed = ch.v(params["dtc_meta"]["payment_fixed_usd"])
    bench = inp["meta_cpa_benchmark_usd"]
    tough = val(inp["new_store_multiplier"])
    r_us, r_us_hi, r_cn = val(inp["refund_pct_us_stock"]), val(inp["refund_pct_us_stock_high"]), val(inp["refund_pct_china_shipped"])
    stress = val(inp["cost_stress_multiplier"])
    setup_fixed = sum(val(x) for x in inp["setup_costs_usd"].values())
    goal = inp["week1_sales_goal_usd"]

    rows = []
    paths = sorted(glob.glob(str(folder / "candidates_*.json")))
    for ex in extra:
        paths += sorted(glob.glob(str(ex / "candidates_*.json")))
    for path in paths:
        file_key = pathlib.Path(path).stem.replace("candidates_", "")
        data = json.loads(pathlib.Path(path).read_text())
        if isinstance(data, dict):
            data = data.get("candidates", [])
        for c in data:
            # Corrections from a skeptic re-check override the scout's values (rank_inputs.json "corrections").
            fix = inp.get("corrections", {}).get(c.get("id"))
            if fix:
                c = dict(c)
                for k in ("best_us_landed_cost", "sell_price", "sell_price_source", "best_us_landed_label"):
                    if k in fix:
                        c[k] = fix[k]
            bkey = benchmark_key(c.get("category"), file_key, inp["category_rules"], bench)
            cpa = bench[bkey]
            price = c["sell_price"]
            us_cost, cn_cost = c.get("best_us_landed_cost"), c.get("best_cn_landed_cost")
            us = economics(price, us_cost, cpa, r_us, pay_pct, pay_fixed, tough) if us_cost else None
            us_hi = economics(price, us_cost, cpa, r_us_hi, pay_pct, pay_fixed, tough) if us_cost else None
            us_stress = economics(price, us_cost * stress, cpa, r_us, pay_pct, pay_fixed, tough) if us_cost else None
            cn = economics(price, cn_cost, cpa, r_cn, pay_pct, pay_fixed, tough) if cn_cost else None
            n_us = sum(1 for s in (c.get("supply") or []) if (s.get("ships_from") or "").upper() == "US" and s.get("unit_cost"))
            total, parts = score(c, us, n_us)
            amazon = c.get("amazon") or {}
            row = {
                "id": c["id"], "group": file_key, "category": c.get("category"), "benchmark_used": bkey,
                "product": c.get("product"), "what_it_solves": c.get("what_it_solves"),
                "sell_price": price, "sell_price_source": c.get("sell_price_source"),
                "proposed_price": (c.get("sell_price_source") or "").strip().lower().startswith("proposed"),
                "amazon_typical_price": amazon.get("typical_price"),
                "amazon_bought_past_month": amazon.get("bought_past_month_top_listings"),
                "amazon_listings_counted": amazon.get("listings_counted"),
                "us_landed_cost": us_cost, "us_landed_label": c.get("best_us_landed_label"),
                "cn_landed_cost": cn_cost, "cn_landed_label": c.get("best_cn_landed_label"),
                "us_sources": n_us, "weight_lb": c.get("weight_lb"), "demo_score": c.get("demo_score_1to5"),
                "whales": [d.get("store") for d in (c.get("dtc_competitors") or []) if d.get("is_whale")],
                "bundle_idea": c.get("bundle_idea"), "whale_note": c.get("whale_note"),
                "ip_safety_flags": c.get("ip_safety_flags"), "season_note": c.get("season_note"), "risks": c.get("risks"),
                "us": us, "us_refund_high": us_hi, "us_cost_up_20pct": us_stress, "china": cn,
                "score": total, "score_parts": parts,
                # Dhruv's rule: no order may lose money. Startable = has US stock and earns money in the tough case.
                "startable_this_week": bool(us and us["profit_tough"] > 0),
                "robust": bool(us and us_stress["profit_tough"] > 0 and us_hi["profit_tough"] > 0),
                "week1": {str(b): week1(us, b, setup_fixed, goal) for b in inp["budgets_usd"]} if us else None,
            }
            rows.append(row)

    # Dhruv's rule is a gate, not a weight: no order may lose money.
    # green = earns money at the tough ad cost; amber = earns money only at the benchmark ad cost;
    # red = loses money even at the benchmark, or has no US stock.
    for r in rows:
        u = r["us"]
        r["tier"] = "green" if (u and u["profit_tough"] > 0) else "amber" if (u and u["profit_benchmark"] > 0) else "red"
    # Skeptic's re-check: the same product at the cost of a better-proven US listing.
    proven = inp.get("proven_listing_cost_usd", {})
    for r in rows:
        pc = proven.get(r["id"])
        if pc and r["us"]:
            cpa_ = r["us"]["benchmark_cpa"]
            e = economics(r["sell_price"], pc["value"], cpa_, r_us, pay_pct, pay_fixed, tough)
            r["proven_listing"] = {"cost": pc["value"], "note": pc["note"], "profit_benchmark": e["profit_benchmark"], "profit_tough": e["profit_tough"]}
        else:
            r["proven_listing"] = None
    # House rules come before money: a product blocked on safety cannot start, whatever it earns.
    review = inp.get("rule_review", {})
    for r in rows:
        if r["id"] in review.get("blocked", {}):
            r["rule_status"], r["rule_note"] = "blocked", review["blocked"][r["id"]]
            r["startable_this_week"] = r["robust"] = False
        elif r["id"] in review.get("caution", {}):
            r["rule_status"], r["rule_note"] = "caution", review["caution"][r["id"]]
        else:
            r["rule_status"], r["rule_note"] = "ok", ""
    near = val(inp.get("shortlist_rule", {"value": 0.15}))
    for r in rows:
        u = r["us"]
        r["shortlist"] = bool(u and r["rule_status"] != "blocked" and u["max_cost_for_cushion"] > 0
                              and r["us_landed_cost"] <= u["max_cost_for_cushion"] * (1 + near))
    order = {"green": 0, "amber": 1, "red": 2}
    rows.sort(key=lambda r: (r["rule_status"] == "blocked", order[r["tier"]], -r["score"]))
    for i, r in enumerate(rows, 1):
        r["rank_overall"] = i
    groups = {}
    for r in rows:
        groups.setdefault(r["group"], []).append(r)
    for g in groups.values():
        for i, r in enumerate(g, 1):
            r["rank_in_group"] = i

    # A capped test plan for each product with US stock: fixed ad budget, benchmark and tough ad cost.
    ad_budget = val(inp["test_plan"]["ad_budget_usd"])
    for r in rows:
        u = r["us"]
        if not u:
            r["test_plan"] = None
            continue
        # Fit the ad budget so setup + sample + ads + supplier payments stay inside the top budget even if
        # every order arrives before any Shopify payout (benchmark ad cost = the most orders). Rounded down to $10.
        cap = max(inp["budgets_usd"])
        fit = (cap - setup_fixed - u["landed"]) / (1 + u["landed"] / u["benchmark_cpa"])
        ab = min(ad_budget, math.floor(fit / 10) * 10)
        plan = {"ad_budget": ab, "ad_budget_per_day": ab / inp["test_plan"]["days"], "ad_budget_was_cut_to_fit_cash": ab < ad_budget,
                "setup_and_sample": setup_fixed + u["landed"],
                "stop_ad_with_no_sale_at": u["break_even_cac"], "checkpoint_half_budget": ab / 2}
        for name, cpa in (("benchmark", u["benchmark_cpa"]), ("tough", u["tough_cpa"])):
            orders = ab / cpa
            plan[name] = {"orders": orders, "sales": orders * u["price"], "supplier_spend": orders * u["landed"],
                          "cash_out_before_payout": setup_fixed + u["landed"] + ab + orders * u["landed"],
                          "net_after_setup_and_sample": orders * (u["pre_ad_contribution"]) - ab - setup_fixed - u["landed"]}
        plan["worst_case_no_sales"] = -(ab + setup_fixed + u["landed"])
        plan["loss_if_stopped_at_checkpoint_with_no_sales"] = -(ab / 2 + setup_fixed + u["landed"])
        r["test_plan"] = plan

    # The "$100,000 before the end of the year" claim, on benchmark numbers.
    cc = inp["claim_check"]
    aov, days = val(cc["average_order_usd"]), val(cc["days_left_in_year"])
    orders_needed = math.ceil(cc["revenue_target_usd"] / aov)
    cost_shares = sorted(r["us_landed_cost"] / r["sell_price"] for r in rows if r["us_landed_cost"])
    median_cost_share = cost_shares[len(cost_shares) // 2] if cost_shares else None
    cm = cc["creator_month"]
    claim = {
        "revenue_target": cc["revenue_target_usd"], "days": days, "average_order": aov, "orders_needed": orders_needed,
        "orders_per_day": orders_needed / days,
        "ad_spend_benchmark": orders_needed * bench["all"], "ad_spend_tough": orders_needed * bench["all"] * tough,
        "ad_spend_per_day_benchmark": orders_needed * bench["all"] / days,
        "median_cost_share_of_price_in_our_candidates": median_cost_share,
        "supplier_spend": cc["revenue_target_usd"] * median_cost_share if median_cost_share else None,
        "creator_month_ad_share_of_revenue": cm["meta_spend"] / cm["revenue"],
        "creator_month_profit_share_of_revenue": cm["net_profit"] / cm["revenue"],
        "profit_if_creator_margin": cc["revenue_target_usd"] * cm["net_profit"] / cm["revenue"],
        "creator_year_profit_share_of_revenue": cc["creator_year"]["net_profit"] / cc["creator_year"]["revenue"],
        "profit_if_creator_year_margin": cc["revenue_target_usd"] * cc["creator_year"]["net_profit"] / cc["creator_year"]["revenue"],
        "budget_multiple_needed_for_ads_alone": orders_needed * bench["all"] / max(inp["budgets_usd"]),
    }

    learn = val(inp["learning_phase_purchases_per_week"])
    summary = {
        "checked": inp["checked"], "products": len(rows),
        "tiers": {t: sum(1 for r in rows if r["tier"] == t and r["rule_status"] != "blocked") for t in ("green", "amber", "red")},
        "blocked": sum(1 for r in rows if r["rule_status"] == "blocked"),
        "green_that_survive_proven_listing_cost": sum(1 for r in rows if r["tier"] == "green" and r["rule_status"] != "blocked" and not (r.get("proven_listing") and r["proven_listing"]["profit_tough"] <= 0)),
        "startable": sum(r["startable_this_week"] for r in rows), "robust": sum(r["robust"] for r in rows),
        "cushion_pass": sum(1 for r in rows if r["us"] and r["us"]["cushion_pass"]),
        "setup_fixed_usd": setup_fixed,
        "learning_phase_weekly_ad_spend_by_benchmark": {k: round(v * learn, 2) for k, v in bench.items() if not k.startswith("_")},
        "claim_check": claim,
        "proposed_prices": sum(1 for r in rows if r["proposed_price"]),
        "under_60": sum(1 for r in rows if r["sell_price"] < 60),
        "green_profits": sorted(round(r["us"]["profit_tough"], 2) for r in rows if r["tier"] == "green" and r["rule_status"] != "blocked"),
        "blocked_that_would_earn": sum(1 for r in rows if r["tier"] == "green" and r["rule_status"] == "blocked"),
        "cushion_pass_unblocked": sum(1 for r in rows if r["us"] and r["us"]["cushion_pass"] and r["rule_status"] != "blocked"),
        "pre_ad_range_all": [min(r["us"]["pre_ad_contribution"] for r in rows if r["us"]), max(r["us"]["pre_ad_contribution"] for r in rows if r["us"])],
        "tough_cpa_range": [min(r["us"]["tough_cpa"] for r in rows if r["us"]), max(r["us"]["tough_cpa"] for r in rows if r["us"])],
        "shortlist": [r["id"] for r in rows if r["shortlist"]],
        "labels": "Costs are marketplace card prices (treat as ESTIMATED until a real order confirms them). Benchmarks ESTIMATED. Refund rates, the 1.3 multiplier and the cost stress are ASSUMED.",
    }
    out = {"summary": summary, "inputs": inp, "rows": rows}
    (folder / "ranked.json").write_text(json.dumps(out, indent=1))

    def m(x):
        return "n/a" if x is None else (f"-${abs(x):,.2f}" if x < 0 else f"${x:,.2f}")

    def table(rs, rank_key):
        lines = ["| # | Product | Sell | US cost | Before ads | Ad cost (tough) | Profit (benchmark) | Profit (tough) | If cost +20% | Amazon/mo | Score | Tier | Start now? |",
                 "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in rs:
            u = r["us"]
            flag = ("BLOCKED on safety" if r["rule_status"] == "blocked" else "YES, robust" if r["robust"] else "yes, thin" if r["startable_this_week"]
                    else ("no US stock" if not u else "no, loses money")) + (" (caution)" if r["rule_status"] == "caution" else "")
            lines.append("| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |".format(
                r[rank_key], r["id"], m(r["sell_price"]), m(r["us_landed_cost"]),
                m(u["pre_ad_contribution"]) if u else "n/a", m(u["tough_cpa"]) if u else "n/a",
                m(u["profit_benchmark"]) if u else "n/a", m(u["profit_tough"]) if u else "n/a",
                m(r["us_cost_up_20pct"]["profit_tough"]) if u else "n/a",
                f"{r['amazon_bought_past_month']:,}" if r["amazon_bought_past_month"] else "n/a", r["score"], r["tier"], flag))
        return "\n".join(lines)

    md = [f"# Fast-test product ranking ({inp['checked']})", "",
          "Produced by `scripts/fast_test_rank.py`. Own store on Shopify, Meta ads, supplier ships from US stock to the customer.",
          "Before ads = price minus supplier cost, card fee and a 6% refund allowance. Tough = benchmark ad cost x 1.3 (new store).",
          "Costs are marketplace card prices read on the date above: ESTIMATED until a real order confirms them.",
          "Order: green first (earns money at the tough ad cost), then amber (only at the benchmark ad cost), then red; by score inside each tier.", "",
          f"Products: {summary['products']}. Earn money in the tough case with US stock: {summary['startable']}. Still earn money if cost is 20% higher and refunds are 10%: {summary['robust']}. Pass the cushion rule: {summary['cushion_pass']}.", "",
          "## Overall", "", table(rows, "rank_overall"), ""]
    for g, rs in groups.items():
        md += [f"## {g}", "", table(rs, "rank_in_group"), ""]
    notes = [r for r in rows if r["rule_status"] != "ok"]
    if notes:
        md += ["## Rule review (ASSUMED: our reading of CLAUDE.md section 2; Dhruv can overrule)", ""]
        md += [f"- {r['id']}: {r['rule_status'].upper()}. {r['rule_note']}" for r in notes]
        md += [""]
    pl = [r for r in rows if r.get("proven_listing")]
    if pl:
        md += ["## Re-check at the cost of a better-proven US listing", "", "| Product | Cheapest listing | Profit (tough) | Better-proven listing | Profit (tough) |", "|---|---|---|---|---|"]
        md += [f"| {r['id']} | {m(r['us_landed_cost'])} | {m(r['us']['profit_tough'])} | {m(r['proven_listing']['cost'])} ({r['proven_listing']['note']}) | {m(r['proven_listing']['profit_tough'])} |" for r in pl]
        md += [""]
    sl = [r for r in rows if r["shortlist"]]
    md += ["## Shortlist for the logged-in cost check (listed cost within 15% of the cost that passes the cushion rule)", "",
           "| Product | Sell | Listed US cost | Go price: cost must be at or under | Profit at that cost (tough) |", "|---|---|---|---|---|"]
    for r in sl:
        u = r["us"]
        md.append(f"| {r['id']} | {m(r['sell_price'])} | {m(r['us_landed_cost'])} | {m(u['max_cost_for_cushion'])} | {m(u['price'] - u['max_cost_for_cushion'] - u['card_fee'] - u['refund_allowance'] - u['tough_cpa'])} |")
    md += [""]
    md += ["## First week on a small budget (top 10 overall, tough ad cost, no payout yet)", "",
           "| Product | Budget | Orders the cash covers | Sales | Profit after setup and sample | Orders for $2,000 | Cash needed for $2,000 |", "|---|---|---|---|---|---|---|"]
    for r in [x for x in rows if x["rule_status"] != "blocked"][:10]:
        if not r["week1"]:
            continue
        for b, w in r["week1"].items():
            md.append(f"| {r['id']} | {m(float(b))} | {w['orders']} | {m(w['sales'])} | {m(w['profit_after_everything'])} | {w['orders_needed_for_goal']} | {m(w['cash_needed_for_goal'])} |")
    md += ["", f"## Capped test plan: up to {m(float(ad_budget))} of ads on one product, cut where needed to keep total cash out under {m(float(max(inp['budgets_usd'])))} (top 8 with US stock)", "",
           "| Product | Ad cap | Orders (benchmark to tough) | Sales | Net after setup and sample | Cash out before any payout | Stop an ad with no sale at |", "|---|---|---|---|---|---|---|"]
    for r in [x for x in rows if x["test_plan"] and x["rule_status"] != "blocked"][:8]:
        b, t_ = r["test_plan"]["benchmark"], r["test_plan"]["tough"]
        md.append(f"| {r['id']} | {m(float(r['test_plan']['ad_budget']))} | {b['orders']:.1f} to {t_['orders']:.1f} | {m(b['sales'])} to {m(t_['sales'])} | {m(b['net_after_setup_and_sample'])} to {m(t_['net_after_setup_and_sample'])} | {m(b['cash_out_before_payout'])} to {m(t_['cash_out_before_payout'])} | {m(r['test_plan']['stop_ad_with_no_sale_at'])} |")
    md += ["", "## The $100,000 by year end claim on benchmark numbers", "",
           f"- Orders needed at a {m(aov)} average order: {claim['orders_needed']:,} in {days} days ({claim['orders_per_day']:.0f} a day).",
           f"- Ad spend at the all-industry benchmark: {m(claim['ad_spend_benchmark'])} ({m(claim['ad_spend_per_day_benchmark'])} a day); at new-store cost: {m(claim['ad_spend_tough'])}.",
           f"- That is {claim['budget_multiple_needed_for_ads_alone']:.0f} times a $1,000 budget for ads alone.",
           f"- Supplier payments at the median cost share in our candidates ({claim['median_cost_share_of_price_in_our_candidates']:.0%} of price): {m(claim['supplier_spend'])}." if median_cost_share else "- Supplier payments: n/a.",
           f"- The creator's own reported month: ads were {claim['creator_month_ad_share_of_revenue']:.0%} of revenue and profit {claim['creator_month_profit_share_of_revenue']:.0%}. At that margin $100,000 of sales leaves {m(claim['profit_if_creator_margin'])}."]
    md += ["", "## China-shipped comparison (where a China cost was found; 10% refund allowance ASSUMED)", "",
           "| Product | US cost | China cost | Profit tough, US | Profit tough, China |", "|---|---|---|---|---|"]
    for r in rows:
        if r["china"]:
            md.append(f"| {r['id']} | {m(r['us_landed_cost'])} | {m(r['cn_landed_cost'])} | {m(r['us']['profit_tough']) if r['us'] else 'n/a'} | {m(r['china']['profit_tough'])} |")
    md += ["", "## Ad spend needed to leave Meta's learning phase (50 purchases in a week)", ""]
    md += [f"- {k}: {m(v)}" for k, v in summary["learning_phase_weekly_ad_spend_by_benchmark"].items()]
    (folder / "ranked.md").write_text("\n".join(md) + "\n")
    print("\n".join(md[:60]))


if __name__ == "__main__":
    main()
