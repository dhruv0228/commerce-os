#!/usr/bin/env python3
"""Cost to win one customer by channel, and profit per order for each product on each channel.

Reads <folder>/channel_inputs.json (every input has low, high, label, source) and a ranked
product file written by scripts/fast_test_rank.py. Writes channel_outputs.json and channels.md.

Channels modelled (cost per customer = CAC):
- meta_benchmark      Meta ads at the category benchmark (established brands)
- meta_new_store      the same x the new-store multiplier
- paid_creator_post   a flat fee for a post on a creator's own account:
                      CAC = fee / (views x link-click rate x store conversion rate)
- gifting             free product sent to creators, no fee:
                      CAC = (product cost + shipping to the creator) x creators per post
                            / (views x link-click rate x store conversion rate)
- affiliate           the creator is paid a share of each sale they bring: CAC = commission x price
- tiktok_shop_affiliate  commission plus TikTok's referral fee, both a share of the price
- organic             your own faceless videos: no cash per customer, only time (reported, not costed)

low/high: "low" uses every input at its most favourable end, "high" at its least favourable,
so the range is wide on purpose. Nothing here is measured from our own store.

Usage:
    python3 scripts/channel_cac.py research/launch-plan-2026-11-22
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def v(inp, key, end):
    node = inp[key]
    return node[end] if isinstance(node, dict) else node


def post_cac(fee, views, ctr, cvr):
    buyers = views * ctr * cvr
    return (fee / buyers) if buyers > 0 else None, buyers


def main():
    folder = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "research/launch-plan-2026-11-22")
    inp = json.loads((folder / "channel_inputs.json").read_text())
    ranked = json.loads((folder / "ranked.json").read_text())
    rows = [r for r in ranked["rows"] if r.get("us") and r.get("rule_status") != "blocked"]

    # Per-post channels: best case pairs cheap fee with high views, worst case the reverse.
    fee_lo, fee_hi = v(inp, "creator_post_fee_usd", "low"), v(inp, "creator_post_fee_usd", "high")
    views_lo, views_hi = v(inp, "views_per_creator_post", "low"), v(inp, "views_per_creator_post", "high")
    ctr_lo, ctr_hi = v(inp, "link_click_rate_from_video", "low"), v(inp, "link_click_rate_from_video", "high")
    cvr_lo, cvr_hi = v(inp, "store_conversion_rate", "low"), v(inp, "store_conversion_rate", "high")
    paid_best, buyers_best = post_cac(fee_lo, views_hi, ctr_hi, cvr_hi)
    paid_worst, buyers_worst = post_cac(fee_hi, views_lo, ctr_lo, cvr_lo)
    gift_cost_per_post_lo = v(inp, "gift_unit_cost_usd", "low") * v(inp, "creators_gifted_per_post", "low")
    gift_cost_per_post_hi = v(inp, "gift_unit_cost_usd", "high") * v(inp, "creators_gifted_per_post", "high")
    gift_best, _ = post_cac(gift_cost_per_post_lo, views_hi, ctr_hi, cvr_hi)
    gift_worst, _ = post_cac(gift_cost_per_post_hi, views_lo, ctr_lo, cvr_lo)
    aff_lo, aff_hi = v(inp, "affiliate_commission_pct", "low"), v(inp, "affiliate_commission_pct", "high")
    tt_ref = v(inp, "tiktok_shop_referral_fee_pct", "low"), v(inp, "tiktok_shop_referral_fee_pct", "high")
    tt_com = v(inp, "tiktok_shop_affiliate_commission_pct", "low"), v(inp, "tiktok_shop_affiliate_commission_pct", "high")

    channels = {
        "paid_creator_post": {"best": paid_best, "worst": paid_worst,
                              "buyers_per_post_best": buyers_best, "buyers_per_post_worst": buyers_worst},
        "gifting": {"best": gift_best, "worst": gift_worst,
                    "cost_per_post_best": gift_cost_per_post_lo, "cost_per_post_worst": gift_cost_per_post_hi},
        "affiliate": {"pct_low": aff_lo, "pct_high": aff_hi},
        "tiktok_shop_affiliate": {"pct_low": tt_com[0] + tt_ref[0], "pct_high": tt_com[1] + tt_ref[1]},
    }

    out_rows = []
    for r in rows:
        u = r["us"]
        price, pre = u["price"], u["pre_ad_contribution"]
        res = {"id": r["id"], "group": r["group"], "price": price, "pre_ad": pre,
               "meta_benchmark": {"cac": u["benchmark_cpa"], "profit": pre - u["benchmark_cpa"]},
               "meta_new_store": {"cac": u["tough_cpa"], "profit": pre - u["tough_cpa"]}}
        for ch in ("paid_creator_post", "gifting"):
            c = channels[ch]
            res[ch] = {"cac_best": c["best"], "cac_worst": c["worst"],
                       "profit_best": (pre - c["best"]) if c["best"] is not None else None,
                       "profit_worst": (pre - c["worst"]) if c["worst"] is not None else None}
        for ch in ("affiliate", "tiktok_shop_affiliate"):
            c = channels[ch]
            res[ch] = {"cac_best": price * c["pct_low"], "cac_worst": price * c["pct_high"],
                       "profit_best": pre - price * c["pct_low"], "profit_worst": pre - price * c["pct_high"]}
        out_rows.append(res)
    out_rows.sort(key=lambda x: -x["affiliate"]["profit_worst"])
    (folder / "channel_outputs.json").write_text(json.dumps({"channels": channels, "rows": out_rows,
        "labels": "Inputs and their labels are in channel_inputs.json. Ranges are best and worst cases, not forecasts."}, indent=1))

    def m(x):
        return "n/a" if x is None else (f"-${abs(x):,.2f}" if x < 0 else f"${x:,.2f}")

    md = ["# Cost to win one customer, by channel (scripts/channel_cac.py)", "",
          f"- Paid post on a creator's account: {m(paid_best)} (best case) to {m(paid_worst)} (worst case) per customer. Buyers per post: {buyers_best:.2f} to {buyers_worst:.3f}.",
          f"- Gifting a product to creators: {m(gift_best)} to {m(gift_worst)} per customer.",
          f"- Affiliate commission: {aff_lo:.0%} to {aff_hi:.0%} of the price.",
          f"- TikTok Shop affiliate plus TikTok's fee: {channels['tiktok_shop_affiliate']['pct_low']:.0%} to {channels['tiktok_shop_affiliate']['pct_high']:.0%} of the price.", "",
          "| Product | Price | Left before ads | Meta (benchmark) | Meta (new store) | Affiliate (best to worst) | Paid creator post (best to worst) |", "|---|---|---|---|---|---|---|"]
    for x in out_rows[:20]:
        md.append(f"| {x['id']} | {m(x['price'])} | {m(x['pre_ad'])} | {m(x['meta_benchmark']['profit'])} | {m(x['meta_new_store']['profit'])} | "
                  f"{m(x['affiliate']['profit_best'])} to {m(x['affiliate']['profit_worst'])} | {m(x['paid_creator_post']['profit_best'])} to {m(x['paid_creator_post']['profit_worst'])} |")
    (folder / "channels.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main()
