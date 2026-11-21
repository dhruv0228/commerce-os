# Fast test lane: beauty tools, personal-care devices, hair tools, massage and recovery, home fitness accessories

Checked 2026-11-21. Research only: nothing was bought, signed up for, logged into or sent.
Data file: `research/fast-test-2026-11-21/candidates_beauty-fitness.json` (5 candidates, one object each).
No margin, CAC, ROAS or profit is computed here; the JSON only carries inputs for the scripts.

Labels: VERIFIED = read on the primary source today. ESTIMATED = third-party figure or a sum of Amazon badge floors. UNKNOWN = not found or blocked. PROXY = a retail price used only as a stand-in for a cost we could not read.

## 1. Bottom line

- The brief asked for 8 to 10. Only 5 are worth passing to the scripts, and only the first two are real fast-lane options. The third is probably shut out by the medical rule; the last two are kept so the scripts can show why they fail.
- By sub-area: beauty tools and personal-care devices, none qualify. Hair tools, none qualify. Massage and recovery, 2 plausible, 1 regulatory problem, 1 cost failure. Home fitness accessories, 1 weak item.
- Fast-lane exception in force: ads may start the same day one sample unit is ordered. It is flagged on every candidate, not used to reject any.

| # | Candidate | DTC price used | Best US landed cost read today | Amazon units a month at $40+ (floor) | Why it sits here |
|---|---|---|---|---|---|
| 1 | Cordless kneading neck and shoulder massager with heat | $89.99 (Kate Minimalist; TheraPexa sells at $119.99) | $23.29 (hand-shaped form, 11 sold, fastest delivery 4 days) | 14,050 over 48 listings | Only item here where a small store sells at about $90 to $120 with visible ad volume (TheraPexa: 2,016 reviews, 18 of 29 ads loaded) and US stock reads in the low $20s. Against: Amazon sells the same forms at $30 to $56, and TheraPexa sells on medical claims we cannot make. |
| 2 | Cordless heated hand massager (air compression) | $79.99 (Nekteck; Lunix sells at $98.97 with 1,938 reviews) | $31.69 (2 sold, "only 4 left") | 14,700 over 59 listings | Clear December gift, no whale, DTC brands hold $65 to $120. Against: thin US stock, Amazon leaders at $47 to $54, hard to show in 3 seconds, ad evidence UNKNOWN. |
| 3 | Leg air-compression massager with heat | $119.99 (Renpho; ReAthlete sells at $149.99 with 2,650 reviews) | $44.29 (SEJOY, 20 sold) | 24,900 over 85 listings | Strongest spread of sellers at $60 or more (20,600 units over 75 listings). Against: this product type is an FDA Class II device when sold for circulation, which is how everyone sells it. Likely excluded. |
| 4 | Shiatsu foot massager machine | $109.99 (ErgonomicLux, Renpho Compact) | $64.49 (no sales) | 34,300 over 88 listings | Largest demand in the scan, but the one clean US cost is about what Amazon charges for the #1 and #2 products ($71.99 and $75.98). Fails on cost. |
| 5 | Music boxing machine | $69.99 (Amazon median at $60+; no DTC store found) | $37.29 (3 sold) | 18,450 over 41 listings | Best 3-second demo and no brand, but no proof anyone gets more than the Amazon price, design patents unchecked, and searches fall from 60,500 in December to 9,900 in January. |

- Candidates with a US-stock cost read today: 5 of 5. Important limit: every one is a price on an AliExpress search card with the ship-from United States filter on, during a Black Friday promotion the site banner says ends Dec 4. Item pages were captcha-blocked, so variant, stock depth and the regular price are not confirmed. Treat them as VERIFIED "as displayed", not as supplier quotes.

## 2. How the numbers were built

