# Skeptic check: cheaper customers than Meta ads? (2026-11-22)

Role: skeptic. I re-opened primary sources for the claims Dhruv is most likely to act on, from
`01_creator_economics.md`, `02_low_cost_tactics.md` and `research/reel-check-2026-11-22/`.
I checked in both directions: claims that are too strong and facts that were missed.

Labels: VERIFIED means I read it on a primary page today. ESTIMATED means third-party or
self-reported, with link and date. ASSUMED means our own placeholder. UNKNOWN means not found.
No arithmetic here. Inputs for the script are listed at the end.

Access notes for this pass:
- Collabstr: WebFetch got HTTP 403 on https://collabstr.com/top-influencers/dog. A second
  Playwright render was not run (the session blocked it). Prices come only from search snippets.
- AG1 (drinkag1.com): HTTP 429 again. Not bypassed.
- finviz release URL used in the notes now returns 404. Facts checked through search results.
- Billo PDF: WebFetch could not read it, so I extracted the text with pdftotext.

## 1. Creator and UGC prices

| Claim in the notes | Verdict | What I found today |
|---|---|---|
| Billo from $99 per 15-second video; $1,000 minimum pack; product and shipping not included | Holds | "Videos start at $99, which covers a 15-second video from a regular creator with basic editing." "It doesn't cover your product or shipping it to the creator." Packs: Essential $1,000 (up to 10 videos), Professional $2,500 plus $300 bonus (up to 28), Refine $5,000 plus $700 bonus (up to 57). Usage rights, raw footage and turnaround are not on the page. VERIFIED, https://billo.app/pricing/ |
| soona (ex Trend.io) $89 to $259 per video, unlimited license, 7 days after product arrives, brand ships | Holds | trend.io/pricing now 301-redirects to soona.co/ugc with a "trend-winddown" tag. "Video prices range from $89/video to $259/video." "All content includes an unlimited, worldwide license for all platforms and purposes." "No annual commitments." Content "within 7 days" after the creator receives the product. "Ship your products directly to the creators." Per-level prices not listed. VERIFIED, https://soona.co/ugc |
| Insense subscription $400 to $650 a month, 7% to 20% fee, UGC from $100, sponsored posts from $125 | Partly holds. The monthly figures are right but understate the commitment | Trial "from $650/mo" lasts one month and auto-upgrades to the quarterly Brand plan unless cancelled at least 48 hours before the trial ends. Brand is $500/mo billed $1,500 a quarter, or $400/mo billed $4,800 a year. Fees: 20% Trial, 10% Brand, 7% Agency. Product seeding is NOT available on the Trial plan. So a physical-product brand needs Brand: $1,500 up front per quarter before any creator pay. Content rights wording conflicts on the page ("full digital copyright" vs "copyright of the content remains with the creator"). VERIFIED, https://insense.pro/pricing |
| Collabstr dog creators: Nash the Berner $50 TikTok, Coconut the Yorkiepoo $75, Mochi $150 | Cannot be checked. Two details look wrong | Live page blocked (403). Search snippets today: Coconut the Yorkiepoo is listed in Ottawa, Canada, at $75 on TikTok; the profile shows "Negotiate a Package", not a fixed price. Nash the Berner's $50 listing is shown as Instagram, not TikTok, and the profile claims 1.5M followers and 250k average views, which does not fit a $50 small-creator rate. The cached list title reads "Top 2,928 Dog Influencers" while the live page showed 3,851 earlier today, so snippets are stale. ESTIMATED, https://collabstr.com/coconut-the-yorkiepoo ; https://collabstr.com/nashtheberner (search snippets, 2026-11-22) |
| Collabstr pets averages $160 to $225 per post | Cannot be checked | Calculator pages blocked earlier; not re-read. Search-summary only. ESTIMATED |
| Market UGC rate guides $150 to $500 per video | Not re-checked | Left as ESTIMATED in the notes. |

Takeaway: the three fixed-price UGC platforms check out. The $50 to $225 paid-post range for pet
creators is not reliable. One example creator is in Canada, one listing is on another platform, and
the snippets are out of date. Insense is not a $400 tool for us. Seeding needs the Brand plan
at $1,500 a quarter.

## 2. TikTok Shop US rules (sellers and affiliates)

