# Fast test lane: car and truck, garage and tools, outdoor and garden, winter candidates

Checked 2026-11-21. Research only: nothing was bought, signed up for, logged into or sent.
Data file: `research/fast-test-2026-11-21/candidates_auto-outdoor.json` (8 candidates, one object each).
No margin, CAC, ROAS or profit is computed here; the JSON only carries inputs for `scripts/economics.py`.

Labels: VERIFIED = read on the primary source today. ESTIMATED = third-party figure or a sum of Amazon badge floors. UNKNOWN = not found or blocked. PROXY = a retail price used only as a stand-in for a cost we could not read.

## 1. Bottom line

- The brief asked for 8 to 10. Eight are in the file and only one, heated gloves, meets the brief's cost guide with room at a price DTC stores charge today. The cordless tire inflator meets it on cost but sits on the $60 price floor against two whales. Heated socks and the heated vest kit have real demand and clean US costs but miss the guide at the prices read. The other four are kept so the scripts can show why they fail.
- The pattern: battery heated wearables are the one cluster in this category where winter timing, Amazon sales at $40 or more, several small DTC stores at premium prices, live Meta ads and a US-stock cost all line up.
- The scripts decide the money. A first run of `scripts/fast_test_rank.py` on an earlier save of this file (see `ranked.md`) put heated gloves in its green tier, the tire inflator in amber, socks, vest, CarPlay screen and night vision in red, and blocked the jump starter and the blanket on its rule review. Prices and costs in this file have not changed since that run; the night vision category label did (it now maps to the outdoor benchmark, not tech), so rerun the script on the final file.
- Fast-lane exception in force: ads may start the same day one sample unit is ordered. Flagged on every candidate, not used to reject any.
- Ranking inside this category:

| # | Candidate | DTC price read today | Best US landed cost read today | Amazon units a month at $40+ (floor) | Why it sits here |
|---|---|---|---|---|---|
| 1 | Heated gloves, 7.4V | $97.99 (Savior Heat); $99.99 to $129.99 at Ororo, Fieldsheer, Weston, Venustas | $25.89 (3 sold); clean listing with real sales $48.69 (110 sold) | 19,250 over 69 listings | Biggest live ad market found (about 2,100 active Meta ads, small stores among them), no single owner, 165,000 Google searches last December. Sizing and battery quality are the refund risks. |
| 2 | Cordless tire inflator | $59.99 (Fanttik); Airmoto $59.49 on Amazon | $15.02 (16 sold) | 77,850 over 58 listings | Lowest US-stock cost in the scan against a $59.99 price, and a real winter trigger, but Airmoto and Fanttik are whales and 179,700 units a month sell under $40. Needs a two-pack to clear $60. |
| 3 | Heated socks, app control | $62.99 (Savior Heat); Weston $79.95 | $24.59 (5 sold); same item $24.69 (17 sold) | 11,450 over 34 listings | Clean US cost, but the price sits at the bottom of the band and 62,700 units a month sell under $40. Better as the second product of a gloves store. |
| 4 | Heated vest plus power bank kit | $79.99 proposed; Ororo $99.99 to $129.99, Venustas $119.99, Weston $149.95 | $34.34 (vest $15.09 plus power bank $19.25, two sellers) | 27,600 over 78 listings | Largest heated-wearable demand (201,000 searches last December, about 970 active ads). Ororo is a whale and US-stock vests come without a battery, so the kit is two parcels. |
| 5 | Jump starter with air compressor | $99.99 (GOOLOO); Amazon no-name $66 to $80 | $33.49 (1 sold) | 82,050 over 74 listings | Largest demand in the scan. Held back by the safety screen: high-current lithium pack, certification unknown. |
| 6 | Cordless heated blanket | $119.99 (ActionHeat); Amazon no-name $52 to $86 | UNKNOWN | 26,900 over 82 listings | New and selling, but no US-stock unit with a battery was found; the nearest card is $54.69 without one. |
| 7 | Portable CarPlay screen | $79.99 (LAMTTO) | $44.44 (no sales shown) | 27,200 over 67 listings | US cost equals the Amazon retail price of the same size. Trademark care, electronics returns. |
| 8 | Digital night vision binoculars | $72.67 (Amazon, no DTC premium verified) | $41.79 (6 sold) | 15,150 over 45 listings | No DTC store found selling the generic unit at a premium; the cost is $41.79 against a $72.67 Amazon price. |

