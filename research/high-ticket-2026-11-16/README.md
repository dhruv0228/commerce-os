# High-ticket dropshipping vs our dog brand (2026-11-16)

Question from Dhruv: should we sell high-ticket items (saunas, golf simulators, cold plunges) that US suppliers dropship, instead of or alongside the dog brand?

## The model

- A store becomes an authorized online dealer for US brands or distributors that ship each order direct to the buyer.
- Products are usually $1,000 to $10,000.
- Gross margins: 15-35%, varying by source (ESTIMATED; affiliate-style guides, links below).
- Prices are usually locked by MAP (minimum advertised price) agreements.
- Traffic comes mostly from Google Shopping and Search, from buyers already looking for the product.
- It is heavily taught by course sellers (examples in the sources).
- Under CLAUDE.md section 1, reselling other brands is allowed for add-ons only, never the hero. Doing this would need Dhruv to change that rule.

## Google demand and click prices (DataForSEO, US, checked 2026-11-16)

Raw data: `google_ads_keywords.json`.

| Keyword | Searches/mo | Avg CPC | Competition |
|---|---|---|---|
| golf simulator | 165,000 | $4.50 | HIGH (100) |
| infrared sauna | 110,000 | $5.92 | HIGH (100) |
| cold plunge | 60,500 | $9.71 | HIGH (100) |
| outdoor sauna | 33,100 | $4.28 | HIGH (100) |
| golf simulator package | 1,600 | $7.02 | HIGH (100) |
| dog car seat cover | 12,100 | $2.18 | HIGH (100) |
| back seat extender for dogs | 1,300 | $2.08 | HIGH (100) |
| dog seat extender | 480 | $1.64 | HIGH (100) |

Every keyword shows HIGH competition.

## Illustration (`calc.py`)

**Inputs:**
- Margin: ASSUMED 20-25%.
- Card fee 2.9% + $0.30, plus the Amboras platform fee of 1%.
- Refund and damage allowance: 5% (ASSUMED).

**Results:**

| Case | Pre-ad profit | Target CAC (75%) | Clicks affordable per sale at target | Conversion rate needed |
|---|---|---|---|---|
| $4,000 sauna | $643.70 | $482.78 | 112 | 0.89% |
| $5,000 golf simulator | $554.70 | $416.03 | 59 | 1.69% |
| $3,000 cold plunge | $482.70 | $362.03 | 52 | 1.92% |

The actual conversion rate of a new store selling these items is UNKNOWN until tested.

**Comparison with the extender kit at scale** (`research/answers-2026-11-15/numbers.json`):
- Pre-ad profit per order: $71.27 on the DTC store, $59.50 on TikTok Shop.
- Clicks for the extender cost about $2.

## Risks specific to high-ticket on $1,800

- **Cash timing:** the supplier is usually paid when the order is placed, but new stores can have payouts delayed or held (CLAUDE.md section 4). One $3,000-5,000 order could need more cash than the whole budget (INFERENCE).
- **Freight:** damage, returns that cost hundreds of dollars in freight, and chargebacks on large orders.
- **Sales process:** phone and chat selling, installation questions, and supplier approval that takes days to weeks.
- **Price:** MAP caps the price, so stores compete on ads, content and service.

## Sources

- https://dropshippingchampions.com/blog/high-ticket-dropshipping
- https://www.salehoo.com/learn/high-ticket-dropshipping
- https://mywifequitherjob.com/episode374/
- https://upsell.com/blog/high-ticket-dropshipping