| Claim | Verdict | What I found today |
|---|---|---|
| Referral fee 6% for Pet Supplies; base is customer payment plus platform discount minus tax, including customer-paid shipping | Holds | Page "Updated at: 10/08/2026". Formula: "Referral Fee = Referral Fee Rate x (Customer Payment + Platform Discount - Tax)". "The Referral Fee calculation base includes the shipping fee paid by the customer." Pet Supplies rows (Dog & Cat Accessories, Furniture, Clothing, Grooming and others): 6%. Automotive rows: 6%. No "8%" anywhere on the page. Caveat: the page title still reads "TikTok Shop Referral Fees in 2024 by Category". VERIFIED, https://seller-us.tiktok.com/university/essay?knowledge_id=5988482086864682 |
| Sellers must own inventory; US sellers cannot use international third-party suppliers; dispatch in 2 business days, deliver in 6 | Holds | Page "Updated at: 09/09/2026". "You may use third-party fulfillment providers to pack and ship your items, provided that you maintain ownership of the inventory." "U.S.-based sellers cannot use international third-party suppliers or consolidation services." "Orders must be dispatched within 2 business days" and "Deliver within 6 business days of Awaiting Shipment". Also: no invoices or packaging that identify another seller or supplier. VERIFIED, https://seller-us.tiktok.com/university/essay?knowledge_id=6179821974439723 |
| Free samples only to creators with sales in the last 120 days; seller approves; post within 14 days | Holds, but the notes missed the second sample type | Page "Updated at: 11/20/2026". There are two sample types. Free Samples: "available to creators who have generated sales on TikTok Shop within the last 120 days", seller may "approve, reject, or ignore". Refundable Samples: "open to eligible creators who buy first and get a full refund only if they post a qualifying shoppable video/LIVE within 14 days and hit the seller's sales goal by Day 54 after delivery." "No seller approval needed." "Sellers usually require 1 to 3 orders generated." Who funds the refund is not stated. VERIFIED, https://seller-us.tiktok.com/university/essay?knowledge_id=5764641632306946 |
| Pet affiliate commission 13.1% average | Holds as a vendor figure | Hubfluence: Pet Supplies 1,515 selling videos, GMV per unit $36.94, average listed price $42.40, average commission 13.1%, GMV per 1,000 views $122. ESTIMATED, https://www.hubfluence.io/blog/tiktok-shop-benchmarks (Michael Tona, Nov 5, 2026) |
| Median selling video 3.64 units per 1,000 views; 86.8% paid-boosted; zero-sales excluded | Holds, with a stronger caveat | "Videos with zero sales are excluded, so these are benchmarks for selling videos, not all shoppable videos." Sample: 12,881 videos posted Oct 6 to 12, 2026, measured in early November; capped at 300 per category and tier; weighted. 86.8% "flagged as having run as paid ads", 88.5% of GMV. But the Pet line says "1,515 selling videos, 30 days", a different window from the headline sample. These per-view figures cannot predict a random creator post, because every non-selling video was removed. ESTIMATED, same link |

Missed fact that matters: Refundable Samples. A creator buys the kit, posts within 14 days, and gets a
refund only after the sales goal is met. This could cut the "lost kit per non-posting creator" risk
for a $149 kit. Who pays the refund, and whether a seller can set the goal, is UNKNOWN from this
creator-facing page.

Still UNKNOWN: whether a kit Dhruv imports, owns and ships from home counts as owned inventory. The
rule bans international third-party suppliers for fulfilment. It does not say owned imported stock is
banned. I did not find an explicit statement either way.

## 3. Do creator or partnership ads cost less per purchase than normal Meta ads?