- Demand: DataForSEO live Amazon US search, 58 keywords, 100 results each. A listing counts if it is priced $40 to $400 and shows a "bought in past month" badge. Badges are floors ("1K+"), so every sum is a floor. Listings were de-duplicated by ASIN across keywords and filtered by title words (filters are written in each `amazon.checked` field). Weights and best-seller ranks came from DataForSEO Amazon product detail for 15 leading listings (ESTIMATED for our unit).
- Search volume: DataForSEO Google Ads, US, 75 keywords in one call, monthly values Nov 2025 to Oct 2026 (ESTIMATED).
- DTC prices: each store's public storefront search JSON, then the product page for review counts (VERIFIED). Most stores were on Black Friday sale, so prices are sale prices.
- Supply: AliExpress search with the ship-from United States filter, read in a headless browser, with three screenshots to check the product form. Rule for `best_us_landed_cost`: the lowest card price that (a) matches the product, (b) shows free shipping and (c) carries no "New shoppers" tag, because a repeat dropship order will not get a first-order discount. Where the most-sold listing has that tag it is listed in `supply` with the tag noted.

### Price-band view (Amazon units a month, floors)

| Candidate | Under $40 | $40 and up | $60 and up | Note on the $60+ tier |
|---|---|---|---|---|
| Neck and shoulder massager (wearable) | 60,100 | 14,050 | 2,350 over 10 listings | Etekcity 1,000 at $75.96; premium lives in DTC, not on Amazon |
| Hand massager | 2,000 | 14,700 | 5,700 over 28 listings | no leader; several new no-name listings at $76 to $100 |
| Leg compression massager | 3,100 | 24,900 | 20,600 over 75 listings | Alljoy 3,000, Quinear 2,700, Cincom 2,550, FIT KING 2,400 |
| Foot massager machine | 7,700 | 34,300 | 29,550 over 76 listings | Renpho 8,600, Nekteck 5,000 |
| Music boxing machine | 13,100 | 18,450 | 7,600 over 19 listings | unbranded |

Against the house hero-first rule (already selling in volume at $60 or more from several sellers): leg, foot and boxing meet it on Amazon; the hand massager partly; the neck massager only through DTC evidence.

Google searches a month (ESTIMATED): foot massager 165,000 (301,000 in Dec 2025), neck massager 49,500 (135,000), hand massager 22,200 (60,500), leg massager 18,100 (33,100), music boxing machine 14,800 (60,500). Every one of these peaks in December and falls by half or more in January.

## 3. What the neck massager check turned up

- TheraPexa (trytherapexa.com) is the one small store in this category that visibly runs volume on Meta: about 260 active results for the exact phrase "neck and shoulder massager", 18 of the 29 loaded ads are theirs, started Sep 7 to Nov 14, 2026. Price $119.99, 2 for $203.98, 3 for $287.98, 2,016 reviews on the page, ships from Dallas in 2 to 4 business days.
- Its page states "FDA cleared Class II medical device", "HSA/FSA eligible" and "No more chronic neck and shoulder pain". Under our rules we can say none of that. The result may not transfer to relaxation-only copy.
- Its product is the U-shaped strap massager. The cheap US-stock listings are the newer hand-shaped "bionic" shawl ($16.49 to $35.79 without a new-shopper tag; the most-sold one shows 20K+ sold at a new-shopper price of $23.15 against a $79.72 list price). For the U-shaped form the clean US cost is not confirmed ($26.57 is a new-shopper price; one untagged card reads $34.49).
- On Amazon the hand-shaped form is small and cheap so far: about 3,800 units over 18 listings, most at $30 to $57.

## 4. US stock or China-shipped, for this category

- US stock. US-filter cards showed free shipping and "fastest delivery in 4 days" or "6 days".
- China-side cards were mostly new-shopper promo prices with no delivery days, and the page did not confirm the China filter. In the two cases where a clean China-side card was readable it was dearer than US stock: hand massager $47.49 against $31.69, boxing machine $47.69 against $37.29.
- These are gift purchases with a December deadline. Anything slower than about a week misses Christmas.

## 5. Rejected, and why

Numbers are Amazon floors at $40 or more unless stated; AliExpress prices are US-filter search cards read today.

