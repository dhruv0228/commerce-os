#!/usr/bin/env python3
"""Profit per order for one product across sales channels.

All channel math for the business lives here (CLAUDE.md section 4). Fees come from
data/channel_params.json, each with a label and source. Product inputs come from the
caller (scripts/opportunity.py or tests). Nothing here is a quote: results are only as
good as their inputs, and every output says which inputs were ASSUMED.

Channels modelled
- dtc_meta      own store (Amboras) + paid Meta ads, shipped from home or a 3PL
- tiktok_aff    TikTok Shop, creator affiliates paid a commission per sale, seller ships
- tiktok_ads    TikTok Shop, paid TikTok ads instead of affiliates
- amazon_fba    Amazon, Fulfilled by Amazon, paid with PPC
- amazon_fbm    Amazon, seller ships from home, paid with PPC

Usage:
    python3 scripts/channels.py --price 59.99 --cost 9 --weight 1.2 --dims 12 9 3 --category pets
"""
import argparse
import json
import math
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PARAMS_PATH = ROOT / "data" / "channel_params.json"

# House assumptions (ASSUMED; adjustable). Kept here so every run uses the same ones.
HOUSE = {
    "packaging": 1.25,              # mailer, insert card (ASSUMED, within 0.75-2.00 range)
    "refund_pct_dtc": 0.06,         # ASSUMED; CLAUDE.md asks for 5% and 10% scenarios
    "refund_pct_tiktok": 0.10,      # TikTok Shop return rates run 10-15% in home/electronics (ESTIMATED)
    "refund_pct_amazon": 0.06,      # ASSUMED
    "samples_per_order": 0.3,       # creator samples sent per order at small scale (ASSUMED)
    "new_store_cpa_mult": 1.3,      # new stores pay more than established-store medians
    "amazon_new_listing_mult": 1.5, # new ASINs with no reviews pay more than PPC medians (ASSUMED)
    "air_usd_per_kg": 12.0,         # express air, 10-30 kg (ESTIMATED range 10-16)
    "air_volumetric_divisor": 6000, # cm3 per kg
    "brokerage_per_unit": 0.50,     # courier entry/brokerage spread over a small batch (ASSUMED)
    "amazon_inbound_per_unit": 1.00,# freight from home to an Amazon warehouse (ASSUMED; source UNKNOWN)
    "amazon_storage_per_unit": 0.30,# about one month of storage for a small box (ASSUMED)
    "ship_zone": "zone5",
    "sea_usd_per_cbm": 200.0,       # LCL sea freight China to US West Coast incl. drayage (ASSUMED; verify with a forwarder)
    "scale_3pl_per_order": 3.00,    # pick/pack at a US 3PL once scaled (ESTIMATED range 2.75-3.20)
    # At scale (stage="scale"): negotiated 3PL / TikTok Shipping rates and fewer samples per order.
    "scale_ship_mult": 0.75,        # ASSUMED: 3PL and Upgraded TikTok Shipping discounts (TikTok cites up to ~20%)
    "scale_samples_per_order": 0.10,# ASSUMED
    "scale_packaging": 0.75,        # ASSUMED (low end of 0.75-2.00)
}

# Category -> keys used to look up fees. Unknown categories fall back to "all".
CATEGORY_MAP = {
    "pets": {"meta": "meta_cpa_pets_usd", "ttads": "tiktok_ads_cpa_pets_usd", "amz_ref": "pet_supplies",
             "ppc": "ppc_cpa_pets_usd", "aff": "pet_standard"},
    "home": {"meta": "meta_cpa_home_garden_usd", "ttads": "tiktok_ads_cpa_home_garden_usd", "amz_ref": "home_and_kitchen",
             "ppc": "ppc_cpa_home_garden_usd", "aff": "home_kitchen_standard"},
    "tech": {"meta": "meta_cpa_electronics_usd", "ttads": "tiktok_ads_cpa_electronics_usd", "amz_ref": "electronics_accessories",
             "ppc": "ppc_cpa_electronics_usd", "aff": "electronics_competitive"},
    "outdoor": {"meta": "meta_cpa_sports_outdoors_usd", "ttads": "tiktok_ads_cpa_all_median_usd", "amz_ref": "sports_and_outdoors",
                "ppc": "ppc_cpa_all_median_usd", "aff": "sports_outdoor_median"},
    "auto": {"meta": "meta_cpa_all_industry_median_usd", "ttads": "tiktok_ads_cpa_all_median_usd", "amz_ref": "automotive_and_powersports",
             "ppc": "ppc_cpa_all_median_usd", "aff": "sports_outdoor_median"},
}


def load_params(path=PARAMS_PATH):
    return json.loads(pathlib.Path(path).read_text())["params"]


def v(node):
    """Return the value of a {'value', 'label', 'source'} node, or the node itself."""
    return node["value"] if isinstance(node, dict) and "value" in node else node


