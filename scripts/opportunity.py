#!/usr/bin/env python3
"""Score product opportunities out of 100 across six lenses.

Input: one or more universe files (JSON, one per niche) in the format the product scanner
writes (research/universe-*/<niche>.json). Output: data/opportunities.csv and
reports/ranked_opportunities.md. All math is here; judgments (demo score, IP flags) come in
labeled from research.

Lenses (points):
  profit       30  best launch channel, tough case (scripts/channels.py), $ and margin %
  proven       20  Amazon units sold per month (floor) and how spread out sellers are
  virality     20  demo score, YouTube views, long-running ads, TikTok evidence
  acquisition  15  US dropship source, small-batch fit (light, small), no certification, no IP flags
  season       10  evergreen (peak/trough), January strength, 12-month trend
  reorder       5  consumable or accessory the same buyer re-buys

A 100 means: thousands sold monthly by many sellers at our price, $25+ profit per order after
the cost of winning the buyer in a tough case, a 3-second wow on video with proof, a US source
or a tiny light box, no seasonality, and a refill.

Usage:
    python3 scripts/opportunity.py research/universe-2026-11-14/*.json
"""
import argparse
import csv
import json
import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import channels  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
NICHE_CATEGORY = {"pets": "pets", "tech": "tech", "home": "home", "outdoor": "outdoor"}
DUTY_DEFAULT = 0.408  # China List 3 good, 2026 stack (ESTIMATED in data/channel_params.json)


def num(x, default=None):
    try:
        if x is None or x == "":
            return default
        return float(x)
    except (TypeError, ValueError):
        return default


def clamp(x, lo, hi):
    return max(lo, min(hi, x))


def lin(x, x0, x1, p):
    """Linear points: 0 at x0, p at x1, clamped."""
    if x is None:
        return 0.0
    return clamp((x - x0) / (x1 - x0), 0, 1) * p


def logp(x, x0, x1, p):
    if not x or x <= 0:
        return 0.0
    return clamp((math.log10(x) - math.log10(x0)) / (math.log10(x1) - math.log10(x0)), 0, 1) * p


def unit_cost(m, stage="test"):
    """Landed unit cost.
    test:  a priced US dropship source if one exists, else the factory price (midpoint) brought in
           by express air with duty (a 10-50 unit batch to the owner's home).
    scale: the lower factory price (volume tier) by sea freight into a US 3PL, with duty.
    """
    us = m.get("us_dropship") or {}
    lo, hi = num(m.get("factory_cost_low")), num(m.get("factory_cost_high"))
    w = num(m.get("weight_lb"), 1.0)
    dims = m.get("dims_in") if isinstance(m.get("dims_in"), list) and len(m.get("dims_in")) == 3 else None
    dims = [num(d, 1) for d in dims] if dims else None
    if stage == "test" and str(us.get("exists", "")).lower() == "yes" and num(us.get("price")):
        return num(us["price"]), "us_dropship"
    if lo is None and hi is None:
        return None, "unknown"
    if stage == "scale":
        landed, _ = channels.landed_at_scale(lo if lo is not None else hi, w, dims, DUTY_DEFAULT)
        return landed + channels.HOUSE["scale_3pl_per_order"], "sea_3pl"
    fc = (lo + hi) / 2 if lo is not None and hi is not None else (lo if lo is not None else hi)
    landed, _ = channels.landed_small_batch(fc, w, dims, DUTY_DEFAULT)
    return landed, "small_batch_air"


BAND_PRICE = {"<20": 15, "20-40": 30, "40-80": 60, "80-130": 105, "130+": 150}
BAND_ORDER = ["<20", "20-40", "40-80", "80-130", "130+"]


def volume_price(bands):
    """Price where the median unit sells: walk the price bands until half the units are covered.
    Returns (price, band). Uses band midpoints (ASSUMED representative)."""
    clean = {k: num(v, 0) for k, v in (bands or {}).items() if k in BAND_PRICE}
    total = sum(clean.values())
    if not total:
        return None, None
    acc = 0
    for b in BAND_ORDER:
        acc += clean.get(b, 0)
        if acc >= total / 2:
            return BAND_PRICE[b], b
    return None, None


