#!/usr/bin/env python3
"""Rank products and suppliers from the CSVs and write the ranked reports.

Product score (out of 100):
    margin 25        computed by economics.py from the base scenario, never judged
    demand 20        judged by the Scout, with evidence links
    supplier 20      judged by the Scout, with evidence links
    differentiation 15
    shipping and return risk 10 (10 = lowest risk)
    advertising potential 10
75 or more qualifies for further investigation, not approval.

Supplier score (out of 100):
    quality 30       capped at 15 until a sample is reviewed (quality_basis = sample)
    landed price 25  computed: 25 x cheapest landed cost / this supplier's landed cost
    US shipping 15
    response speed 10
    packaging and branding 10
    technology and integration 10
75 or more makes the shortlist, but a supplier fails outright unless legitimacy is verified.

Usage:
    python3 scripts/score.py
"""
import csv
import pathlib
import sys
from datetime import date

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
REPORTS = ROOT / "reports"

PRODUCT_CAPS = {"demand_pts": 20, "supplier_pts": 20, "differentiation_pts": 15,
                "risk_pts": 10, "ad_pts": 10}
SUPPLIER_CAPS = {"quality_pts": 30, "us_shipping_pts": 15, "response_pts": 10,
                 "packaging_pts": 10, "tech_pts": 10}
QUALIFY = 75


def read(path):
    if not path.exists():
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if any((v or "").strip() for v in r.values())]


def num(value, cap, where):
    if value in (None, ""):
        return None
    x = float(value)
    if x < 0 or x > cap:
        sys.exit(f"{where}: {x} is outside 0 to {cap}")
    return x


def score_products():
    candidates = read(DATA / "candidates.csv")
    econ = {r["product_id"]: r for r in read(DATA / "economics_outputs.csv") if r["scenario"] == "base"}
    rows = []
    for c in candidates:
        pid = c["product_id"]
        parts = {k: num(c.get(k), cap, f"candidates.csv {pid} {k}") for k, cap in PRODUCT_CAPS.items()}
        e = econ.get(pid)
        margin = float(e["margin_points"]) if e and e.get("status") != "blocked" and e.get("margin_points") else None
        known = [v for v in parts.values() if v is not None]
        total = sum(known) + (margin or 0)
        complete = margin is not None and len(known) == len(PRODUCT_CAPS)
        rows.append({
            "product_id": pid, "name": c.get("name", ""), "category": c.get("category", ""),
            "stage": c.get("stage", ""), "margin": margin, **parts, "total": total,
            "complete": complete, "econ_status": e["status"] if e else "no economics",
            "cushion": e.get("cushion_pass", "") if e else "",
        })
    rows.sort(key=lambda r: (not r["complete"], -r["total"]))
    return rows


def score_suppliers():
    suppliers = read(DATA / "suppliers.csv")
    cheapest = {}
    for s in suppliers:
        if s.get("landed_cost") and s.get("landed_label", "").upper() != "UNKNOWN":
            pid, cost = s["product_id"], float(s["landed_cost"])
            cheapest[pid] = min(cost, cheapest.get(pid, cost))
    rows = []
    for s in suppliers:
        sid = s["supplier_id"]
        parts = {k: num(s.get(k), cap, f"suppliers.csv {sid} {k}") for k, cap in SUPPLIER_CAPS.items()}
        if s.get("quality_basis", "proxy").strip().lower() != "sample" and parts["quality_pts"] is not None:
            parts["quality_pts"] = min(parts["quality_pts"], 15)
        price = None
        if s.get("landed_cost") and s.get("landed_label", "").upper() != "UNKNOWN":
            price = round(25 * cheapest[s["product_id"]] / float(s["landed_cost"]), 1)
        total = sum(v for v in parts.values() if v is not None) + (price or 0)
        legit = s.get("legitimacy_verified", "").strip().lower()
        verdict = "fail: legitimacy not verified" if legit != "yes" else (
            "shortlist" if total >= QUALIFY else "below threshold")
        rows.append({"supplier_id": sid, "product_id": s["product_id"], "name": s.get("name", ""),
                     "type": s.get("type", ""), "price": price, **parts, "total": total,
                     "basis": s.get("quality_basis", "proxy"), "verdict": verdict})
    rows.sort(key=lambda r: (r["product_id"], r["verdict"] != "shortlist", -r["total"]))
    return rows


def cell(x):
    return "" if x is None else (f"{x:g}" if isinstance(x, float) else str(x))


def main():
    REPORTS.mkdir(exist_ok=True)
    today = date.today().isoformat()

    products = score_products()
    lines = [f"# Ranked products ({today})", "",
             "Margin points come from `economics.py` (base scenario). Rows missing any score are listed last.", "",
             "| Rank | Product | Category | Margin /25 | Demand /20 | Supplier /20 | Diff /15 | Risk /10 | Ads /10 | Total | Economics | Cushion | Next |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(products, 1):
        nxt = ("investigate" if r["complete"] and r["total"] >= QUALIFY and r["cushion"] == "yes"
               else "fix offer" if r["complete"] and r["total"] >= QUALIFY
               else "incomplete" if not r["complete"] else "reject")
        lines.append(f"| {i} | {r['name']} | {r['category']} | {cell(r['margin'])} | {cell(r['demand_pts'])} | "
                     f"{cell(r['supplier_pts'])} | {cell(r['differentiation_pts'])} | {cell(r['risk_pts'])} | "
                     f"{cell(r['ad_pts'])} | **{cell(r['total'])}** | {r['econ_status']} | {r['cushion']} | {nxt} |")
    (REPORTS / "ranked_products.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    suppliers = score_suppliers()
    lines = [f"# Ranked suppliers ({today})", "",
             "Quality is capped at 15 until a sample is reviewed. Price points are relative to the cheapest landed cost for the same product.", "",
             "| Product | Supplier | Type | Quality /30 | Price /25 | US ship /15 | Response /10 | Packaging /10 | Tech /10 | Total | Quality basis | Verdict |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in suppliers:
        lines.append(f"| {r['product_id']} | {r['name']} | {r['type']} | {cell(r['quality_pts'])} | {cell(r['price'])} | "
                     f"{cell(r['us_shipping_pts'])} | {cell(r['response_pts'])} | {cell(r['packaging_pts'])} | "
                     f"{cell(r['tech_pts'])} | **{cell(r['total'])}** | {r['basis']} | {r['verdict']} |")
    (REPORTS / "ranked_suppliers.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"{len(products)} products -> reports/ranked_products.md")
    print(f"{len(suppliers)} suppliers -> reports/ranked_suppliers.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
