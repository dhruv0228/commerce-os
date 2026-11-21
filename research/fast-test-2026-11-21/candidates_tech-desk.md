# Fast test lane: desk setup, tech-worker gear, phone and laptop accessories, small gadgets, smart-home add-ons (notes)

Checked: 2026-11-21. Data file: `candidates_tech-desk.json` (6 candidates, same folder). Research only: nothing was bought, signed up for, logged into or sent.

No margin, CAC, ROAS or profit math is done here. The JSON holds inputs for `scripts/economics.py`. Where this file says a cost is "above the 35 percent guide", that is a reading of the brief's rule of thumb against two inputs, not a result; the scripts decide.

## How to read the labels

- VERIFIED: read on the primary source on 2026-11-21 (a store page, a store's public `products.json`, an AliExpress search card, the Meta Ad Library page, or Amazon and Google data returned by DataForSEO). This is the fast-lane meaning. It is weaker than the CLAUDE.md meaning: none of these costs is a supplier quote, invoice or test order.
- ESTIMATED: a third-party figure, a search snippet, or a promo price whose repeat price is unknown.
- UNKNOWN: not found or blocked.
- PROXY: a retail price used only as a stand-in for a cost.

Limits that apply to every row:

1. Amazon "bought in past month" badges are rounded-down floors ("2K+"), so sums are floors. Counts are for listings at $40 or more whose title matches the product, de-duplicated by ASIN. "Brand names" means the first word of the listing title, which is rough.
2. AliExpress costs are search-card values read with the "Shipping from: United States" filter. Item pages sit behind a captcha, so shipping fee and delivery are the card tags ("Free shipping", "Fastest delivery in 6 days"). Cards tagged "New shoppers save" show a first-order promo price; those rows are ESTIMATED.
3. Meta Ad Library counts are keyword matches across all advertisers, not ads for one product. "First screen" means the advertisers on the first load plus one scroll.

## Bottom line

- The brief asked for 8 to 10. Only 6 are worth passing to the scripts, and only the first looks like a possible fast-lane product on the raw inputs. Candidates 2 and 3 have strong demand but cost too much against the price they can hold. Candidates 4 to 6 are kept so the scripts can show why they fail.
- This category has a structural problem for the fast lane: the buyer checks Amazon. For every product below, the non-promo AliExpress US-stock cost is close to the Amazon retail price of the same item (portable CarPlay screen $54.99 against $59.98; mini projector $36.39 against $41.99; desk lamp $32.53 against $44.15). A new store has to sell well above Amazon to cover a $35 to $50 ad cost.
- All 6 candidates have a non-promo US-stock cost read today (VERIFIED in the fast-lane sense). None has a cost from CJdropshipping, Zendrop, Spocket or another app catalog: all were blocked or behind a login.
- Fast-lane exception in force: ads may start the same day one sample unit is ordered. That is flagged on every candidate, not used to reject any.

## The 6 candidates (inputs only)

| # | Candidate | Sell price (source) | Best US-stock landed cost (label) | Amazon units a month at $40+ (listings) | Google searches a month | Demo 1 to 5 |
|---|---|---|---|---|---|---|
| 1 | Portable wireless CarPlay screen kit, 9 to 10 inch | $119.99 proposed; LAMTTO 9 inch kit $139.99, Ottocast $159 to $169 | $54.99 (VERIFIED card, 12 sold); $36.35 on the 1,000+ sold listing is a promo price | 26,300 (63), median $76.70 | carplay screen 8,100; wireless carplay adapter 49,500 | 4 |
| 2 | Mini smart projector (HY300 class) | $99.99 (Lumi Beam) | $36.39 (VERIFIED card, 182 sold) | 54,150 in the $40 to $100 band (61), median $56.98 | mini projector 27,100 (40,500 in Dec 2025) | 5 |
| 3 | Compact digital camera kit | $79.99 proposed; KLIK $68.71, Camp Snap 2 $69.99 | $33.69 (VERIFIED card, 591 sold, rating 4.3) | 17,600 generic (52), median $58.48 | digital camera 368,000 (550,000 in Dec 2025) | 4 |
| 4 | AI translation earbuds | $69.95 (Aviorra) | $37.79 (VERIFIED card, 53 sold) | 7,200 (28), median $94.99 | translation earbuds 33,100 | 3 |
| 5 | Wireless CarPlay adapter | $59.99 proposed; Ottocast from $55 | $26.29 (VERIFIED card, 2,000+ sold) | 9,350 (27); 72,200 more under $40 | wireless carplay adapter 49,500 | 3 |
| 6 | Architect LED desk lamp with clamp | $69.99 proposed; Amazon median $50.34 | $32.53 (VERIFIED card, 48 sold) | 14,350 (28); only 1,000 at $60+ | led desk lamp 9,900; architect desk lamp 590 | 3 |

Order is my judgment of fit, not a script ranking.

1. **Portable CarPlay screen kit.** Fragmented Amazon demand with no whale, three DTC specialists at $80 to $170, about 3,200 Meta keyword results for "carplay screen", works in any car so there is no fit chart, and December gifting helps. Against: the same class of screen is $45 to $77 on Amazon; the non-promo US cost read ($54.99) is well above the 35 percent guide at $119.99 and only the promo price ($36.35) comes near it; LAMTTO's own 9 inch kit with camera is $139.99 with a 20 percent code on the page; CarPlay licence status of generic units is unknown.
2. **Mini smart projector.** Largest demand in the scan and the best 3-second demo. One store (Lumi Beam) has sold this hardware at $99.99 for about a year by positioning it as reading ambience and selling digital scene packs at $29.99, which is a software add-on Dhruv could build with original footage. Against: Amazon sells it at $42 to $67 and the maker's own site at $54; dim-picture returns; the deepest US listing is a promo price.
3. **Compact digital camera kit.** December demand is large and two DTC stores (KLIK, Camp Snap) prove a $69 camera sells with Meta ads. Against: their product is the screen-free style, which we found only China-shipped ($30 to $32); the US-stock option is the generic flip-screen camera that sells for $41 to $61 on Amazon; picture quality is below a phone.
4. **AI translation earbuds.** Long-running ads (oldest seen Apr 2025) at $60 to $70. Against: accuracy claims we cannot substantiate, a competitor page showing 18 percent one-star reviews, advertorial funnels we would not match in a week, Apple and Samsung now ship translation. Not recommended.
5. **Wireless CarPlay adapter.** Best-proven US listing (2,000+ sold). Against: a $60 item cannot carry the ad cost, 72,200 units a month sell under $40, leading Amazon listings rate 3.5 to 3.9. Possible second product next to candidate 1.
6. **Architect desk lamp.** The best desk-setup entry found, and winter is its season. Against: Amazon ceiling of $41 to $60, weak demo, thin ad field. Not recommended.

## Verdict by sub-area

| Sub-area | Verdict |
|---|---|
| Desk setup | None qualify. Everything that sells in volume is under $60 (lamps, seat cushions, foot rests, desk pads, risers) or over 10 lb (walking pads, standing desk converters). Desk lamp kept as the closest. |
| Laptop accessories | None qualify. Portable monitors and screen extenders cost about what Amazon charges; cooling pads are owned by llano; stands and sleeves are under $40. |
| Phone accessories | None qualify at $60 or more except the two car items. Chargers, mics and gimbals are owned by Anker, Belkin, DJI and Hollyland. |
| Small gadgets | Mini projector and digital camera have the demand; both miss the cost guide on today's inputs. |
| Smart-home add-ons | None qualify. Doorbells and cameras belong to Ring, Blink, Wyze and eufy; smart locks have workable costs but need door installation and security trust. |
| Car tech tied to the phone | The portable CarPlay screen is the only product in this file that reaches a three-figure price with DTC stores already selling it. |

## US stock or China-shipped: what this category shows

- Larger electronics cost the same or less from US stock. CarPlay screen: $54.99 US against $58.39 China (both non-promo), $36.35 against $37.84 (both promo). Mini projector: $36.39 US generic, while the Magcubic HY300 Pro reads $58.59 to $58.79 non-promo from China and $34.73 promo from US stock.
- Small, light items are cheaper from China: camera $19.59 against $33.69; CarPlay adapter $13.33 against $26.29; translation earbuds $11.69 against $37.79 (different products).
- Delivery tags: US cards say "Fastest delivery in 6 days" (3 days on the LAOPAO lamp, 4 on a few). China cards read on Nov 21 say "Delivery: Nov. 30 - Dec. 05", which is 9 to 14 days. Both are AliExpress estimates, not tests.
- Several AliExpress "US" results had the US filter on but few or no sales and "only 1 left" tags (backup cameras, VHS converters, 7 inch CarPlay screens). Proven depth exists for projectors (50,000+ sold), CarPlay adapters (2,000 to 10,000+), the 10.26 inch CarPlay screen (1,000+) and the flip-screen camera (about 600 on each of two listings).
- So for candidates 1 and 2 US stock is the clear choice on cost and speed. For the camera and the adapter China saves $13 to $14 a unit at the price of a 9 to 14 day wait and the Christmas cutoff in `03_fulfillment_and_money.md`.

## Rejected, with the number that decided it

Amazon figures are units bought in the past month at $40 or more from the 2026-11-21 scan (floors) unless stated.

| Product | Why rejected |
|---|---|
| AI voice recorder (Plaud style) | Plaud holds 15,700 units on 8 listings at $103 to $150; non-Plaud 11,750 on 35 listings, led by Pocket at $135.15. No AI note taker in AliExpress US stock (28 results, all plain recorders); China $41.29 to $87.55. Needs an app and a transcription plan (Pocket sells plans at $59 to $219, Plaud at $29.99 a month). Google CPC $6.08 to $14.76. |
| AI camera glasses | 10,300 non-Meta units on 46 listings, median $66.49. US-stock cost $36.36 to $53.69 with 14 to 37 sold, against an Amazon price of $45 to $70. Recording-privacy concerns. Meta Ray-Ban at $254 to $344. |
| Magnetic solar wireless backup camera | 7,250 units at $60 or more on 35 listings, median $119.69; AUTO-VOX sells direct at $119.99 to $199.99. Only one US-stock listing found ($139.69, no sales); China $61.77 to $103.17 on promo cards. Cost too close to price. |
| VHS to digital converter | 4,700 units on 21 listings (Portta 2,000 at $94.99; ClearClick $119.95 to $129.95 on its own store). US-stock standalone recorder $90.59 to $103.32 (12 to 31 sold), China $58.36 to $79.45. Cost over half the price. |
| Digital family calendar | 26,850 non-whale units on 59 listings, median $129.99, plus Skylight (7,000+ at $239 to $270; 450,000 Google searches a month, 1,000,000 in Dec 2025) and Echo Show 15. No 10 or 15.6 inch unit found on AliExpress from US stock or China. Large LCD panel. |
| Fingerprint smart lock | 37,150 units on 61 listings, median $69.99; Wyze $79, eufy $89.99 and Philips $75.97 to $104.47 sell 2,000 to 3,000 each. US-stock cost is workable ($27.29 non-promo, 55 sold). Rejected for return complexity (installed on a door), lockout risk and security trust for an unknown brand. |
| 3-in-1 wireless charging station | 28,700 units on 29 listings, but the $60 and up band (18,600 units, 15 listings) is Anker and Belkin, and 102,900 units sell under $40. US-stock cost $11.52 to $17.79 non-promo. A single unit cannot carry the ad cost and no believable bundle was found. Meta: about 3,200 keyword results, AliExpress 8 and Spotminders 8 on the first screen. |
| Portable monitor, laptop screen extender | 68,300 and 52,450 units, but KYY sells 10,000+ at $55.99 and US-stock 15.6 inch units read $49.49 to $55.38 on promo cards. Triple extenders read $200 to $210 from US stock. LCD panels. |
| Wireless lavalier mics, phone gimbals | DJI Mic Mini 10,000+ on each of two listings at $45 to $79, Hollyland 3,000 on each of two; DJI Osmo Mobile 3,000 at $129. Brand-owned. |
| Creator face-tracking tripod kit | 4,700 units, none at $60 or more; Amazon ceiling $56. No US-stock kit found. |
| Vlog selfie monitor | 4,350 units; Insta360 2,000 at $74.99, Rollei 1,000 at $41.99. |
| Electric precision screwdriver set | 19,900 units; Fanttik holds 12,500 on 7 listings at $45 to $60, DeWalt 5,000 at $82.80. Generic JAKEMY from US stock $29.78 to $31.97 on promo cards. |
| Laptop cooling pad | 5,550 units; llano holds about 3,300 at $72 to $114, Razer 500 at $127.99. No US-stock turbo cooler found. |
| Office seat cushion, lumbar pillow | 30,150 units but Everlasting Comfort (10,000 at $45.59) and Cushion Lab ("Patented", 11,000 at $59.99 on three listings) own it; 172,450 units under $40; only 700 at $60 or more. Back-pain selling story is a health claim. |
| Heated seat cushion, heated desk pad, heated foot rest | 4,500 units. Heating products from an unverified factory: excluded for safety, the same call the home scout made on heated blankets. |
| Temperature-control mug, mug warmer set | Ember holds 8,000 units on 15 listings at $76 to $145; non-Ember 4,650 at a $56.98 median. Ceramic or lithium in the cup. |
| Monitor light bar | 3,800 units, of which BenQ 1,600 at $118 to $169; generics $42 to $50. Folded into candidate 6 as an add-on. |
| Dual monitor riser, desk shelf | 3,250 units; 29,200 under $40. Heavy. |
| Standing desk mat, balance board | 3,300 mat units; Ergodriven Topo 1,800 on two listings at $62 to $87. Balance-board results were mixed with fitness steppers. |
| Under-desk foot rest, leather desk pad, desk pegboard, lap desk | 4,200, 2,850, 1,350 and 15,600 units; ceilings of $50 to $60; the same searches show 40,800, 56,250, 4,700 and 64,000 units under $40. |
| Walking pad | One listing 10,000+ at $99.99; 301,000 Google searches a month, 450,000 in Jan 2026. The strongest desk-worker demand found, but 40 lb and up: excluded by weight. |
| Open-ear clip earbuds | Shokz 20,000+ at $100 to $175; generics top out at $59.99 (Raycon, Baseus). |
| Thumb-size action camera | 3,000 generic units at $53 to $80; US-stock card $13.27 on promo with 30 sold. Small and unproven: watch list only. |
| Coin and soldering microscope | 7,150 units; TOMLOV and Elikliv. Cost not priced. |
| Phone blocker (Brick) | 9,000 on one listing at $56.80. A branded NFC tag plus app; no generic supply. A software idea for the slow lane, not a dropship product. |
| Label makers, thermal printers, film scanners, pixel clocks | Brother, DYMO, Phomemo, Jadens, Kodak, Epson, Divoom. |
| Smart curtain opener, video doorbell, solar and bulb security cameras | SwitchBot; Ring 10,000+ on each of two listings; Blink, Wyze and eufy 6,000 to 10,000 each. Generic bulb cameras 1,600 units. |
| MagSafe car charger, key light, teleprompter, tablet floor stand, phone lens, camera grip, page-turner remote, typewriter keyboard, laptop backpack | Each under 10,000 units at $40 or more, mostly brand-led (Anker, ESR, Neewer, Elgato, JanSport, Swissgear) or with the volume under $40. |
| Retro game consoles, Android TV boxes | Not scanned. Excluded for IP (bundled game ROMs, unlicensed streaming). |
| Drones | Not scanned. Excluded for safety, FAA rules and lithium. |
| Power banks, jump starters, electric air dusters, hand warmers | Not scanned. Large lithium batteries. |

Earlier repo scans were reused, not redone: the tech rows in `data/opportunities.csv` (mice, keyboards, hubs, stands, risers, watch bands, LED strips, webcams, headsets, speakers, tracker tags and others) already showed medians under $40 to $60, brand-led flags or oversize weight.

## "What is selling now" lists: what they gave for this category

All of these are vendor content written to sell a tool or a supplier.

- CJdropshipping "Best Dropshipping Products November 2026" (published Oct 19, 2026): ten items, no prices or sales. The only phone-related item is touchscreen winter gloves.
- AutoDS "Best dropshipping products for November 2026" (Oct 15, 2026): no tech or desk item (electric wine opener, candle warmer lamp, heated hanger).
- Copyfy November list (updated Oct 27, 2026): precision electric screwdriver kit (sell 34 to 49 euros, cost 15 to 19 euros, no sales evidence), three-axis phone stabilizers named; a "traffic growth" widget shows heated seat cushion +312 percent with no method.
- Zendrop tech-products page: 20 "trending" items with a cost and a retail price (for example mechanical gaming keyboard cost $41.61, wireless gaming mouse $23.95, RGB gaming headset $17.11, "58MP outdoor camera" $23.47). On 19 of the 20 the retail price is exactly four times the cost, so it is a formula, not market evidence. Ship-from is not shown.
- Sell The Trend "Top 6 tech gadgets" (updated Oct 1, 2026): names branded goods (DJI Osmo Pocket 3, Galaxy Buds, Anker Prime, Plaud Note) with no numbers. Not dropshippable.
- FindNiche TikTok phones and electronics ranking (dataset dated 2026-11-01): the top 10 are Southeast Asian listings priced in rupiah, pesos and dong. Not US data.
- AfterShip TikTok Shop US electronics ranking: selfie sticks, phone charms, tripods, e-reader cases, screen protectors. Low-price items; the list is labeled Apr 2025 with an "updated" stamp of 2026-11-21.
- Kalodata and FastMoss dashboards: gated, not opened. Minea and Winning Hunter: no November list found.
- Amazon Best Sellers ranks came from listing data through DataForSEO: the top CarPlay screen is #3 in Car Audio Receivers and #1,188 in Electronics; the top mini projector is #1 in Video Projectors; the top generic camera is #10 in Digital Point & Shoot Cameras and #716 in Electronics; the top architect lamp is #6 in Desk Lamps; the top translation earbuds are #7 in Electronic Foreign Language Translators.

## Sources that blocked or failed

| Source | What happened |
|---|---|
| CJdropshipping | Search redirects to a "Human verification" page in WebFetch and Playwright. Every CJ US-warehouse cost is UNKNOWN. |
| Zendrop catalog | Redirects to the login page. Only the public marketing page with formula prices was readable. |
| Spocket | The products URL loads a marketing page with print-on-demand items, no searchable catalog or prices. |
| Doba | Search loads and shows stock and "3 Business Day(s)", but "Sign Up to See Price". |
| TopDawg, Syncee, AutoDS | Search URLs land on the home page or a login prompt; no prices without an account. |
| DHgate | Cloudflare "Just a moment" page (HTTP 403). |
| Banggood | Loads, but the search returned unrelated items; not used. |
| AliExpress item pages | Captcha, per the home scout; not retried. Costs are search-card values only. |
| Amazon Movers and Shakers (Electronics) | Page loads in Playwright but the product grid comes back empty. |
| Meta Ad Library | Loads without login, but often returns "No ads match" on the first load; each keyword was tried up to 4 times. "hy300 projector" and "wireless carplay" returned nothing on all 4 tries (UNKNOWN). |
| Foreplay MCP | One call made; HTTP 402, "Insufficient credits", 0 remaining. |
| autolinkr.com | Redirects to a "/lander" bot wall; price UNKNOWN. |
| carlinkit.com, portta.com, eppiebasic.com, flashbackcamera.com | `products.json` returned an HTML page or nothing; prices not read. |

## Biggest unknowns

1. The real, repeatable US-stock cost of the CarPlay screen: $54.99 on a thin listing or $36.35 on the proven listing's promo price. This one number decides whether candidate 1 is a fast-lane product. It can be read for free by opening the item page in a normal browser, or priced in CJdropshipping and Zendrop once Dhruv has accounts.
2. Product quality and what is in the box (rear camera, mounts, memory card): no sample exists. The fast lane's same-day sample order is the first check.
3. Whether generic CarPlay units and mini projectors hold the Apple, Google, Netflix or FCC approvals their listings imply.
4. Patent and trade-dress status for the HY300 shape and the Camp Snap style camera: web searches only, nothing found, USPTO not searched.
5. Whether a new store can sell any of these above Amazon's price. Amazon data shows demand; it does not show that a new store can capture it.
6. Stock depth on the US listings and a second US source for each product.

## Sources (all accessed 2026-11-21)

- DataForSEO: `merchant/amazon/products/live/advanced` (66 keyword scans, one of which returned nothing), `merchant/amazon/asin/live/advanced` (8 listings), `keywords_data/google_ads/search_volume/live` (55 keywords, US).
- AliExpress US search pages with the US ship-from filter and without it (52 searches; item URLs are in the JSON).
- Meta Ad Library: https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=KEYWORD (21 keywords).
- Store catalogs (`/products.json` or pages): lamtto.com, ottocast.com, carpuride.com, trylumibeam.com, magcubic.com, aurzen.com, klikcamera.com, campsnapphoto.com, papershoot.com, aviorra.com, vylaras.com, viora-shop.com, lumecube.com, quntis.com, auto-vox.com, clearclick.tech, heypocket.com, plaud.ai, wolfbox.com.
- Lists: https://cjdropshipping.com/blogs/winning-products/Best-Dropshipping-Products-November-2026 , https://www.autods.com/blog/best-dropshipping-products-for-november-2026/ , https://www.copyfy.io/en/blog/best-dropshipping-products-to-sell-in-november , https://zendrop.com/tech-products/ , https://www.sellthetrend.com/blog/top-6-tech-gadgets-to-dropship-for-high-profit , https://findniche.com/tiktok/trending-phones-and-electronics-products , https://ecommerce.aftership.com/product-trend-list/best-electronics-product-to-sell-tiktok-shop-us
- Repo: `research/fast-test-2026-11-21/03_fulfillment_and_money.md` (delivery times, Christmas cutoff), `candidates_home.md` (label conventions, AliExpress method), `data/opportunities.csv`, `research/platform-winners-2026-11-15/winners_scored.csv`.

Raw scan files were kept in the session scratchpad and are not part of the repo.
