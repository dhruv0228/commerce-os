# Fast test lane: pet product candidates (dogs and cats)

Checked 2026-11-21. Research only: nothing was bought, signed up for, logged into or sent.
Data file: `research/fast-test-2026-11-21/candidates_pets.json` (7 candidates, one object each).
No margin, CAC, ROAS or profit is computed here; the JSON only carries inputs for `scripts/economics.py`.

Labels: VERIFIED = read on the primary source today. ESTIMATED = third-party figure or a sum of Amazon badge floors. UNKNOWN = not found or blocked. PROXY = a retail price used only as a stand-in for a cost we could not read.

## 1. Bottom line

- The brief asked for 8 to 10. Only 7 are worth passing to the scripts, and only the first two look like real fast-lane options on the raw numbers. The other five are kept so the scripts can show why they fail, not because they are recommended.
- Fast-lane exception in force: ads may start the same day one sample unit is ordered. That is flagged on every candidate, not used to reject any.
- Ranking inside this category:

| # | Candidate | DTC price read today | Best US landed cost read today | Amazon units a month at $40+ (floor) | Why it sits here |
|---|---|---|---|---|---|
| 1 | Cordless stainless cat water fountain | $74.95 (KittySpout) | $31.29 (thin listing; proven listings $28.10 and $30.75 carry a new-shopper tag) | 17,250 over 24 listings | Sells on Amazon, four small DTC stores are advertising it now at $75 to $132 (Petlibro and HomerunPET sell at $69.99), 1.5 lb, filters reorder. Petlibro is a whale; battery and pump defects are the refund risk. |
| 2 | Small-dog booster car seat | $69.99 (FunnyFuzzy) | $21.88 (no sales shown) to $35.13 (27 sold) | 16,000 over 75 listings | Same customer as Barkfare. FunnyFuzzy has 626 reviews and ships in 7 to 30 business days, so 2 to 8 day US delivery is a real edge. Only 3,900 units sell at $60 or more on Amazon. |
| 3 | Waterproof pet throw blanket | $79.00 (Paw.com) | UNKNOWN | 4,850 over 15 listings (almost all sofa covers) | Best 3-second demo. No US-stock source found, two whales, Amazon sells throws at $18 to $30. Cannot start this week on this evidence. |
| 4 | XL stainless litter box kit | $58.99 (HAPAW) | $30.69 | 54,850 over 104 listings | Largest demand in the scan, but it is an Amazon commodity at $42 to $57 and the DTC price is under the $60 floor. |
| 5 | Foam dog stairs for bed | $69.99 (FunnyFuzzy) | $56.39 (5-step) | 21,250 over 67 listings | US cost for the size that sells is about the same as Amazon's retail price. About 10.4 lb. |
| 6 | Lightweight pet stroller | $84.99 (Amazon median, no DTC price verified) | $37.89 | 10,200 over 56 listings | Good spread of sellers at $60 or more, but about 11 lb (edge of the weight screen), off season until spring. |
| 7 | Dog force dryer (the video's example) | $109.99 (HomerunPET) | $52.42 | 9,250 over 39 listings | Mains heated appliance with unknown certification, about 10.3 lb, Shelandy and oneisall entrenched. Weakest. |

- Candidates with a US-stock cost read today: 6 of 7 (all but the blanket). Important limit: every one of those is a price on an AliExpress search card with the ship-from United States filter on. Item pages were captcha-blocked, so size or variant, stock depth and the regular price after the Black Friday promotion are not confirmed. Treat them as VERIFIED "as displayed", not as supplier quotes.

## 2. How the numbers were built

- Demand: DataForSEO live Amazon US search, 64 keywords, 100 results each. A listing counts if it is priced $40 to $400 and shows a "bought in past month" badge. Badges are floors ("1K+"), so every sum is a floor. Listings were de-duplicated by ASIN across keywords and filtered by title words (filters are written in each `amazon.checked` field).
- Search volume: DataForSEO Google Ads, US, monthly values Nov 2025 to Oct 2026 (ESTIMATED).
- DTC prices: each store's public storefront search JSON, then the product page for review counts (VERIFIED). Most stores were on sale for Black Friday, so prices are sale prices.
- Supply: AliExpress search with the ship-from United States filter, read in a headless browser. Rule used for `best_us_landed_cost`: the lowest card price that (a) matches the product whose sell price is quoted, (b) shows free shipping and (c) does not carry a "New shoppers" tag, because a repeat dropship order will not get a first-order discount. Where the most-sold listing has that tag, it is listed in `supply` with the tag noted.
- Weights: Amazon product detail of the leading comparable listing (ESTIMATED for our unit).

### Price-band view (Amazon units a month, floors)

| Candidate | Under $40 | $40 and up | $60 and up | Note on the $60+ tier |
|---|---|---|---|---|
| Cat fountain (wireless only) | 18,700 | 17,250 | 6,150 over 7 listings | Petlibro 4,500, KittySpout 1,000 |
| Booster car seat | 24,550 | 16,000 | 3,900 over 24 listings | Lealchum 2,650 |
| Waterproof blanket and couch covers | 103,650 | 4,850 | 50 over 1 listing | Premium exists only in DTC |
| Stainless litter box | 49,150 | 54,850 | 9,700 over 45 listings | 2-packs and XXL sizes |
| Dog stairs | 40,850 | 21,250 | 8,450 over 37 listings | Miorun 1,700, rest unbranded |
| Pet stroller | 1,500 | 10,200 | 6,250 over 40 listings | ROODO 1,550, Zoosky 1,200 |
| Dog force dryer | not meaningful (human dryers in results) | 9,250 | 8,000 over 32 listings | Shelandy 3,700 |

Against the house hero-first rule (already selling in volume at $60 or more from several sellers): strollers, stairs and litter boxes meet it on Amazon; the fountain meets it only with Petlibro counted; the booster seat and the blanket do not meet it on Amazon and rest on DTC evidence.

## 3. US stock or China-shipped, for this category

- US stock is the practical choice on what could be read. US-filter listings showed free shipping and "fastest delivery in 6 days" on the card.
- China-side landed cost is UNKNOWN for every candidate: cards without the US filter do not show shipping, and item pages were blocked. Where a comparable card could be read, the China-side unit price was not lower than the US-stock price for the bulky items (litter box $44.93 against $30.69; dryer $52.79 against $52.42), and lower only for small items (fountain $12.02, console seat $14.44) before unknown shipping.
- The leading DTC seller of booster seats, stairs and couch covers (FunnyFuzzy) states processing within 15 business days and standard US delivery in 7 to 30 business days (VERIFIED on its shipping policy page), and a visible review complains about it. Fast US delivery is the one clear way to stand out.

## 4. Rejected, and why

Numbers are Amazon floors at $40 or more unless stated; AliExpress prices are US-filter search cards read today.

| Product | Evidence | Reason |
|---|---|---|
| Heated outdoor cat house | 53,550 units over 138 listings, median $70.38; "heated cat house" 33,100 Google searches in Dec 2025 | Strongest winter demand in the scan, but US-stock cards read $57.71 to $109.41 against Amazon prices of $56.52 to $89.99, so there is no room. Mains heating pad used outdoors with unknown UL or MET listing: safety exclusion. Unheated houses sell only a few hundred each. |
| Cat exercise wheel | 3,100 units over 19 listings, $59.49 to $185.72; US card $55.54 (493 sold, new-shopper tag) | A 31 to 48 inch wheel is far over the 10 lb screen (exact weight not read) and costly to return. Revisit only if the weight rule is relaxed. |
| Automatic ball launcher | 5,900 units over 43 listings, median $52.99; many new no-name sellers | Only US card for a real launcher read $46.42, about the Amazon retail price. Motor and moving parts, possible iFetch patents. |
| Indoor grass potty with tray | 5,450 units over 25 listings, median $59.49 | US cards $56.98 to $125.39, at or above Amazon retail. |
| Cat wall shelves | 4,650 units over 40 listings | US cards $49.33 to $58.39 for sets that sell at $45.99 to $68.99; wall mounting causes returns. |
| Dog grooming vacuum kit | 28,200 units over 48 listings | oneisall 10,200, Buenkee 4,200 and Neakasa 3,200 hold most of it; mains appliance of about 8.7 lb (earlier scan). |
| Automatic cat feeder | 28,850 units over 49 listings | Petlibro 8,150 and oneisall 8,100; app and cloud dependency. |
| Dog clipper kits | large, but oneisall, Wahl and Andis lead | Brand-owned. |
| Absorbent dog door mat | 1,250 units over 6 listings, 1,000 of them the Muddy Mat brand; "muddy mat" 135,000 Google searches against 390 for "dog door mat" | Demand belongs to a TV brand name we cannot use. |
| Soft dog seat cover or hammock | 2,050 units over 8 listings; 4Knines leads | Thin above $40 and overlaps the Barkfare extender lane. |
| Dog ramp or steps for cars | 24,200 units over 61 listings | Already researched (works only on FBA per the Nov 19 synopsis); heavy. |
| GPS tracker collar | earlier scan | Needs a cellular service backend. |
| Dog talking buttons | 750 units over 6 listings, 650 of them the Speak Up brand | Brand-led; generic sets sell under $40. |
| Dog lift harness | 1,850 units over 12 listings | Mobility aid, too close to the medical exclusion. |
| Large calming or orthopedic bed | 5,700 units over 21 listings; Bedsure leads | Bulky, crowded, whales (Bedsure, Paw.com). |
| Soft collapsible crate | 6,050 units over 23 listings; Amazon Basics at $40.12 | Commodity, bulky (weight not read), no DTC premium found. |
| Dog travel gear bag | 200 units at $44.95 (the rest of that search is airline carriers) | No demand at the price needed. |
| Foldable dog bathtub | 1,800 units over 16 listings | Bulky, thin. |
| Elevated bowls | 2,550 units over 10 listings; Neater leads | Brand-led, thin. |
| Dog or cat backpack and sling carriers | 1,850, 1,200 and 450 units in three searches | Thin above $40. |
| Dog winter coat and boots | 1,400 and 850 units; Carhartt and Canada Pooch lead | Brand-led, sizing returns. |
| Dog drying robe, paw washer, nail scratch board, shower sprayer, window perch, self-warming bed, car barrier, interactive ball, agility set | 0 to 2,050 units each | Not enough sales at $40 or more. |
| Snuffle mat, lick mat, slicker and steam brushes, hair remover, water bottle, puzzle toys, nail grinder | under $20 to $25 on Amazon (earlier scan, `research/platform-winners-2026-11-15/winners_scored.csv`) | Cannot reach $60 without stacking cheap parts, which the house rule says does not earn a premium. |
| Anti-bark devices, remote training collars | earlier scan | Efficacy claims and shock: safety and claims exclusions. |
| Self-cleaning litter box, pet door, playpen, cat tree, crate furniture | earlier scan | Heavy or complex returns. |

Vendor "winning product" lists added nothing that survived: CJ's November 2026 list has one pet item (washable plush bed), AutoDS's November list is not pet-focused, HyperSKU's list of 25 is mostly low-priced accessories (its dearer entries, dryers at $65 to $120, ramps at $55 to $95 and feeders at $45 to $89, are covered above), and Zendrop's public pet page shows 20 items costing $0.73 to $11.93.

## 5. Sources that blocked or failed

- CJdropshipping: search and product pages redirect to a Cloudflare human check (WebFetch and Playwright). No US-warehouse price could be read. A further attempt to query other CJ endpoints was denied by the session's permission system and was not retried.
- AliExpress item pages: captcha in Playwright, login redirect in WebFetch. Only search result cards were readable. With the US filter off, cards do not show shipping, so China-side landed costs are UNKNOWN.
- Zendrop: catalog behind login; only the public pet showcase was readable.
- AutoDS marketplace, Syncee: behind login, not read. Spocket: WebFetch returned 403 and the public search returned no results. TopDawg: search redirects to the home page. Doba: listings and processing days visible, prices need a signup.
- Foreplay MCP: 402, no active subscription.
- Meta Ad Library: loaded results for 5 of 19 attempts in Playwright, then returned an empty page (throttled). Read: "cat water fountain" about 410 results; "waterproof dog blanket" about 5; "dog booster seat" about 3; "dog car seat bed" about 1; loose search "dog car seat" about 16,000 (matches unrelated ads). Everything else is UNKNOWN. The Meta Ads Connector library search returned unrelated ads and was not used.
- Kalodata, FastMoss, Minea, Winning Hunter, Sell The Trend: no readable November data without an account. AfterShip's TikTok Shop pet page gave category scores only, so product-level TikTok Shop evidence is UNKNOWN.
- petgear.com (503) and ibiyaya.com (404); iprimio.com, snoozerpetproducts.com and bestpetsupplies.com do not expose a storefront search JSON.
- Amazon Best Sellers and Movers and Shakers pages were not opened; DataForSEO search results and product detail (including Best Sellers Rank) were used instead.

## 6. Bias to keep in mind

- CJ, AutoDS, Zendrop, HyperSKU, Dropified, Eprolo and Doba blog posts are vendor marketing; their margin ranges are unverified and were not used.
- "Best dog stroller" roundups are affiliate pages; only weights and retailer prices were taken from them, labeled ESTIMATED.
- DTC compare-at prices ($149.95, $279.00 and so on) are the sellers' own anchors, not evidence of what people pay.
- Long-running or numerous ads are a signal, never proof of profit.

## 7. What must be checked before any go decision

1. Open the listed AliExpress items in a logged-in AliExpress or DSers account (Dhruv's action) and record the real variant price, shipping line, delivery estimate and stock for a repeat buyer. Until then every US cost is "as displayed".
2. CJ and Zendrop US-warehouse price and stock for the fountain and the booster seat (login needed).
3. Battery and electrical certification for the fountain; none for the dryer means it stays out.
4. One sample of the chosen product ordered the day ads start, and no claim on the page that the sample has not proven.
5. Run `scripts/economics.py` on the JSON inputs with the pets cost-per-purchase benchmark already in `data/channel_params.json` ($38.51, ESTIMATED) and the tough case.
