# Consumables check: supplements and skincare, US-made or US-stocked, shipped direct

Checked 2026-11-19. Machine-readable rows: `consumables.json` (same folder; reseller rows carry `amazon_price` beside the MSRP `price`; extra fields hold sources, delivery times and minimums). It replaces the illustration numbers in `research/models-2026-11-19/inputs.json` for the skincare and supplement rows.

Labels follow CLAUDE.md section 5. Nothing here is a supplier quote, so nothing is VERIFIED. Published price lists and rate cards are ESTIMATED. Margins, CAC and payback are not computed here. Run them through the scripts.

## Executive summary

1. **Supplements stay out of scope.** CLAUDE.md section 2 excludes them, and the economics give no reason to reopen that. Category Meta cost per purchase is the highest found ($80.50 median, small agency sample). Amazon and TikTok Shop now require third-party lab testing. Meta can block Purchase-event optimization for health advertisers. The cheapest on-demand route (Rocktomic) costs $97 a month, and its Basic-plan creatine costs $14.97 against a $35.97 suggested price. Amazon sells magnesium glycinate from big brands at $11.70 to $27.
2. **Own-brand skincare made on demand (Blanka) is possible but slow and expensive per unit.** A 30 ml hyaluronic acid serum costs $14.90 plus $9.99 flat shipping. Made-to-order branded orders take about 8 to 14 business days, which breaks the 2-to-8-day rule, unless stock is held at Blanka. The same serum category sells on Amazon for $5.97 to $9.90 (Good Molecules, The Ordinary) at 20k to 100k+ units a month.
3. **Reselling K-beauty is a price-taker business.** COSRX Snail essence costs $9.26 wholesale from a US distributor with a $750 minimum. Its MSRP is $25, but Amazon sells it at $15.99 (50k+ a month). Anua is similar: $13.50 wholesale against $17 on Amazon. The real ceiling is the Amazon price, not the MSRP. Counterfeit and gray-market risk is real, and none of the four brands publishes an open US wholesale program.
4. **Benchmarks to use:** beauty Meta cost per purchase $39.31 (Triple Whale) to $51.45 (MHI); supplements $80.50 (MHI). The 12-month repeat rate is 26% for cosmetics and 29% for supplements, from older data. Subscription survival falls to 33.8% by the 3rd reorder and 9.8% by the 6th (Recharge cohorts). Consultancies put healthy payback at 3 to 6 months. They describe single-product supplement orders as losing money on the first order.

## 1. Own-brand supplements, made and shipped on demand in the US

| Item | Rocktomic (Georgia) | Supliful |
|---|---|---|
| Monthly fee | Basic $97, Launch $157, Scale $297 (Black Friday; list $497), after a 30-day trial | Pro $69/mo (about $48 billed yearly); a Free plan exists, but whether it fulfills orders is UNKNOWN |
| Fulfillment fee | $2.00 per item, label printing included | $1.99 first unit of each product, $1.29 each extra |
| Supplier card fee | 3.45% + $0.25 on what we pay them | not stated |
| Shipping | carrier rates, not published | USPS Ground Advantage: up to 0.5 lb $5.29, 0.76-1 lb $7.49, 1-2 lb $9.99 (updated 2026-09-01) |
| Delivery | picked in 1-2 business days, then 3-5 (USPS Priority) or 3-7 (UPS Ground) | 2-4 days in transit; processing time UNKNOWN |
| Minimums | none for dropship; 24 bulk; 197 custom | none; samples min 3 products x up to 3 units |
| Label design | Brand Book packages from $497 (optional) | add-on about $149 (older third-party figure) |

Unit costs (ESTIMATED; vendor pages, not quotes):

| Product | Suggested retail | Unit cost | Note |
|---|---|---|---|
| Creatine 300g (Rocktomic) | $35.97 | $14.97 Basic / $9.30 Scale | stated on rocktomic.com/pricing |
| Collagen 1&3 powder 350g (Rocktomic) | $39.97 | $14.99 Scale | derived from the stated 62.5% margin; Basic higher, UNKNOWN |
| Magnesium glycinate caps (Rocktomic) | $29.97 | $7.73 Scale | derived from 74.2%; an older page showed $5.52-6.62 |
| Collagen gummies (Rocktomic) | $29.97 | $7.58 Scale | derived from 74.7% |
| Supliful creatine / magnesium / collagen | $22-35 / $28-40 / $34-55 | $6-9 / $8-12 / $10-15 | vendor blog ranges (2026-11-12); real prices are behind login: UNKNOWN |

