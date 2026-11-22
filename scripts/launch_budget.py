#!/usr/bin/env python3
"""Where the $1,800 goes: totals per lane, per CLAUDE.md budget line, and money at risk.

Reads <folder>/budget_inputs.json:
{
  "total_budget": 1800,
  "budget_lines": {"Store and essential software": 100, ...},      # CLAUDE.md section 0
  "lanes": [
    {"id": "black-friday", "name": "...", "window": "...", "items": [
        {"what": "...", "amount": 120, "budget_line": "First advertising test",
         "kind": "spend" | "float" | "reserve",                      # float = paid to a supplier, comes back at payout
         "only_if": "...optional gate...", "label": "ASSUMED", "source": "..."}
    ]}
  ]
}

kind:
- spend   money that is gone once used (ads, creator fees, samples, apps)
- float   supplier payments for orders already sold; it returns when Shopify pays out
- reserve money held back and not planned to be used

Writes <folder>/budget_outputs.json and budget.md. All amounts are planning allocations
(ASSUMED unless an item says otherwise), not quotes.

Usage:
    python3 scripts/launch_budget.py research/launch-plan-2026-11-22
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def main():
    folder = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "research/launch-plan-2026-11-22")
    inp = json.loads((folder / "budget_inputs.json").read_text())
    total = inp["total_budget"]
    lines = inp["budget_lines"]
    by_line = {k: 0.0 for k in lines}
    lanes_out = []
    grand = {"spend": 0.0, "float": 0.0, "reserve": 0.0}
    gated = 0.0
    ungated_spend = 0.0
    for lane in inp["lanes"]:
        t = {"spend": 0.0, "float": 0.0, "reserve": 0.0}
        lane_gated = 0.0
        for it in lane["items"]:
            amt = float(it["amount"])
            t[it["kind"]] += amt
            grand[it["kind"]] += amt
            if it.get("only_if"):
                lane_gated += amt
            elif it["kind"] == "spend":
                ungated_spend += amt
            by_line.setdefault(it["budget_line"], 0.0)
            by_line[it["budget_line"]] += amt
        gated += lane_gated
        lanes_out.append({"id": lane["id"], "name": lane["name"], "window": lane.get("window", ""),
                          "spend": t["spend"], "float": t["float"], "reserve": t["reserve"],
                          "total": sum(t.values()), "gated_amount": lane_gated,
                          "items": lane["items"]})
    planned_total = sum(grand.values())
    line_rows = [{"line": k, "planned": float(lines.get(k, 0)), "allocated": v,
                  "over_by": max(0.0, v - float(lines.get(k, 0)))} for k, v in by_line.items()]
    out = {
        "total_budget": total,
        "allocated": planned_total,
        "unallocated": total - planned_total,
        "spend": grand["spend"], "float": grand["float"], "reserve": grand["reserve"],
        "gated_amount": gated,
        "ungated_spend": ungated_spend,
        "most_at_risk_if_nothing_sells": grand["spend"],
        "lanes": lanes_out,
        "budget_lines": line_rows,
        "fits": planned_total <= total,
        "labels": "Planning allocations (ASSUMED) unless an item gives a quote. Float comes back when Shopify pays out; spend does not.",
    }
    (folder / "budget_outputs.json").write_text(json.dumps(out, indent=1))

    def m(x):
        return f"${x:,.0f}"

    md = ["# Where the $1,800 goes (scripts/launch_budget.py)", "",
          f"Allocated {m(planned_total)} of {m(total)}; unallocated {m(total - planned_total)}.",
          f"Spend (gone once used) {m(grand['spend'])}; supplier float (comes back at payout) {m(grand['float'])}; reserve {m(grand['reserve'])}.",
          f"Spent only if a gate passes: {m(gated)}. Spent before any gate: {m(ungated_spend)}.", "",
          "| Lane | Window | Spend | Float | Reserve | Total | Of which gated |", "|---|---|---|---|---|---|---|"]
    for l in lanes_out:
        md.append(f"| {l['name']} | {l['window']} | {m(l['spend'])} | {m(l['float'])} | {m(l['reserve'])} | {m(l['total'])} | {m(l['gated_amount'])} |")
    md += ["", "| CLAUDE.md budget line | Planned | Allocated | Over by |", "|---|---|---|---|"]
    for r in line_rows:
        md.append(f"| {r['line']} | {m(r['planned'])} | {m(r['allocated'])} | {m(r['over_by'])} |")
    (folder / "budget.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main()
