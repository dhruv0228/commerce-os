# Holiday gifts: product scout (2026-11-22)

Group: holiday-gifts. Data file: `candidates_holiday-gifts.json` (8 products, same schema as `research/fast-test-2026-11-21/candidates_home.json` plus `creator_fit_1to5`, `creator_fit_reason` and `tiktok_shop_evidence`). This file explains the method and what the data shows. It does not hold facts of its own; the numbers below are quoted from the JSON. No margins or profits are computed here: run them through `scripts/fast_test_rank.py` or `scripts/economics.py`.

## Labels used

- VERIFIED: read on a primary page today, in the fast-lane sense used in `research/fast-test-2026-11-21/candidates_home.md` (a store's public `products.json` or product page, an AliExpress US search card, the Meta Ad Library page, or Amazon and Google data returned by DataForSEO). None of these costs is a supplier quote, invoice or test order.
- ESTIMATED: a third-party figure, or a promo price. TikTok Shop sold counts are ESTIMATED because they come from Google result snippets for shop.tiktok.com pages, not from opening the pages. AliExpress cards with a "New shoppers" tag are ESTIMATED because that price is for a first order only.
- ASSUMED and UNKNOWN as in CLAUDE.md section 5.

## Method

1. Amazon demand: 22 keyword scans through DataForSEO `merchant/amazon/products/live/advanced` (US, depth 100), counting "bought in past month" by price band; 8 listings checked with `merchant/amazon/asin/live/advanced` for weight, rank and ratings.
2. Google demand and season: DataForSEO `keywords_data/google_ads/search_volume/live` for 24 keywords (December 2025 against July 2026).
3. TikTok Shop: DataForSEO Google searches `site:shop.tiktok.com <product> sold` (13 queries). Sold counts were read from the snippets.
4. US-stock cost: AliExpress US search pages in headless Chromium (Playwright) with the ship-from-United-States filter, 21 searches (2 of them China-stock for comparison). Item pages were not opened.
5. DTC prices: public `products.json` tried on 25 store domains (some failed, see below), plus 4 product pages read for review counts.
6. Ads: Meta Ad Library in Playwright for 6 keywords (up to 4 tries each).

Products screened and dropped early, from the Amazon scans: custom photo pet blanket (low Amazon volume, and the earlier print-on-demand sweep already put Printful costs near half the price), interactive dog ball (most volume under $30), flame diffuser (most volume under $40), retro typewriter keyboard, pocket and photo printers (TikTok sells them at $12 to $29), levitating moon lamp (US cost $41 for a $26 to $30 Amazon price), digital picture frame (no US-stock Frameo-type frame found; TikTok sells at $31.99), rechargeable table lamp (US cards mostly new-shopper promos), bartender kit (no US stock found), electric precision screwdriver (US cards at $19.58 to $29.78 were new-shopper promos against Fanttik at $37.97 and HOTO at $28.48).

## Findings

Cost share = best US landed cost divided by the sell price in the JSON. The task's target is about one third.

| Rank | Product | Sell price (basis) | Best US cost | Cost share | Cost vs. lowest proven price | Creator fit | Home batch of 10 to 20 |
|---|---|---|---|---|---|---|---|
| 1 | rolling-knife-sharpener-kit | $69.00 (proposed kit; Hatori sells at $79.95 with 1,307 reviews, vendor figure) | $13.07 | 19% | 38% of Amazon $33.99; 34% of TikTok $39 | 5 | Yes (1.3 lb, about $13 each) |
| 2 | monitor-light-bar-desk-kit | $44.99 (proposed kit; Quntis $41.99 to $43.99 on its own store) | $8.85 | 20% | 26% of Amazon $33.96; 35% of TikTok $24.99 | 4 | Yes (1.3 lb, about $9 to $12) |
| 3 | electric-salt-pepper-grinder-set | $39.97 (ThermoMaven, 3,000+ a month on Amazon) | $10.55 | 26% | 30% of TikTok $34.99 | 4 | Only via China; US cards show 1 unit left |
| 4 | cocktail-smoker-kit | $33.24 (ComboJoy, 10,000+ a month on Amazon) | $22.11 | 67% | fails on US stock | 5 | Only via China, and only if the torch can be shipped |
| 5 | mini-car-vacuum-blower | $39.99 (IYOFINE, 10,000+ a month on Amazon) | $24.68 (new-shopper price) | 62% | fails | 4 | Possible, but the repeat cost is UNKNOWN |
| 6 | cordless-pressure-washer-gun | $69.99 (KEEPEAK, 3,000+ a month on Amazon) | $32.49 | 46% | above TikTok's $29.90 | 4 | No |
| 7 | wireless-meat-thermometer | $33.99 (ThermoMaven, 8,000+ a month) | $30.42 | 89% | fails | 3 | No |
| 8 | smart-bird-feeder-camera | $51.29 (HEAPETS, 2,000+ a month) | $58.79 | 115% | fails | 5 | No |

What this means:

- Two products meet the one-third rule against a price other sellers prove: the rolling knife sharpener and the monitor light bar. The salt and pepper set meets it on paper, but US stock is effectively empty today.
- Rolling knife sharpener is the strongest find. Evidence at three price levels: Amazon generics at $31.99 to $37.99 (about 16,000 units a month counted across 38 listings), a TikTok Shop listing with 10,783 sold at $39, and small DTC stores selling the same generic at $79.95 (Hatori, with 1,307 reviews on the page and active Meta ads) to $99.90 (NorthernKnife). The Meta Ad Library showed about 770 results with Tumbler (10 ads, including a creator partnership ad), Hatori, HORL, HoneyHone and NorthernKnife. A new brand can stand between the $34 generics and the $159 Tumbler. Weak points: US-stock listings show 4 to 10 sales and "only 3 left", and HORL or Tumbler patents were not cleared.
- Monitor light bar fits Dhruv's tech-worker category and sells all year, not only at Christmas. The weak point is price: TikTok sells it at $24 to $37, so a $44.99 store price depends on the gift kit framing.
- The two products with the best creator fit and December demand (cocktail smoker kit, smart bird feeder) fail the cost rule on US stock. The smoker kit could pass through a 10 to 20 unit China batch shipped from home (China card $4.96 with 900+ sold), but the torch's shipping rules are UNKNOWN and the timing to Christmas is tight. Several DTC stores advertise smoker kits at $49.95 to $100 (Barvelle, DrinkSmoked, Smoky Cocktail, Aged & Charred).
- Products 5 to 8 are kept in the file so the ranking shows why they lose: their US-stock cost is 46% to 115% of the proven price.

Season (Google, December 2025 against July 2026, VERIFIED via DataForSEO): smart bird feeder 165,000 against 14,800; wireless meat thermometer 90,500 against 18,100; electric salt and pepper grinder 40,500 against 6,600; whiskey smoker kit 33,100 against 4,400; monitor light bar 8,100 against 8,100 (flat); gifts for dad 450,000 against 22,200.

## Risks and unknowns that apply to all

- Every cost is an AliExpress search-card price, not a quote. Stock depth on US cards is thin (many say 1 to 4 left), so a cost can vanish overnight. CJdropshipping, Zendrop and Spocket were not tried (blocked or login-only last time).
- TikTok Shop sold counts are lifetime listing counts from Google snippets; some snippets list related products, so which product a count belongs to is not always clear (noted per item).
- Meta Ad Library counts are keyword matches across all advertisers. "monitor light bar" and "electric salt and pepper grinder" returned "No ads match" on 4 tries, which means UNKNOWN, not zero.
- TikTok Shop US requires sellers to own inventory, so the creator route means buying 10 to 20 units and shipping from home in Florida. For the top two that is about $130 to $260 of stock.
- Christmas timing: US-stock orders should reach customers by about Dec 10 to 14. A China batch ordered now arrives around Dec 2 to 5 at the earliest (card delivery windows on Nov 21 were 9 to 14 days), which leaves little room.

## What blocked me

| Source | What happened |
|---|---|
| AliExpress item pages | Not opened (captcha last time). Shipping fees, variants (bar length, one or two mills) and stock counts are card values only. |
| TikTok Shop pages | Not opened. Sold counts come from Google snippets. Google returned redirect links, so exact shop.tiktok.com URLs were not resolved. |
| Meta Ad Library | Flaky: two keywords returned "No ads match" on 4 tries. Meat thermometer and bird feeder were not checked (time). |
| Store `products.json` | 404 for mybirdbuddy.com, horl.com, ganiza.com and middletonmixology.com; connection failed for nelko.net, itutn.com, foghatcocktails.com, ganizausa.com and ganizashop.com. |
| Patent checks | Two web searches for rolling sharpeners and one each for light bars (no results) and gravity grinders found no lawsuit. That is not a clearance. |
| CJdropshipping, Zendrop, Spocket | Not tried (verification wall or login needed, per the Nov 21 notes). |

## Recommended next step

Put rolling-knife-sharpener-kit and monitor-light-bar-desk-kit through `scripts/fast_test_rank.py` with the creator and organic channel as well as Meta. Before any purchase, Dhruv decides (Gate 1) whether to check these two with a real US-stock order or a logged-in supplier search. Nothing was bought, contacted or published.
