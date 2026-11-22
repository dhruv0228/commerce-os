# Reel check 3: LTV to CAC, the LTV formula, AG1 / IM8 / Grüns offers, and add-ons for a one-time dog car product

Research date: Sunday 2026-11-22. Researcher: Claude (subagent). Public pages only. Nobody was contacted. Nothing was bought or signed up for.

Labels: VERIFIED = read today on a primary page. ESTIMATED = third-party or self-reported (link and date given). ASSUMED = our placeholder. UNKNOWN = not found (what I tried is noted).

No arithmetic is done in this file. Ratios and shares that need computing are listed as script inputs at the end.

## Short answer

- The "LTV must be 3x CAC" rule comes from SaaS investing (David Skok). Skok himself calls it a guideline. It was built for software with high gross margins and long customer lives.
- Credible sources that are strict about it (a16z, Drew Fallon) say LTV in this ratio must be profit per customer (contribution or net profit), not revenue. Many ecommerce blogs use revenue or gross margin, which inflates the ratio.
- Real consumer brands often run well below 3 to 1. IM8 (one of the reel's three examples) says each $1 of acquisition spend has returned $1.44 of gross profit across mature cohorts, and it finances 70% of its marketing with an outside fund. Amp's Shopify dataset gives a median LTV to CAC of 2.4x.
- The slide formula (AOV x frequency x gross margin x lifespan) is standard. Shopify's own blog prints it word for word as "margin-adjusted CLV". It still counts gross margin, not contribution, and it needs a measured repeat rate that a new store does not have.
- AG1, IM8 and Grüns all sell an ingestible on subscription with a first-order hook (discount, free welcome kit, free shipping, guarantee). The mechanics that carry over to Barkfare are bundles, a gift with first order (only within the FTC "free" Guide), replacement parts, checkout add-ons and post-purchase upsells. A true subscription needs a consumable, and the dog car category has few.
- Pet travel brands with a $150 to $190 hero sell seat covers, door guards, beds, tethers, harnesses, bowls, replacement straps and inserts, extended warranties and shipping protection. No public repeat-rate data exists for these durable accessories (UNKNOWN). Proxies are below.

---

## 1. "LTV needs to be 3x your CAC"

### 1.1 Where the rule comes from

| Fact | Label | Source |
|---|---|---|
| Skok's essay says: "The best SaaS businesses have a LTV to CAC ratio that is higher than 3, sometimes as high as 7 or 8." | VERIFIED | David Skok, "SaaS Metrics 2.0", forEntrepreneurs.com, https://www.forentrepreneurs.com/saas-metrics-2/ (read 2026-11-22) |
| The same essay: "I should stress that these are only guidelines, there are always situations where it makes sense to break them." | VERIFIED | same page |
| The same essay on payback: profitability is "anemic if the time to recover CAC extends beyond 12 months", and "many of the best SaaS businesses are able to recover their CAC in 5-7 months." | VERIFIED | same page |
| The essay page shows no publication date (only a "©2000-2021" footer). Secondary sources date it to about 2012 or 2013. | UNKNOWN (exact date) | same page; secondary dating via search results, e.g. https://www.kellblog.com/the-ultimate-saas-metric-ltv-cac/ |
| The essay page does not define LTV as revenue or gross margin. It links out to a separate definitions document, which I did not read. | UNKNOWN (Skok's LTV basis, from this page) | same page |
| Drew Fallon frames the ratios: 1.0x is break-even on unit economics (the business burns cash once opex is included), 2.0x pays back CAC with enough to buy one more customer (linear growth), 3.0x funds two more customers (compounding). He calls 3.0x "the gold standard in venture capital." | ESTIMATED | Drew Fallon thread, posted Nov 14 (year not shown on the page), https://threadreaderapp.com/thread/1857078536827212253.html (read 2026-11-22) |

### 1.2 How credible sources define LTV for the ratio

| Source | LTV basis | Period | Label |
|---|---|---|---|
| a16z, "16 Startup Metrics" (Jeff Jordan, Anu Hariharan, Frank Chen, Preethi Kasireddy, Aug 21, 2015): "Lifetime value is the present value of the future net profit from the customer over the duration of the relationship." It warns that a revenue or gross-margin LTV "suggests a higher upper limit on what you can spend on customer acquisition." | Net profit (contribution), discounted | "the conservative way to measure LTV is to look at historical value to date"; prefers "12 month and 24 month LTV" | VERIFIED, https://a16z.com/16-startup-metrics/ |
| a16z, same article: "investors consider paid CAC to be more important than blended CAC". | Paid CAC, not blended | n/a | VERIFIED, same page |
| Drew Fallon: "LTV in the context of LTV:CAC is the LIFETIME CONTRIBUTION per customer, not revenue." Contribution = profit after all variable costs including logistics. He says a 3.0x on sales with about 50% contribution margin is closer to 2.0x. | Contribution | Lifetime, but timing matters: a 3.0x that takes 36 months to recover CAC can be worse in IRR terms than a 2.0x recovered on the first purchase | ESTIMATED, thread above |
| Shopify blog (Michael Keenan, 8 Oct 2026): gives revenue CLV and a "Margin-adjusted CLV" using gross margin, which it describes as gross profit before acquisition and other operating costs. | Revenue, or gross margin | Lifespan in years | VERIFIED, https://www.shopify.com/au/blog/customer-lifetime-value |
| Eightx (Matt Putra, May 29, 2026): uses contribution margin for CAC payback; does not state the LTV basis for its LTV to CAC table; calls its compiled benchmarks "directional, not audited." | Not stated for the ratio | "Lifetime" | ESTIMATED, https://eightx.co/blog/average-ecommerce-ltv-cac-ratio-by-vertical-2026 |
| This repo's script (`scripts/ltv_cac.py`) uses the strict basis: money left per customer after product, shipping, fees and refunds, before ads. | Contribution | First order, and 12 months where reorders were modelled | Repo file, /home/user/commerce-os/research/reel-check-2026-11-22/ltv_cac.md |

### 1.3 Typical LTV to CAC and payback for consumer brands

All of these are vendor or company figures. None is audited.

| Figure | Label | Source |
|---|---|---|
| Amp "2025 DTC Mega Report": dataset of $10.1B+ revenue, 107M orders, 77M customers across Shopify DTC brands. Median CAC $54. Median first-order profit $31. 52% of brands are "underwater after order one"; 37% "don't recover CAC on the first order." Payback 1.7 orders or 18 days. Median LTV:CAC 2.4x. 90-day repurchase for new customers 14.7%. 365-day repurchase for returning customers 51.4%. The page does not say which costs "first-order profit" includes. The page date reads Aug 26, 2026, but the image path suggests 2025. | ESTIMATED | Laura Daley, Amp, https://useamp.com/blog/2025-dtc-mega-report/ (read 2026-11-22) |
| Amp, same page, cost structure by industry (share of revenue): Pet Supplies COGS 13.1%, shipping 9.8%, marketing 34.6%, CM 44.3%. Home & Garden 14.0%, 12.0%, 22.6%, 47.5%. Jewelry & Accessories 10.7%, 7.4%, 31.9%, 44.3%. The COGS shares look low for physical goods; definitions are not given. Treat with caution. | ESTIMATED | same page |
| Eightx 2026 table: Pet LTV:CAC 3.5 to 4.5:1 (top quartile 5x+), blended CAC $68 to $90, CAC payback 8 to 14 months. Home & Lifestyle 2.0 to 3.0:1, CAC $68 to $112, payback 15 to 24 months. Consumer Electronics 1.8 to 2.5:1, CAC $100 to $377, payback 18 to 24+ months. Supplements/Wellness 3.0 to 4.0:1, payback 8 to 14 months. Cross-industry median 3.4:1, top quartile 5.6:1. No sample size disclosed. | ESTIMATED | Matt Putra, Eightx, May 29, 2026, https://eightx.co/blog/average-ecommerce-ltv-cac-ratio-by-vertical-2026 |
| IM8 (Prenetics): "Every $1 invested in customer acquisition has returned $1.44 in gross profit, blended across all mature cohorts." Dollar CAC, LTV and payback are not disclosed. | ESTIMATED (self-reported by the company) | Prenetics press release, July 14, 2026, copy at https://finviz.com/news/368046/prenetics-im8-secures-1-billion-growth-financing-from-general-catalysts-customer-value-fund-cvf |
| IM8's financing: General Catalyst's Customer Value Fund finances up to 70% of IM8's marketing spend by monthly customer cohort, repaid from a capped share of those cohorts' "Reference Income" (collections x assumed gross margin). No equity issued. No recourse beyond the funded cohorts. | ESTIMATED (self-reported) | same release |

What this means for the reel's claim: one of the reel's own example brands reports a gross-profit return per acquisition dollar far below 3, and funds most of its ad spend with cohort-based outside money. Amp's dataset median is also below 3. "3x" is a venture target, not a typical result.

### 1.4 Where the rule misleads a brand-new store

1. No measured repeat rate. Shopify's own CLV tools need history: cohort projections need 24 months of store data, and predicted spend tiers need more than 100 sales (VERIFIED, Shopify AU blog above). a16z says the conservative LTV is "historical value to date" (VERIFIED). A new store has zero history, so any lifetime figure is ASSUMED.
2. Cash comes in late. The ad cost is paid on day one. Reorder profit arrives months later, if at all. Skok's own second rule is payback under 12 months (VERIFIED). Fallon's IRR point (ESTIMATED) says a slow 3x can be worse than a fast 2x. CLAUDE.md section 4 already requires 3 weeks of ad spend plus product cost in reserve, and notes new stores can have payouts held.
3. Basis inflation. A revenue-based or gross-margin-based LTV looks bigger than a contribution-based one (a16z, Fallon). The slide formula in section 2 uses gross margin, so it still leaves out shipping, fees, refunds and fulfillment.
4. Blended versus paid CAC. Blended CAC includes free customers and looks cheaper (a16z, VERIFIED).
5. Benchmarks are from established brands. This repo already applies a 1.3x new-store penalty (CLAUDE.md section 4).
6. A durable hero has little or no reorder. The Barkfare extender is bought once. The repo script models no reorders for any Barkfare route, so the 12-month ratio equals the first-order ratio (repo file `ltv_cac.md`).
7. Funding model. Brands like IM8 can run a low ratio because a fund pays most of the ads up front (ESTIMATED, above). This repo has $1,800 total and no second tranche (CLAUDE.md section 0).

### 1.5 What the repo script already found (quoted, not recomputed)

From /home/user/commerce-os/research/reel-check-2026-11-22/ltv_cac.md:

- "The reel's rule asks for a ratio of 3. The house cushion rule equals a first-order ratio of 1.33."
- "Options that reach 3 to 1 in their best case: ext_fba." (Barkfare extender on Amazon FBA with bulk stock, read against an Amazon pay-per-click cost from `channels.py`.)
- "Options that pass the house rule on the first order: ext_fba, bulk_sea_bundle, bulk_sea, pod_149."
- The US-stock fast-lane extender and the 5-kit home-shipped trial do not pass the house rule on the first order in that table.
- Its footer: benchmarks are ESTIMATED (Triple Whale medians), reorder counts are ASSUMED, and "Nothing here is measured from our own store."

---

## 2. The slide formula: LTV = AOV x purchase frequency x gross margin x customer lifespan

### 2.1 Is it standard?

Yes, as a simple textbook version.

| Fact | Label | Source |
|---|---|---|
| Shopify blog: "CLV = Average order value x Purchase frequency x Average customer lifespan" | VERIFIED | https://www.shopify.com/au/blog/customer-lifetime-value (Michael Keenan, 8 Oct 2026) |
| Shopify blog: "Margin-adjusted CLV = Average order value x Purchase frequency x Average customer lifespan x Gross margin". This is the slide formula. | VERIFIED | same page |
| Shopify blog also gives a retention version: "Discounted future CLV = (m x r) / (1 + d − r)" with m = gross profit per retained customer per period, r = retention rate, d = discount rate; and a subscription version: (monthly recurring revenue per customer x gross margin) / monthly churn. | VERIFIED | same page |
| Shopify says frequency and lifespan must use the same time unit (annual frequency with lifespan in years). | VERIFIED | same page |
| Shopify gives no method for a store with no history. | VERIFIED (absence) | same page |

Gaps in the slide formula, by the stricter sources: it uses gross margin, not contribution (a16z, Fallon); it does not discount future profit (a16z, Shopify's discounted version); and "lifespan" and "frequency" are guesses until a store has cohorts.

### 2.2 Repeat purchase rate benchmarks

Definitions differ (window, subscription versus one-off), so numbers do not line up across sources.

| Category | Figure | Window | Label | Source |
|---|---|---|---|---|
| Pet | 31.5% | 12 months | ESTIMATED | StoreGrowers via Eightx, May 29, 2026, https://eightx.co/blog/average-ecommerce-repeat-purchase-rate-by-vertical-2026 |
| Pet | 28% (30-day), 55% (365-day) | 30 and 365 days | ESTIMATED | Bloy via Eightx, same page. Eightx says Bloy's panel skews to mid-market Shopify brands. |
| Home and furniture | 20% (12-mo); 18% (30-day); 34% (365-day) | as stated | ESTIMATED | same page |
| Electronics | 17% (12-mo); 8% (30-day); 25% (365-day) | as stated | ESTIMATED | same page |
| Apparel | 26% (12-mo); 22%; 40% | as stated | ESTIMATED | same page |
| Beauty | 28% (12-mo); 30%; 50% | as stated | ESTIMATED | same page |
| Supplements | 29.1% (12-mo); 30%; 48% | as stated | ESTIMATED | same page |
| Durable goods | not covered | n/a | UNKNOWN | same page says no row; home, electronics and luxury are nearest proxies |
| Subscription models, any vertical | 55%+; 365-day midpoint 70% | as stated | ESTIMATED | same page |
| Pet consumables (food, treats, litter, supplements) | 32% to 38% | "typically 12 months" | ESTIMATED, no data source cited | Finsi, Aug 14, 2026, https://finsi.ai/blog/pet-repeat-purchase-rate-2026/ |
| Pet toys and apparel (discretionary) | 18% to 26% | as above | ESTIMATED, no data source cited | same page |
| Pet accessories, durable gear, travel | not covered | n/a | UNKNOWN | same page has no figure |
| All DTC, new customers | 14.7% | 90 days | ESTIMATED | Amp, link in 1.3 |
| Cross-industry ecommerce | about 28% (range quoted 9.9% luxury to 65.2% grocery; traced to Metrilo) | not clear | ESTIMATED, secondary; I did not open the Metrilo source | search summary citing https://www.rivo.io/blog/repeat-purchase-rate-complete-guide and https://opensend.com/post/repeat-purchase-rate-ecommerce |

Pet supplies versus pet accessories and durable goods, from a primary filing (Chewy 10-K, fiscal year ended February 1, 2026; VERIFIED, read from https://s23.q4cdn.com/610444331/files/doc_financials/2025/q4/Chewy-2025-10-K-4.pdf):

| Chewy fiscal 2025 line | Value |
|---|---|
| Net sales | $12,601.5M |
| Consumables | $8,777.9M |
| Hardgoods | $1,436.3M (up 13.4% year on year) |
| Pet health and specialty products | $1,980.5M |
| Other | $406.8M |
| Active customers | 21.327M |
| Net sales per active customer | $591 |
| Autoship customer sales | $10,497.1M |
| Autoship customer sales as a percentage of net sales | 83.3% |

Chewy's definition matters: "Autoship customer sales" include all purchases by Autoship customers, inside and outside the subscription, in the period (VERIFIED, same 10-K). So 83.3% is not "share of sales that are subscription orders". Chewy does not publish a repeat rate for hardgoods alone (UNKNOWN). The split shows that at the largest US pet retailer, consumables are most of the money and hardgoods (where a car extender would sit) are a small part.

---

## 3. AG1, IM8 and Grüns

All three sell ingestible supplements, which this repo excludes (CLAUDE.md section 2). They are here only for their offer mechanics.

### 3.1 AG1 (drinkag1.com)

Access: WebFetch returned HTTP 429. A plain Playwright render returned "Vercel Security Checkpoint ... Failed to verify your browser" (HTTP 429). I did not try to get around the bot check. The facts below are Google result snippets pulled through DataForSEO today, so they are ESTIMATED and their crawl date is UNKNOWN.

| Fact | Label | Source |
|---|---|---|
| US snippet: "From $79/month with free shipping. Get an additional 25% off your first subscription. Valid for new subscribers to Essentials, Next Gen, Energy+, Pro, AGZ, ..." | ESTIMATED (Google snippet of drinkag1.com, 2026-11-22) | DataForSEO Google SERP, query "site:drinkag1.com subscription price welcome kit" |
| US snippet: "We offer exclusive member pricing to subscribers. Premium Welcome Kit plus free gifts with first subscription order." Another US snippet shows "$79 $99". | ESTIMATED | same |
| Snippet terms: "AG1 Welcome Kit Offer valid for new AG1 subscribers only." "Welcome Kit and gifts are one-time only. Subscription renews automatically unless cancelled beforehand." | ESTIMATED | same (EU and US snippets) |
| What is in today's US Welcome Kit; exact cancel steps; guarantee terms | UNKNOWN | page blocked |
| Funding: $115M raised at a $1.2B valuation, led by Alpha Wave Global (2022). | ESTIMATED | Front Office Sports, https://frontofficesports.com/article/athletic-greens-raises-115m-valued-at-over-1b/ ; Crunchbase News, https://news.crunchbase.com/news/nutrition-startup-athletic-greens-ag1-vc-funding-unicorn (via search summary; not opened) |
| Fortune (Jan 2025) reported AG1 was projected to reach $600M revenue that fiscal year. A projection, not a reported result. | ESTIMATED | https://fortune.com/2025/01/21/athletic-greens-launching-new-products-channels-2025/ (via search summary; not opened) |
| AG1 says it is profitable but declined to release 2025 results to Fast Company. | ESTIMATED | https://www.fastcompany.com/91538779/ag1s-green-with-envy-over-the-gummy-ification-of-wellness (via search summary; not opened) |
| Reuters reportedly said AG1 was exploring a sale at a $2B+ valuation (month April; year not confirmed by me). | ESTIMATED / partly UNKNOWN | via search summary citing https://finimize.com/content/ag1-weighs-a-deal-as-supplement-ma-heats-up |

### 3.2 IM8 (im8health.com), co-founded by David Beckham, owned by Prenetics (NASDAQ: PRE)

| Fact | Label | Source |
|---|---|---|
| Black Friday offer: Essentials Pro "$59/mo", "Previously $112", "Save 47%". The Beckham Stack "$139/mo", regular "$261/mo". "Buy 2 months, get 1 FREE + free Welcome Kit." | VERIFIED | https://im8health.com/ (read 2026-11-22) |
| "Your Free $123 Welcome Kit" on every 90-day plan during the sale: 5 sachets ($25 value), Luxe Edition bottle ($45), mixer ($18), Players Cap ($35). "Free Welcome Kit available for new subscribers only." | VERIFIED | same page |
| No one-time purchase price shown; only monthly subscription prices. Free shipping. Referral credits applied in cart (amount not stated). | VERIFIED | same page |
| Homepage says "Cancel anytime", "Up to 90-Day Money Back Guarantee", "Three full months to experience the difference on the 90-day plan. If you don't feel it, you get a complete refund." | VERIFIED | same page |
| Terms of Service: subscriptions "will automatically renew unless canceled"; "To avoid a recurring charge you must cancel your subscription by the last day of your billing period"; the page describes cancelling by contacting care@im8health.com and a portal only for billing details. The 30-day satisfaction guarantee there applies to first-time purchases only, requires returning the product, refund within 6 weeks of receipt, shipping not refunded. | VERIFIED | https://im8health.com/pages/terms-of-service (read 2026-11-22; no date shown) |
| The homepage guarantee (up to 90 days) and the Terms page (30 days, first purchase) differ. The Terms point to a separate Subscription Policy that I did not read, which may cover the 90-day plan and any online cancel method. | VERIFIED (that both pages say this); reconciliation UNKNOWN | both pages above |
| Size: FY2025 release headline "IM8 Achieves $120M ARR in 12 Months". | ESTIMATED (self-reported) | https://finviz.com/news/314237/prenetics-reports-record-q4-and-fy-2025-results-im8-achieves-120m-arr-in-12-months-revenue-surges-480-yoy |
| Q1 2026 (reported May 14, 2026): about 82,000 active subscribers; 93% of IM8 revenue from subscriptions; May monthly revenue about $16.7M "implying" about $200M annualized. Prenetics computes ARR as last month's revenue x 12. | ESTIMATED (self-reported; via search summary) | https://finviz.com/news/360849/prenetics-announces-record-q1-2026-results-with-im8-revenue-reaching-a-record-167-million-in-may-implying-200-million-in-annualized-recurring-revenue |
| July 14, 2026: June 2026 preliminary unaudited revenue about $17M; FY2026 IM8 revenue guidance raised to $210M to $220M; expects $300M annualized run rate by end of 2026 and $400M+ in 2027; $1B General Catalyst CVF facility (terms in 1.3). | ESTIMATED (self-reported) | release linked in 1.3 |
| A later Q3 2026 release (seen only in the page sidebar) reaffirmed FY2026 total revenue guidance of $220M to $230M. | ESTIMATED (not opened) | same page sidebar |

### 3.3 Grüns (gruns.co)

| Fact | Label | Source |
|---|---|---|
| Headline: "Save 25% + free shipping on your first order". "Order by November 22nd for 25% Off With Free Shipping!" | VERIFIED | https://gruns.co/ (read 2026-11-22) |
| Subscribe and Save, 28 packs every 4 weeks: Low Sugar $49.99 (struck from $66.65); Sugar-Free $54.99 (struck from $73.32). One-time: Low Sugar $66.65, Sugar-Free $73.32, marked "No Free Shipping" and "No First Order Discount". | VERIFIED | same page |
| The first-order 25% depends on an SMS sign-up: "Offer assumes customer has received and uses promotional SMS discount reserved for new customers only." | VERIFIED | same page |
| A badge reads "Most Popular: Get 55% Off + Free Shipping". How 55% is calculated is not shown next to the prices I read. | VERIFIED (badge text); basis UNKNOWN | same page |
| No free gift or welcome kit listed on the page today. | VERIFIED (absence on page) | same page |
| "30-Day Money-Back Guarantee"; "Less than 2% of customers use our Money-Back Guarantee." | VERIFIED (claim on page); the 2% figure is self-reported, ESTIMATED | same page |
| Subscription policy (last updated 10/14/26): renews automatically at the chosen frequency; cancel online in the member homepage (My Subscriptions > Manage > Cancel) or by email; deadline "11:59 p.m. ET on the day before your renewal date"; no minimum commitment mentioned. | VERIFIED | https://gruns.co/policies/subscription-policy |
| Unilever announced it is acquiring Grüns (April 9, 2026), amount undisclosed. Grüns said in Oct 2025 it had passed a "$300 million annualized run rate". Founder raised about $50M over just under three years. The Information reported a May 2025 raise at a $500M valuation. Retail: Amazon, Sprouts, Target, Walmart, Sam's Club, Costco, Ulta and grocers. | ESTIMATED | Anna Hensel, Modern Retail, https://www.modernretail.co/operations/a-timeline-of-what-led-up-to-gruns-being-acquired-by-unilever/ |
| A $1.2B price is reported by aggregators and in a Beauty Independent headline. Not confirmed by the companies. | ESTIMATED | https://multiples.vc/private-comps/gruns ; https://www.beautyindependent.com/?p=187631 (via search summary; not opened) |

### 3.4 Which mechanics carry over to a non-ingestible product

| Mechanic seen | Used by | Carries over to Barkfare? | Notes |
|---|---|---|---|
| Subscription with a lower subscriber price | AG1, IM8, Grüns | Only with a real consumable or wear part. The dog car category has few (see section 4). | ROSCA and state auto-renewal laws apply to any online subscription. |
| Prepaid multi-month plan (90 days) | IM8, AG1 (90-day EU price seen) | Not a fit for a one-time durable. | |
| First-order discount | AG1, Grüns (SMS-gated) | Yes. | A first-order discount lowers the first-order contribution the house rule tests. |
| Free welcome kit or gift with first order | AG1, IM8 | Yes, as a gift with purchase. | "Free" claims fall under 16 CFR 251 (below). CLAUDE.md already says door guards may be called "free" only after they have really sold separately at that price. |
| "Buy 2, get 1 free" | IM8 | Possible on add-ons. | Same "free" rules. |
| Bundles and kits | All three sell stacks or bundles | Yes. This is already the Barkfare model. | |
| Money-back guarantee | All three | Yes. | Must be honored as stated; terms in one place. |
| Referral credits | IM8 | Yes. | |
| Free shipping tied to subscription | AG1, IM8, Grüns | Free shipping, yes; tied to subscription, no. | |
| Refills / replacement parts | Not seen on these pages | Yes: replacement straps, inserts, covers, beds (section 4). | |

### 3.5 FTC and state rules that apply

| Rule | Status today | Label | Source |
|---|---|---|---|
| FTC "Click-to-Cancel" amendments to the Negative Option Rule | Vacated by the Eighth Circuit in July 2025 on procedural grounds. Not in effect. | ESTIMATED (law firm summaries) | Jones Day, May 2026, https://www.jonesday.com/en/insights/2026/05/ftc-revives-clicktocancel-rule-new-risks-for-subscription-businesses ; Gibson Dunn, https://gibsondunn.com/ftc-restarts-negative-option-rulemaking-after-eighth-circuit-vacatur-enforcement-under-rosca-continues/ |
| New FTC rulemaking | Advance Notice of Proposed Rulemaking published March 2026 (Federal Register, March 13, 2026); comments were due April 13, 2026; about 100 comments. The FTC asked whether to amend the 1973 rule, revive parts of the vacated rule, or take other approaches. | ESTIMATED | Jones Day above; Federal Register document https://www.govinfo.gov/content/pkg/FR-2026-03-13/html/2026-04952.htm (not opened) |
| Any proposed or final rule after the March 2026 ANPRM | Not found in two searches today. | UNKNOWN | searches on 2026-11-22; the FTC docket would confirm |
| ROSCA (online subscriptions, in force) | Disclose all material terms clearly before taking billing details; get express informed consent before charging; give "simple mechanisms" to stop recurring charges. | ESTIMATED (law firm summary) | Jones Day above |
| Enforcement | Amazon Prime settlement $2.5B (Section 5 and ROSCA); Care.com $8.5M (2024); NextMed complaint used the vacated rule's three core requirements as Section 5 violations. | ESTIMATED | Jones Day above |
| State auto-renewal laws | About 30 states have them; California's requires an annual reminder with renewal, price and cancel methods. Whether each state requires online cancellation for online sign-ups was not checked today. | ESTIMATED; online-cancel detail UNKNOWN | Jones Day above |
| FTC Guide on "free" claims, 16 CFR 251.1 | Regular price = lowest price with substantial sales in a 30-day period. Conditions "should be set forth clearly and conspicuously at the outset of the offer" (an asterisk footnote does not count). No "free" offer for a new product unless the seller in good faith plans to end it after a limited time and then sell the item at the advertised price. A "free" offer should not run in a trade area more than 6 months in any 12; at least 30 days between offers; no more than three such offers in an area in 12 months. | VERIFIED | https://www.law.cornell.edu/cfr/text/16/251.1 (read 2026-11-22; eCFR redirected to an unblock page) |
| FTC Mail Order Rule | Already covered in CLAUDE.md section 9. | n/a | CLAUDE.md |

---

## 4. Add-ons and repeat items for a one-time $149 dog car product

### 4.1 What pet travel brands sell beside the hero (public Shopify product feeds, read today)

Prices are the variant prices in each store's public `/products.json` feed on 2026-11-22 (VERIFIED). Some may be sale prices. The feed lists published products only; it says nothing about sales volume.

Ruff Liners (https://ruffliners.com/products.json), 5 products:
- Hard Bottom Backseat Extenders with Door Protection: $169.99 to $189.99 (hero)
- Travel Dog Bed for Car: $69.99 to $79.99
- Soft Backseat Dog Hammock with Door Protection: $109.99
- Replacement Window Inserts (6 pieces): $15.00 (replacement part)
- XL Floor Cover for crew cab trucks: $159.99 to $199.99

RuffRover (https://ruffrover.com/products.json), 28 products, selected:
- RuffRover 2.0 Hard Bottom Back Seat Extender + (FREE Dog Bed): $166.00 and $169.95 listings; protector without bed $141.25 and $159.95
- Luxe Dog Bed for the RuffRover 2.0: $89.95 (the "free" bed is also sold on its own)
- Luxe Square Dog Bed: $39.95
- DoorGuard (2-pack): $39.95
- Portable Dog Stairs for RuffRover 2.0: $149.99
- Pup Passenger Seat Cover: $49.95
- Window Head Rest, "Buy 1 Get 1 FREE": $39.95
- Ultimate Accessories Value Pack: $79.95
- Leash and harness combo $29.95; safety harness bundle $29.95; bungee seat-belt leash $24.99
- Dog coat $29.95 to $59.98; goggles $34.99; booties $29.99
- Checkout add-ons: 5-Year Extended Warranty $14.99; Shipping Protection $4.99 (several listings); "VIP Skip The Line Shipping" $9.99

4Knines (https://4knines.com/products.json), 47 products, selected:
- Hard Bottom Extender: $169.99 Regular, $189.99 XL (hero)
- Rear seat covers $79.99 to $129.99; front bucket seat cover $44.99; cargo liners $79.99 to $149.99; crew cab truck covers $139.99 to $169.99
- Car door covers $44.99 to $59.99
- Replacement Straps, set of 2: $14.99 (replacement part)
- Dog Seat Belt $13.99; Headrest Seat Belt $13.99; Harness $22.39 to $35.99
- Stainless steel bowl $19.99; dog blankets $59.00; crate mat or travel bed $26.99 to $28.99; plush car seat bed $47.99
- Seat back organizer $35.99; crate cover $35.99 to $45.99; deterrent barrier $34.99
- Consumable: dog poop bags (recycled) $14.99
- Gift card $30 to $200

Sleepypod (https://sleepypod.com/products.json), 32 products, selected (carriers and crash-tested harnesses, so a different hero):
- Carriers $139.99 to $224.99; Clickit harnesses $103.49 to $142.49
- Replacement parts: Foam Insert $19.99 to $23.99; Handilock $4.99; Privacy Panel $4.99; Safety Tether $4.99; replacement bedding $29.99 to $35.99
- Yummy Travel Bowls $35.99 to $47.99; Go Bag $99.99; leashes and collars $15.59 to $47.99

Kurgo: kurgo.com has no public `/products.json` (HTTP 404) and `/collections/car-travel` returned 404. Retail listings seen in search: Kurgo "Enhanced Strength Replacement Tether" about $13 to $16 at PetSmart; "Direct to Latch" tether $19.99 at Tractor Supply; Wander Hammock and Co-Pilot bucket seat covers at Chewy and PetSmart (ESTIMATED, search snippets, https://www.petsmart.com/dog/collars-harnesses-and-leashes/harnesses/kurgo-seat-belt-dog-tether-37212.html , https://www.tractorsupply.com/tsc/product/kurgo-direct-to-latch-dog-seat-belt-2001151).

Pattern: the brands sell protection for the rest of the car (front seat, cargo, doors), comfort (beds, blankets), safety (tethers, harnesses), and a few low-price replacement parts ($5 to $15). Real consumables are rare (poop bags at 4Knines). Checkout add-ons (warranty, shipping protection, faster shipping) are common at RuffRover.

### 4.2 Repeat-rate data for these items

| Question | Answer | Label | Source |
|---|---|---|---|
| Repeat rate for dog car seat covers, extenders, tethers or travel gear | Not found. No public benchmark for pet accessories, durable gear or travel. | UNKNOWN | Tried: Eightx and Finsi benchmark pages (no row), APPA public pages (product-level data is in the paid report), one targeted search |
| Nearest proxies | Pet toys and apparel 18% to 26% (Finsi, no data source cited); home 20% and electronics 17% at 12 months (Eightx/StoreGrowers); pet overall 31.5% at 12 months (mostly consumables) | ESTIMATED | links in 2.2 |
| Weight of hardgoods in US pet ecommerce | Chewy hardgoods $1,436.3M of $12,601.5M net sales in fiscal 2025 | VERIFIED | Chewy 10-K, link in 2.2 |
| Car use as a wear driver | APPA 2025: 53% of dog owners take their dogs in the car for errands or routines at least weekly; 22% own a harness. No replacement frequency published publicly. | ESTIMATED (via search summary) | https://americanpetproducts.org/news/the-american-pet-products-association-appa-releases-2025-dog-cat-report |
| Add-on take rate right after checkout (one-click post-purchase offer) | About 4.7% average across 40,000+ Shopify merchants (ReConvert, 2023, quoted secondhand); other guides say 3% to 8%; app vendors claim 8% to 25%. Most figures are per offer view, not per order. | ESTIMATED | search summary citing https://www.launchtip.com/upsell-statistics , https://zipify.com/blog-post-purchase-upsells-shopify-2026/ , https://www.digismoothie.com/blog/upsell-benchmarks |

Reading: for a one-time $149 hero, "LTV" grows mainly from the add-on attached at the first checkout or right after it, not from reorders months later. That money also arrives on day one, which avoids the cash problem in 1.4. Any reorder figure for Barkfare stays ASSUMED until the store has its own cohorts.

---

## 5. Inputs for a script (no math done here)

| Input | Value | Label | Source |
|---|---|---|---|
| Reel / venture LTV to CAC target | 3.0 | ESTIMATED | Skok (VERIFIED wording "higher than 3") |
| SaaS CAC payback guideline | 12 months max; best 5 to 7 months | VERIFIED | Skok |
| IM8 gross profit per $1 of acquisition spend, mature cohorts | 1.44 | ESTIMATED (self-reported) | Prenetics, July 14, 2026 |
| IM8 share of marketing financed by CVF | up to 70% | ESTIMATED (self-reported) | same |
| Amp median LTV:CAC | 2.4 | ESTIMATED | Amp |
| Amp median CAC | $54 | ESTIMATED | Amp |
| Amp median first-order profit | $31 | ESTIMATED | Amp |
| Amp share of brands underwater after order one | 52% | ESTIMATED | Amp |
| Amp 90-day repurchase, new customers | 14.7% | ESTIMATED | Amp |
| Eightx pet LTV:CAC range | 3.5 to 4.5 | ESTIMATED | Eightx |
| Eightx pet CAC payback | 8 to 14 months | ESTIMATED | Eightx |
| Pet 12-month repeat rate | 31.5% | ESTIMATED | StoreGrowers via Eightx |
| Home 12-month repeat rate | 20% | ESTIMATED | same |
| Electronics 12-month repeat rate | 17% | ESTIMATED | same |
| Pet toys/apparel repeat rate | 18% to 26% | ESTIMATED | Finsi |
| Durable pet travel gear repeat rate | none | UNKNOWN | |
| Post-purchase upsell take rate | 4.7% (range 3% to 8%) | ESTIMATED | ReConvert via secondary pages |
| Chewy fiscal 2025 net sales | $12,601.5M | VERIFIED | Chewy 10-K |
| Chewy fiscal 2025 hardgoods | $1,436.3M | VERIFIED | Chewy 10-K |
| Chewy fiscal 2025 consumables | $8,777.9M | VERIFIED | Chewy 10-K |
| Add-on prices seen (door guards, beds, replacement parts, warranty) | see 4.1 | VERIFIED | brand product feeds |

## 6. What I could not get

- AG1's live US offer page (bot checkpoint, HTTP 429). Used Google snippets instead.
- Skok's own LTV definition (in a linked document I did not open) and the essay's exact date.
- Repeat rates for any pet accessory or durable travel product.
- Whether the FTC has issued a proposed negative option rule after March 2026.
- IM8's separate Subscription Policy page (to reconcile the 30-day and 90-day guarantees and the cancel method).
- Kurgo's own catalog (no public feed; collection URL 404).
- A second DataForSEO query failed with "You can set only one task at a time" and was not retried.