| Claim | Verdict | What I found today |
|---|---|---|
| Meta: partnership ads cut CPA about 19% | Partly holds. Old, small and self-reported | 15 advertiser tests, North America and APAC, June 2021 to January 2022. Comparison: campaigns with partnership ads above 20% of spend. Confidence level not stated. Run by Meta. ESTIMATED, https://ppc.land/meta-says-partnership-ads-cut-incremental-purchase-costs-45-in-emea-tests/ (Oct 11, 2026) |
| Meta: cost per incremental purchase 45% lower | Partly holds. Different metric and different setup | 20 conversion lift studies, EMEA advertisers, Jan 1 to Jun 30, 2025. Business-as-usual cell vs a cell where at least 30% of assets were partnership ads (added to existing campaigns). Median 45% lower cost per incremental purchase. 92% confidence, below the usual 95%. Meta's own analysis. Same article: agency Charlie Oscar found 30% more incremental conversions "with in-platform CPA unchanged" (94 MMMs). ESTIMATED, same link |
| Agentio: 5% lower CPA, 19% higher CPM | Partly holds. Wrong baseline for our question | 65,000 ads, 137 brands, $130M spend. Comparison is partnership ads vs licensed UGC run from brand accounts, so both arms are creator content. No comparison to normal brand ads. Date range and significance not stated. Agentio sells creator-ad services. Stories placement had 25% higher CPA. ESTIMATED, https://www.netinfluencer.com/meta-partnership-ads-outperform-licensed-ugc-across-130m-usd-in-ad-spend-report-finds/ (Aug 13, 2026) |
| TikTok: Spark Ads 37% lower CPA | Holds as TikTok's claim; useless as a benchmark | "69% higher conversion rate and 37% lower CPA than ever before", credited to the "new profile landing page UI". Footnote: "2022 Spark Ads Internal AB Test Result Data - Performance Auction". No baseline. VERIFIED that TikTok says it, https://ads.tiktok.com/business/en/blog/spark-ads-101-make-tiktoks-into-ads |
| Billo: pet video ad ROAS 1.66 vs 2.41 average; pet last of 14 | Holds as a vendor figure | Press release dated May 29, 2026: 80,069 Meta video ads, July to December 2025, about $105M spend, $206M sales, 14 industries. "Pet Supplies earned just $1.66." "Animals & Pet Supplies finished last on both attention and sales." Toys: 1.46 in July, 2.90 in December. ROAS method and attribution window not stated. These are ads from a UGC platform's dataset, so they are mostly creator-style ads. ESTIMATED, https://s3.amazonaws.com/media.mediapost.com/uploads/BILLO_Benchmarking_2026_05.pdf |

Verdict: there is no evidence that creator or partnership ads win customers more cheaply than normal
Meta ads for a new pet store. Every CPA gain is self-reported by Meta, TikTok or a creator-ad vendor.
The samples are small or old, and some use different baselines. None is pet-specific or new-store-specific. The only
pet-specific data (Billo, mostly UGC ads) points the other way. The notes' "5 to 19%" range mixes
two different baselines and should not go into the script as one number.

## 4. Strongest low-cost tactic claims

| Claim | Verdict | What I found today |
|---|---|---|
| Google free listings $0; review up to 3 to 5 business days | Holds | Reviews "typically take up to 3-5 business days for Shopping ads and free listings." Applies when you are new to Merchant Center or upload products for the first time. No separate timeline for new accounts; you can request review if it takes longer. VERIFIED, https://support.google.com/merchants/answer/160491 |
| Klaviyo free plan: 250 profiles, 500 emails, $5 of mobile messages | Holds | "Up to 250 active profiles and 500 emails per month", "$5 of mobile messages per month". Email support only for the "First 60 days". Lowest paid email plan $20/month. VERIFIED, https://www.klaviyo.com/pricing |
| Buffer: posting more raises breakout odds, not median views; no sales data | Holds | 11.4M posts, 150,000+ accounts, Oct 8, 2025. Median views 489 (1/week), 506 (2 to 5), 487 (6 to 10), 459 (11+). 90th percentile 3,722 (1/week) to 14,401 (11+). No sales or conversion claims. "Posting more helps, but mostly because it increases your chances of getting lucky." VERIFIED, https://buffer.com/resources/how-often-should-you-post-on-tiktok/ |
| Shopify Collabs fee 2.9% on each commission payment | Holds; plan list still unknown | "There's a 2.9% processing fee applied to every automatic commission payment." Billed to the merchant. The page does not say which plans can use Collabs. VERIFIED fee, https://help.shopify.com/en/manual/promoting-marketing/collabs/merchants/payments |
| Search CPC "dog back seat extender" about $1.98, about 590 searches a month | Not re-checked | DataForSEO, run by the researcher today. |

Low-cost tactics hold up as described. None of them has sales evidence for a new store. The fair claim
is "cheap to set up", not "cheap customers".

## 5. The "$50 million" sale, the YouTube video, and the reel

