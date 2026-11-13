# Commerce OS

The operating system for our premium DTC brand: one master context, one skill per agent, and scripts that do every calculation. Claude Code reads and writes this repo; nothing lives only in a chat.

## Start

```bash
cd commerce-os
git init && git add . && git commit -m "Commerce OS v0.1"
python3 scripts/test_economics.py        # 7 checks should pass
claude                                   # open Claude Code here
```

Then, inside Claude Code:

```
/product-scout
```

## What's in here

| Path | What it does |
|---|---|
| `CLAUDE.md` | Master context: budget, milestones, hard rules, pipeline and gates, financial rules, data labels, tool routing, approvals |
| `.claude/skills/product-scout/` | Agent 01. Discover 30 to 50 products, screen to 10, deep dive on 3. Ends at Gate 1 |
| `.claude/skills/supplier-validation/` | Agent 02. Up to 10 suppliers, 5 compared, 2 recommended for samples, inquiries drafted, never sent |
| `.claude/skills/creative-strategy/` | Agent 03. Competitor ad research, 10 original concepts, a test plan sized to the $400 first test |
| `.claude/skills/store-teardown/` | Agent 04. Reverse-engineer competitor and benchmark stores (Ridge, Quad Lock, Blueland) |
| `scripts/economics.py` | Pre-ad contribution, break-even CAC and ROAS, target CAC, cushion test, low, base and high scenarios |
| `scripts/score.py` | Product score out of 100 (margin points computed, not judged) and supplier scorecards, written to `reports/ranked_*.md` |
| `scripts/test_economics.py` | Hand-checked tests for the economics math |
| `data/*.csv` | The source of truth: candidates, economics inputs, suppliers, competitors, ads, daily performance. Every fact has a label and a source |
| `reports/decisions.md` | Every gate question and approval |
| `suppliers/_templates/inquiry.md` | Standard supplier inquiry |
| `examples/economics_example.csv` | A made-up product showing the input format, including a blocked scenario |

## How a product moves

Discover (G1) → preliminary economics (G2) → market validation (G3) → suppliers and samples (G4) → verified economics (G5) → brand and store (G6) → creative and launch (G7) → optimize. Dhruv decides every gate in `reports/decisions.md`.

## Not built yet

- Brand and store skill, and the growth analyst (daily performance pull). Built when a product reaches Gate 6.
- `scripts/pull_daily.py` for Shopify and Meta numbers.
- Permission rules in `.claude/settings.json` that force an approval prompt on Shopify, Meta and email write tools. Add once the exact tool names show up in `/mcp` on Dhruv's machine.