- Candidates with a US-stock cost read today: 7 of 8 (all but the blanket). Important limit: every one is a price on an AliExpress search card with the ship-from United States filter on. Item pages were captcha-blocked, so variant, box contents, stock depth and the regular price after the Black Friday promotion are not confirmed. Treat them as VERIFIED "as displayed", not as supplier quotes.
- If one product must be named for this lane: heated gloves, with heated socks as the add-on. It is a 10 to 12 week product (searches fall from 165,000 in December to 33,100 in February and 8,100 in March). Its listed price ($97.99) is an established brand's; the JSON asks the scripts to also run $79.99.

## 2. How the numbers were built

- Demand: DataForSEO live Amazon US search, 104 keywords, 100 results each. A listing counts if it is priced $40 to $400 and shows a "bought in past month" badge. Badges are floors ("1K+"), so every sum is a floor. Listings were de-duplicated by ASIN across keywords and filtered by title words (filters are written in each `amazon.checked` field).
- Search volume: DataForSEO Google Ads, US, monthly values Nov 2025 to Oct 2026 (ESTIMATED).
- DTC prices: each store's public storefront search JSON, then the product page for review counts (VERIFIED). Most stores were on sale for Black Friday.
- Supply: AliExpress search with the ship-from United States filter, read in a headless browser. Rule for `best_us_landed_cost`: the lowest card price that matches the product, shows free shipping and does not carry a "New shoppers" tag, because a repeat dropship order does not get a first-order discount. Where the most-sold listing has that tag it is listed in `supply` with the tag noted. A supply-side pass (14 broad queries sorted by orders, $18 to $55) was also run to see what actually moves out of US warehouses; it surfaced seat covers, branded OBD2 scanners, mini chainsaws, dent kits and rifle optics, nothing that changes the list.
- Weights: Amazon product detail of a comparable listing (ESTIMATED for our unit); null where no listing showed one.

### Price-band view (Amazon units a month, floors)

| Candidate | Under $40 | $40 and up | $60 and up | Note |
|---|---|---|---|---|
| Heated gloves | 42,450 | 19,250 | 10,500 over 46 listings | Wasoto 1,950, Savior 1,300, rest unbranded |
| Heated vest | 1,750 | 27,600 | 17,450 over 49 listings | Ororo holds the $100+ tier |
| Heated socks | 62,700 | 11,450 | 4,100 over 15 listings | Nothing sells at $100+ |
| Tire inflator (no jump combos) | 179,700 | 77,850 | 38,000 over 26 listings | Airmoto 11,000, DeWalt 11,000, AstroAI 8,200, Fanttik 8,100 |
| Jump starter with compressor | 5,050 | 82,050 | 70,150 over 50 listings | GOOLOO 14,700; NOCO owns plain jump starters (40,700) |
| Cordless heated blanket | 5,850 | 26,900 | 16,450 over 50 listings | Mostly new listings with under 130 ratings |
| Portable CarPlay screen | 550 | 27,200 | 16,700 over 48 listings | 28 different first words |
| Night vision | 3,600 | 15,150 | 8,100 over 31 listings | Thermal and scope listings excluded |

Against the house hero-first rule (already selling in volume at $60 or more from several sellers): all eight meet it on Amazon. That is not the binding test in this category; the cost a US-stock source charges is.

## 3. US stock or China-shipped, for this category

- US stock, on what could be read. For the three products with a clean China-side card, the China-side price was higher than the US-stock price: gloves $54.99 against $25.89, socks $37.89 against $24.59, jump starter combos $41.39 against $33.49.
- For the rest, China-side landed cost is UNKNOWN: the most-sold China-side cards all carry new-shopper tags, and the ship-from label did not render on those pages, so origin rests on the URL filter alone.
- Winter products cannot wait 10 to 15 business days. An order placed in the first week of December from China lands around Christmas or after it; `03_fulfillment_and_money.md` already gives the cutoffs.
- US-filter cards for these products showed free shipping and "Fastest delivery in 6 days".

## 4. Rejected, and why

Numbers are Amazon floors at $40 or more (listings / units a month) unless stated; AliExpress prices are US-filter search cards read today.

