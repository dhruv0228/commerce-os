# Barkfare add-ons and learning products: candidates

Checked 2026-11-22. Research only: nothing was bought, signed up for, logged into or sent.
Data file: `research/launch-plan-2026-11-22/candidates_barkfare-addons.json` (7 candidates, same schema as `research/fast-test-2026-11-21/candidates_home.json` plus `creator_fit_1to5`, `creator_fit_reason` and `tiktok_shop_evidence`).
No margin, CAC, ROAS or profit is computed here. The cost share column below was computed by the build script (best US landed cost divided by sell price), not by hand; the real test is `scripts/economics.py` and `scripts/fast_test_rank.py`.

Labels: VERIFIED = read on the primary page or API today (AliExpress US cards count as "as displayed", not supplier quotes). ESTIMATED = third-party figure or a sum of Amazon badge floors. ASSUMED = our placeholder. UNKNOWN = not found or blocked.

## 1. Bottom line

- Only three products clear the "US cost about one third of a proven price" bar, and all three are commodity soft goods: the soft back-seat hammock, the SUV cargo liner and the front seat cover. Their $70 to $110 prices are proven only for brands with reviews and warranties (4Knines, Ruff Liners, Team K9); most Amazon volume is at $20 to $46.
- None of the seven is a strong stand-alone Meta product. The hammock is the best Black Friday and Christmas learning product for the Barkfare name: light, easy to film, sold by creators in this category already, $24.58 US-stock cost with 473 sales on the card. The others work as order-value add-ons to the extender.
- The most important finding is outside this group: US-stock hard-bottom back-seat extenders showed on AliExpress US cards today at $47.31 and $48.92 with free shipping and 6-day delivery tags (section 4). The Nov 21 ranking used $76.99. If one of these matches the hero spec, Barkfare's own economics change more than any add-on can.

| # | Candidate | Sell price | Price basis | Best US landed cost | Cost share (script) | Amazon units/mo at $40+ (floor) | Creator fit | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | waterproof-dog-hammock-seat-cover | $69.00 | Proposed kit; 4Knines $79.99 (300+ a month on each of 2 Amazon listings, 911 DTC reviews), Ruff Liners $109.99 (500+ a month, 1,507 reviews) | $24.58 (473 sold) | 0.36 | 2,500 over 17 listings | 4 | Best learning product; commodity risk |
| 2 | suv-cargo-liner-dog | $69.00 | Proposed; 4Knines and Team K9 list $79.99 (no sales counts); Amazon $90 to $96 at 200+ a month | $21.42 (no sales on card) | 0.31 | 1,900 over 13 | 3 | Add-on for SUV owners; weak source |
| 3 | front-bucket-seat-cover-dog | $44.99 | 4Knines on Amazon, 200+ a month, 1,800 ratings | $15.45 (3 sold) | 0.34 | 300 over 3 | 2 | Add-on only |
| 4 | dog-car-door-covers-2pack | $29.99 | Proposed; Amazon $25.99 at 1,000+ a month | UNKNOWN | n/a | 0 (all volume under $40) | 3 | Already in the hero kit; no US source; patent check needed |
| 5 | backseat-dog-car-bed | $59.49 | Ruff Liners on Amazon, 300+ a month | $48.09 (closest match, no sales) | 0.81 | 3,450 over 15 (mixed with boosters) | 3 | Good bundle idea, no matching US source |
| 6 | custom-pet-portrait-canvas | $62.00 | Crown & Paw 12x18 canvas | $35.38 (ESTIMATED, Printful) | 0.57 | 0 | 5 | Best creator fit, fails cost test, crowded |
| 7 | folding-dog-car-ramp | $75.98 | Amazon generic, 3,000+ a month | $54.19 (no sales) | 0.71 | 17,100 over 60 | 4 | Big demand, fails cost test, heavy |

## 2. Method