def ship_from_home(params, weight_lb, dims_in=None):
    """USPS Ground Advantage commercial rate for one parcel, billed on the greater of actual
    and dimensional weight (divisor 139 above 1 cubic foot)."""
    table = v(params["ship_from_home"]["usps_ground_advantage_commercial_usd"])
    zone = HOUSE["ship_zone"]
    billable = weight_lb + 0.25  # packaging weight
    if dims_in:
        l, w, h = dims_in
        if l * w * h > 1728:
            billable = max(billable, l * w * h / 139)
    if billable < 1:
        return table["under_1lb_flat"][zone]
    steps = [(1, "1lb"), (2, "2lb"), (3, "3lb"), (5, "5lb")]
    for limit, key in steps:
        if billable <= limit:
            return table[key][zone]
    # Above 5 lb: extend linearly from the 3-5 lb slope (ESTIMATE)
    slope = (table["5lb"][zone] - table["3lb"][zone]) / 2
    return table["5lb"][zone] + slope * (math.ceil(billable) - 5)


def landed_small_batch(factory_cost, weight_lb, dims_in, duty_pct):
    """Per-unit cost to get a unit from a factory to the owner's home by express air."""
    kg = weight_lb * 0.4536
    if dims_in:
        l, w, h = (d * 2.54 for d in dims_in)
        kg = max(kg, l * w * h / HOUSE["air_volumetric_divisor"])
    freight = kg * HOUSE["air_usd_per_kg"]
    duty = factory_cost * duty_pct
    return factory_cost + freight + duty + HOUSE["brokerage_per_unit"], {"freight": freight, "duty": duty}


def landed_at_scale(factory_cost, weight_lb, dims_in, duty_pct):
    """Per-unit landed cost once volume justifies sea freight (LCL) into a US 3PL."""
    if dims_in:
        l, w, h = (d * 0.0254 for d in dims_in)
        cbm = l * w * h
    else:
        cbm = max(weight_lb, 0.5) * 0.004  # rough: 4 litres per lb when dims are unknown (ASSUMED)
    freight = cbm * HOUSE["sea_usd_per_cbm"]
    duty = factory_cost * duty_pct
    return factory_cost + freight + duty, {"freight": freight, "duty": duty}


def fba_fee(params, weight_lb, dims_in):
    fba = params["amazon_fba"]
    oz = (weight_lb + 0.2) * 16
    dims = sorted(dims_in or [10, 8, 4], reverse=True)
    small = dims[0] <= 15 and dims[1] <= 12 and dims[2] <= 0.75 and oz <= 16
    large = dims[0] <= 18 and dims[1] <= 14 and dims[2] <= 8 and oz <= 320
    if small:
        rows = v(fba["fba_fee_small_standard_2026"])
    elif large and oz <= 48:
        rows = v(fba["fba_fee_large_standard_2026"])
    elif large:
        p = v(fba["fba_fee_large_standard_3_to_20lb_2026"])
        return (p["base_usd"] + p["per_4oz_above_3lb_usd"] * math.ceil((oz - 48) / 4)) * (1 + v(fba["fuel_logistics_surcharge_pct"]))
    else:
        p = v(fba["fba_fee_large_bulky_2026"])
        return (p["base_usd"] + p["per_lb_above_first_lb_usd"] * max(0, math.ceil(oz / 16) - 1)) * (1 + v(fba["fuel_logistics_surcharge_pct"]))
    for max_oz, fee in rows:
        if oz <= max_oz:
            return fee * (1 + v(fba["fuel_logistics_surcharge_pct"]))
    return rows[-1][1] * (1 + v(fba["fuel_logistics_surcharge_pct"]))


def referral_pct(params, key, price, table="amazon_fba"):
    ref = v(params[table]["referral_fee_pct"]) if table == "walmart" else params["amazon_fba"]["referral_fee_pct"]
    node = v(ref[key]) if isinstance(ref, dict) and key in ref else 0.15
    if isinstance(node, dict):  # tiered (first $100 / above)
        first = node["first_100_usd"]
        above = node["above_100_usd"]
        return (min(price, 100) * first + max(0, price - 100) * above) / price
    return node