Market reality check (Amazon, DataForSEO, 2026-11-19):

- Creatine: Optimum Nutrition 60 servings (about 300g) sells at $17.97 (50k+ bought a month) and Nutricost 500g at $21.50 (100k+). Rocktomic's Basic cost for 300g is $14.97 before fees and shipping.
- Magnesium glycinate: Nature Made, Nature's Bounty and Pure Encapsulations sell at $11.70 to $27 (30k to 100k+ a month each).

Not reached: wholesalesupplementsplus.com and the Nutra on Demand site would not resolve (session network allowlist). Dropified's private-label supplement page returns 404, and its pricing page ($50/mo, $500/yr) now sells only an AI dropshipping tool, so that line may be gone (UNKNOWN). nerdbot.com returned 403.

Vendor bias: Rocktomic's "member revenue" and margin figures are marketing. Its Scale prices need $297 a month, which a $2,000 budget cannot carry.

## 2. Own-brand skincare made on demand in the US

**Blanka** (fulfills from Farmers Branch, Dallas, TX; public price list, checked 2026-11-19):

| Product | Cost to us | Blanka's suggested retail |
|---|---|---|
| Hyaluronic acid serum 30 ml | $14.90 | $35.00 |
| Hydrating facial cleanser 100 ml | $15.00 | $30.00 |
| Niacinamide vitamin boost serum 30 ml | $18.10 | $43.30 |
| Hyaluronic moisturizer | $28.70 | $64.30 |

- Shipping is a flat $9.99 standard or $29.99 expedited per US order (updated 2026-08-18). No per-order fulfillment fee is listed.
- Plans: Free $0 (3 products), Essentials $39/mo, Signature $79, VIP $149. Logo design is $500. Bulk discounts run 5% to 15% at 12+ units.
- Timing: branded made-to-order orders take 5 to 9 business days to produce (2 to 5 on VIP), plus 3 to 5 in transit. Stored inventory ships in 1 to 2 days.
- Blanka's $16 Oil-Free Daily Moisturizer lists octinoxate, a sunscreen drug active. Avoid it: selling it would make us a drug labeler.

**Rocktomic skincare:** Red Tea HA serum 2 oz, suggested retail $45.97, Scale cost $20.96 (derived). Vitamin C serum: $55.97 retail, 57.2% margin. Same $2 fee and monthly plans as above.

**UNKNOWN:**
- Supliful skincare (PDRN and retinol serums are in the catalog, prices behind login).
- Selfnamed: Latvian company with US fulfillment in Charlotte, NC. It claims 2 to 5 day US shipping and no MOQ, but prices are not public and its rate table is an image.
- Innacos: EU-based; only a catalog cover was indexed.

Market reality check (Amazon, 2026-11-19): hyaluronic acid serums sell for $5.97 (Good Molecules, 20k+ a month) and $9.90 (The Ordinary, 100k+ a month). La Roche-Posay sells for $39.99. A Blanka-label serum at $35 competes with dermatologist brands, not with the cheap leaders.

## 3. Reselling established K-beauty brands in the US

**Getting stock**
- None of COSRX, Beauty of Joseon, Anua or SKIN1004 shows an open US wholesale application in what I could reach.
- HeavenPrime (US) lists 129 brands with a $750 minimum order. It says it is authorized for "a number of" them, without naming which.
- Faire carries these brands through resellers ("Best Beauty Group" and others; minimums around $150), not through the brands. Faire pages returned 403, so wholesale prices were not visible.
- A Closo guide (2026, vendor) says US cosmetics distributors open at $500 to $2,500 and resellers keep 35% to 55% gross. Treat both figures as ESTIMATED.

