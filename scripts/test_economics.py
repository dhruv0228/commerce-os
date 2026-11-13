#!/usr/bin/env python3
"""Checks for economics.py. Run: python3 scripts/test_economics.py"""
import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from economics import compute, REQUIRED  # noqa: E402


def fields(label="ESTIMATED", **overrides):
    base = dict(price=60, discount_pct=0, product_cost=12, supplier_shipping=6, duties_other=0,
                packaging=1, fulfillment_fee=0, payment_pct=0.029, payment_fixed=0.30,
                refund_pct=0.05, benchmark_cpa=25)
    base.update(overrides)
    return {k: {"value": str(v), "label": label} for k, v in base.items()}


def close(a, b):
    return math.isclose(a, b, abs_tol=0.005)


def test_hand_worked_example():
    # 60 revenue - (12 + 6 + 1 + 2.04 payment + 3.00 refunds) = 35.96
    r = compute(fields())
    assert r["status"] == "preliminary"
    assert close(r["variable_costs"], 24.04)
    assert close(r["pre_ad_contribution"], 35.96)
    assert close(r["breakeven_cac"], 35.96)
    assert close(r["breakeven_roas"], 60 / 35.96)
    assert close(r["target_cac"], 26.97)
    assert r["cushion_pass"] == "yes"
    assert r["margin_points"] == 16
    assert close(r["contribution_after_ads_benchmark"], 10.96)
    assert close(r["contribution_after_ads_tough"], 35.96 - 32.5)


def test_discount_reduces_revenue_and_fees():
    r = compute(fields(discount_pct=0.10))
    # net 54, payment 1.866, refunds 2.70, variable 12+6+1+1.866+2.70 = 23.566
    assert close(r["net_revenue"], 54)
    assert close(r["pre_ad_contribution"], 54 - 23.566)


def test_cushion_fails_when_benchmark_above_target():
    r = compute(fields(benchmark_cpa=30))
    assert r["cushion_pass"] == "no"


def test_unknown_blocks():
    f = fields()
    f["product_cost"]["label"] = "UNKNOWN"
    r = compute(f)
    assert r["status"] == "blocked"
    assert "product_cost" in r["missing_or_unknown"]


def test_missing_field_blocks():
    f = fields()
    del f["benchmark_cpa"]
    assert compute(f)["status"] == "blocked"


def test_all_verified():
    assert compute(fields(label="VERIFIED"))["status"] == "verified"


def test_negative_contribution_never_passes():
    r = compute(fields(product_cost=70))
    assert r["pre_ad_contribution"] < 0
    assert r["cushion_pass"] == "no"
    assert r["margin_points"] == 0


if __name__ == "__main__":
    tests = [v for k, v in dict(globals()).items() if k.startswith("test_")]
    for t in tests:
        t()
        print(f"ok  {t.__name__}")
    print(f"{len(tests)} passed")