- Demand: DataForSEO live Amazon US search, 31 keywords, 100 results each, de-duplicated by ASIN and filtered by title words per candidate (filters written in each `amazon.checked` field). A listing counts toward `bought_past_month_top_listings` if priced $40 to $400 with a "bought in past month" badge; badges are floors, so sums are floors. Seven ASIN detail reads for weights.
- Search volume: DataForSEO Google Ads, US, 24 keywords, monthly values to Oct 2026 (ESTIMATED).
- DTC prices: public Shopify `/products.json` feeds of ruffliners.com, 4knines.com, lussogear.com, teamk9.com, petsvetsupply.com, firmpaw.com, solaracovers.com, crownandpaw.com and originaldoggybag.com (VERIFIED). Review counts read on the 4Knines and Ruff Liners hammock pages.
- Supply: AliExpress US search cards in headless Chromium with `shipFromCountry=US`, 13 queries. Rule for `best_us_landed_cost` (same as Nov 21): lowest card price that matches the product, shows free shipping and has no "New shoppers" tag. Prices moved between reads on the same day (the $24.58 hammock showed $16.58 with a new-shopper tag on a later read).
- Print on demand: Printful public catalog API (canvas unit prices) and printful.com/shipping (canvas US rates).
- Ads: Meta Ad Library in Playwright (US, active, keyword search), 7 queries.
- TikTok Shop: web search only.

## 3. Findings by candidate

### 3.1 Soft back-seat hammock (learning product)

- Demand is large but cheap: 96 badged soft-hammock listings sum 44,050 units a month, 41,550 of them under $40. URPOWER alone sells 9,000+ at $23.98 and 1,000+ at $33.99 with 47,000 ratings.
- The premium tier exists but is narrow: 2,500 units a month at $40+, led by Ruff Liners ($109.99, 500+) and 4Knines ($79.99, 300+ on each of two listings).
- Ads and creators: "dog car seat cover" has about 5,400 Meta keyword results; PetsVet Supply, Team K9, Ruff Liners, 4Knines and FirmPaw were on the first screen, and 4Knines runs at least two creator partnership ads. This is the category where creators already sell.
- Search: "dog car seat cover" 12,100 a month, "dog hammock for car" 4,400, flat across the year.
- US stock: $24.58 with 473 sold and a 6-day tag; mesh-window version $27.60 with 5 sold.
- Patent note: Ruff Liners' door protection uses window inserts (repo: US 12,221,024). Do not source door flaps that clip into the window seal.

### 3.2 SUV cargo liner

- Amazon: 5,950 units a month over 33 listings, best seller $33.23 at 1,000+. At $40+: 1,900 units over 13 listings, with XL liners at $90.09 and $95.99 selling 200+ each.
- DTC: 4Knines lists $79.99 to $149.99 and Team K9 $79.99, with no sales counts read.
- Google demand is tiny ("cargo liner for dogs" 320 a month). Cheapest US source ($21.42) has no sales and an unconfirmed spec.

### 3.3 Front bucket seat cover

- Only 4Knines sells at $44.99 with volume (200+ a month). Everything else is under $30. US stock $15.45 with 3 sold. Add-on only.

### 3.4 Door covers, 2-pack

- Amazon sells 3,750 units a month over 23 listings, all under $40 (best $25.99 at 1,000+). PetsVet Supply ($39.99) and 4Knines ($44.99) list higher without visible sales.
- No US-stock source found in three AliExpress US searches. The repo's patent notes (4Knines US 12,409,763; Ruff Liners US 12,221,024) apply to hook-in designs.
- These are already part of the hero kit at launch (CLAUDE.md section 0).

### 3.5 Back-seat dog bed

- Ruff Liners sells a back-seat bed at $59.49 with 300+ a month on Amazon, and both Ruff Liners and Team K9 sell a bed made to sit on their own hard-bottom extender. That proves the "extender plus bed" bundle.
- No US-stock bed sized to the extender was found. The closest large-dog item is a booster at $48.09 with no sales; a BingoPaw bolster bed at $21.97 is probably the smallest size.

### 3.6 Custom pet portrait canvas (gift)