| Product | Evidence | Reason |
|---|---|---|
| 12V heated car seat cushion | 12 / 1,950; under $40: 13 / 8,900. Best ad signal after gloves: about 100 active Meta ads, 11 of 30 loaded from Sakerplus partner pages and 7 from Manrock pages, 29 of 30 started between Oct 14 and Nov 18, 2026. US 2-pack $34.39; ActionHeat 12V cushion $39.99; Manrock UTV versions $69 to $119 | Sells at $25 to $40. A two-pack at $60 to $70 leaves no room on the US cost. The UTV angle is real for Manrock but thin on Amazon (the "utv heated seat cushion" search returns hunting seats). |
| Heated stadium or hunting seat with power bank | 46 / 7,700; Hoperan 2,250, Tidewe 1,400 | US cards $42.53 (two USB pads, battery not named) and $53.23 (Alpcour, a brand) against Amazon $43 to $90. Stadium season ends by early February. |
| Heated jacket, heated hoodie | 102 / 18,700, median $81.69 | Folded into the vest candidate as a variant (US hoodie $25.39, no battery). Same sizing problem, larger garment. |
| Heated insoles | 19 / 5,850 | US cards $39.89 to $40.19 with 1 sale each; trim-to-fit sizing. |
| Heated scarf, heated pants | 11 / 950 and 20 / 1,300 | Sell under $40 (17,150 and 27,750 units there). |
| Rechargeable hand warmers | 2 / 500 at $40+, but 416,750 units over 99 listings at all prices | Price floor. US two-packs $9.33 to $15.95: use as an add-on to gloves, not as a product. |
| 12V heated car blanket | 10 / 4,500 in a mixed search; Sealy at $44.99 | US $28.89 to $30.29 against a $45 retail price. |
| Heated camping chair | 70 / 25,650, median $94.98, in a mixed search (one Mr. Heater product is 10,000 of it) | Folding chair, bulky; weight not read; not pursued. |
| Smart bird feeder with camera | 56 / 14,400, median $89.99; "bird feeder camera" 165,000 Google searches in Dec 2025 | Best Christmas-gift demand in outdoor and garden, but US cards read $58.79 to $86.89 with no sales against Amazon no-name prices of $43.68 to $66.49. Birdfy and Bird Buddy are the known brands (about 2,150 and 650 units); the unit depends on a third-party app. |
| Indoor hydroponic garden | 44 / 9,700, median $59.49 | US $44.49 to $60.83 against Amazon $47 to $60. |
| Heated bird bath, squirrel-proof feeder, seed starter kit | 12 / 1,100; 11 / 5,300; 8 / 3,600 | Thin. |
| Cordless ratchet wrench | 45 / 14,700; Milwaukee 2,900, AOBEN 2,600, DeWalt 2,350 | Tool brands lead. Retail is $47 to $80 at Walmart and Best Buy (ESTIMATED, search summary); US cards $34.39 (no sales) and $46.69 (Seesii, 234 sold). No DTC premium found. |
| Cordless impact wrench | 58 / 22,450; DeWalt 6,700, Milwaukee 6,200 | Brand-owned above $100; no-name kits $37 to $61 on US cards, most with new-shopper tags; weight with batteries not read. |
| Electric screwdriver set | 19 / 44,000 | DeWalt (25,000) and Fanttik (11,000) are most of it. |
| Articulating borescope | 31 / 16,150; Teslong 5,250 | US cards $87.99 to $134.85 against Amazon $65 to $100. |
| Under-hood and magnetic work lights | 11 / 7,400; the magnetic work light search is Olight and DeWalt | Brand-led; one under-hood light bar at $48.99 shows 3,000+, and the only US card for that form read $25.89 with no sales. Low price for the band. |
| LED hexagon garage lights | 7 / 5,900; 5-grid kits $43 to $48 on Amazon | US $41.99 for the small kit. Large kits that sell on looks read about $130 and up on US cards (new-shopper prices) and are bulky. |
| OBD2 scanner | 43 / 37,700 | Branded (Topdon, Mucar, Launch move the US-stock volume). |
| Cordless air duster | 16 / 19,650 | Wolfbox 10,000 and Fanttik 7,200. |
| Cordless rotary tool, tool backpack, tactical flashlight | 15 / 21,800; 45 / 7,900; 31 / 48,600 | Brand-owned: Dremel 11,750 and Fanttik 9,500; Klein, Swissgear, Veto and DeWalt; Olight 38,600. |
| Mini chainsaw, electric pruning shears | 54 / 20,200; 61 / 17,150; the best-selling US-stock garden listings (3,000+ and 4,000+ sold) | Cutting tools: safety exclusion. Off season. |
| Cordless electric heated lunch box (truckers, job sites) | 21 / 11,250; new listings at $62.65 and $85.48 show 2,000+ each | US $42.99 to $49.39 against $60 to $110 retail; food contact plus a lithium heater. Worth a second look only with a certified unit. |
| Cordless snow shovel | 67 / 22,000, median $149.99; EGO 3,800, Voltask 3,600; "electric snow shovel" 450,000 Google searches in Jan 2026 | At the top of the price band, long and bulky to ship; weight not read. |
| Roof snow rake, heated snow-melting mats | 24 / 4,850; 20 / 1,700 (median $186.99) | Long poles; mains heating outdoors and heavy. |
| Tire snow socks and chains | 32 / 6,750 | AutoSock and SCC lead; per-tire sizing; traction device liability. |
| Traction boards and mats | 27 / 1,750 | Thin demand; US $35.89 for a pair of 10-ton boards; bulky. |
| Windshield snow cover, snow brush, ice cleats, 12V defroster, heated steering wheel cover | 2 / 200; 2 / 450; 3 / 850; 2 / 300; 5 / 550 | Under $40 items (32,350, 51,400 and 13,800 units at all prices for the first three). No honest bundle reaches $60. |
| Winter car emergency and roadside kits | 31 / 22,900 and 29 / 50,050 | The results are jump starters, first-aid kits and lanterns, not one product. |
| Rooftop and hitch cargo bags | 39 / 5,900 | US $59.19 to $64.79 against Amazon $55 to $76. Summer peak. |
| SUV and truck-bed air mattresses, truck bed tent, tailgate tent | 39 / 52,200 and 22 / 21,750; 16 / 1,150; 9 / 1,350 | Mattresses sell well (US cards $39.12 to $39.15, 409 to 1,000+ sold, new-shopper tags) but December to February is the wrong season. Revisit in March. |
| Cordless pressure washer, cordless car polisher | 65 / 29,450; 55 / 15,450 | Off season; polishers sell at $40 to $51. |
| Wireless CarPlay adapter | 22 / 7,950 of 75,250 at all prices | Sells under $40; CARLUEX already torn down in `05_store_teardowns.md`. |
| Solar wireless backup camera | 41 / 7,550, median $119.99 | Only US card read was $139.69; install and pairing returns. |
| Starlight headliner, ambient lighting, underglow, TPMS, heads-up display | 30 / 4,450; 10 / 1,600; 24 / 3,550; 22 / 3,500; 5 / 2,700 | Headliner kits need the roof lining removed; the rest sell under $40 or are thin. |
| LED light bars | 46 / 13,400 | Nilight 6,050; wiring install. |
| Car dent puller kit | 24 / 4,350 | US kits $22.83 to $29.99 sell well, but retail is under $60 and results claims are risky. |
| Trunk organizer, seat-back organizer, seat gap organizer, car cover, hail cover | 8 / 2,700; 10 / 1,300; 0; 20 / 4,750; 10 / 1,800 | Under $40 or bulky and fit-specific. |
| Emergency hand-crank radio | 24 / 26,550; Midland 7,000 | Only one US card found ($34.45, 3,000 mAh, no shipping line). Demand follows storms and peaks in October. |
| Trail camera, metal detector, telescope | 63 / 35,250 (Moultrie 11,000, Tactacam 4,600, GardePro 4,200, Spypoint 4,000); 39 / 21,500 (a stud finder is 10,000 of it); 30 / 11,500 (median $139.99) | Brand-led and hunting season ending; mixed search; fragile optics. |
| Kindling splitter, firewood rack, tabletop fire pit | 14 / 5,350; 25 / 6,700; 35 / 15,050 | Cast iron, and the original Kindling Cracker design is believed to be patented (not checked today); low price; open flame is a safety exclusion. |
| Garage door insulation kit, portable car garage tent | 28 / 9,700 (median $99.95); 29 / 2,900 (median $199.99) | Bulky freight. |
| Underwater fishing camera, ice fishing flasher, snowshoes, snow tubes, magnetic ski goggles | 19 / 2,350; 11 / 1,950; 7 / 400; 17 / 1,300; 9 / 500 | Thin. |
| Car battery charger, plain jump starter | 51 / 86,150 (NOCO 53,000); 80 / 138,050 (NOCO 40,700) | One brand owns both. |
| Diesel air heaters | not scanned | Combustion heater, carbon monoxide risk: safety exclusion. |
| Dash cam | earlier repo decision (synopsis of Nov 19) | Already rejected. |

