#!/usr/bin/env python3
"""Line-by-line fee breakdown per sales channel, built on scripts/channels.py.

channels.py returns profit per order; this script shows where each dollar goes
(product, shipping, packaging, platform fees, refunds, acquisition) and checks
that the lines add up to the same profit channels.py reports.

Usage:
  python3 scripts/fee_breakdown.py --price 149 --cost 73.06 --weight 9 --dims 20 14 5.5 --category pets --stage test
  add --json to print machine-readable output.
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import channels as ch  # noqa: E402

LABELS = {
    "dtc_meta": "Own store (Amboras) + Meta ads",
    "tiktok_aff": "TikTok Shop + creator affiliates",
    "tiktok_ads": "TikTok Shop + TikTok ads",
    "amazon_fba": "Amazon FBA",
    "amazon_fbm": "Amazon FBM (ship from home)",
}


def breakdown(params, price, unit_cost, weight_lb, dims_in=None, category="all", stage="test", ship_cost=None):
    H = ch.HOUSE
    cat = ch.CATEGORY_MAP.get(category, ch.CATEGORY_MAP["auto"])
    res = ch.channel_economics(params, price, unit_cost, weight_lb, dims_in, category, stage, ship_cost)

    ship = ch.ship_from_home(params, weight_lb, dims_in)
    pack = H["packaging"]
    spo = H["samples_per_order"]
    if ship_cost is not None:
        ship, pack = ship_cost, 0.0
    if stage == "scale" and ship_cost is None:
        ship *= H["scale_ship_mult"]
        pack = H["scale_packaging"]
        spo = H["scale_samples_per_order"]

    out = {}
    meta = params["dtc_meta"]
    card = price * ch.v(meta["payment_pct"]) + ch.v(meta["payment_fixed_usd"])
    platform = price * ch.v(meta["platform_fee_pct"])
    out["dtc_meta"] = [
        ("Product (landed)", unit_cost), ("Shipping to customer", ship), ("Packaging", pack),
        ("Card processing 2.9% + $0.30", card), ("Amboras platform fee 1%", platform),
        (f"Refund allowance {H['refund_pct_dtc']:.0%}", price * H["refund_pct_dtc"]),
        ("Meta ads per purchase (category median)", res["dtc_meta"]["acq"]),
    ]

    tt = params["tiktok_shop"]
    ref = ch.v(tt["referral_fee_pct_reported_since_aug_4_2026"])
    aff_node = ch.v(tt["affiliate_commission_open_collab"])[cat["aff"]]
    aff = sum(aff_node) / 2 if isinstance(aff_node, list) else aff_node
    samples = spo * (unit_cost + ship + pack)
    out["tiktok_aff"] = [
        ("Product (landed)", unit_cost), ("Shipping to customer", ship), ("Packaging", pack),
        (f"TikTok referral fee {ref:.0%}", price * ref),
        (f"Refund allowance {H['refund_pct_tiktok']:.0%}", price * H["refund_pct_tiktok"]),
        (f"Creator commission {aff:.1%}", price * aff),
        (f"Free samples to creators ({spo} per order)", samples),
    ]

    rp = ch.referral_pct(params, cat["amz_ref"], price)
    fee = ch.fba_fee(params, weight_lb, dims_in)
    out["amazon_fba"] = [
        ("Product (landed)", unit_cost), (f"Amazon referral fee {rp:.0%}", price * rp),
        ("FBA pick, pack and ship fee", fee), ("Freight to Amazon warehouse", H["amazon_inbound_per_unit"]),
        ("Storage", H["amazon_storage_per_unit"]), ("Packaging", pack * 0.5),
        (f"Refund allowance {H['refund_pct_amazon']:.0%}", price * H["refund_pct_amazon"]),
        ("Amazon PPC per sale (category median)", res["amazon_fba"]["acq"]),
    ]

    result = {}
    for key, lines in out.items():
        total = sum(x for _, x in lines)
        profit = price - total
        expected = res[key]["profit"]
        assert abs(profit - expected) < 0.01, (key, profit, expected)
        result[key] = {
            "label": LABELS[key], "price": price,
            "lines": [{"item": n, "usd": round(x, 2)} for n, x in lines],
            "fees_only": round(sum(x for n, x in lines if n not in ("Product (landed)",)), 2),
            "profit": round(profit, 2), "profit_tough": round(res[key]["profit_tough"], 2),
            "pre_acq": round(res[key]["pre_acq"], 2),
        }
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--price", type=float, required=True)
    ap.add_argument("--cost", type=float, required=True)
    ap.add_argument("--weight", type=float, required=True)
    ap.add_argument("--dims", type=float, nargs=3)
    ap.add_argument("--category", default="auto", choices=["auto", "home", "outdoor", "pets", "tech"])
    ap.add_argument("--stage", default="test", choices=["test", "scale"])
    ap.add_argument("--ship", type=float)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    params = ch.load_params()
    r = breakdown(params, a.price, a.cost, a.weight, a.dims, a.category, a.stage, a.ship)
    if a.json:
        print(json.dumps(r, indent=1))
        return
    for k, d in r.items():
        print(f"\n{d['label']}  (price ${d['price']:.2f}, stage {a.stage})")
        for ln in d["lines"]:
            print(f"  {ln['item']:<44} ${ln['usd']:>8.2f}")
        print(f"  {'Profit per order':<44} ${d['profit']:>8.2f}   (tough case ${d['profit_tough']:.2f})")


if __name__ == "__main__":
    main()