| Product | Brand-site MSRP | Amazon price (bought past month) | US wholesale list (HeavenPrime) |
|---|---|---|---|
| COSRX Snail 96 essence 100 ml | $25.00 | $15.99 (50k+) | $9.26 |
| Anua Heartleaf cleansing oil 200 ml | $22.00 | $17.00 (50k+) | $13.50 |
| Anua Heartleaf 77 toner 250 ml | $23.00 | $19.69 (10k+) | $15.14 |
| SKIN1004 Centella ampoule 100 ml | $22.00 (site sells $19.80; one listing $8.80) | $19.00 (10k+) | not listed |
| Beauty of Joseon Glow Serum | $17.00 (site sells $11.90) | many sellers | BoJ Light On serum $13.57 |

- **Wholesale as % of retail:** these list prices work out from about 37% of MSRP (COSRX) to about 66% (Anua toner). Against the Amazon price they are much higher. The table above holds the raw figures; run the ratios through a script before using them.
- **MAP:** no published MAP policy found for any of the four brands (UNKNOWN). In practice, Amazon and the brands' own sites set the price.
- **Amazon gating and brand control:**
  - Beauty brand approval usually needs distributor invoices or a brand letter of authorization (secondary seller guides; no brand-specific rule confirmed).
  - Beauty of Joseon runs its own Amazon and TikTok Shop stores to push out unauthorized resellers (Glossy interview; BoJ FAQ).
  - Gudai Global, which owns Beauty of Joseon, TIRTIR and SKIN1004, set up an IP task force in 2024 that uses AI to flag listings.
  - A consumer blog says COSRX joined Amazon Transparency in late 2025, but I could not verify it.
- **Counterfeits:**
  - Korea Customs data shows losses from IP theft of K-beauty brands rose 24-fold in 2025 to about $15M, and 99% of fakes came from China.
  - A Foshan raid seized 56,000 fake items, including Beauty of Joseon and SKIN1004 (Korea Herald/ANN, 2025-11-07).
  - The DataForSEO Amazon search shows Relief Sun sold by many sellers at $6.99 to $28.99.
- **Olive Young and YesStyle:** us.oliveyoung.com returned 403. One guide says Olive Young Global dropped US direct shipping on 2026-05-29, and another claims a New Jersey warehouse selling 15% to 25% below Amazon on some items. Both are unverified. YesStyle was not checked.
- **Sunscreen:** sunscreens (Relief Sun and other SPF products) are OTC drugs in the US. Do not resell Korean-market versions.

## 4. Prices, ad costs, repeat and payback benchmarks

| Metric | Beauty / skincare | Supplements | Source |
|---|---|---|---|
| Median AOV | $55-75 (top 25% $80-115) | $55-80 (top 25% $90-130) | Carty Labs, 5,000+ Shopify stores, 2026-06-01 (vendor) |
| Meta cost per purchase | $39.31 median | Health & Wellness $40.53 | Triple Whale, Aug 2025-Jul 2026 (snippet; page blocked) |
| Meta CPA, agency sample | $51.45 (12 brands; 90-day $57.71) | $80.50 (9 brands; 90-day $84.93) | MHI Media clients, 29 Oct 2025-28 Oct 2026 |
| TikTok ads CPA | $10.32, but median ROAS 0.46 | H&W $11.17, ROAS 0.42 | Triple Whale via sovran.ai (checked 2026-09-29). The low ROAS makes the CPA unusable for planning. |
| 12-month repeat rate | 25.9% (cosmetics); vendor ranges 30-40%, strong brands 40-55% | 29.1%; range 29-36%, top quartile 40-45% | eightx.co (2026-06-29); 25.9% and 29.1% partly trace to Metrilo 2019 data, so they are OLDER |
| Subscription survival | not found | reorder 1: 86.6%, reorder 3: 33.8%, reorder 6: 9.8%, reorder 12: 1.4% | Recharge cohorts, about 1,800 brands, mid-2025 to mid-2026, via upcounting.com |
| CAC payback | about 2 to 10+ months depending on AOV and repeat | 3-6 months healthy; 1-3 for subscription cohorts; up to 9 for one-time buyers | eightx.co (CFO consultancy, 2026-06-07); finsi.ai |
| First-order result | not given as a benchmark | Eightx's worked example ($90 CAC, $45 AOV, 70% gross margin) needs about 2.86 orders to break even | eightx.co (illustration, not data) |

Triple Whale's 2026 Health & Beauty report says category cost per purchase rose 11.68% and conversion rate fell 14.34% year on year. The report is gated, so its median was not seen.

