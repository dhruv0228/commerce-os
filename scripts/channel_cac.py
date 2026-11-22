#!/usr/bin/env python3
"""Cost to win one customer by channel, and profit per order for each product on each channel.

Reads <folder>/channel_inputs.json (every input has low, high, label, source) and
<folder>/ranked.json (scripts/fast_test_rank.py). Writes channel_outputs.json and channels.md.

Channels
- meta_benchmark, meta_new_store   Meta ads: the category benchmark, and x the new-store multiplier
- affiliate                        own-store affiliate (Shopify Collabs, UpPromote): commission + app fee, as a share of price.
                                   You pay only when a sale happens.
- tiktok_shop_affiliate            TikTok Shop: creator commission + TikTok referral fee, as a share of price.
                                   Needs owned inventory shipped within 2 business days.
- paid_post                        a flat fee for one post on a creator's account. The link click rate from a post to a
                                   store has no public benchmark (UNKNOWN), so the script reports, for each ASSUMED click
                                   rate, the buyers per post, the cost per customer, and the views a post would need to
                                   match the Meta benchmark.
- gifting                          a free unit sent to creators; only some post. Same view math as paid_post, with the
                                   cost per posting creator = unit cost / post rate.

Nothing here is measured from our own store.

Usage:
    python3 scripts/channel_cac.py research/launch-plan-2026-11-22
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def lo(inp, k):
    return inp[k]["low"]


def hi(inp, k):
    return inp[k]["high"]


def main():
    folder = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "research/launch-plan-2026-11-22")
    inp = json.loads((folder / "channel_inputs.json").read_text())
    ranked = json.loads((folder / "ranked.json").read_text())
    rows = [r for r in ranked["rows"] if r.get("us") and r.get("rule_status") != "blocked"]

    aff = (lo(inp, "affiliate_commission_pct") + lo(inp, "affiliate_app_fee_pct_of_sale"),
           hi(inp, "affiliate_commission_pct") + hi(inp, "affiliate_app_fee_pct_of_sale"))
    tts = (lo(inp, "tiktok_shop_affiliate_commission_pct") + lo(inp, "tiktok_shop_referral_fee_pct"),
           hi(inp, "tiktok_shop_affiliate_commission_pct") + hi(inp, "tiktok_shop_referral_fee_pct"))
    cvr = inp["store_conversion_rate"]["low"]
    views = (lo(inp, "views_per_small_creator_post"), hi(inp, "views_per_small_creator_post"))
    fee = (lo(inp, "paid_post_fee_usd"), hi(inp, "paid_post_fee_usd"))
    post_rate = (lo(inp, "gifting_post_rate"), hi(inp, "gifting_post_rate"))
    bench_ref = inp["reference_meta_cac_usd"]["low"]

    # Per click-rate scenario: buyers per post and cost per customer for a typical post.
    scen = []
    for ctr in inp["link_click_rate_scenarios"]["values"]:
        b_lo, b_hi = views[0] * ctr * cvr, views[1] * ctr * cvr
        scen.append({
            "click_rate": ctr,
            "buyers_per_post_low": b_lo, "buyers_per_post_high": b_hi,
            "paid_post_cac_best": fee[0] / b_hi if b_hi else None,      # cheap fee, many views
            "paid_post_cac_worst": fee[1] / b_lo if b_lo else None,     # dear fee, few views
            "views_needed_to_match_meta_cheap_post": fee[0] / (bench_ref * ctr * cvr),
            "views_needed_to_match_meta_dear_post": fee[1] / (bench_ref * ctr * cvr),
        })

    out_rows = []
    for r in rows:
        u = r["us"]
        price, pre = u["price"], u["pre_ad_contribution"]
        landed = u["landed"]
        gift_cost_per_post = (landed / post_rate[1], landed / post_rate[0])   # best: high post rate
        mid = scen[len(scen) // 2]
        g_buyers = (views[0] * mid["click_rate"] * cvr, views[1] * mid["click_rate"] * cvr)
        out_rows.append({
            "id": r["id"], "group": r["group"], "price": price, "landed": landed, "pre_ad": pre,
            "meta_benchmark": {"cac": u["benchmark_cpa"], "profit": pre - u["benchmark_cpa"]},
            "meta_new_store": {"cac": u["tough_cpa"], "profit": pre - u["tough_cpa"]},
            "affiliate": {"cac_best": price * aff[0], "cac_worst": price * aff[1],
                          "profit_best": pre - price * aff[0], "profit_worst": pre - price * aff[1]},
            "tiktok_shop_affiliate": {"cac_best": price * tts[0], "cac_worst": price * tts[1],
                                      "profit_best": pre - price * tts[0], "profit_worst": pre - price * tts[1]},
            "gifting": {"cost_per_posting_creator_best": gift_cost_per_post[0], "cost_per_posting_creator_worst": gift_cost_per_post[1],
                        "cac_best_mid_click_rate": gift_cost_per_post[0] / g_buyers[1] if g_buyers[1] else None,
                        "cac_worst_mid_click_rate": gift_cost_per_post[1] / g_buyers[0] if g_buyers[0] else None},
        })
    out_rows.sort(key=lambda x: -x["affiliate"]["profit_worst"])
    out = {"affiliate_share_of_price": aff, "tiktok_shop_share_of_price": tts, "paid_post_scenarios": scen,
           "views_typical": views, "paid_post_fee": fee, "store_conversion_rate": cvr, "reference_meta_cac": bench_ref,
           "rows": out_rows,
           "labels": "See channel_inputs.json for each input's label and source. Click rates are ASSUMED scenarios because no public benchmark exists."}
    (folder / "channel_outputs.json").write_text(json.dumps(out, indent=1))

    def m(x):
        return "n/a" if x is None else (f"-${abs(x):,.2f}" if x < 0 else f"${x:,.2f}")

    md = ["# Cost to win one customer, by channel (scripts/channel_cac.py)", "",
          f"- Own-store affiliate: {aff[0]:.0%} to {aff[1]:.0%} of the price, paid only when a sale happens.",
          f"- TikTok Shop affiliate plus TikTok's fee: {tts[0]:.0%} to {tts[1]:.0%} of the price. Needs owned stock.",
          f"- Paid post ({m(fee[0])} to {m(fee[1])}) on a small creator ({views[0]:,.0f} to {views[1]:,.0f} views), store conversion {cvr:.1%}:", ""]
    md += ["| Click rate from post to store (ASSUMED) | Buyers per post | Cost per customer | Views a cheap post needs to match Meta | Views a dear post needs |", "|---|---|---|---|---|"]
    for s in scen:
        md.append(f"| {s['click_rate']:.1%} | {s['buyers_per_post_low']:.3f} to {s['buyers_per_post_high']:.2f} | {m(s['paid_post_cac_best'])} to {m(s['paid_post_cac_worst'])} | {s['views_needed_to_match_meta_cheap_post']:,.0f} | {s['views_needed_to_match_meta_dear_post']:,.0f} |")
    md += ["", "| Product | Price | Left before ads | Meta (benchmark) | Meta (new store) | Affiliate (worst to best) | TikTok Shop affiliate (worst to best) |", "|---|---|---|---|---|---|---|"]
    for x in out_rows[:25]:
        md.append(f"| {x['id']} | {m(x['price'])} | {m(x['pre_ad'])} | {m(x['meta_benchmark']['profit'])} | {m(x['meta_new_store']['profit'])} | "
                  f"{m(x['affiliate']['profit_worst'])} to {m(x['affiliate']['profit_best'])} | {m(x['tiktok_shop_affiliate']['profit_worst'])} to {m(x['tiktok_shop_affiliate']['profit_best'])} |")
    (folder / "channels.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main()
