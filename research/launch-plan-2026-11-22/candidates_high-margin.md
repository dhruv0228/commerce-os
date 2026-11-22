# High-margin product scout (2026-11-22)

Group: "high-margin". Goal: proven sellers at $60 to $150 whose US-stock cost, shipped to the customer, is about one third of a price other sellers prove they get, or products that creators and organic video can sell. Researcher: Claude (Commerce OS). Public pages and data APIs only. Nothing was contacted, signed up for, bought or posted.

Output: `research/launch-plan-2026-11-22/candidates_high-margin.json` (8 candidates, same schema as `research/fast-test-2026-11-21/candidates_home.json` plus `creator_fit_1to5`, `creator_fit_reason`, `tiktok_shop_evidence`).

Labels follow the fast-lane meaning in `research/fast-test-2026-11-21/candidates_home.md`: VERIFIED means read on a primary page or returned by DataForSEO today. None of the costs is a supplier quote, invoice or test order. AliExpress cards tagged "New shoppers" are first-order promo prices and are labeled ESTIMATED.

## Short answer

1. Only one candidate meets the one-third rule at a price another seller proves: the **dog carrier backpack kit** (US-stock card $25.99 with free shipping against Kurgo G-Train at $79.99 with 200+ bought in past month). It also fits the Barkfare customer. Its weak points are an unproven $25.99 listing (no sold count, no reviews) and cheap Amazon generics.
2. The **large custom pet portrait canvas** (Printful, printed in the US) comes next: $44.45 landed for 18x24 against Crown & Paw's $99.95 for 16x24, and $62.81 for 24x36 against their $159.95. It overlaps the barkfare-addons candidate `custom-pet-portrait-canvas` and should be ranked with it as one size ladder.
3. Everything else checked lands at about half the proven price or worse on US stock, the same problem as the 36. AliExpress US-stock sellers price near half of Amazon in generic categories. The one-third gap shows up only where a brand sets the proven price (K9 Sport Sack, Kurgo, Crown & Paw) and generics are cheap.
4. Four candidates are here mainly for route (b), creators and organic video: metal detector kit, car starlight headliner kit, window cleaning robot and rug tufting kit all score 5 for creator fit, but their US-stock cost ratios are 0.46 to 0.85.

## Cost to price (computed by a throwaway script from the JSON values; rerun in `scripts/fast_test_rank.py` before any decision)

| id | Sell (proven by) | Best US landed | Landed / sell | Amazon listings counted | Amazon bought past month (sum) | Creator fit |
|---|---|---|---|---|---|---|
| dog-carrier-backpack-kit | $79.99 (Kurgo G-Train, Amazon) | $25.99 VERIFIED card | 0.325 | 13 at $60+ | 550 | 5 |
| custom-pet-portrait-canvas-large | $99.95 (Crown & Paw 16x24) | $44.45 VERIFIED price list (+$5 ASSUMED art) | 0.445 | n/a | n/a | 4 |
| carbon-fiber-pickleball-paddle-kit | $79.99 (Vatic Pro Prism, Amazon) | $36.41 ESTIMATED promo | 0.455 | 21 at $60+ | 4,750 | 4 |
| metal-detector-kit | $104.49 (Gbnryg, Amazon) | $48.45 ESTIMATED promo | 0.464 | 29 at $50+ | 8,500 | 5 |
| pet-grooming-vacuum-kit | $75.99 (oneisall, Amazon) | $39.43 ESTIMATED promo | 0.519 | 30 at $50+ | 24,500 | 4 |
| car-starlight-headliner-kit | $75.65 (VASTFIRE, Amazon) | $41.09 VERIFIED card | 0.543 | 43 at $50+ | 4,250 | 5 |
| rug-tufting-starter-kit | $93.99 (BESGEER, Amazon) | $70.48 ESTIMATED promo | 0.750 | 38 at $60+ | 750 | 5 |
| window-cleaning-robot | $119.99 (Anminto, Amazon; thin proof) | $101.44 VERIFIED card | 0.845 | 32 at $60+ | 1,400 | 5 |

Other ratios from the same script, for context:

- Dog carrier against K9 Sport Sack Urban 3 at $99.95: 0.26. The proof at $99.95 is weaker (Urban 3 shows 50+ bought in past month on Amazon and 55 reviews on its own page).
- Canvas 24x36 ($52.02 plus $10.79 shipping) against Crown & Paw's $159.95: 0.393.
- Without promo prices: pickleball $59.39 card gives 0.742; grooming vacuum $56.09 card gives 0.738.
- If the PuRuiKai window robot ($56.29, 208 sold) ships free, its ratio would be 0.469; its shipping fee is not on the card.
- If the generic tufting kit ($50.73, 27 sold) ships free, 0.54; its shipping fee is not on the card.

Amazon counts are the scan's organic listings at or above the stated price floor that match the product words (see `amz()` filters in the build step); "bought past month" is Amazon's rounded "N+ bought" badge summed over those listings, so variants of one product are counted separately.

## Method