## 5. Regulation and insurance

**Supplements** (out of scope for us; summary only):
- **Claims:**
  - Structure/function claims need substantiation, a notice to FDA within 30 days of first marketing, and the DSHEA disclaimer (fda.gov, page updated 2024-03-28).
  - The FTC standard is competent and reliable scientific evidence, generally randomized controlled human trials. An endorser's claim must meet the same bar (FTC Health Products Compliance Guidance, Dec 2022).
- **Brand-owner duties:** the company named on the label must report serious adverse events to FDA within 15 business days. A regulatory consultant notes that the private labeler owns the claims, even when catalog copy came from the maker (Blue Ocean Regulatory, 2024, older).
- **Marketplaces and ads:**
  - Amazon requires third-party testing through approved TIC bodies; enforcement is reported from 2026-03-31, with scope disputed.
  - TikTok Shop requires ISO 17025 lab testing, and the supplement category is reported as invite-only.
  - Meta moved to claim-by-claim review in July 2026. Weight claims require 18+ targeting.
  - Meta's health-and-wellness tiers can block Purchase and Add-to-Cart optimization. These are vendor reports, not Meta text.
- **Insurance:** $2,800 to $4,500 a year typical (Insurance Canopy, broker). Other quotes run $350 to $810 for general liability only (TRUiC, The Hartford via Tivly).

**Cosmetics under MoCRA** (we would be the "responsible person" for any own-brand product; fda.gov page updated 2026-10-29):
- **Applies to us whatever our size:**
  - Report serious adverse events within 15 business days, and report follow-up information found within a year.
  - Keep safety substantiation records.
  - Put a US contact on the label for adverse event reports.
- **Product listing:** list each product with its ingredients and update the listings yearly.
- **Facility registration:** the manufacturer registers its facility, every 2 years.
- **Small-business exemption:** average gross sales under about $1M a year over 3 years (inflation-adjusted; the current exact figure is UNKNOWN). It exempts us from listing, registration and future GMP rules, but not from adverse event reporting, safety records or labeling. It does not cover eye-area, injected, internal-use or 24h+ appearance-altering products.
- **Recent FDA actions:**
  - The talc-testing proposal was withdrawn in November 2025.
  - FDA issued final mandatory-recall guidance on 2026-10-29.
  - Fragrance-allergen labeling is still pending.
- **Insurance:** $2,000 to $3,000 a year typical for indie cosmetics, $1,200 to $5,000 by risk (Insurance Canopy, broker). Another source puts topical beauty under $1M revenue at $1,000 to $1,800 (2026 guide). The median general-liability policy for online sellers is $850 (Assureful).
- **Reselling:** we are not the responsible person, but seller liability insurance is still needed.

## 6. Risks and unknowns

- No per-unit price from Supliful, Selfnamed, Innacos, Wholesale Supplements Plus or Nutra on Demand. Getting them needs logins or a quote request, and any request is a supplier message that needs Dhruv's approval.
- Rocktomic's Basic-plan unit costs are UNKNOWN except creatine. The derived costs are Scale-tier, the cheapest.
- Shipping from Rocktomic and from home uses Supliful's USPS table as a proxy, with ASSUMED weights.
- Repeat-rate figures are thin and partly from 2019. Vendor sources (Eightx, Finsi, reOtter) sell retention or finance services.
- Benchmarks come from established stores. Apply the CLAUDE.md new-store x1.3 case.
- Sources blocked: Triple Whale (Cloudflare), Faire (403), nerdbot.com (403), us.oliveyoung.com (403), wholesalesupplementsplus.com and nutraondemand.com (DNS outside allowlist).

## Confidence

- **Medium** on the skincare and reseller cost figures (public price lists read today).
- **Low to medium** on supplement unit costs (vendor-derived).
- **Low** on repeat rates and payback (consultancy blogs).
- **Medium** on Meta cost-per-purchase ranges (two independent sources, about $39 vs $51 for beauty).

## Recommended next action

Feed `consumables.json` into `scripts/model_compare.py` (or `economics.py`) and compare the skincare and reseller rows against the Barkfare extender rows. Use the Amazon price, not MSRP, as the reseller retail price, and the 1.3x tough case.
