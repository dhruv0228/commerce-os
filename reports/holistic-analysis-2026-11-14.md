# Holistic product analysis, Nov 14, 2026

Built around Dhruv's answers on Nov 14 (decisions log):
- channels open
- $1,800 firm
- test before stock (self-ship)
- US-only delivery
- margins decide price
- virality core
- goal $10k+/month profit

Data: `research/universe-2026-11-14/` (4 niche universes plus manual entries) and `research/business-models-2026-11-14.json`. Scoring: `scripts/opportunity.py` (output `data/opportunities.csv`, `reports/ranked_opportunities.md`). Channel math: `scripts/channels.py` with `data/channel_params.json`. All costs are ESTIMATED or ASSUMED until suppliers quote.

## 1. Executive summary

- **What was analysed:** 462 Amazon searches gave thousands of listings (pets 5,713, home 6,503, tech 5,929, outdoor not recorded), grouped into 505 product types. 443 passed the first filters, before the exclusion checks on the top 30 per niche. The top 30 per niche (120 products) were checked on margin, ease of getting the product, virality and seasonality. Then the deep-dived back-seat extender kit was added, for 121 products in all.
- **Only 6 of 121 pass both must-haves:**
  - a demo score of 3 or more (virality)
  - $8 or more profit per order at scale in the tough case (the floor for reaching $10k a month)
- **The best score is 78/100: the dog back-seat extender kit at $149.** No product scores near 100. Section 4 explains why.
- **Recommended launch order:**
  1. Back-seat extender kit (78)
  2. Dash cam (72)
  3. Knife sharpener (69, with the premium rolling version pending a patent check)
- **Best business model** (`research/business-models-2026-11-14.json`): a hybrid.
  - Start: TikTok Shop with creator affiliates, paid per sale.
  - Alongside: the Amboras store for bundles, email and a bigger order value.
  - Later: Amazon FBA for proven winners.
  - Why: Meta ads cost $38 to $52 per buyer up front, while affiliates cost a commission only when a sale happens.

## 2. The six that pass both gates

| Score | Product | Price | Best launch channel | Profit/order at scale (tough) | Test batch (tough) | TikTok aff | Own store + Meta | Amazon FBA |
|---|---|---|---|---|---|---|---|---|
| 78.2 | Dog back-seat extender kit | $149.00 | Amazon FBM* | $41.76 | −$11.03 | $44.45 | $43.07 | $53.51 |
| 72.3 | Dash cam | $109.99 | TikTok aff | $15.75 | −$26.01 | $23.77 | $3.88 | $24.26 |
| 69.8 | iPad keyboard case | $76.24 | TikTok aff | $27.36 | −$18.14 | $32.17 | −$3.43 | $16.98 |
| 69.0 | Knife sharpener | $33.99 | TikTok aff | $10.21 | +$2.80 | $12.44 | −$28.23 | −$0.63 |
| 68.3 | Bluetooth speaker | $69.98 | TikTok aff | $26.27 | +$0.32 | $30.63 | −$6.43 | $14.67 |
| 58.7 | Car floor mats | $61.45 | TikTok aff | $13.01 | −$58.91 | $17.30 | −$13.95 | $9.82 |

\*By tough-case profit the extender's best start is Amazon self-shipped. TikTok affiliates and the own store are within a few dollars, and FBA is best once stock is in place.

**Near misses** (demo 3+, $5 to $8 profit at scale): car vacuum, LED strip lights, artificial plants, spin mop, TV backlight, massage gun, wireless charging station.

**High scores that fail the virality gate:** wireless mouse (71.8), gaming headset (70.6) and gaming mouse (69.6). They have good margins but no visual wow, and big brands dominate.

## 3. Test vs scale

A small test batch flown in from a factory almost always loses money per order. The losses come from express air at about $12/kg, about 41% China tariffs, retail postage and creator samples. Big sellers make $20 to $60 items work only through volume: sea freight, factory volume pricing and negotiated shipping.

So the $1,800 should buy **evidence that people buy**, not profit. Products with a light, small box keep the test cheap: the knife sharpener tests at +$2.80 an order, the extender at −$11.03.

## 4. Why nothing scores near 100

A 100 needs all of these at once:

- thousands sold every month by many sellers at our price
- $25+ profit per order after paying to win a buyer, even in the tough case
- a 3-second wow on video, with proof that videos of it sell
- a US source or a tiny light box
- sales all year round
- a refill or reorder

These pull against each other. Proven, viral products attract many sellers, who compete margins down. High-margin products are usually either branded (with moats and patents) or not visual.

Score is raised by the offer, not by finding a magic product:
- a premium kit that lifts the order value
- owned content, such as your AI twin and real creators
- a brand that lowers ad costs over time
- a reorder product as product 2

## 5. Seasonality of the finalists

- **Back-seat extender:** steady, with a peak-to-trough ratio of 1.49; January at 0.84 of the average.
- **Dash cam:** ratio 1.83; peaks in December, January at 1.07.
- **Knife sharpener:** ratio 3.32; January at 2.07, the peak.

## 6. Risks and unknowns

1. No supplier quotes yet. Every factory cost is a listing snippet.
2. US-warehouse dropship prices are unknown: CJdropshipping blocks automated access.
3. Tariff rates are taken at 40.8%, the higher typical figure; they could be lower.
4. TikTok Shop's referral fee is taken at 8%, though the published rate is 6%. New sellers are paid 31 days after delivery.
5. Patents:
   - Extender: avoidable by design (quick screen).
   - Rolling sharpeners: HORL holds about 12 US patents.
   - iPad keyboard cases may conflict with Apple design patents.
6. Electronics (dash cam, speaker, iPad case) need FCC certification through the factory, and have higher return rates.

## 7. Decision (Gate 1 for the new universe)

- **A (recommended):** Launch track for the dog back-seat extender kit: Gate 2 passed; supplier validation next. Keep the dash cam as product 2 in research. Put the rolling knife sharpener through a patent check and a factory quote.
- **B:** Same as A, but research the dash cam in parallel now.
- **C:** Pick a different finalist from section 2.
- **D:** Widen the search first (more niches, or paid TikTok Shop data such as EchoTik Pro at about $14 to $29 a month).
