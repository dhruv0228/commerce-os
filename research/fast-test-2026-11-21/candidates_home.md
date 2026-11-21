# Fast test lane: home category scout (notes)

Checked: 2026-11-21. Scope: home, kitchen, cleaning, organization, lighting and decor, bedroom and bathroom comfort. Data file: `candidates_home.json` (9 candidates, same folder). Research only: nothing was bought, signed up for, logged into or sent.

No margin, CAC, ROAS or profit math is done here. The JSON holds inputs for `scripts/economics.py`.

## How to read the labels

- VERIFIED: read on the primary source on 2026-11-21 (a store page, a store's public `products.json`, an AliExpress search card, the Meta Ad Library page, or Amazon and Google data returned by DataForSEO). This is the fast-lane meaning. It is weaker than the CLAUDE.md meaning: none of these costs is a supplier quote, invoice or test order.
- ESTIMATED: third-party figure, a promo price whose repeat price is unknown, or a snippet.
- UNKNOWN: not found or blocked.

Three limits apply to every row:

1. Amazon "bought in past month" badges are rounded-down floors ("2K+"). Sums are floors too. Counts are for listings at $40 or more whose title matches the product, after removing duplicates by ASIN.
2. AliExpress costs come from search cards with the "Shipping from: United States" filter. Item pages are behind a captcha, so shipping fee and delivery are the card tags ("Free shipping", "Fastest delivery in 6 days"). Cards tagged "New shoppers save" show a first-order promo price; the repeat price is UNKNOWN, and those rows are labeled ESTIMATED.
3. Meta Ad Library counts are keyword matches across all advertisers, not ads for one product. "First screen" means the advertisers visible on the first load.

## The 9 candidates (inputs only)

| # | Candidate | Proposed or observed sell price | Best US-stock landed cost (label) | Amazon units a month at $40+ (listings) | Google searches a month, main keyword | Demo 1 to 5 |
|---|---|---|---|---|---|---|
| 1 | Handheld vacuum sealer kit with reusable bags | $69.99 | $18.89 (VERIFIED card, 4 sold) | 24,850 (16) | vacuum sealer 74,000; handheld vacuum sealer 6,600; chef preserve 27,100 | 4 |
| 2 | Filtered shower head with 3 filters | $79.00 | $12.95 (VERIFIED card, 1 sold) | 23,150 (40) | filtered shower head 110,000 | 2 |
| 3 | Rechargeable wall sconces, pair with bulbs | $109.99 | $36.69 (VERIFIED card, 12 sold) | 20,950 (56) | battery operated wall sconces 18,100 | 3 |
| 4 | Japanese-style knife set | $99.00 | $26.49 (VERIFIED card, 12 sold) | 23,100 (79) | japanese knife set 9,900 | 3 |
| 5 | HD galaxy projector with discs | $59.99 | $28.06 (VERIFIED card, 80 sold) | 10,600 (23) | galaxy projector 12,100 | 5 |
| 6 | Electric spin scrubber kit | $59.99 | $22.22 (VERIFIED card, 104 sold, rated 3.9) | 4,100 (12) | electric spin scrubber 4,400 | 5 |
| 7 | Mattress vacuum | $99.99 | $34.83 (ESTIMATED, promo card; $51.77 on vevor.com) | 14,150 (53) | mattress vacuum 6,600 | 4 |
| 8 | Waterless scent diffuser kit | $79.95 | $40.41 (VERIFIED card, device only) | 37,200 (79) | scent diffuser 12,100; waterless diffuser 9,900 | 2 |
| 9 | Towel warmer bucket | $109.99 | $51.90 (VERIFIED card, 1 sold) | 33,350 (72) | towel warmer 110,000 (550,000 in Dec 2025) | 3 |

Order is my judgment of fit, not a script ranking. Candidates 1 to 4 look able to meet the "landed cost at or under about 35 percent of price" guide on the inputs found; 5 and 6 only if a price well above the Amazon street price holds; 7, 8 and 9 look too costly from US stock on their face. The scripts decide.

Eight of the nine have a US-stock cost read today at a non-promo price with a "Free shipping" tag. One (mattress vacuum) has only a promo price. None has a cost from CJdropshipping, Zendrop, Spocket or another app catalog.

### What each candidate has going for it, and against it

1. **Handheld vacuum sealer kit.** One DTC brand, Chef Preserve, proves the offer at $67.99 to $79.99: 15,000+ Amazon units a month, 12,593 site reviews (its figure), about 6,100 Meta keyword results, and Google searches for the brand of 135,000 in Dec 2025. Generic kits sell too (4,000+ a month at $59.99 on a listing with 33 ratings). Against: we would sell the generic next to the name people search for, and the US-stock listings are new with 2 to 5 sales.
2. **Filtered shower head kit.** Cheapest landed cost relative to price, flat year-round demand and a real reorder item (43,300 replacement cartridges a month on Amazon at $20 or more). Against: the selling story in this market is hair and skin, which is a health claim we do not make; filtration claims need a lab report; Google CPC is $4.92.
3. **Rechargeable wall sconces.** No whale: 22 brands, none above 2,000 a month. DTC stores charge $60 to $99 per light (Pridola, Solariko, Poplight) while Amazon sets of 2 run $45 to $57. Demand rises in January. Against: US-stock cost is $37 to $53 a pair and the ad field is small (about 170 keyword results), which can mean open space or weak response.
4. **Japanese-style knife set.** Fragmented, gift-friendly, premium prices are normal ($69 to $280 for 3 pieces on DTC stores). Against: quality cannot be judged without a sample, origin and "Damascus" wording are legal traps, and Meta's rule on knife ads was not checked.
5. **Galaxy projector.** Best 3-second demo and deep US stock (1,000 to 2,000+ sold per listing). Against: the disc type sells under $40 on Amazon, and the one store at $59.99 sits at 1.4 on Trustpilot.
6. **Spin scrubber.** Best demo with the projector, cheap US stock. Against: Amazon sells it at $20 to $40; only a bundle reaches $60.
7. **Mattress vacuum.** Clear dust-reveal demo, no whale. Against: cost, and UV or allergy claims pull in EPA device rules and the health-claim exclusion.
8. **Scent diffuser.** Large market with a consumable. Against: two giants give the device away against oil subscriptions, smell cannot be shown, and it needs two suppliers.
9. **Towel warmer bucket.** Strongest December demand in the scan and no whale. Against: about $52 to $60 landed against an Amazon price of $58 to $90, a 9.2 lb bulky parcel, and an 80 percent drop in searches after December.

## US stock or China-shipped: what this category shows

- For these nine products the US-stock price on AliExpress is close to, or above, the China price. Where both were readable: mattress vacuum $34.83 promo US against $31.89 China; scent diffuser $40.41 US against $40.89 China (shipping unknown); galaxy projector $28.06 US (non-promo) against $15.45 China (promo); knife set $26.49 US (15 pieces) against $20.89 China (4 pieces).
- Delivery tags: US-stock cards say "Fastest delivery in 6 days" (3 days on the diffuser, 4 on a few). China cards read on Nov 21 say "Delivery: Nov. 30 - Dec. 05", which is 9 to 14 days. Both are AliExpress's own estimates, not tests.
- US-stock listings are thin: most have 0 to 12 sales, several show "only 1 left" or "only 3 left". The exceptions are galaxy projectors (1,000 to 5,000 sold), the SucceBuy mattress vacuum (258), the SucceBuy towel warmer (193) and one spin scrubber (104 to 800).
- So the cost premium for US stock is small here, but the supply risk is real: a listing can run out mid-test. A second US source should be named before ads start. CJdropshipping's US warehouse is the obvious one to price, and it could not be read (see blocks below).

## Rejected, with the number that decided it

Amazon figures are units bought in the past month from the 2026-11-21 scan (floors).

| Product | Why rejected |
|---|---|
| Digital picture frame | 99,950 units at $40+, but Aura (6,000+ at $139 on each of two listings), Skylight (6,000+ at $109.99) and Amazon Echo Show own the premium tier; generics sit at $50 to $57. Whale-owned. |
| Humidifier | Dreo, Levoit and Vicks hold the top listings (10,000, 8,000 and 7,000); Carepod leads Meta (9 first-screen ads). Bulky, health-adjacent. |
| Portable carpet and spot cleaner | Bissell Little Green alone shows 50,000+ at $79.99. Whale-owned. |
| Handheld steam cleaner | Sells (20,000+ at $47.02 on one generic listing) but pressurized steam is a burn risk. Excluded under significant safety risk. |
| Titanium cutting board | 14,650 units at $40+ and about 9,300 Meta keyword results, with one advertiser ("Pure Cut") filling the first screen (25 ads). US-stock titanium 3-piece sets cost $46.49 to $65.39 against an Amazon price of $42 to $65. "Pure titanium" and microplastic claims cannot be verified. |
| Rolling knife sharpener | Tumbler and HORL dominate ads (10 and 4 first-screen) and the $100+ Amazon listings. HORL's patent position was not checked. No US-stock rolling sharpener found (results were whetstones). |
| Mason jar vacuum sealer | 16,500 units at $30+ but the price tops out at $46 to $48; Mason Genie holds 17 first-screen ads; a jar-sealer patent is in litigation. Possible add-on to candidate 1 later. |
| Sunrise alarm clock | Hatch shows 10,000+ at $135.99; generics cap at $45 to $55. |
| Bidet attachment | Luxe, Tushy and Brondell; $42 to $90; plumbing-fit returns. |
| Boot dryer | 17,850 units at $40+ but three legacy units at $42 to $50 set the price; no DTC ad model; winter only. |
| Bread proofing box and sourdough kits | 4,700 units at $40+; price ceiling about $60 (Brod & Taylor at $149 to $269 moves about 800 across three listings); US-stock listings had 0 to 2 sales. |
| Cocktail smoker kit | 7,150 units at $40+; torch and alcohol adjacency; searches fall from 22,200 in December to 5,400 in January; thin US supply. |
| Candle warmer lamp | 315,050 units, nearly all under $40; only 600 at $40+. No believable $60 bundle; halogen bulb and glass. |
| Electric salt and pepper grinder set | 76,500 units under $40; 5,400 at $40+. |
| Electric jar opener | 95,550 units under $40; 1,500 at $40+. |
| Milk frother and steamer | Nespresso, Breville and Instant lead; the top generic (5,000+ at $61.99) has 16 ratings, so it is not a stable signal. |
| Wearable blanket hoodie | The Comfy markets itself as patented; licensed characters fill the $40+ band (8,400 units). |
| Silk pillowcase | 750 units at $40+; Slip and Blissy own the premium. |
| Foot spa | Massage and health claims, water plus mains power, bulky. |
| Window cleaning robot | 1,800 units at $40+; Ecovacs; fall risk. |
| Levitating plant pot | About 550 relevant units at $40+. |
| Portable blackout curtain | 1,250 units at $40+, almost all Amazon Basics. |
| Motion stair lights, under-cabinet light kits, rechargeable hand warmers | Sell under $40 (hand warmers: 433,400 units, none at $40+). |
| Chunky knit throw, bathtub caddy tray, charcuterie board set, electric wine opener set | Mostly under $40, with 8,100 or fewer units at $40+; commodity or bulky. |
| Cordless table lamps and battery picture lights | Sets sell at $44 to $59 (7,100 and 4,050 units at $40+). Folded into candidate 3 as add-ons. |
| Portable espresso maker | Search results dominated by Bialetti, Nespresso and Casabrews; unit cost not priced. Not pursued. |
| Heated blankets, space heaters, tabletop fire pits | Not scanned. Excluded for significant safety risk. |

**Sub-areas where nothing qualified:** organization (under-sink organizers, shoe racks, storage bins and closet systems sit under $40 or are bulky; see `data/opportunities.csv`, not rescanned) and bedroom textiles (blankets, pillowcases, sheets are whale-owned or under $40).

## "What is selling now" lists: what they gave

All of these are vendor content written to sell a tool or a supplier.

- CJdropshipping "Best Dropshipping Products November 2026" (published Oct 19, 2026): ten items, no prices or sales. Home items: wearable blanket hoodies, holiday cushion covers, ornaments.
- Sell The Trend "Winning Product Friday" page (updated Oct 21, 2026): November list is holiday novelties. Earlier months include a steam cleaner (cost $24.45, sell $89.95), an electric grill brush and a mop. Its "estimated monthly revenue" figures have no stated method. Only the first 100,000 characters were read.
- HyperSKU "TikTok Trending Products for BFCM and Holiday 2026" (Oct 14, 2026, citing FastMoss Q4 2025): throw blankets, candle warmer lamps, ambient LED lamps, kitchen gadgets, renter-friendly decor. Category-level only.
- AfterShip TikTok Shop US Home & Garden ranking: tumblers, thermoses, fragrance oil, cordless floor scrubbers (rank 12). No prices, units or clear date range.
- Not found or not opened: a current AutoDS monthly list (only older ones surfaced), Zendrop, Minea and Winning Hunter lists, and the Kalodata and FastMoss dashboards (paid or gated).
- Amazon Best Sellers and Movers and Shakers pages were not opened directly. Best-seller ranks came from Amazon listing data through DataForSEO, for example: SAMEAT towel warmer #1 in Towel Warmers and #929 in Home & Kitchen; Chef Preserve #2 in Vacuum Sealers and #68 in Kitchen & Dining; AirScent #2 in Aromatherapy Diffusers; Weddell #4 in Showerhead Filters; Nekhung sconce set #5 in Wall Sconces.
- Earlier repo scans (`research/platform-winners-2026-11-15/winners_scored.csv`, `data/opportunities.csv`) were reused to skip items already known to sell under $40 (spin scrubber at base price, cabinet lights, milk frother, door draft stopper, vegetable chopper and others).

## Sources that blocked or failed

| Source | What happened |
|---|---|
| CJdropshipping (search and product pages) | Redirects to a "Human verification" page in both WebFetch and Playwright. Every CJ US-warehouse cost is UNKNOWN. A check of other CJ hosts was stopped by this session's permission rules and not retried. |
| AliExpress item pages | Captcha ("punish") page in Playwright. Search pages worked, so costs are search-card values only. |
| Spocket search | HTTP 403. |
| Doba | Catalog loads and shows stock, "3 Business Day(s)" and "Prepaid label", but no prices without an account. |
| EPROLO | Search URL not found; catalog sits behind a login. |
| Zendrop, AutoDS, Syncee, TopDawg catalogs | Behind a login per `03_fulfillment_and_money.md`; not retried today. |
| VEVOR.com | Prices readable; shipping fee, ship-from and delivery days not shown on the search page. |
| Meta Ad Library | Loads in Playwright without login, but the first load often returns "No ads match"; each keyword was tried up to 4 times. "spin scrubber" returned nothing on all 4 tries (treated as UNKNOWN). |
| Foreplay MCP | One call made; HTTP 402, "Insufficient credits", 0 remaining. |
| poplight.com and labigo.com | Redirect to a "/lander" bot wall. Poplight's price is from press snippets (ESTIMATED). |
| jolieskinco.com and orzorz.com | Cloudflare "Just a moment" page. |
| mistivastudio.com, livefullshop.com, thenaturalhousehold.com | Empty response; these domains were guessed from Meta page names and may be wrong. |
| chefpreserve.com | Readable, but the product page showed "Out of stock" and does not say which bag count goes with which price. |

## Biggest unknowns

1. Real, repeatable US-stock cost and stock depth for every candidate (CJdropshipping, Zendrop and Spocket prices unread).
2. Product quality: no sample exists. The fast lane's same-day sample order is the first check.
3. Repeat price on the promo-tagged AliExpress cards.
4. Patent status for the sconce mount (Poplight) and the handheld sealer; only web searches were run, not USPTO.
5. Meta's current rule on kitchen knife ads.
6. Whether any of these converts for a new store at a price above Amazon's. The Amazon data shows demand exists; it does not show that a new store can capture it.

## Sources (all accessed 2026-11-21)

- DataForSEO: `merchant/amazon/products/live/advanced` (54 keyword scans), `merchant/amazon/asin/live/advanced` (10 listings), `keywords_data/google_ads/search_volume/live` (60 keywords, US).
- AliExpress US search pages with the US ship-from filter and unfiltered (item URLs are in the JSON).
- Meta Ad Library: https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=KEYWORD (24 keywords).
- Store catalogs (`/products.json` or pages): chefpreserve.com, masongenie.com, eskiin.com, senkenknives.com, seidoknives.com, forgedblade.com, pridola.com and pridola.co, solariko.com, pococo.com, tibatoes.com, jigoolife.com, sakerplus.com, aroma360.com, hotelcollection.com, scentiment.com, aromatechscent.com, aromely.com, zadroinc.com, keenray.com, vevor.com, doba.com.
- Repo: `research/fast-test-2026-11-21/05_store_teardowns.md` (Galaxy Lamps, Synoshi), `03_fulfillment_and_money.md` (delivery times, Christmas cutoff), `data/opportunities.csv`, `research/platform-winners-2026-11-15/winners_scored.csv`.
- Lists: https://cjdropshipping.com/blogs/winning-products/Best-Dropshipping-Products-November-2026 , https://www.sellthetrend.com/blog/winning-product-friday-episode-291 , https://www.hypersku.com/blog/tiktok-trending-products-bfcm-holiday/ , https://ecommerce.aftership.com/product-trend-list/best-home-garden-product-to-sell-tiktok-shop-us
- Press snippets for Poplight (price, patents): looper.com, nbcnews.com/select, sharktankblog.com.

Raw scan files were kept in the session scratchpad and are not part of the repo.