1. Skimmed `research/fast-test-2026-11-21/ranked.md` (Overall and Shortlist) and the sibling files `candidates_barkfare-addons.json` and `candidates_holiday-gifts.json` to avoid repeats.
2. Amazon keyword scans through DataForSEO `merchant/amazon/products/live/advanced` (depth 40, US): 24 keywords. Listing details (weight, rank, ratings) for 7 ASINs through `merchant/amazon/asin/live/advanced`.
3. AliExpress US search cards with the `shipFromCountry=US` filter in headless Chromium (Playwright): 14 searches. Item pages were not opened. Shipping fee and delivery come only from card tags.
4. Competitor DTC prices from public Shopify `products.json` (K9 Sport Sack, Vatic Pro, Tuft the World, Crown & Paw, oneisall, Neakasa, West & Willow) and the Crown & Paw product JSON for the size ladder.
5. Print-on-demand cost from Printful's public catalog API (`api.printful.com/products/3`, `/614`, `/2`, `/536`) and the public shipping page (`printful.com/shipping`).
6. Google search volume (US, 12 months) for 17 keywords through DataForSEO `keywords_data/google_ads/search_volume/live`.
7. Meta Ad Library keyword search in Playwright for 6 keywords (3 tries each); TikTok Shop search pages for 4 keywords.

## Checked and left out (with the reason)

| Product | Why it is out |
|---|---|
| Dog harness and leash set | Amazon prices $6.79 to $42.99; no proof at $60+ (DataForSEO scan 2026-11-22). |
| Camping hammock with bug net | Median $36.48; listings at $50+ summed 150 bought in past month. |
| Airline-approved pet carrier | Median $39.98; Sherpa $49.88 with 1,000+ bought; volume sits under $60. |
| Car ambient lighting kit | Median $35.99; Govee $14.99 with 6,000+ bought; listings at $50+ summed 50. |
| Sunrise alarm clock | Hatch Restore 3 sells at $135.99 (10,000+ bought) but the price is brand-led; generics sell at $28 to $51 (Odokee $50.99, 7,000+). US-stock generics $24.94 to $34.39; one US card ("Sunrise 2", $63.36) looks like a copy of a branded clock. |
| Custom embroidered pet sweatshirt | Amazon custom listings sell at $17.95 (600+ bought), which caps the price far below $60. Printful embroidered sherpa blanket base is $46.82, also too high. |
| Dash cam, front and rear | Strong demand ($80 to $160, about 53,300 bought in past month at $60+ in one scan; ROVE R2 $139.99 with 10,000+), but US-stock 4K cards are branded (DDPAI $69.87 promo, Baseus $76.95 promo), so cost is near the price. |
| Digital picture frame | Big Christmas demand (Aura $139 and Skylight $109.99 with 6,000+ bought each; Frameo 15.6 inch $94.95 with 3,000+). AliExpress US returned only 12 cards and no comparable 10.1 inch Frameo frame, so US cost is UNKNOWN. Worth a second look on a logged-in US-warehouse supplier. |
| Pet camera with treat toss | Furbo sells at $18 to $34 with a subscription, which sets the price expectation. |
| Leather desk pad | Amazon $8.48 to $41.97. |
| Mulberry silk pillowcase | Blissy is $39.47 on Amazon; generics $5.65 to $20.99. |
| Dog winter coat | Amazon listings all under $45 in the scan. |
| Steel tongue drum | Amazon mostly $16.99 to $49.99. |
| Golf putting green, car seat covers | Mostly under $60, bulky; not pursued. |

## What blocked me

| Tool or site | Result |
|---|---|
| TikTok Shop (`tiktok.com/shop/s/...`) | "Verify to continue" puzzle on all 4 searches. Google results for shop.tiktok.com pages returned no sold counts. Every `tiktok_shop_evidence` is UNKNOWN. |
| Meta Ad Library | Only "starlight headliner" returned a count (about 180 results, second try). Five other queries showed no count after 3 tries. |
| Foreplay MCP | HTTP 402 "Insufficient credits", remaining credits 0. |
| AliExpress item pages | Not opened (captcha on Nov 21). Costs are search-card values; shipping fee is UNKNOWN wherever the card has no "Free shipping" tag. |
| kurgo.com, canadapooch.com, maxineone.com, fcklightbars.com | 404, 429, proxy 502 and 429 (the guessed FCKLIGHTBARS product URL returned 404). |
| Printify | Not read: the catalog API needs a token and product pages render in JavaScript. A cheaper canvas provider might exist there. |
| Etsy, CJdropshipping, Zendrop, Spocket | Not tried (known bot blocks or logins). Etsy sales proof for POD is therefore missing. |
| Patent checks | One Google search for K9 Sport Sack patents returned only retail pages. No patent clearance was done for any product. |

## Risks and unknowns that matter most

- The dog carrier's $25.99 card has no sold count or reviews; a sample is the only way to know if it can sit beside Kurgo at $79.99. Kit extras (bowl, rain cover, pouch) have no US-stock source yet.
- Most US-stock prices here are "New shoppers" promo prices that apply to a first order only.
- Several US-stock listings carry other brands (HONOLULU, GEN5, SucceBuy, SunPow, PuRuiKai, COTIAR, Taskstar, JHK). Blind shipping and own branding are UNKNOWN for all of them.
- Mains-powered tools (grooming vacuum, tufting gun, window robot adapter) need a visible UL or ETL listing under the house rule; none was seen on a card.

## Confidence

Medium on demand and proven prices (DataForSEO and primary pages read today). Low on costs (marketplace cards, many promo prices, no item pages). Low on ads and TikTok evidence (mostly blocked).

## Suggested next step for the ranker

Add these 8 to the next `scripts/fast_test_rank.py` run. Run the dog carrier at $79.99 and at $99.95, and run the canvas together with the barkfare-addons canvas as one product at 8x10, 18x24 and 24x36. Treat the four creator-fit-5 products as candidates only for a creator or organic test, not for a Meta-only test, since their cost ratios repeat the problem found with the 36.