| Product | Evidence | Reason |
|---|---|---|
| 6-in-1 air styler (Airwrap style) | 40,900 units over 88 listings, 28,350 at $60+; top no-name listing 5,000 at $88.59; Shark 10,700 | Best beauty demand in the scan, but Dyson holds a design patent (D853,642) and a utility patent (11,044,979) on this styler and has sued 100+ marketplace sellers in "Schedule A" cases (ESTIMATED, litigation blog summaries). US cards read $48.49 to $94.99, so no room either. Mains heated tool, certification unknown. |
| Thermal brushes, straightening brushes, automatic curling irons | 258,050 units over 131 listings, but TYMO 92,600, Wavytalk 61,500, L'ange 39,000 | Three brands own it at $45 to $57. |
| High-speed hair dryer | 33,050 units over 42 listings; 111,950 units under $40; Laifen, BaBylissPRO, Shark, Dyson | Whales above, commodity below; mains appliance with unknown certification. |
| LED face mask, red light therapy mask | 34,450 units over 47 listings; Shark, Medicube, INIA | Sold as light therapy for skin: medical and health-claim exclusion (device status not re-verified today). |
| IPL hair removal | 29,450 units over 48 listings; INNZA 12,100, Braun 5,000, Ulike 3,350 | Light-based hair removal: medical exclusion and burn risk (device status not re-verified today). |
| Microcurrent and "glow" facial devices | Medicube 9,000 at $149; Shark FacialPro | Whale plus device claims. |
| Facial steamer; nail drill kit; paraffin wax bath; bonnet dryer | 4,650 over 29; 4,150 over 8; 5,750 over 40; 5,900 over 24 | Too little sold at $40 or more. Hot wax adds a burn risk. |
| Rolling makeup case; makeup bag with LED mirror | 4,150 over 49; 650 over 4 | Thin; mirrors are fragile. |
| Head shavers and body groomers | 67,650 over 30; Manscaped 26,500, Philips 17,700 | Whales. |
| Filtered shower head; towel warmer bucket | see `candidates_home.md` | Already covered by the home scout; not repeated. |
| Electric scalp massager | 1,950 over 8; 41,950 units under $40 | A DTC price exists (ErgonomicLux $109.99, Comfier $59.99) but nothing shows people pay $60. On Copyfy's November list (vendor). |
| Eye massager | 19,250 over 42, Renpho 15,650 | One brand owns it at $47 to $57. |
| Massage gun | 41,050 over 54; Theragun 11,100, Renpho 7,700, Bob and Brad 5,600; 90,300 under $40 | Whales and saturation; the earlier scan (`winners_scored.csv`) already scored it negative. |
| Cordless massage pillow | 24,450 over 17, of which 22,850 at $40 to $60 | Sells under $60; US cards $26.57 to $35.09. |
| Full-body massage mat with heat | 5,200 over 32, median $89.99 | US cards $63.79 to $73.79 against Amazon $89.99 to $99.24; thin demand. |
| Shiatsu massage chair pad | Snailax and Comfier lead | US cards $75.99 to $160.99; brand-led. |
| Knee massager; lumbar traction device (SmoothSpine style, 4,000 at $119.95) | 10,250 over 31 | Sold only on pain and decompression claims: health-claim and medical exclusion. |
| Foot spa | 18,050 over 41 | Water plus mains power; the home scout rejected it. |
| Cold plunge tub; sauna blanket and steam sauna tent | 1,750 over 11; 2,450 over 14 | Too little sold; heat safety for saunas. |
| Vibrating foam roller | 7,950 over 35 | Chirp, Hyperice, TriggerPoint. |
| Vibration plate | 38,900 over 53; AXV 15,000, Merach 9,900 | Two brands hold about two thirds; untagged US cards read $77.39 and $93.99 against an Amazon median of $72.19; weight not read (floor machine). |
| Under-desk elliptical; mini stepper | 22,750 over 47; 10,150 over 35 | Motorized or steel floor units (weight not read), Merach, Sunny and Cubii lead, Amazon price $45 to $81. |
| Pilates board; pilates bar kit; push-up board; slant board | 2,350; 1,650; 2,600; 4,350 | Sell under $40 to $57. "Pilates board" searches peak at 60,500 in January, but at prices that cannot carry an ad. |
| Weighted vest | 6,400 over 22; 40,950 units under $40 | Cheap and heavy by design. |
| Doorway pull-up bar; aerobic step; balance board | 9,350 over 28; 10,450 over 29; GoBalance 4,000 | Mostly $42 to $58, bulky, or one brand. |
| Aqua (water) weight bag | 2,000 over 8, Tidal Tank 1,800 | One brand. The only fitness item on AutoDS's November list. |
| Heatless curling sets | CJ November list | Under $20. |