- Strong December pull ("custom pet portrait" 12,100 in Dec 2025; "crown and paw" 9,900 in Dec 2025) and the highest creator fit.
- Crown & Paw charges $62.00 for a 12x18 unframed canvas; Printful's 12x18 canvas is $24.99 plus about $10.39 US shipping, so it fails the one-third test at the same size. Meta shows about 3,000 keyword results across many small sellers. It was parked once already (2026-11-13).

### 3.7 Folding dog car ramp

- Largest demand in this group (17,100 units a month at $40+ over 60 listings; "dog ramp for car" 12,100 searches in Oct 2026) and a great senior-dog video, but US-stock ramps cost $54.19 to $56.29 against $59.99 to $75.98 proven prices. Heavy and load-bearing.

## 4. Lead for the hero (not re-scouted, flagged for the extender owner)

AliExpress US cards read today with the ship-from United States filter, free shipping and "Fastest delivery in 6 days":

| Card | Price | Tags | Note |
|---|---|---|---|
| https://www.aliexpress.us/item/3256812978307212.html | $47.31 | no promo tag, no sold count | "Back Seat Extender for Dogs Hard Bottom ... Dog Travel Bed" |
| https://www.aliexpress.us/item/3256812341106652.html | $48.92 | no promo tag on one read; "Early bird deal, only 1 left" on another | BingoPaw large hard-bottom extender with pockets |
| https://www.aliexpress.us/item/3256812407081941.html | $54.36 to $57.36 | "New shoppers" tag | mesh window, 220 lb |
| https://www.aliexpress.us/item/3256812503963297.html | $66.69 | no promo tag seen | 53 x 24.8 in, 350 lb, mesh window |

The build script put $47.31 and $48.92 at 0.32 and 0.33 of the $149 hero price. Size, board rigidity, weight rating and stock depth are UNKNOWN until an item page or sample is read. Worth a supplier-validation pass before any add-on work.

## 5. Screened out today

| Product | Evidence (Amazon floors, 2026-11-22) | Reason |
|---|---|---|
| Dog seat belts and car harnesses | 44,800 units a month under $30 vs 2,800 at $30 to $60; crash-tested harnesses (EzyDog $125) need certification | Too cheap; safety claims need certificates |
| Travel water bottles and bowls | 18,050 units under $30, 150 at $30 to $60 | Too cheap |
| Dog travel bags | Original Doggy Bag $38.95 to $44.95 at 200+ a month; most results are pet carriers | Weak demand at the needed price |
| Wire car barriers | Best sellers $28 to $34 (1,000+); PetSafe $69.98 at 100+ | Cheap, fit returns |
| Collapsible soft crates | $64.99 (600+) and $84.99 (700+); one US-stock soft kennel at $26.49 of unknown size; 12.9 lb listing weight | Heavy, weak car link, size unmatched |
| Portable paw cleaners | 35,150 units under $30 | Too cheap |
| Portable showers | Rechargeable camping pumps $36 to $40 (1,000+) | Battery item, not dog-car specific |
| Team K9 backseat USB cooling fan ($59.99 to $179.99 in its feed) | Not researched further | Summer product, off season now |

## 6. What blocked or limited the work

- Foreplay MCP: HTTP 402, "Insufficient credits". No Foreplay data.
- Meta Ad Library (Playwright): loaded for "dog car seat cover" (second try), "dog hammock", "4knines" and "custom pet portrait"; empty pages for "ruff liners" and "cargo liner for dogs". Counts are keyword matches, not ads per product.
- AliExpress item pages were not opened (captcha on 2026-11-21); shipping and delivery come from card tags, stock depth is unknown, and prices changed between reads the same day.
- CJdropshipping was not retried (human verification on 2026-11-21). Zendrop and Spocket need logins (not attempted).
- TikTok Shop sold counts: two web searches found none for these products (one booster seat listing with 5 sold). All `tiktok_shop_evidence` fields are UNKNOWN except that note.
- kurgo.com has no public `/products.json` (404); myfunnyfuzzy.com refused the connection.
- No patent search was run today; patent notes repeat the repo's earlier findings and what pages said.
- Weights are UNKNOWN for most items; only door covers (14.4 oz) and the Ruff Liners bed (1.93 kg) were read.
