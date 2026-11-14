# Hero-first deep dive, Nov 14, 2026

Follows Gate 1 (revised), option A: research four products already selling at $60+ in volume. All numbers come from `data/*.csv`, `economics.py` and the researchers' files; every cost is ESTIMATED or ASSUMED until suppliers quote.

## 1. Executive summary

- **One survivor: the dog back-seat extender kit ($149).** Base case: profit before ads $62.37, target ad cost $46.78 vs the $38.51 pet benchmark (cushion 1.21). It stays positive at benchmark x 1.3 (+$12.31). The pessimistic case fails.
- **Three rejected:**
  - **Puzzle station:** $8.94 before ads; the oversize carton bills as 37 lb, costing $35 to $48 per order.
  - **Grooming vacuum:** $4.63 before ads; about 37.5% tariff, Amazon MCF fees, and a mains appliance that needs safety certification.
  - **Putting kit:** $30.16 before ads; it only passes at $179.
- **Why the extender works:**
  - People already buy it at our price: 5,500+ a month above $130 on Amazon (mostly Ruff Liners at $169.99).
  - RuffRover sells almost exactly our kit at $169.95 on its own site, with 3,700+ ratings and Meta ads running 400+ days.
  - It has no electronics, the board folds into a small box, and pet ad costs are lower.
- **The catch is cash:**
  - No US warehouse sells it to us at a listed price, so we would have to buy 15 to 25 kits (about $900 to $1,500 landed) against a $300 stock line.
  - Patents (Ruff Liners US 12,221,024, 4Knines US 12,409,763) look avoidable with plain door guards that don't attach to the extender or the window. This is a quick screen, not legal advice.
- **Score: 71/100,** held back by suppliers (9/20). Confidence: medium-low.

## 2. Results by product

| Product | Price | Before ads | Target ad cost | Benchmark | Cushion | At benchmark x 1.3 | Verdict |
|---|---|---|---|---|---|---|---|
| Dog back-seat extender kit | $149 | $62.37 | $46.78 | $38.51 | pass (1.21) | +$12.31 | investigate further |
| Puzzle station kit | $149 | $8.94 | $6.70 | $34.85 | fail (0.19) | −$36.37 | reject |
| Dog grooming vacuum kit | $119 | $4.63 | $3.47 | $38.51 | fail (0.09) | −$45.43 | reject |
| Putting practice kit | $139 | $30.16 | $22.62 | $44.53 | fail (0.51) | −$27.73 | reject |

## 3. Amazon units per month by price band (floors)

| Product | under $40 | $40 to $80 | $80 to $130 | $130+ |
|---|---|---|---|---|
| Back-seat extender (hard bottom) | 9,500 | 11,600 | 5,400 | 5,500 |
| Puzzle boards and tables | 3,850 | 28,250 | 5,650 | 5,100 (tables) |
| Grooming vacuum | 1,000 | 16,300 | 11,800 | 200 |
| Putting mats | 2,300 | 3,350 | 350 | 650 |

## 4. The extender kit

- **What's in the box:**
  - A rigid 3-panel back-seat platform (Standard and XL), with a published sag test and a folded box of 20 inches or less.
  - A seat-belt tether.
  - Two door guards that hang from the window frame, not attached to the extender.
  - A fur-removal tool.
- **Costs per order (base):**
  - product $29
  - shipping $14.30
  - duties $18.80
  - packaging $2.50
  - fulfillment $4
  - refunds 8%
- **Your software edge:** a make, model and year fit finder that cuts fit returns, the #1 complaint.
- **Competitors** (full details in `data/competitors.csv`):
  - Ruff Liners: $169.99, Shark Tank
  - RuffRover: $169.95 direct
  - 4Knines: $169.99
  - URPOWER: $39.99 to $65.99
  - YJGF: $109.99
- **Suppliers:** 6 factories plus Amazon MCF and US-stock resellers, all `legitimacy_verified=unknown` (`data/suppliers.csv`).
- **Reorders:** weak. Products 2 and 3 should be a fitted cargo liner and a platform bed topper.

## 5. Risks and unknowns

1. A supplier with US stock, or approval for a 15 to 25 kit stock buy.
2. Real folded carton size and weight. This decides whether shipping is $13 or $24+.
3. Whether a $149 kit converts against RuffRover ($169.95) and URPOWER ($65.99), and the real fit-return rate.
4. Tariff classification (HTS 6307.90 is a guess). Duties are the biggest single cost after the product.
5. A patent design-around confirmed by a professional before ordering stock.

## 6. Gate 2 decision (dog back-seat extender kit)

- **A (recommended):** Advance to supplier validation. Claude drafts inquiries to the 6 factories and the 2 US-stock resellers; you send them. Order 2 samples (about $100 to $150 from the samples line). Decide the stock buy at Gate 5 on real quotes.
- **B:** Advance only if a US-stock supplier is found. No stock buy at all.
- **C:** Stop importing. Go back to the pet portrait (print on demand) at a proven $79 to $99 price with add-ons, and rerun the numbers.
- **D:** Pause and rethink the model: the budget, or channels with different ad costs (Amazon, TikTok Shop affiliates).
