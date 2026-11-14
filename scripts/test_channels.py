#!/usr/bin/env python3
"""Checks for scripts/channels.py."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import channels as c

P = c.load_params()

def test_ship_tiers():
    assert c.ship_from_home(P, 0.5) == P["ship_from_home"]["usps_ground_advantage_commercial_usd"]["value"]["under_1lb_flat"]["zone5"]
    assert c.ship_from_home(P, 1.6) == P["ship_from_home"]["usps_ground_advantage_commercial_usd"]["value"]["2lb"]["zone5"]
    # a big light box bills on dimensional weight (24x18x10 = 4,320 cu in / 139 = 31 lb)
    assert c.ship_from_home(P, 2, [24, 18, 10]) > c.ship_from_home(P, 5)

def test_dtc_math_by_hand():
    r = c.channel_economics(P, 100, 20, 0.5, [8, 6, 2], "pets")["dtc_meta"]
    ship = c.ship_from_home(P, 0.5, [8, 6, 2])
    expected_pre = 100 - 20 - ship - c.HOUSE["packaging"] - (100 * 0.039 + 0.30) - 100 * c.HOUSE["refund_pct_dtc"]
    assert abs(r["pre_acq"] - expected_pre) < 1e-9
    assert abs(r["profit"] - (expected_pre - 38.51)) < 1e-9

def test_tiered_referral():
    pct = c.referral_pct(P, "electronics_accessories", 200)
    assert abs(pct - (100 * 0.15 + 100 * 0.08) / 200) < 1e-9

def test_higher_cost_lowers_profit_everywhere():
    a = c.channel_economics(P, 60, 10, 1, None, "home")
    b = c.channel_economics(P, 60, 20, 1, None, "home")
    assert all(b[k]["profit"] < a[k]["profit"] for k in a)

def test_small_batch_landed_adds_freight_and_duty():
    landed, parts = c.landed_small_batch(10, 1, [10, 8, 3], 0.408)
    assert landed > 10 + 0.408 * 10 and parts["freight"] > 0

if __name__ == "__main__":
    n = 0
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn(); print("ok ", name); n += 1
    print(f"{n} passed")