What the vendor lists added (all vendor marketing, margins not used): Copyfy's November 2026 page (updated Oct 27, 2026) names a portable car jump starter, a USB heated vest, a precision screwdriver kit, magnetic ski goggles and ice cleats, and shows "heated seat cushion, traffic +312%". CJ's November 2026 list has windshield snow covers and touchscreen winter gloves with no prices. Sell The Trend's November 2026 picks are holiday decor and kitchen items. AutoDS has no December 2026 list. A Kalodata-based list for December 2025 put a Hieha jump starter at 64,370 units and $34.09 a unit on TikTok Shop (ESTIMATED, a year old). The heated-wearables cluster is consistent with these lists; nothing else on them survived the cost check.

## 5. Sources that blocked or failed

- Meta Ad Library: results loaded for 5 of 17 attempts in Playwright, then empty pages (throttled, also after a 4 minute pause and 150 second spacing). Read: "heated gloves" about 2,100 results; "jump starter" about 1,600; "heated vest" about 970 (second attempt); "heated socks" about 340; "heated seat cushion" about 100. Empty for "tire inflator" (twice), "heated blanket", "cordless heated blanket", "carplay screen", "portable carplay", "night vision goggles" (twice), "heated jacket" and "cordless ratchet" (twice): those are UNKNOWN.
- Foreplay MCP: 402, no credits (one call).
- AliExpress item pages: captcha (known from the pets scout an hour earlier; not retried). Only search cards were read. With the China filter in the URL the page does not show a ship-from label, so China origin is unconfirmed.
- CJdropshipping: search URL redirects to a validation (human check) page. No US-warehouse price read.
- Spocket: HTTP 403. Doba: heated-glove listings and processing days (2 to 3 business days) visible, prices need an account.
- Zendrop, AutoDS marketplace, Syncee, TopDawg: not retried; the pets scout found them behind login the same day. Zendrop's trending tab is limited to paid plans by its own help page.
- Kalodata, FastMoss, Minea, Winning Hunter: no readable November 2026 data without an account; not opened.
- Stores with no readable storefront JSON: snowdeer.com, invisibleheat.com (Cloudflare check), sierna.com, dayheat.com, weheated.com, avapow.com, seesii.com (HTTP 503), kimotools.com, sakertool.com, aobentools.com, creativexp.com. airmoto.com shows no price.
- Amazon Best Sellers and Movers and Shakers pages were not opened; DataForSEO search results and product detail (including Best Sellers Rank) were used instead.

