# 05. Store teardowns and screenshots: what these stores actually look like

Research date: 2026-11-21. Research only: nothing was signed up for, bought, logged into or contacted. No margins, CAC, ROAS or profit are computed here; this file only collects inputs for the scripts.

Label key:
- VERIFIED = read on the primary source on 2026-11-21 (the store's live page, its public product JSON, its policy page, the Trustpilot page, or the Meta Ad Library through the Meta Ads connector). "VERIFIED" on a review count means the page displays that number today. It does not mean the reviews are genuine.
- ESTIMATED = third-party figure, with source and date.
- UNKNOWN = not found or not accessible.

Timing caveat: every store was captured in Black Friday week. Sale banners, countdowns and "was" prices are seasonal and will differ in December.

Screenshots are in `research/fast-test-2026-11-21/shots/` with a machine-readable list in `shots/index.json` (32 images).

---

## 0. Short answer

1. The video's style reference, oneisall, is not a dropship store. It is a Shenzhen pet-appliance maker with its own designs, US stock ("We ship from the USA", 3 to 4 working days), a 24-month warranty, a replacement-parts catalog and 121 active Meta ads. Its own pages also present it as an Amazon pet brand. Copying its look does not copy what makes it work. (VERIFIED)
2. The creator's own brand, Haven Golf, is a stocked apparel brand with 1,176 on-site reviews, a 2 to 4 day shipping promise and a multi-buy ladder (2 for $90, 3 for $120, 4 for $140). It runs on a paid Theme Store theme (Symmetry), not on the builder's theme. (VERIFIED)
3. The free builder's own example images show a plain store on a Dawn-style layout: "My Store" as the name, "Free Worldwide Shipping" bar, a stock hero photo, three generic icon blocks, a product grid and default buttons. No live public example of a builder store could be found. StoreBuild's Shopify App Store listing currently reads "This app is not currently available on the Shopify App Store." (VERIFIED)
4. The seven dropship-style stores that show traction all do the same five things the default store does not: one hero product with quantity or bundle pricing, a large visible review count at the top, a specific shipping and guarantee promise next to the button, video and before/after proof, and an add-on or refill that raises order value.
5. Reputation splits by shipping. Stores that state US stock and short delivery mostly show healthy public ratings (oneisall 4.9 on 746 Trustpilot reviews; Haven 4.7 on 54; Nood 4.0 on 40). Stores selling a generic product with slow or unclear delivery show poor ones (Pillow Slides 1.6 on 53; Galaxy Lamps 1.4 on 104; Bleame 3.3 on 2,003 with 30% one-star). Two exceptions cut the other way: Uproot Clean ships from Florida yet sits at 2.0 on only 19 Trustpilot reviews, and Synoshi quotes 8 to 12 business days yet holds 4.2 on 6,385 with an actively managed profile. Samples are small and this is a pattern, not proof of cause. (VERIFIED counts)
6. The same products are openly available as generics: crystal hair erasers from $3.76 on Amazon, cloud slides from $8.54, spin scrubbers from $16.14, lint scrapers at $6.79 for three. A store selling these at $26 to $60 survives on presentation and ad spend, and gets undercut by Amazon the moment a buyer searches. (ESTIMATED, DataForSEO Amazon data, 2026-11-21)

---

## 1. Screenshots captured

All live captures used Playwright Chromium, JPEG quality 70, top of page only. Desktop viewport 1280x800, phone viewport 390x844 (phone views used an iPhone user agent). Popups and cookie banners were dismissed or hidden where they appeared. No store blocked the headless browser: every desktop page loaded with the default headless user agent, so the normal-user-agent retry was never needed.

| File | Store | What it shows |
|---|---|---|
| `oneisall_home_desktop.jpg` | oneisall | Home page |
| `oneisall_home_phone.jpg` | oneisall | Home page, phone |
| `oneisall_product_cozy-c1_desktop.jpg` | oneisall | Cozy C1 vacuum and dryer kit product page |
| `oneisall_product_cozy-c1_phone.jpg` | oneisall | Same product page, phone |
| `haven_home_desktop.jpg` | Haven Golf Company | Home page |
| `haven_product_the-inferno_desktop.jpg` | Haven Golf Company | Polo product page |
| `haven_product_the-inferno_phone.jpg` | Haven Golf Company | Same product page, phone |
| `storebuild_home_desktop.jpg` | StoreBuild.ai | Builder landing page |
| `storebuild_example-section_desktop.jpg` | StoreBuild.ai | The landing page's own "AI-Built Store Example" mockups |
| `storebuild_austinrabin_desktop.jpg` | StoreBuild.ai | The creator's co-branded signup page |
| `storebuildai-com_home_desktop.jpg` | storebuildai.com | The creator's funnel site ("By Zendrop X Austin Rabin") |
| `storebuild_app_niche-picker_desktop.jpg` | StoreBuild.ai app | First builder step: pick a niche |
| `storebuild_app_examples-section_desktop.jpg` | StoreBuild.ai app | "AI-Built Store Examples" mockup ("My Store") |
| `storebuild_shopify-app-listing_desktop.jpg` | Shopify App Store | Listing page saying the app is not currently available |
| `storebuild_vendor-example-store_top_desktop.jpg` | StoreBuild example store | Top of the vendor's full-page example image. Vendor image, not a live store |
| `storebuild_vendor-example-store_fullpage.jpg` | StoreBuild example store | The same image at full length (700x2033) |
| `uprootclean_home_desktop.jpg` | Uproot Clean | Home page |
| `uprootclean_product_cleaner-pro_desktop.jpg` | Uproot Clean | Cleaner Pro product page |
| `uprootclean_product_cleaner-pro_phone.jpg` | Uproot Clean | Same product page, phone |
| `galaxylamps_home_desktop.jpg` | Galaxy Lamps | Home page (US market) |
| `galaxylamps_product_galaxy-projector_desktop.jpg` | Galaxy Lamps | Galaxy Projector 2.0 product page |
| `galaxylamps_product_galaxy-projector_phone.jpg` | Galaxy Lamps | Same product page, phone |
| `pillowslides_home_desktop.jpg` | Pillow Slides | Home page |
| `pillowslides_product_pillow-slides_desktop.jpg` | Pillow Slides | The Pillow Slides product page |
| `bleame_home_desktop.jpg` | Bleame | Home page |
| `bleame_product_crystal-hair-eraser_desktop.jpg` | Bleame | Crystal Hair Eraser product page |
| `nood_home_desktop.jpg` | Nood | Home page |
| `nood_product_flasher-2_desktop.jpg` | Nood | Flasher 2.0 product page |
| `carluex_home_desktop.jpg` | CARLUEX | Home page |
| `carluex_product_pro-plus-2_desktop.jpg` | CARLUEX | PRO+ 2.0 AI Box product page |
| `synoshi_home_desktop.jpg` | Synoshi | Single-product sales page |
| `synoshi_order_desktop.jpg` | Synoshi | Order page with quantity price ladder |

Notes on the captures:
- The task asked for phone views of the two most important stores (oneisall and Haven). Two more phone views were added for Uproot Clean and Galaxy Lamps because most paid social traffic lands on a phone product page.
- Galaxy Lamps first rendered its Canada market for the capture server. It was recaptured with the US market forced (`?country=US`); the price shown was the same.
- The delivery-date widget on the Haven product page shows a ZIP code. That is the capture server's location, not anyone's home.
- `storebuild_vendor-example-store_*.jpg` were made from an image file that StoreBuild embeds on its own landing page (`/wp-content/uploads/2025/11/image-92.svg`). They show what the vendor says its output looks like. They are not captures of a live store.

---

## 2. Comparison table (inputs only)

Prices are the hero product's current price on 2026-11-21. "Meta active ads" is the Ad Library's own estimated count of active US ads on the brand's Facebook page.

| Store | Category | Hero price (was) | Offer structure | Shipping promise on site | Ship-from stated | Returns | On-site reviews shown | Trustpilot | Meta active ads (page) | Theme |
|---|---|---|---|---|---|---|---|---|---|---|
| oneisall | Pet grooming appliances | $97.99 ($149.99) | 4 kit tiers $97.99 to $129.99; buy 2 save 6%, buy 3 save 10%; add-on parts | Free over $40; 1 to 2 working days processing plus 3 to 4 working days | "We ship from the USA" | 30 days; 24-month warranty | 105 on this product | 4.9 on 746 | 121 | Fetch 2.1.0 (custom name) |
| Haven Golf | Golf apparel | $50 ("$98 Comp value" on page; $74 compare-at in product JSON) | 2 for $90, 3 for $120, 4 for $140 | "Fast 2-4 Day Shipping"; free over $150 | North Carolina warehouse (creator's words) | 30 days | 1,176 site-wide, 4.9 | 4.7 on 54 | 62 | Symmetry 8.2.0 (paid Theme Store theme) |
| Uproot Clean | Pet hair remover | $16.99 ($19.99) | 1 pack $16.99, 2 pack $24.99 "Most Popular", 3 pack $32.99; free mystery gift; kits $24.99 to $69.99; laundry refills on subscription | Free over $49; processed in 1 to 3 business days | "Ships Fast From Florida" | 30-day first-purchase guarantee; buyer pays return shipping | 24,896, 4.9 | 2.0 on 19 | 2,183 | Custom |
| Galaxy Lamps | Star projector | $59.99 ($149.99) | Single unit; second model at $79.99; Shop Pay installments | "USA - 2-4 Day Standard or 2 Day Express"; free 2-day over $100 | UNKNOWN | "Free Returns", "Lifetime Guarantee" icons; no policy page found | None on product page; 4 dated testimonials on home | 1.4 on 104 | 0 found | Dawn-based custom |
| Pillow Slides | Cushioned slides | $39.99 ($59.99) | Single pair; 50-product catalog of related footwear; free shipping over $60 | 1 to 4 business days processing, then USA 4 to 12 days | UNKNOWN | 30 days; buyer pays return shipping on most items; no refunds for delays | 4,007 on product card; "300,000+ happy customers" | 1.6 on 53 | 8 (billed in CAD) | Wonder 2.3.0 |
| Bleame | Crystal hair eraser | $53 for 2 pack ($99); $26 for 1 ($44) | 2 pack default with free shipping and free body scrub; countdown; "next 128 orders" counter | Product page: "Free Shipping from US", "Want it by Monday, 23 Nov?" Policy page: United States 5 to 18 business days | Contradictory (see teardown) | 30-day guarantee on page; policy says 15 days to request | 4,974 at top, 1,319 mid-page, 7,322 on home | 3.3 on 2,003 | 0 active | Focal 11.1.0 |
| Nood | IPL hair removal device | $129 ($199) | Device, then serum and razor cross-sells; sets up to $507; refill subscriptions; Affirm | "Ships free tomorrow"; processed within 24 hours | "one of our U.S. warehouses" | 90 days, less $29.95 restocking fee | 19,934, 4.5 | 4.0 on 40 | 468 | Custom (Brooklyn base) |
| CARLUEX | CarPlay AI box | $269 ($399) | Single unit; accessories $6.99 to $80; Shop Pay installments | 1 to 2 business days processing; 5 to 10 business days free standard ($51 to $300 orders); 3 to 7 premium | Not stated; policy discusses customs duties | 30 days; $15 fee on any refund; $30 restocking for change of mind | None on product page | 3.0 on 44 (carluex.store profile) | 12 | Savor 2.1.6 |
| Synoshi | Spin scrubber | $42.99 for 1; $49.96 for 2; $69.96 for 3; $85.96 for 4 ("70% off $71.99") plus $9.95 shipping | Quantity ladder with 4 units preselected as "Most Popular" | 1 to 2 business days processing; United States 8 to 12 business days | UNKNOWN; "international delivery to most regions" | 60 days; shipping not refunded | 6 text testimonials | 4.2 on 6,385 | 0 found on its page | Custom funnel, not Shopify |

Labels for the table: every cell is VERIFIED (read on the store's page, policy page or product JSON, on Trustpilot, or in the Meta Ad Library today) except "North Carolina warehouse", which is the creator's own statement from an earlier video (ESTIMATED, self-reported). Meta counts are Meta's own estimates.

Generic availability on Amazon (ESTIMATED: DataForSEO Amazon search, 2026-11-21; "bought" is Amazon's rounded "bought in past month" figure):

| Product type | Amazon organic price range | Example generic listing | Store that sells it |
|---|---|---|---|
| Crystal hair eraser | $3.76 to $39.99 | "Crystal Hair Eraser for Women and Men (Gradient Blue)", $7.59, 4.0 stars, about 5,300 ratings, 1K+ bought | Bleame at $26 to $53 |
| Cloud or pillow slides | $8.54 to $59.95 | "Cushioned Thick Sole Pillow Slippers", $19.33, 4.3 stars, about 62,100 ratings, 2K+ bought | Pillow Slides at $39.99 |
| Galaxy projector | $9.49 to $189.95 | "Star Projector Galaxy Night Light, Astronaut", $27.99, 4.5 stars, about 17,000 ratings, 7K+ bought | Galaxy Lamps at $59.99 |
| Electric spin scrubber | $16.14 to $93.49 | "Electric Spin Scrubber, Cordless Cleaning Brush", $33.99, 4.4 stars, about 9,100 ratings, 10K+ bought | Synoshi at $42.99 plus $9.95 shipping |
| Pet hair carpet scraper | $3.99 to $79.99 | "Qbily Pet Hair Remover 2nd Gen (3 Pack)", $6.79, 4.4 stars, about 3,600 ratings, 3K+ bought | Uproot Clean at $16.99 (Uproot's own Amazon listing: $15.99, about 31,400 ratings, 900+ bought) |
| Wireless CarPlay AI box | $28.48 to $289 | "LAMTTO Wireless Carplay Adapter", $69.99, 3.5 stars, about 996 ratings, 1K+ bought | CARLUEX at $269 |
| IPL hair removal device | $28.49 to $437.99 | "INNZA IPL Hair Removal", $67.99, 4.4 stars, about 3,700 ratings, 9K+ bought | Nood at $129 (Nood Flasher Pro on Amazon: $249, about 745 ratings, 900+ bought) |

A supplier-side data point for the cheapest of these: a Global Sources listing for a custom-logo crystal hair remover shows $0.73 to $0.82 per piece at 200 pieces and up (ESTIMATED: web search result, 2026-11-21, listing not opened; https://www.globalsources.com/Epilator/Epilators-1213166744p.htm).

Whether any store's unit comes from the same factory as a given Amazon listing is UNKNOWN. What is VERIFIED is that the same product type, in the same form, is sold by many unbranded sellers at a fraction of the store price.

---

## 3. Teardowns

### A. oneisall (the video's style reference)

Screenshots: `oneisall_home_desktop.jpg`, `oneisall_home_phone.jpg`, `oneisall_product_cozy-c1_desktop.jpg`, `oneisall_product_cozy-c1_phone.jpg`. URL: https://oneisall.com/

| Item | Finding | Label |
|---|---|---|
| What it sells | Pet grooming and pet home appliances under its own brand: grooming vacuums, clippers, dryers, a self-cleaning litter box, air purifiers, feeders, fountains. 219 published products, many of them replacement parts. Oldest product record 2022-07-26. | VERIFIED (products.json) |
| Product looked at | Cozy C1 8-in-1 Pet Grooming Vacuum and Dryer Kit. This is the closest thing on the site to the video's "dog hair dryer". | VERIFIED |
| Price | Standard Set $97.99 (was $149.99, "Save 35%"). Other tiers: Detail Care set $119.99, Stay Sharp Set $127.99, Clean Air Set $129.99. | VERIFIED |
| Offer structure | Four kit tiers chosen with a radio selector. Site-wide "Build Your Bundle: Buy 2, Save 6%, Buy 3, Save 10%". "Add More, Save More" row of replacement blades and filters under the button. Sale countdown. Klarna installments. | VERIFIED |
| Shipping promise | "FREE SHIPPING ON ORDERS OVER $40 IN THE US". Policy: shipped within 1 to 2 working days, then USA 3 to 4 working days. Ships to the 48 contiguous states only. | VERIFIED (shipping policy) |
| Ships from | "We ship from the USA". The company address on the same policy page is in Longhua District, Shenzhen. | VERIFIED |
| Returns | 30 days from receipt. Buyer pays return freight unless the fault is the seller's. A 20% restocking fee applies to returns outside the window. Original shipping not refunded. | VERIFIED (refund policy) |
| Trust elements | 5-star rating with 105 reviews on this product (Loox, with customer photos). "Fast & Free Shipping", "30-Day Money Back", "24-Month Warranty" icon row. US phone number. Home page has an events section (trade shows, a GRAMMY gift lounge) and a press section (CES picks, PEOPLE pet awards, "best of" roundups). | VERIFIED that the page shows these |
| Trustpilot | 4.9 on 746 reviews, claimed profile | VERIFIED |
| Product page order | 1. Large image gallery and star rating. 2. Six benefit chips and six use-case chips. 3. Kit selector with what each tier includes. 4. Price, countdown, add to cart. 5. Bullet benefits. 6. Add-on parts. 7. Shipping, return and warranty row. 8. Short customer-style videos. 9. Long illustrated feature story, one block per nozzle and tool, with numbers on the images (noise in dB, drying time by dog size). 10. "What's in the box". 11. Comparison of three models. 12. Specs. 13. FAQ. 14. Demo video. 15. Reviews with photos. 16. "Why Oneisall" brand proof block. 17. Accessories grid. Total page length about 23,000 px on desktop. | VERIFIED |
| Apparent traffic | Meta pixel, Google Ads tag, Klaviyo email. 121 active US ads on the "Oneisall_Official" page. Also sells on Amazon (its own home page cites Amazon roundups). | VERIFIED for the tags and ad count; the mix between channels is UNKNOWN |
| Dropshipping signs | None. Own brand moulded on the product, own replacement parts catalog, warranty, US stock. This is a manufacturer selling direct. | VERIFIED observations |

Why it matters: the video uses this store only as a look to imitate. Its strength is the 23,000 px of product-specific proof, the parts ecosystem and US stock, none of which a generated image set can supply.

### B. Haven Golf Company (the creator's own brand)

Screenshots: `haven_home_desktop.jpg`, `haven_product_the-inferno_desktop.jpg`, `haven_product_the-inferno_phone.jpg`. URL: https://havengolfcompany.com/ . Identity was already established in `01_video_decode.md`; it is the store the creator means by "Haven".

| Item | Finding | Label |
|---|---|---|
| What it sells | Printed golf polos, hats, hoodies, quarter-zips. 89 products. | VERIFIED |
| Price | Polos $50, shown against "$98 Comp value" on the page. The product JSON carries a $74 compare-at price, so the page and the data disagree on the "was" price. Announcement bar: "Polos, Q-Zips & Hoodies $50, Youth Polos $30, Hats $20". | VERIFIED |
| Offer structure | "Mix & Match Adult Polos, Hoodies & Q-Zips: 2 for $90, 3 for $120, 4 for $140". A countdown for a collection being removed (it showed zeros at capture). Upsell and returns-coverage apps in the cart. | VERIFIED |
| Shipping promise | "Fast 2-4 Day Shipping" under the button, plus a Shop Promise box with a dated delivery estimate and "Arrives by Christmas". Policy: ships within 2 business days; free over $150. | VERIFIED |
| Ships from | Own warehouse in North Carolina | ESTIMATED (creator's statement; see file 01) |
| Returns | 30 days | VERIFIED |
| Trust elements | Okendo reviews: 1,176 site-wide at 4.9; 6 on the polo captured. "USA Small Business" and "Fast & Easy Returns" icons. Instagram feed. | VERIFIED |
| Trustpilot | 4.7 on 54 reviews | VERIFIED |
| Home page order | 1. Price ladder bar. 2. Collection navigation (Military, Patriotic, Hawaiian Islands, Americana). 3. Lifestyle hero photo. 4. Holiday sale and mix-and-match banner. 5. Men's tiles and new arrivals. 6. Women's. 7. Hats. 8. Fabric technology block. 9. Instagram. 10. Reviews. | VERIFIED |
| Apparent traffic | 62 active US Meta ads on the "Haven Golf Company" page. Meta pixel, Google Ads tag, Klaviyo, Triple Whale. | VERIFIED |
| Theme | Symmetry 8.2.0, a paid Shopify Theme Store theme. The builder's theme is a different theme (file 01). | VERIFIED |
| Dropshipping signs | None. | VERIFIED observations |

Why it matters: the proof behind the video's headline number is a multi-product apparel brand with repeat buyers and a multi-buy offer, not a one-product dropship store.

### C. The free AI store builder (StoreBuild.ai) and the store it makes

Screenshots: `storebuild_home_desktop.jpg`, `storebuild_example-section_desktop.jpg`, `storebuild_austinrabin_desktop.jpg`, `storebuildai-com_home_desktop.jpg`, `storebuild_app_niche-picker_desktop.jpg`, `storebuild_app_examples-section_desktop.jpg`, `storebuild_shopify-app-listing_desktop.jpg`, `storebuild_vendor-example-store_top_desktop.jpg`, `storebuild_vendor-example-store_fullpage.jpg`.

The landing page (https://storebuild.ai/):

| Item | Finding | Label |
|---|---|---|
| Promise | "Create Your Shopify Store for Free with our Ai Store builder in 2 minutes"; "will add 10 Top products from a trusted supplier" | VERIFIED |
| Inputs | One niche from six tiles: Clothing, Pets, Tech, House, Sports, "Need Inspiration" | VERIFIED |
| Social proof claimed | "Awarded 1# Shopify Partner in Americas"; "Trusted by over 350,000+ sellers"; "Used by over 340,000 stores"; "Every day, over 228 new individuals make their first sale"; "Rated Excellent 4.8/5 by our 9000+ Reviews on Shopify & TrustPilot". The app page says "1.5 Million Stores Created" and shows "(5,675 Reviews)" and "(4.7 - 10.420 Reviews)". | VERIFIED that the pages say this |
| What can be checked | Trustpilot shows 146 reviews at 4.4 (file 01). The Shopify App Store page for "Storebuild.ai AI StoreBuilder" reads "This app is not currently available on the Shopify App Store. If you have support questions, contact Storebuild.ai directly." So the "9000+ reviews on Shopify & Trustpilot" line cannot be reconciled with either source today. | VERIFIED |
| Odd copy | "Sell with no upfront payments: Customers get their products in just hours and pay only upon delivery". Pay-on-delivery in hours is not how Shopify plus Zendrop works for US orders. The phone mockup's status bar shows a Portuguese app name. The page appears to be adapted from another market. | VERIFIED reads; the origin is our inference |
| Creator pages | storebuild.ai/austinrabin is an email capture box: "3-day free trial and just $1/month for your first 3 months". storebuildai.com is titled "Free Ai Shopify Store Builder - By Zendrop X Austin Rabin" and leads with a welcome video. | VERIFIED |

The store it produces. No live public example was found: three reviews that rank for the builder (ecomm.design, DropMagic, a bearblog review) link to none, and the store name in the vendor's own example (youngroadsters.com) does not resolve. The post-signup result could not be inspected because signing up is outside the rules. What follows is read from the vendor's own example images and from the video's captions.

| Element of the default store | What the vendor's examples and the video show | Label |
|---|---|---|
| Layout | Shopify's free default layout pattern: centered logo text, "Choose options" buttons on product cards, "Shipping calculated at checkout", quantity box, outline "Add to cart" plus solid "Buy it now", "Follow on Shop", "Powered by Shopify" footer. One review reports secondary coverage calling it Dawn-based; the theme's real name is UNKNOWN. | VERIFIED from the vendor image; theme name UNKNOWN |
| Store name and logo | "My Store" in text, no logo. In the video Claude's audit reports "the default my store, no logo or description". | VERIFIED (vendor image, captions) |
| Announcement bar | "Free Worldwide Shipping" | VERIFIED (both vendor examples) |
| Navigation | Home, Catalog, Contact | VERIFIED |
| Hero | One stock lifestyle photo with a headline and a button | VERIFIED |
| Value blocks | Three icon columns with generic text. In the fitness example: "TOP QUALITY PRODUCTS" and "WORLDWIDE SHIPPING ... so you can enjoy your new tech without delays" (tech copy on a fitness store). | VERIFIED |
| Products | A grid of white-background product photos with a "Save" badge, star row and single-digit review counts; one featured product with color swatches. The built store carries 10 products in the chosen niche; one competitor review says every user in a niche gets the same ten. | VERIFIED for the image; "same ten" is ESTIMATED (DropMagic, a competitor, read 2026-11-21) |
| Reviews | The example image shows three text testimonial cards with names. In the video the real built store had no review app, and Claude could not add reviews. | VERIFIED |
| Guarantee | A "30 days warranty" seal with a short paragraph | VERIFIED (vendor image) |
| Other sections | A lead-magnet block, a founder-story block, a newsletter block, default policy links | VERIFIED (vendor image) |
| Missing | No quantity or bundle pricing, no delivery-time statement by the button, no video, no before/after proof, no comparison table, no FAQ (Claude adds one in the video), no cross-sell, no press | VERIFIED as absent from the vendor image |

Three cautions for our test:
1. If a built store arrives with pre-written testimonial cards like the example image, they must be deleted before any traffic. CLAUDE.md section 9 bans fake reviews, and they are an FTC problem.
2. "Free Worldwide Shipping" as a default bar is a shipping-time promise we would own under the FTC Mail Order Rule. It needs to be replaced with a time we can meet.
3. The example store in the vendor's own image sells children's ride-on cars, which is on our excluded list. The builder's product picks are not filtered for our rules.

### D1. Uproot Clean (pets)

Screenshots: `uprootclean_home_desktop.jpg`, `uprootclean_product_cleaner-pro_desktop.jpg`, `uprootclean_product_cleaner-pro_phone.jpg`. URL: https://uprootclean.com/

| Item | Finding | Label |
|---|---|---|
| What it sells | A hand scraper with a copper-colored edge that pulls pet hair out of carpet and fabric, in four sizes (Mini, Pro, Max, Xtra), then grooming tools and pet-laundry consumables. First product record 2021-03-06. | VERIFIED |
| Price | Cleaner Pro $16.99 (was $19.99) | VERIFIED |
| Offer structure | Pack selector: 1 for $16.99, 2 for $24.99 marked "Most Popular", 3 for $32.99. "Free Mystery Gift" if ordered today. Kit bundles directly under the button from $24.99 to $69.99. Laundry tabs and sheets on subscription. A $9.99 "Lifetime Replacement Voucher" exists in the catalog. | VERIFIED |
| Shipping promise | Free shipping over $49; in-stock orders processed in 1 to 3 business days; delivery days not stated in the policy | VERIFIED |
| Ships from | "Ships Fast From Florida" icon under the button. Footer address in Atlanta, Georgia. | VERIFIED |
| Returns | "First-Purchase Guarantee": 30 days from delivery, opened or used is fine, buyer pays return shipping, repeat purchases not refundable | VERIFIED |
| Trust elements | 4.9 stars with 24,896 reviews next to the title. Press quotes from BuzzFeed, Today and Nifty. Easy Returns, 30-Day Guarantee, Ships Fast icons. Store locator link (retail distribution). | VERIFIED that the page shows these |
| Trustpilot | 2.0 on 19 reviews (79% one-star); profile claimed this month | VERIFIED; tiny sample next to the on-site count |
| Product page order | 1. Gallery and review count. 2. Price, five ticked benefits, pack selector, stock dot, button. 3. Free gift strip and three trust icons. 4. Bundle upsells. 5. "See it in Action" row of seven short videos. 6. Results section with a list of surfaces. 7. Before/after slider. 8. How to use, with three angles. 9. FAQ, first answer open with a money-back promise. 10. Size comparison table. 11. Press quotes. 12. "You may also like". 13. Reviews with photos. | VERIFIED |
| Apparent traffic | Heavy paid social. 2,183 active US ads on its own page. Separate persona pages ("Rachel's Finds", "Maria's Finds", "Noah's Deals") also run Uproot ads. Meta pixel, AppLovin and Northbeam tags, Klaviyo. Also on Amazon: Uproot Clean Pro at $15.99 with about 31,400 ratings. | VERIFIED for tags and Ad Library; Amazon figures ESTIMATED (DataForSEO, 2026-11-21) |
| Dropshipping signs | The product type is generic (three-packs at $6.79 on Amazon). The business is no longer dropship-style: US stock, retail, patents link, subscriptions. | VERIFIED observations; Amazon ESTIMATED |

Lesson: a $17 generic item works here only because the average basket is pushed up with packs, kits and refills, and because a 24,896 review count sits beside the price.

### D2. Galaxy Lamps (home)

Screenshots: `galaxylamps_home_desktop.jpg`, `galaxylamps_product_galaxy-projector_desktop.jpg`, `galaxylamps_product_galaxy-projector_phone.jpg`. URL: https://galaxylamps.co/

| Item | Finding | Label |
|---|---|---|
| What it sells | Two products: Galaxy Projector 2.0 and Galaxy Projector Rhythm. A true one-product-style store. Current product records were created 2025-09-02; its Trustpilot profile was claimed in August 2020, so the brand is older than the current catalog. | VERIFIED |
| Price | $59.99 (was $149.99, "Save 60%"); Rhythm $79.99 | VERIFIED |
| Offer structure | Single unit, star color choice, quantity box, Shop Pay installments. "60% Off While Supplies Last" badge on the image. No bundles. | VERIFIED |
| Shipping promise | "Free 2-Day Shipping on Order Over $100 in the US" (one projector does not reach $100). Shipping tab: "USA - 2-4 Day Standard or 2 Day Express"; Canada 4 to 9 days; Rest of World 5 to 15 days. | VERIFIED |
| Ships from | UNKNOWN. No shipping policy page exists at the standard address (404). | VERIFIED 404 |
| Returns | "Free Returns" and "Lifetime Guarantee" icons. No refund policy page at the standard address (404). Terms UNKNOWN. | VERIFIED |
| Trust elements | Press logo images (NYT, AP, The Guardian, Mashable, Business Insider) under "As Seen In", with no links. Four testimonials on the home page dated 2021 to 2023. No review count or review widget on the product page. | VERIFIED |
| Trustpilot | 1.4 on 104 reviews; visible reviews describe orders that took months or never arrived | VERIFIED |
| Product page order | 1. Gallery and price. 2. Color, quantity, button. 3. Three icons. 4. Description, specs and shipping accordions. 5. Press logos. 6. Three feature blocks whose text describes an LED TV backlight strip ("simply cut our LED strip"), not a projector. 7. Icon grid of features. 8. FAQ. 9. App block. Total length about 4,500 px. | VERIFIED |
| Apparent traffic | No active ads found for its domain. A keyword search returns other small pages ("KaelroCozy", "KaelroHoliday", "Zvorna choice", "Toveq/cozy") running "HOT DEAL 55% OFF" galaxy projector ads. Meta pixel and Klaviyo are installed. Current traffic source UNKNOWN. | VERIFIED Ad Library reads |
| Dropshipping signs | Generic product (Amazon $9.49 to $189.95; a $27.99 astronaut projector has about 17,000 ratings). Leftover template copy for a different product. No policy pages. Delivery complaints. | VERIFIED; Amazon ESTIMATED |

Lesson: this is what a once-famous one-product store looks like after the product became a commodity. It is the cautionary example in the set, not a model.

### D3. Pillow Slides (home comfort, footwear)

Screenshots: `pillowslides_home_desktop.jpg`, `pillowslides_product_pillow-slides_desktop.jpg`. URL: https://pillowslides.com/

| Item | Finding | Label |
|---|---|---|
| What it sells | Thick-soled foam slides, grown into 50 products: slippers, clogs, sneakers, insoles. First product record 2020-11-22. | VERIFIED |
| Price | $39.99 (was $59.99) | VERIFIED |
| Offer structure | Single pair with nine colors and eleven sizes. Free US shipping over $60 pushes a second pair. A Meta ad on its page reads "Buy 2 Get 1 Free Today!". "Priority insured and tracked shipping" add-on that only shortens processing. | VERIFIED |
| Shipping promise | Policy: 1 to 4 business days to process, then USA 4 to 12 days. Product page: processed in 1 to 2 business days, USA 4 to 12 business days. | VERIFIED |
| Ships from | UNKNOWN | |
| Returns | 30-day request window; buyer pays return shipping on the main products. Shipping policy: "We will not be accepting any refunds for delayed orders unless it is lost in tracking." | VERIFIED |
| Trust elements | "300,000+ happy customers"; 4,007 reviews on the product card (Judge.me); "HOT" and "Most Loved" badges; "30-Day Comfort Guarantee" | VERIFIED that the page shows these |
| Trustpilot | 1.6 on 53 reviews, 86% one-star, unclaimed profile | VERIFIED |
| Product page order | 1. Gallery, price, color and size. 2. Button. 3. Customer count line. 4. Benefits, shipping and care tabs. 5. Cross-sell row. 6. "Why Pillow Slides" checklist. 7. Customer photo quotes. | VERIFIED |
| Apparent traffic | Meta pixel, Google Ads and Taboola tags. 8 active US ads on its page, billed in Canadian dollars. | VERIFIED |
| Dropshipping signs | Generic product (Amazon from $8.54; one listing has about 62,100 ratings at $19.33). 4 to 12 day delivery. Support runs from a free webmail address. Refusal to refund for delay. | VERIFIED; Amazon ESTIMATED |
| Compliance note | Copy leans on "plantar fasciitis", "arthritis" and "orthopedic". Those are health claims and are off limits for us. | VERIFIED |

### D4. Bleame (beauty tools)

Screenshots: `bleame_home_desktop.jpg`, `bleame_product_crystal-hair-eraser_desktop.jpg`. URL: https://bleame.com/

| Item | Finding | Label |
|---|---|---|
| What it sells | A hand-held "crystal hair eraser" (a textured glass pad), plus a scrub, a mask and a gua sha set. Five products. First product record 2022-01-10. | VERIFIED |
| Price | 2 pack $53 (was $99), preselected. 1 pack $26 (was $44). | VERIFIED |
| Offer structure | Two-pack default "Includes FREE shipping" plus a free body scrub. Countdown timer in the top bar. "Body Scrub included for the next 128 orders!". "Want It By Monday, 23 Nov? Order within 2 hours 12 minutes". Footer links to a "VIP Membership" cancellation page, which suggests a membership add-on at checkout (not opened). | VERIFIED |
| Shipping promise | Product page: "Free Shipping from US" and the dated "want it by" line. Shipping policy page: "United States: 5-18 business days". These two cannot both be true for the same order. | VERIFIED contradiction |
| Ships from | Contradictory, so UNKNOWN | |
| Returns | Page: "30-Day Guarantee". Policy: 15 days after receipt to request a return; 24 hours to cancel. | VERIFIED |
| Trust elements | "Excellent 4.8, 4974 reviews" at the top of the product page; "Rated 4.8/5 by 1,319+ Happy Customers" lower on the same page; "7,322 trusted reviews" on the home page; "175,000+ Happy Babes". The "Excellent 4.8" wording is in the style of a review-site badge. | VERIFIED that the three counts disagree |
| Trustpilot | 3.3 on 2,003 reviews; 56% five-star and 30% one-star | VERIFIED |
| Product page order | 1. Gallery with free-gift banner, rating, price. 2. Emoji benefit list. 3. Pack selector with scarcity counter. 4. Button, payment icons, "want it by" timer, two icons. 5. FAQ accordions. 6. Customer video wall. 7. Body-area demo tabs. 8. Three benefit icons around a before/after slider. 9. Percent-of-users stats. 10. Before/after photos with quotes. 11. Comparison table against waxing and laser. 12. Guarantee block. 13. FAQ. 14. Risk-free icons. 15. Cross-sell. | VERIFIED |
| Apparent traffic | 0 active US ads on its page today; the only Bleame ad the search returned started in February 2023. Klaviyo, Triple Whale and a price-testing tool are installed. Current source UNKNOWN (likely email and organic, our inference). | VERIFIED Ad Library reads |
| Dropshipping signs | The clearest generic in the set: the same item type sells from $3.76 on Amazon and under $1 a piece wholesale. Policy delivery of 5 to 18 business days. | VERIFIED; prices ESTIMATED |

Lesson: this page is the full dropship playbook in one place, including the parts we must not copy (conflicting shipping claims, a moving scarcity counter, inconsistent review totals).

### D5. Nood (beauty tools, higher ticket)

Screenshots: `nood_home_desktop.jpg`, `nood_product_flasher-2_desktop.jpg`. URL: https://trynood.com/

| Item | Finding | Label |
|---|---|---|
| What it sells | An at-home IPL hair removal handset (Flasher 2.0, Flasher Pro), then razors, serums, an LED mask and skincare. 35 products. First product record 2021-08-10. | VERIFIED |
| Price | Flasher 2.0 $129 (was $199). Flasher Pro $249. Sets up to $507. | VERIFIED |
| Offer structure | Device first, then a "Pairs well with" row ($15 to $39 items), sets, and refill subscriptions. Affirm installments. | VERIFIED |
| Shipping promise | "In stock: ships free tomorrow". "Every order is processed within 24 hours and shipped directly from one of our U.S. warehouses". | VERIFIED |
| Returns | 90-day guarantee on the device, refund less a $29.95 restocking fee; other items final sale; box-free return drop-off through a returns partner | VERIFIED |
| Trust elements | 19,934 reviews at 4.5 next to the title. Lifetime guarantee. A named dermatologist on an advisory board. Comparison table against a Braun device. "92% reduction in hair regrowth" clinical claim. | VERIFIED that the page shows these |
| Trustpilot | 4.0 on 40 reviews | VERIFIED |
| Product page order | 1. Gallery, bestseller tag, rating, price. 2. Button and a rotating guarantee strip. 3. Cross-sell row. 4. Detail accordions. 5. Clinical results block. 6. Device specs. 7. Model comparison. 8. Doctor quote. 9. Cost comparison against laser and waxing. 10. Routine cross-sell. 11. FAQ with a skin-tone suitability chart. 12. Reviews. | VERIFIED |
| Apparent traffic | 468 active US ads on its page. The same persona pages seen for Uproot ("Noah's Deals", "Tess Recommends", "Maria's Finds", "Rachel's Finds") run Nood ads too. Meta, TikTok, Google Ads, Pinterest, AppLovin and Taboola tags. SMS and email capture. Its Flasher Pro model is on Amazon at $249 with about 745 ratings and 900+ bought in the past month. | VERIFIED for tags and Ad Library; Amazon ESTIMATED (DataForSEO, 2026-11-21) |
| Dropshipping signs | The category is full of generic handsets on Amazon ($28.49 to $437.99). Whether Nood's unit shares a factory with any of them is UNKNOWN. Operations are not dropship-style: US warehouses, 90-day guarantee. | Amazon ESTIMATED |
| Compliance note | An IPL device carries clinical and skin-safety claims. That sits in our excluded "medical, health claims, safety risk" territory. Included here for store structure only. | |

### D6. CARLUEX (car, gadgets)

Screenshots: `carluex_home_desktop.jpg`, `carluex_product_pro-plus-2_desktop.jpg`. URL: https://www.carluex.com/

| Item | Finding | Label |
|---|---|---|
| What it sells | Plug-in boxes that add wireless CarPlay and streaming apps to a car screen. 14 products on this storefront (first record 2023-11-01). A second storefront at carluex.store has 13 products (first record 2022-09-28). | VERIFIED |
| Price | PRO+ 2.0 $269 (was $399). Other models $59 to $359. | VERIFIED |
| Offer structure | Single unit, quantity box, Shop Pay installments ("from $24.28/mo"). Accessories $6.99 to $80. | VERIFIED |
| Shipping promise | 1 to 2 business days processing. Orders $51 to $300: 5 to 10 business days free, or 3 to 7 for $19.99. Over $301: 3 to 7 business days free. | VERIFIED |
| Ships from | Not stated. The policy says the buyer is responsible for customs duties and that the seller tries "to reduce the declared value of the package". Return instructions ask for an international courier and for brand names to be removed from the package. This reads as cross-border shipping. | VERIFIED text; the conclusion is our inference |
| Returns | 30 days. "$15 USD will be charged" on any refund. $30 restocking fee for change of mind or after 15 days. Buyer pays return shipping. 1-year warranty. | VERIFIED |
| Trust elements | Almost none on the page: four ticked lines and installments. No reviews, no guarantee block, no shipping line by the button. | VERIFIED |
| Trustpilot | 3.0 on 44 reviews for carluex.store (41% five-star, 50% one-star). No profile for carluex.com. | VERIFIED |
| Product page order | 1. Gallery, title, price. 2. Four ticked benefits. 3. Quantity and buttons. 4. Related products. 5. Footer. Total length about 2,500 px. | VERIFIED |
| Apparent traffic | 12 active US ads on its page. Tech-blog reviews exist (AndroidGuys, The Gadgeteer). Meta pixel only. | VERIFIED Ad Library; blog reviews ESTIMATED (web search, 2026-11-21) |
| Dropshipping signs | Long delivery window, customs language, fee on refunds. It is a Chinese electronics brand selling direct, with similar boxes on Amazon from $28.48 to $289. | VERIFIED; Amazon ESTIMATED |

Honest note: this is the weakest traction evidence in the set. It is included as the example of a high-ticket gadget sold from a thin page with cross-border shipping, and its public rating shows the cost of that.

### D7. Synoshi (home gadget, funnel style)

Screenshots: `synoshi_home_desktop.jpg`, `synoshi_order_desktop.jpg`. URL: https://synoshi.com/

| Item | Finding | Label |
|---|---|---|
| What it sells | One cordless electric spin scrubber with swap heads. Operator named on the site: EcomLT LLC. Not a Shopify store; a custom sales funnel. | VERIFIED |
| Price | The sales page shows no price, only "SAVE up to -70%". The order page shows: 1 unit $42.99, 2 for $49.96, 3 for $69.96, 4 for $85.96 ("Most Popular", preselected), each against a $71.99 per-unit "was" price. Shipping "Standard $9.95" is added. | VERIFIED |
| Offer structure | Quantity ladder built so that two units ($49.96) cost only slightly more than one ($42.99). Checkout form is on the same page as the ladder. Opt-in boxes for SMS and for follow-up phone calls with offers. An accessories page and an affiliate program link. | VERIFIED |
| Shipping promise | Processing 1 to 2 business days. "United States 8-12 d." (business days). The policy says timelines are "illustrative" and not guaranteed. | VERIFIED |
| Ships from | UNKNOWN. "International delivery to most regions"; customs charges may be payable by the recipient. | VERIFIED text |
| Returns | 60 days from receipt, including change of mind, through a return form and RMA; shipping not refunded; refund within 14 business days of receipt | VERIFIED |
| Trust elements | Six "Verified Customer" text testimonials. Before/after photos. Comparison table against "traditional tools". IPX5 claim. Phone numbers for four countries. | VERIFIED that the page shows these |
| Trustpilot | 4.2 on 6,385 reviews; claimed profile with a paid Trustpilot subscription; 13% one-star | VERIFIED |
| Page order | 1. Hero with discount and Order Now. 2. Three icon benefits. 3. A list of conditions the buyer may have (mobility issues, arthritis, Parkinson's, back pain). 4. Three benefit blocks. 5. Design features. 6. Before/after pairs. 7. Surfaces. 8. Comparison table. 9. Five reasons. 10. FAQ. 11. Testimonials. Order buttons repeat throughout. | VERIFIED |
| Apparent traffic | No active ads found on its own Facebook page. Seven active ads from a listicle publisher ("54 Genius Products on Amazon You've Never Seen Before") match the brand name. With the affiliate link in the footer, this looks like affiliate and advertorial traffic. | VERIFIED Ad Library reads; the reading is our inference |
| Dropshipping signs | Generic product (Amazon $16.14 to $93.49; a $33.99 unit shows 10K+ bought in the past month). 8 to 12 business day delivery. Discount anchored to a price never charged. | VERIFIED; Amazon ESTIMATED |
| Compliance note | Naming medical conditions as the reason to buy is a health-claim angle we cannot use. | |

---

## 4. Patterns across the stores

What the stores with real traction share (Uproot Clean, Nood, oneisall, Haven; and, for page craft only, Bleame and Synoshi):

1. One hero, sold in multiples. Pack selectors (Uproot 1, 2, 3; Bleame 1, 2; Synoshi 1 to 4), kit tiers (oneisall four sets) or mix-and-match (Haven 2, 3, 4). The middle or larger option is preselected or badged "Most Popular". Nood is the exception: it sells the device as a single unit and raises the basket with a cross-sell row and sets instead.
2. A big review number at the very top of the product page: 24,896 (Uproot), 19,934 (Nood), 4,974 (Bleame). oneisall and Haven show smaller per-product counts (105 and 6) backed by larger site-wide totals. Pillow Slides shows 4,007 on its product card. The two stores with no count at all (Galaxy Lamps, CARLUEX) have the shortest pages and weak public ratings.
3. A specific promise within a thumb's reach of the button: where it ships from, how fast, and the guarantee length. "Ships Fast From Florida", "Ships free tomorrow", "Fast 2-4 Day Shipping", "30-Day Money Back", "24-Month Warranty".
4. Proof that the thing works, in motion: short customer-style video rows, before/after sliders, demonstration clips. Uproot has seven videos above the description.
5. A reason to spend more or come back: refills and subscriptions (Uproot laundry, Nood serum), replacement parts (oneisall), sibling products (Haven collections).
6. Comparison and objection handling: a table against the alternative (waxing, laser, a named competitor, "traditional tools"), then an FAQ whose first answer restates the guarantee.
7. Long pages. Product pages run about 9,600 to 23,000 px on desktop for the strong stores, against about 2,500 to 4,500 px for the weak ones.
8. Paid social at volume, with many creatives. Active US ad counts on brand pages: 2,183, 468, 121, 62. Two of the brands also appear on shared persona pages with names like "Rachel's Finds". What those pages are (an agency network or affiliates) is UNKNOWN.

What separates the healthy stores from the ones with bad public ratings:

| Store | Delivery stated for US | Stated US stock | Trustpilot | Label |
|---|---|---|---|---|
| oneisall | 1 to 2 plus 3 to 4 working days | Yes | 4.9 on 746 | VERIFIED |
| Haven Golf | 2 to 4 days | Yes (creator's words) | 4.7 on 54 | VERIFIED rating |
| Nood | Ships next day | Yes | 4.0 on 40 | VERIFIED |
| Synoshi | 8 to 12 business days | No | 4.2 on 6,385 (profile actively managed) | VERIFIED |
| Bleame | 5 to 18 business days in policy | Claimed on page, contradicted by policy | 3.3 on 2,003 | VERIFIED |
| CARLUEX | 5 to 10 business days | No | 3.0 on 44 | VERIFIED |
| Uproot Clean | Processed in 1 to 3 business days | Yes | 2.0 on 19 | VERIFIED; sample too small to weigh against 24,896 on-site reviews |
| Pillow Slides | 4 to 12 days after 1 to 4 processing | No | 1.6 on 53 | VERIFIED |
| Galaxy Lamps | 2 to 4 days claimed | Not stated | 1.4 on 104 | VERIFIED |

Read with care: Trustpilot attracts complaints, several samples are small, and Synoshi shows that an actively managed profile can look fine with slow shipping. The direction still matches Dhruv's instinct. In this set, long or unclear delivery on a generic product goes together with refund fights and one-star reviews, and the stores that say plainly "ships from the US in a few days" do not have that problem.

---

## 5. How a winning store differs from the default store the builder makes

In plain words:

- The default store is a small general shop. A winning store is a sales page for one product. The builder gives you ten unrelated items in a niche with equal weight on the home page. The winners point everything at one hero and send ad traffic straight to its product page.
- The default store sells one unit at one price. Winners sell packs. There is no quantity ladder, kit tier or "buy 2" offer in the default. Every store with traction has one, and it is the main lever on order value.
- The default store has no proof. It ships with no review app, and the vendor's example shows three text testimonial cards. Winners open with a five-figure review count, customer photos and video. A new store cannot fake this and must not try; it has to borrow other proof (demonstration video, a clear guarantee, an honest "new brand" tone) until real reviews exist.
- The default store promises "Free Worldwide Shipping". Winners state a place and a number of days. "Ships from Florida", "ships tomorrow", "2 to 4 days". The default line is vague, and we would be legally bound to whatever it implies.
- The default product page is short. Photos, title, price, button, a paragraph. Winners run ten to fifteen sections: benefits, bundles, video, before/after, how to use, comparison, FAQ, press, reviews.
- The default images are supplier photos on white. Winners show the product in a hand, in a home, in use, with numbers printed on the image. The video's answer is AI-generated images. The winners' answer is real footage of the real product, which is also what our rules require.
- The default store has no name, no logo and no voice. "My Store". Winners have a name, a color, a tone and a reason to exist that shows up in every section.
- The default has nothing to buy next. Winners have refills, parts or a second product for the same customer.
- The default policies are template text written around the supplier. Winners (the healthy ones) have short, specific return terms a customer can understand in ten seconds.
- The default theme is a free-style layout. Haven uses a paid Theme Store theme, and Uproot, Nood and oneisall run custom themes. The theme matters less than the sections on the page, but the claim that the builder gives "the exact same theme" as Haven does not hold.

What the video's Claude workflow fixes and what it does not: it rewrites the description, adds an FAQ and swaps images. It does not add an offer structure, reviews, video proof, a shipping promise or a second product. Those are the items that separate the stores above.

---

## 6. Inputs this file hands to later steps

For the scripts and for the ranking work in other files (no math done here):

- Price points that carry traffic in these stores: $16.99 to $59.99 for generic low-ticket heroes sold in multiples; $97.99 to $129 for appliance-type heroes; $269 for a car gadget.
- Multi-unit ladders observed: $16.99, $24.99, $32.99 (Uproot); $26, $53 (Bleame); $42.99, $49.96, $69.96, $85.96 plus $9.95 shipping (Synoshi); $50 each or 2 for $90, 3 for $120, 4 for $140 (Haven).
- Free-shipping thresholds observed: $40 (oneisall), $49 (Uproot), $60 (Pillow Slides), $100 (Galaxy Lamps), $150 (Haven).
- Return terms observed: 15 to 90 days; restocking or refund fees of $15, $29.95 and $30 on the higher-ticket devices; buyer-paid return shipping is the norm.
- Amazon floor prices for each generic product type are in the table in section 2. Any candidate whose Amazon generic sells at a third of our price needs a reason a buyer would not search first.

Flag for the fast lane (approved exception, recorded here so it is not lost): selling before holding the product means the store's images and claims describe an item Dhruv has not seen. The stores above with the worst ratings are the ones whose pages promised more than the parcel delivered.

---

## 7. Unknowns

1. What a store built by StoreBuild today really contains: theme name, the ten pet products, their prices, whether testimonial cards are pre-filled, and the policy text. Needs a signup, which was outside the rules.
2. Whether any of the generic-product stores are still fulfilled per order from a supplier, or hold stock. Only the shipping times and policies are visible.
3. Ship-from location for Galaxy Lamps, Pillow Slides, Synoshi and CARLUEX.
4. Current traffic sources for Bleame, Galaxy Lamps and Synoshi (no active ads found on their own pages).
5. Who operates the persona ad pages that advertise both Uproot Clean and Nood.
6. How long each brand's oldest active ad has run. The Ad Library search returns newest first and only an estimated total, so "long-running" could not be measured. Foreplay, which can, was out of credits.
7. Revenue for every store. Not guessed.

---

## 8. Blocks and limits

- Foreplay MCP: one call tried (`get_brands_by_domain` for uprootclean.com). Returned HTTP 402, "Insufficient credits", 0 remaining. Not retried.
- Trustpilot: pages answered HTTP 403 to the browser request but the content rendered and was read. No Trustpilot profile exists for carluex.com; the brand's profile is under carluex.store.
- Shopify App Store: the StoreBuild listing loads but says the app is not currently available, so no rating or screenshots could be read there.
- galaxylamps.co: `/policies/shipping-policy` and `/policies/refund-policy` return 404. bleame.com and trynood.com return an empty body at `/policies/shipping-policy`; their own shipping pages or product-page shipping text were used instead.
- Dropped candidates that did not respond at all from this network: calmingdog.com, thisworx.com. The vendor example's store name, youngroadsters.com, also does not resolve.
- Meta Ad Library through the Meta Ads connector worked. Keyword searches return many unrelated advertisers, so counts here are page-level wherever a page ID could be found. No page ID was found for Galaxy Lamps.
- Not accessed by rule: any signup, login, checkout or supplier catalog.
- Bias flags: DropMagic sells a competing store builder; ecomm.design carries referral-style links; the bearblog review promotes its own guide. StoreBuild, Zendrop and every store page are vendor marketing. On-site review counts are the stores' own displays.

## 9. Sources (all read 2026-11-21)

- oneisall: https://oneisall.com/ , https://oneisall.com/products/cozy-c1-dog-grooming-vacuum , https://oneisall.com/policies/shipping-policy , https://oneisall.com/policies/refund-policy , https://oneisall.com/products.json , https://www.trustpilot.com/review/oneisall.com
- Haven: https://havengolfcompany.com/ , https://havengolfcompany.com/products/the-inferno , https://havengolfcompany.com/products.json , https://www.trustpilot.com/review/havengolfcompany.com
- StoreBuild: https://storebuild.ai/ , https://storebuild.ai/austinrabin/ , https://www.storebuildai.com/ , https://app.storebuild.ai/page/new-desk , https://apps.shopify.com/storebuildai , https://storebuild.ai/wp-content/uploads/2025/11/image-92.svg , https://storebuild.ai/wp-content/uploads/2025/11/image-93.svg ; reviews: https://ecomm.design/storebuild-ai-review/ , https://dropmagic.ai/ai-store-builder/storebuild-ai-review , https://launchpadreviews.bearblog.dev/store-build-ai-review/ ; video captions for lJtgRzCBePM (pulled earlier through DataForSEO)
- Uproot Clean: https://uprootclean.com/ , https://uprootclean.com/products/uproot-lint-pro , https://uprootclean.com/policies/shipping-policy , https://uprootclean.com/policies/refund-policy , https://uprootclean.com/products.json , https://www.trustpilot.com/review/uprootclean.com
- Galaxy Lamps: https://galaxylamps.co/?country=US , https://galaxylamps.co/products/galaxy-projector?country=US , https://galaxylamps.co/pages/about-us , https://galaxylamps.co/products.json , https://www.trustpilot.com/review/galaxylamps.co
- Pillow Slides: https://pillowslides.com/ , https://pillowslides.com/products/pillow-slides , https://pillowslides.com/policies/shipping-policy , https://pillowslides.com/policies/refund-policy , https://pillowslides.com/products.json , https://www.trustpilot.com/review/pillowslides.com
- Bleame: https://bleame.com/ , https://bleame.com/products/crystal-hair-eraser , https://bleame.com/pages/shipping , https://bleame.com/policies/refund-policy , https://bleame.com/products.json , https://www.trustpilot.com/review/bleame.com
- Nood: https://trynood.com/ , https://trynood.com/products/the-flasher-2 , https://trynood.com/policies/refund-policy , https://trynood.com/products.json , https://www.trustpilot.com/review/trynood.com
- CARLUEX: https://www.carluex.com/ , the PRO+ 2.0 product page, https://www.carluex.com/policies/shipping-policy , https://www.carluex.com/policies/refund-policy , https://www.carluex.com/products.json , https://www.carluex.store/products.json , https://www.trustpilot.com/review/carluex.store
- Synoshi: https://synoshi.com/ , https://synoshi.com/synoshi-pro/order , https://synoshi.com/synoshi-pro/shipping , https://synoshi.com/synoshi-pro/return , https://synoshi.com/synoshi-pro/about-us , https://www.trustpilot.com/review/synoshi.com
- Meta Ad Library (through the Meta Ads connector): page-level active US ad counts for Uproot Clean, Oneisall_Official, Nood, Haven Golf Company, Pillow Slides, Bleame and CarLuex-CarPlay-Adapter; keyword searches for Galaxy Lamps and Synoshi
- Amazon listings: DataForSEO `merchant/amazon/products/live/advanced`, seven keyword searches, US
- Global Sources crystal hair remover listing (via web search result): https://www.globalsources.com/Epilator/Epilators-1213166744p.htm