Vendor "winning product" lists added little. CJ's November 2026 list has one item in this category (heatless curling sets). AutoDS's November list has one (water weight bag, source $35.99, sell $62.00). Sell The Trend's November top 10 has none. Copyfy's November list has two (electric scalp massager; heated air compression hand massager with a stated source cost of 54 to 62 euros, which is above the US cards read today). Zendrop's public pages show only low-cost items (face roller $15.01, facial massager $11.81, LED photon mask $17.36, 5-in-1 hot air comb $6.68) with no shipping or warehouse detail.

## 6. Sources that blocked or failed

- CJdropshipping: search redirects to a human check (validation page). Not retried through other CJ endpoints.
- AliExpress item pages: captcha ("punish" redirect) in Playwright. Only search cards were readable. With ship-from China requested the page did not confirm the filter and cards showed no delivery days.
- Spocket: 403. Zendrop: catalog behind login, public showcase only. Doba: 40 neck massagers listed in stock with 1 to 3 business days, prices need an account. AutoDS marketplace, Syncee and TopDawg: not retried (the pets scout found them behind a login earlier today).
- Foreplay MCP: 402, no credits.
- Meta Ad Library in Playwright: loaded 2 of 10 attempts ("leg massager" about 150 results, "neck and shoulder massager" about 260 results), then returned an empty page for "hand massager", "music boxing machine", "foot massager" and "massage mat" (two attempts each, several minutes apart). Ad evidence for those is UNKNOWN. The Meta Ads Connector library search returned loose, mostly unrelated matches and was not used.
- Kalodata, FastMoss, Minea, Winning Hunter: no readable November data found through search; dashboards need an account and were not opened. AfterShip's TikTok Shop health and beauty page is category-level and dated April 2025 (only "curling irons" is a device). One TikTok Shop listing was readable (neck massager, $76.00, 20 sold, out of stock).
- cloudmassage.com (error 526), breo.com (error page); fitkinghealth.com, cincomhealth.com, quinear.com and bobandbrad.com do not expose a storefront search JSON. A newswire "review" page for a neck massager returned 404.
- Amazon Best Sellers and Movers and Shakers pages were not opened; DataForSEO search results and product detail (including Best Sellers Rank) were used instead.

## 7. Bias to keep in mind

- CJ, AutoDS, Zendrop, Sell The Trend and Copyfy lists are vendor marketing; their margin figures are unverified and were not used.
- DTC compare-at prices ($269.99, $299.99 and so on) are the sellers' own anchors, not evidence of what people pay. Store claims such as "326,000+ customers" or "100,000+ necks saved" are the stores' own.
- On-site review counts can include imported or syndicated reviews.
- Long-running or numerous ads are a signal, never proof of profit.
- Dyson litigation details come from a patent-analytics blog whose case summaries were inconsistent; the patent numbers should be checked at the USPTO before relying on them.

## 8. What must be checked before any go decision

1. Open the listed AliExpress items in a logged-in AliExpress or DSers account (Dhruv's action) and record the real variant price, shipping line, delivery estimate and stock for a repeat buyer. Until then every US cost is "as displayed", and it is a Black Friday price.
2. CJ and Zendrop US-warehouse price and stock for the neck massager (both forms) and the hand massager (login needed).
3. Decide the form for the neck massager. The proof is for the U-shaped form; the cheap stock is the hand-shaped form.
4. A design-patent search for the hand-shaped neck massager and for the boxing machine before any spend on either.
5. Battery and electrical certification marks on the sample; a page that makes no pain, circulation or condition claim.
6. A sourced massager or beauty benchmark for cost per purchase in `data/channel_params.json` (the file carries a beauty value of $39.31, ESTIMATED and not re-verified), then run the scripts on the JSON inputs with the tough case.
7. Timing: these are December gifts. A test that starts after the first week of December cannot deliver for Christmas with 4 to 6 day shipping, and searches drop by half or more in January.