| Claim | Verdict | What I found today |
|---|---|---|
| Reel Df0pApmqi9s by @masondoesecom, caption "This is insane." | Holds | Embed shows the caption "This is insane. #ecom #shopify #ecomconversionrate". New fact: the embed data shows video_view_count 302, 5 likes and 2 comments. The reel embed shows 167 followers; the profile embed shows 199 followers and 66 posts (cached values differ). VERIFIED, https://www.instagram.com/reel/Df0pApmqi9s/embed/captioned/ ; https://www.instagram.com/masondoesecom/embed/ |
| No paid-partnership label in the caption | Holds, but the flag proves little | The reel embed data has no is_paid_partnership field and no sponsor. The six newest posts in the profile embed carry is_paid_partnership false and empty sponsor_user. That flag only reflects Instagram's branded-content tool, so false does not prove the creator was unpaid. Paid status: cannot be checked. VERIFIED (flags), same links |
| No "Luca Maratti" channel or "$50 million (Full Playbook)" video exists | Holds as "not found" | WebSearch for "Luca Maratti" ecommerce: no result mentions the name. DataForSEO YouTube search "sold ecommerce brand $50 million playbook": 19 results, none from Luca Maratti or with that title. VERIFIED (searches today) |
| No independent support for the $49.6M or $50M sale, or the Julia Burt article | Holds | WebSearch for the 18-year-old, $49.6M and Julia Burt found no such report or byline. DataForSEO Google for "amboraspartner" $50M returned nothing relevant except a Reddit thread on Amboras. UNKNOWN whether any such sale happened. |

Verdict: the sale story has no independent support. The reel reached about 302 views and sits in a
pattern of near-identical posts tagged #amboras or #amboraspartner. Treat it as advertising. Whether
this account was paid cannot be checked.

## 6. LTV definition used with the 3 to 1 rule

| Claim | Verdict | What I found today |
|---|---|---|
| Skok: LTV:CAC above 3, sometimes 7 or 8; "only guidelines"; payback over 12 months is anemic | Holds | "The best SaaS businesses have a LTV to CAC ratio that is higher than 3, sometimes as high as 7 or 8." "These are only guidelines." "Many of the best SaaS businesses are able to recover their CAC in 5-7 months." Profitability is "anemic if the time to recover CAC extends beyond 12 months." The essay does not define LTV as revenue, gross margin or profit. No date shown (update note 05/2016, footer 2000 to 2021). VERIFIED, https://www.forentrepreneurs.com/saas-metrics-2/ |
| a16z: LTV is present value of future net profit; revenue or gross-margin LTV is a mistake; paid CAC matters more than blended | Holds | "Lifetime value is the present value of the future net profit from the customer over the duration of the relationship." "A common mistake is to estimate the LTV as a present value of revenue or even gross margin." VERIFIED, https://a16z.com/16-startup-metrics/ (Aug 21, 2015) |
| Shopify: margin-adjusted CLV = AOV x frequency x lifespan x gross margin; cohort tools need 24 months | Holds | Formula as quoted. The page calls it "gross profit before acquisition costs and other operating expenses". "Cohort projections need 24 months of store data." Dated 8 Oct 2026. VERIFIED, https://www.shopify.com/au/blog/customer-lifetime-value |

Verdict: the slide's formula (Shopify's) is a gross-margin LTV. a16z calls that a mistake for spend
decisions. Using it with Skok's 3 to 1 makes the test easier to pass than a net-profit LTV would. For
Barkfare, LTV must be net of shipping, fees, refunds and the cost of the repeat order, and the repeat
rate for durable pet travel gear is UNKNOWN.

## 7. AG1, IM8 and Grüns offers

| Claim | Verdict | What I found today |
|---|---|---|
| IM8 BF: Essentials Pro $59/mo (was $112), buy 2 months get 1 free, free $123 Welcome Kit for new subscribers | Holds, with one condition the notes left out | "$59/mo", "$112/mo" ("47% OFF"), "Buy 2 months, get 1 FREE". Kit: "Included with every 90-day plan during the sale", "available for new subscribers only". Contents listed: 5 sachets ($25), bottle ($45), mixer ($18), cap ($35). Banner: "Free Shipping + 90 Day Guarantee"; elsewhere "Up to 90-Day Money Back Guarantee". The kit needs a 90-day plan, not any subscription. VERIFIED, https://im8health.com/ |
| IM8 $1.44 gross profit per $1 of acquisition; General Catalyst funds up to 70% of marketing | Holds as company claims | Company statements say $1.44 is blended across mature cohorts; GC finances up to 70% of marketing per monthly cohort and is repaid first. A Nasdaq call summary gives 4.1x for a Q1 2025 cohort. A LinkedIn critic cites 0.72x after three months for a broader cohort. No independent audit found. ESTIMATED, https://finviz.com/news/368046/prenetics-im8-secures-1-billion-growth-financing-from-general-catalysts-customer-value-fund-cvf (search result; the short URL in the notes now 404s) |
| Grüns: $49.99 per 28 packs subscribed vs $66.65 one-time; 25% first-order discount tied to SMS; no gift | Holds | "Subscribe & Save 28 packs each 4 weeks" "$49.99 $66.65"; one-time "$66.65". "Save 25% + free shipping on your first order." Footnote: "Offer assumes customer has received and uses promotional SMS discount reserved for new customers only." No gift. "30-Day Money-Back Guarantee"; "Less than 2% of customers use our Money-Back Guarantee" (self-reported). New: a label reads "Get 55% Off + Free Shipping" although listed prices show about 25% off; banner "Order by November 22nd for 25% Off". VERIFIED, https://gruns.co/ |
| AG1: from $79/month, extra 25% off first subscription, Welcome Kit plus gifts | Cannot be checked | drinkag1.com returned HTTP 429 again today. Search snippets only. ESTIMATED |