def channel_economics(params, price, unit_cost, weight_lb, dims_in=None, category="all", stage="test"):
    """Return {channel: {...}} with revenue, costs, acquisition and profit per order.

    unit_cost is the landed cost of one unit at the owner's home or US warehouse.
    stage "test": retail postage from home, 0.3 creator samples per order.
    stage "scale": negotiated shipping, 0.1 samples per order, cheaper packaging (all ASSUMED).
    """
    cat = CATEGORY_MAP.get(category, CATEGORY_MAP["auto"])
    ship = ship_from_home(params, weight_lb, dims_in)
    pack = HOUSE["packaging"]
    samples_per_order = HOUSE["samples_per_order"]
    if stage == "scale":
        ship *= HOUSE["scale_ship_mult"]
        pack = HOUSE["scale_packaging"]
        samples_per_order = HOUSE["scale_samples_per_order"]
    out = {}

    # Own store + Meta ads
    meta = params["dtc_meta"]
    cpa = v(meta[cat["meta"]])
    pay = price * v(meta["payment_pct_combined_for_economics_py"]) + v(meta["payment_fixed_usd"])
    refunds = price * HOUSE["refund_pct_dtc"]
    pre = price - unit_cost - ship - pack - pay - refunds
    out["dtc_meta"] = {"pre_acq": pre, "acq": cpa, "acq_tough": cpa * HOUSE["new_store_cpa_mult"],
                       "profit": pre - cpa, "profit_tough": pre - cpa * HOUSE["new_store_cpa_mult"],
                       "note": "acq = Meta median cost per purchase for the category"}

    # TikTok Shop + affiliates
    tt = params["tiktok_shop"]
    ref = v(tt["referral_fee_pct_reported_since_aug_4_2026"])
    aff_node = v(tt["affiliate_commission_open_collab"])[cat["aff"]]
    aff = sum(aff_node) / 2 if isinstance(aff_node, list) else aff_node
    samples = samples_per_order * (unit_cost + ship + pack)
    refunds_tt = price * HOUSE["refund_pct_tiktok"]
    pre_tt = price - unit_cost - ship - pack - price * ref - refunds_tt
    acq_aff = price * aff + samples
    out["tiktok_aff"] = {"pre_acq": pre_tt, "acq": acq_aff, "acq_tough": price * min(aff + 0.05, 0.30) + samples * 1.5,
                         "profit": pre_tt - acq_aff, "profit_tough": pre_tt - (price * min(aff + 0.05, 0.30) + samples * 1.5),
                         "note": f"referral {ref:.0%}, commission {aff:.0%}, samples {samples_per_order}/order"}

    # TikTok Shop + ads
    # Category medians from established advertisers; the pets figure ($5.46) looks implausibly low,
    # so never go below the all-category median (ASSUMED floor).
    tcpa = max(v(params["dtc_meta"][cat["ttads"]]), v(params["dtc_meta"]["tiktok_ads_cpa_all_median_usd"]))
    out["tiktok_ads"] = {"pre_acq": pre_tt, "acq": tcpa, "acq_tough": tcpa * HOUSE["new_store_cpa_mult"],
                         "profit": pre_tt - tcpa, "profit_tough": pre_tt - tcpa * HOUSE["new_store_cpa_mult"],
                         "note": "acq = TikTok ads median cost per purchase (established advertisers)"}

    # Amazon FBA and FBM
    fba = params["amazon_fba"]
    rp = referral_pct(params, cat["amz_ref"], price)
    ppc = v(fba[cat["ppc"]]) if v(fba.get(cat["ppc"])) else v(fba["ppc_cpa_all_median_usd"])
    refunds_amz = price * HOUSE["refund_pct_amazon"]
    fee = fba_fee(params, weight_lb, dims_in)
    pre_fba = (price - unit_cost - price * rp - fee - HOUSE["amazon_inbound_per_unit"]
               - HOUSE["amazon_storage_per_unit"] - refunds_amz - pack * 0.5)
    out["amazon_fba"] = {"pre_acq": pre_fba, "acq": ppc, "acq_tough": ppc * HOUSE["amazon_new_listing_mult"],
                         "profit": pre_fba - ppc, "profit_tough": pre_fba - ppc * HOUSE["amazon_new_listing_mult"],
                         "note": f"referral {rp:.0%}, FBA fee ${fee:.2f}, PPC median as acq"}
    pre_fbm = price - unit_cost - price * rp - ship - pack - refunds_amz
    out["amazon_fbm"] = {"pre_acq": pre_fbm, "acq": ppc * 1.2, "acq_tough": ppc * 1.2 * HOUSE["amazon_new_listing_mult"],
                         "profit": pre_fbm - ppc * 1.2, "profit_tough": pre_fbm - ppc * 1.2 * HOUSE["amazon_new_listing_mult"],
                         "note": "no Prime badge: PPC assumed 20% less efficient (ASSUMED)"}
    for k, r in out.items():
        r["margin_pct"] = r["profit"] / price if price else 0.0
    return out


def best_channel(results, launchable=("dtc_meta", "tiktok_aff", "amazon_fbm")):
    """Best channel to START on. FBA needs stock in Amazon (a later step) and TikTok ads
    medians come from established advertisers, so both are shown as references only."""
    name = max(launchable, key=lambda k: results[k]["profit_tough"])
    return name, results[name]


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--price", type=float, required=True)
    ap.add_argument("--cost", type=float, required=True, help="landed unit cost")
    ap.add_argument("--weight", type=float, required=True, help="lb")
    ap.add_argument("--dims", type=float, nargs=3)
    ap.add_argument("--category", default="auto", choices=sorted(CATEGORY_MAP))
    a = ap.parse_args()
    params = load_params()
    res = channel_economics(params, a.price, a.cost, a.weight, a.dims, a.category)
    print(f"{'channel':<12}{'pre-acq':>9}{'acq':>8}{'profit':>9}{'tough':>9}{'margin':>8}")
    for k, r in res.items():
        print(f"{k:<12}{r['pre_acq']:>9.2f}{r['acq']:>8.2f}{r['profit']:>9.2f}{r['profit_tough']:>9.2f}{r['margin_pct']:>8.1%}  {r['note']}")
    name, r = best_channel(res)
    print(f"\nBest channel to start (by tough-case profit): {name}")


if __name__ == "__main__":
    main()