## 6. Bias to keep in mind

- CJ, AutoDS, Copyfy, Sell The Trend, Eprolo, Syncee and SaleHoo pages are vendor marketing; their margin and "traffic growth" figures are unverified and were not used.
- Airmoto's "1.5 million units" and its three different review counts are its own claims.
- The heated-vest "review" pages found in search (ThermiVest, HeatArmor, Alpha Heat, Solana Gear on newswire sites) are paid releases for single-product funnels, which is itself a sign that dropshippers are working this product now.
- DTC compare-at prices ($139.99, $189.00, $299.98) are sellers' anchors, not what people pay.
- Long-running or numerous ads are a signal, never proof of profit.

## 7. What must be checked before any go decision

1. Open the listed AliExpress items in a logged-in AliExpress or DSers account (Dhruv's action) and record the real variant price, sizes in stock, what is in the box (batteries, charger), shipping line and delivery estimate for a repeat buyer. Until then every US cost is "as displayed".
2. CJ and Zendrop US-warehouse price and stock for heated gloves and socks (login needed). A single supplier that stocks gloves, socks and a vest with battery would remove the two-parcel problem.
3. Battery and heating certification paperwork (UL or ETL, UN38.3) for whichever unit is chosen. No paperwork means no jump starter at all, and a clear warning line on the wearables page.
4. One sample pair ordered the day ads start, sized for Dhruv, and no claim on the page that the sample has not proven (heat-up time, hours of heat, waterproofing).
5. A sizing chart and a stated exchange policy before the first ad; returns come back to Florida.
6. Run `scripts/economics.py` on the JSON inputs at the listed sell price and at the lower rerun prices named in `sell_price_source`, with the tough case. No apparel or automotive cost-per-purchase benchmark was collected here; use the sourced ones in `data/channel_params.json` or mark it UNKNOWN.