Barkfare relevance: these are consumable subscriptions. Their LTV math does not carry over to a
durable $149 kit. The parts that do carry over are the offer mechanics. Note the "55% off" label
mismatch at Grüns. Before Barkfare shows any "% off" or "was" price, check the FTC pricing guides
(16 CFR 233, not read today) and 16 CFR 251 (read by the earlier researcher).

## Corrections for the plan

1. Insense is not $400 to $650 a month for us. Seeding is not on the Trial, and the Trial auto-renews into a $1,500 quarterly Brand plan. Treat Insense as a $1,500 minimum before creator pay, and drop it from a $500 to $1,000 test.
2. Remove the named Collabstr dog creator prices ($50, $75, $150) from scenario inputs, or label them stale. Coconut is in Canada. Nash's $50 is an Instagram listing on a profile claiming 1.5M followers. The snippets predate today's page.
3. Add TikTok Shop Refundable Samples to the creator plan. Creators buy first and are refunded only after a sales goal ("usually 1 to 3 orders") by Day 54. Who funds the refund is UNKNOWN.
4. Do not enter "partnership ads CPA -5% to -19%" as one range. The -19% is Meta's 2021-22 test with no confidence level. The -5% is vs licensed UGC, not vs brand ads. The -45% is cost per incremental purchase at 92% confidence. For the script, use 0% as the base case and treat the vendor figures as an upside scenario.
5. The Hubfluence per-view sales figures exclude every zero-sales video. Do not use $122 GMV per 1,000 views to forecast a new creator post.
6. The reel had about 302 views. It is advertising with no independent proof behind it.
7. If the 3 to 1 rule is used, compute LTV as net contribution per customer (a16z), not Shopify's gross-margin CLV. Add Skok's payback test (12 months at most).
8. IM8's free Welcome Kit needs a 90-day plan. It does not come with any subscription.

## Scenario inputs added or changed by this pass

| name | low | high | unit | label | source |
|---|---|---|---|---|---|
| insense_min_commitment_for_seeding | 1500 | 1500 | USD per quarter (Brand plan, billed quarterly) | VERIFIED | https://insense.pro/pricing |
| insense_trial_price | 650 | 650 | USD for 1 month, auto-upgrades unless cancelled 48h before end; no seeding | VERIFIED | https://insense.pro/pricing |
| billo_min_pack | 1000 | 1000 | USD, up to 10 videos | VERIFIED | https://billo.app/pricing/ |
| soona_ugc_video | 89 | 259 | USD per video, no annual commitment | VERIFIED | https://soona.co/ugc |
| tiktok_referral_fee_pet | 6 | 6 | percent, base includes customer-paid shipping | VERIFIED | knowledge_id=5988482086864682 |
| tiktok_refundable_sample_sales_goal | 1 | 3 | orders per creator (TikTok's "usually") | ESTIMATED | knowledge_id=5764641632306946 |
| partnership_ads_cpa_change_base_case | 0 | 0 | percent | ASSUMED | No independent evidence; vendor claims as upside only |
| partnership_ads_cpa_change_meta_2021 | -19 | -19 | percent, vs campaigns with under 20% partnership spend | ESTIMATED | ppc.land, Oct 11, 2026 |
| partnership_ads_cpa_change_vs_licensed_ugc | -5 | -5 | percent | ESTIMATED | netinfluencer.com, Aug 13, 2026 |
| reel_views_Df0pApmqi9s | 302 | 302 | views | VERIFIED | Instagram embed data, 2026-11-22 |
| pet_creator_paid_post_fee | null | null | USD per post | UNKNOWN | Live rates hidden; snippets stale and partly non-US |
