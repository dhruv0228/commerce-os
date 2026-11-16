# Post check: @maddyglynn_ "Copy me + build a million dollar dropshipping brand" (2026-11-16)

Post: https://www.instagram.com/p/DfK2U2RIHFO/ (12 slides; 449 likes, 463 comments; account about 143k followers, read through the public embed 2026-11-16).

Labels: VERIFIED = seen in the post, the embed or a tool result. ESTIMATED = third-party figure. ASSUMED = our placeholder. INFERENCE = our reading.

## What the post claims

- **Curling iron:** costs $10.33 on AliExpress, sells for $60, "$50 profit".
- **Leggings:** cost $5.54, sell for $50, "$44 profit".
- **Neck pillow:** costs $11.55, sells for $80, "$68 profit".
- **The scale claim:** "Sell 5 a day for 45 days" gives $9,900 to $15,300, and "I make $1k-4k a DAY".
- **Proof shown:** blurred Shopify payout emails.

## Verified

- **The caption is a lead funnel.** It says "I train women...", claims "2,000+ women" in a mentorship program and "$3M in the online space", and closes with "Comment CLASS" for a free masterclass.
- **The Kalodata figures on screen belong to established brands, not to her stores:**

| Product | Brand | Revenue (Oct 1-30) | Units | Price shown | Avg unit price | Commission |
|---|---|---|---|---|---|---|
| Curling iron | SHEGLAM | $869.5k | 20.22k | $51.99-96.99 | not shown | 7% |
| Leggings | Halara | $1.02M | 35.29k | not stated | $29.00 | 10% |
| Neck pillow | VIPfree | $1.40M | 44.73k | not stated | $31.29 | 8% |

- **All three Kalodata listings say "Ship From Local"**, meaning US stock, not AliExpress parcels.
- **Her bookmarks bar shows "Import to Loox"**, a tool that imports reviews into a store.
- **The brand boards are labeled "... brand board PNG"** in a Claude window. They are AI mockups; no real product photos are shown.

## Amazon check (DataForSEO, 2026-11-16, units bought in the past month by price band)

| Keyword | Total | <$20 | $20-40 | $40-60 | $60-80 | $80+ | Median price (100+ units) |
|---|---|---|---|---|---|---|---|
| automatic hair curler | 95,350 | 450 | 9,900 | 54,200 | 24,700 | 6,100 | $48.50 |
| tummy control flare leggings | 39,350 | 28,400 | 10,950 | 0 | 0 | 0 | $16.99 |
| cervical neck pillow for sleeping | 221,450 | 1,000 | 150,350 | 64,500 | 500 | 5,100 | $39.98 |

- The curler really does sell at $40-80, but TYMO dominates the top listings.
- Leggings show no sales at $40+.
- The pillow sells at $20-60, and almost nothing at $60-80.

## Economics (`calc.py`, built on `scripts/fee_breakdown.py`)

**Cost assumptions:**
- Product cost is the AliExpress price plus 30% for tariff and import fees (ASSUMED). The US de minimis exemption ended for all countries on Aug 29, 2025.
- Shipping is set to $0 (generous ASSUMED).
- Acquisition is the Meta median cost per purchase: $38.99 for the curler and leggings, $47.93 for the pillow (home category).

**Profit per order on her own model (Shopify + Meta ads):**

| Product | At her price | At the price the market actually pays |
|---|---|---|
| Curling iron | $60: +$1.34 (tough -$10.36) | about $43 (SHEGLAM revenue / units): -$13.98 |
| Leggings | $50: -$1.44 | $28.90: -$20.45 |
| Neck pillow | $80: +$8.83 | $31.30: -$35.04 |

**What the slide math leaves out:**
- Ad cost per customer: about $39-48.
- Card and platform fees.
- Refunds.
- Duties.
- Shipping time from China: about 7-15 days per INFERENCE, which breaks our 2-8 day rule and the FTC Mail Order Rule promise.

## Verdict

**Not for us as shown.** Each product fails on a different point:
- **Leggings:** apparel with size returns, and no sales at her price.
- **Pillow:** "neck alignment" invites health claims, and $80 is far above where it sells.
- **Curler:** a hot electrical appliance, so it carries safety and certification risk. TYMO and SHEGLAM own the market. It is outside our niches. It is the only one with real premium sales; it could go to the scanner as a beauty candidate later.

**Compliance flags:**
- The earnings claims fall under the FTC Business Opportunity Rule.
- Importing supplier reviews into the store conflicts with FTC 16 CFR 465.
- AI brand boards must not become product photos (CLAUDE.md section 2).

## What we take from it

1. **Kalodata's TikTok Shop revenue, units and average unit price** are exactly the data our scanner lacks (upgrade 2). Price is roughly $36-49/month with a 7-day trial (ESTIMATED; sources conflict, so confirm on kalodata.com).
2. **Price at the average unit price, not the list price.** The scanner already does this on Amazon; it should do the same on TikTok Shop.
3. **A brand board as a step before the store build.** For us it uses photos of the real sample.
4. **Her core idea holds:** take a proven product and give it premium branding. It only works if the premium price is backed by sales data and a real product difference.