def units_at_or_above(bands, price):
    """Units sold in bands whose midpoint is at least 80% of our price (proof people pay it)."""
    return sum(num(v, 0) for k, v in (bands or {}).items() if k in BAND_PRICE and BAND_PRICE[k] >= 0.8 * price)


def score(p, niche, params):
    am, m = p.get("amazon", {}), p.get("margin_inputs", {})
    vi, ac, se, ro = p.get("virality", {}), p.get("acquisition", {}), p.get("seasonality", {}), p.get("reorder", {})
    listing_median = num(m.get("retail_price")) or num(am.get("median_price"))
    vprice, vband = volume_price(am.get("bands"))
    # Price at the volume median unless the entry deliberately targets a proven premium band
    # (price_override = true, used only with band evidence that people pay it).
    if m.get("price_override") or vprice is None:
        price = listing_median
    else:  # conservative: never above the median of busy listings
        price = min(vprice, listing_median) if listing_median else vprice
    support = units_at_or_above(am.get("bands"), price) if am.get("bands") else num(am.get("units_month"))
    cost, cost_basis = unit_cost(m, "scale")
    test_cost, test_basis = unit_cost(m, "test")
    w = num(m.get("weight_lb"), 1.0)
    dims = m.get("dims_in") if isinstance(m.get("dims_in"), list) and len(m.get("dims_in")) == 3 else None
    dims = [num(d, 1) for d in dims] if dims else None
    row = {"niche": niche, "type": p.get("type"), "price": price, "unit_cost": cost, "cost_basis": cost_basis,
           "test_cost": test_cost, "test_basis": test_basis,
           "weight_lb": w, "units_month": num(am.get("units_month")), "photo": p.get("photo", ""),
           "listing_median": listing_median, "volume_band": vband, "units_at_price": support}

    # Profit (30)
    if price and cost is not None:
        res = channels.channel_economics(params, price, cost, w, dims, NICHE_CATEGORY.get(niche, "auto"), stage="scale")
        name, best = channels.best_channel(res)
        row.update(best_channel=name, profit=best["profit"], profit_tough=best["profit_tough"], margin_pct=best["margin_pct"],
                   fba_profit=res["amazon_fba"]["profit"], dtc_profit=res["dtc_meta"]["profit"], tiktok_profit=res["tiktok_aff"]["profit"])
        row["s_profit"] = lin(best["profit_tough"], 0, 25, 20) + lin(best["margin_pct"], 0, 0.25, 10)
        if test_cost is not None:
            t = channels.channel_economics(params, price, test_cost, w, dims, NICHE_CATEGORY.get(niche, "auto"))
            tn, tb = channels.best_channel(t)
            row.update(test_channel=tn, test_profit_tough=tb["profit_tough"])
    else:
        row.update(best_channel="", profit=None, profit_tough=None, margin_pct=None, fba_profit=None, dtc_profit=None, tiktok_profit=None)
        row["s_profit"] = 0.0

    # Proven buying (20)
    share = num(am.get("top_brand_share"))
    if share is not None and share > 1:
        share /= 100
    row["s_proven"] = logp(support, 1000, 30000, 12) + lin(num(am.get("listings_100plus")), 3, 15, 4) \
        + (4 * (1 - clamp(((share if share is not None else 0.5) - 0.3) / 0.4, 0, 1)))

    # Virality (20)
    tik = str(vi.get("tiktok_evidence", "")).lower()
    tik_pts = 0 if (not tik or any(x in tik for x in ("none", "no evidence", "not found", "unknown"))) else 2
    row["s_virality"] = lin(num(vi.get("demo_score")), 0, 5, 9) + logp(num(vi.get("yt_views_top10")), 10_000, 2_000_000, 5) \
        + lin(num(vi.get("foreplay_longest_days")), 0, 120, 4) + tik_pts

    # Acquisition (15)
    us = str((m.get("us_dropship") or {}).get("exists", "")).lower() == "yes"
    sb = str(ac.get("small_batch_feasible", "")).lower()
    cert = str(ac.get("certifications", "")).lower()
    ip = str(ac.get("ip_flags", "")).lower()
    clean = lambda t: (not t) or any(x in t for x in ("none", "no ", "n/a", "not required", "pass"))
    row["s_acquisition"] = (4 if us else 0) + {"yes": 5, "maybe": 2.5}.get(sb, 0) + (3 if clean(cert) else 0) + (3 if clean(ip) else 0)

    # Season (10)
    ratio, jan, trend = num(se.get("peak_trough_ratio")), num(se.get("jan_vs_avg")), num(se.get("trend_12m_pct"))
    row["s_season"] = (6 - lin(ratio, 1.5, 4, 6) if ratio else 3) + (lin(jan, 0.6, 1.0, 2) if jan else 1) + (lin(trend, -20, 10, 2) if trend is not None else 1)

    # Reorder (5)
    path = str(ro.get("path", "")).lower()
    row["s_reorder"] = 0 if (not path or path.startswith("none")) else (5 if ro.get("cadence") and "none" not in str(ro.get("cadence")).lower() else 3)

    row["score"] = round(sum(row[k] for k in ("s_profit", "s_proven", "s_virality", "s_acquisition", "s_season", "s_reorder")), 1)
    for k in list(row):
        if isinstance(row[k], float):
            row[k] = round(row[k], 2)
    row["exclusion"] = p.get("exclusion", "")
    return row


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("files", nargs="+")
    ap.add_argument("--out", default=str(ROOT / "data" / "opportunities.csv"))
    ap.add_argument("--report", default=str(ROOT / "reports" / "ranked_opportunities.md"))
    a = ap.parse_args(argv)
    params = channels.load_params()
    rows = []
    for f in a.files:
        d = json.loads(pathlib.Path(f).read_text())
        raw = (d.get("niche") or pathlib.Path(f).stem).lower()
        niche = ("pets" if "pet" in raw else "tech" if "tech" in raw else "home" if "home" in raw
                 else "outdoor" if ("outdoor" in raw or "car" in raw or "fitness" in raw) else pathlib.Path(f).stem)
        for p in d.get("products", []):
            if str(p.get("exclusion", "pass")).lower().startswith("fail"):
                continue
            rows.append(score(p, niche, params))
    rows.sort(key=lambda r: -r["score"])
    cols = ["score", "niche", "type", "price", "listing_median", "volume_band", "units_at_price", "unit_cost", "cost_basis", "best_channel", "profit", "profit_tough", "margin_pct",
            "test_cost", "test_basis", "test_channel", "test_profit_tough",
            "tiktok_profit", "dtc_profit", "fba_profit", "units_month", "weight_lb", "s_profit", "s_proven", "s_virality",
            "s_acquisition", "s_season", "s_reorder", "photo", "exclusion"]
    with open(a.out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    lines = ["# Ranked opportunities", "", "Scores from `scripts/opportunity.py`; profit from `scripts/channels.py` (tough case, best launch channel).", "",
             "| # | Score | Niche | Product type | Price | Unit cost at scale | Best channel | Profit/order at scale (tough) | Test-batch profit (tough) | Units/mo | Profit /30 | Proven /20 | Viral /20 | Acquire /15 | Season /10 | Reorder /5 |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(rows, 1):
        f = lambda x: "" if x is None else (f"{x:,.2f}" if isinstance(x, float) else str(x))
        lines.append(f"| {i} | **{r['score']}** | {r['niche']} | {r['type']} | {f(r['price'])} | {f(r['unit_cost'])} | {r['best_channel']} | "
                     f"{f(r['profit_tough'])} | {f(r.get('test_profit_tough'))} | {f(r['units_month'])} | {f(r['s_profit'])} | {f(r['s_proven'])} | {f(r['s_virality'])} | "
                     f"{f(r['s_acquisition'])} | {f(r['s_season'])} | {f(r['s_reorder'])} |")
    pathlib.Path(a.report).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(rows)} products scored -> {a.out}, {a.report}")
    for r in rows[:15]:
        print(f"{r['score']:>6}  {r['niche']:<8} {str(r['type'])[:40]:<40} ${r['price']}  {r['best_channel']:<11} scale ${r['profit_tough']}  test ${r.get('test_profit_tough')}")


if __name__ == "__main__":
    main()
