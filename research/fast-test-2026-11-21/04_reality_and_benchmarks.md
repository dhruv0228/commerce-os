# 04. Reality check and benchmarks: how often this model works and what it costs to find out

Research date: 2026-11-21. Research only. Nothing was bought, signed up for, logged into or sent. No margins, CAC, ROAS or profit are computed here; section 9 lists the inputs for `scripts/economics.py`.

Companion files (not repeated here): `01_video_decode.md` (the video, the funnel, who gets paid) and `02_youtube_sweep.md` (what 15 creators did, their self-reported test results).

## How to read the labels

- **VERIFIED** = I read it today on the publisher's own page or document. It confirms that the source says it. It does not confirm the number will hold for Dhruv's store. When a VERIFIED benchmark from an analytics vendor goes into `data/`, it must be stored as ESTIMATED (third-party benchmark), as CLAUDE.md section 5 requires.
- **ESTIMATED** = third-party or secondary (press coverage, blog, search summary), with URL and date.
- **UNKNOWN** = not found.
- "Raw" means I read the page text directly (headless browser or `pdftotext`). "Fetch" means the WebFetch tool quoted the page for me.
- "Weak" marks a statistic with no traceable dataset or method.

Bias flags used below: **[vendor]** sells a tool to the people the statistic describes. **[affiliate]** is paid when the reader signs up. **[survivor]** the sample only contains businesses that already survived or sold.

---

## 0. Short answer

1. **Nobody publishes a dropshipping success rate.** Shopify says so itself: "There's no dropshipping-specific failure rate" (VERIFIED, fetch, Shopify blog updated Aug 15, 2026). The "90% fail" and "10 to 20% succeed" numbers trace to vendor blogs and one 2019 UK agency survey of failed owners. Weak.
2. **The best hard data points all say the same thing: a small share wins, and it is concentrated.** Meta ads: about 4% of creatives from small advertisers become winners (VERIFIED, Motion, 578,750 creatives). TikTok Shop: the top 1% of sellers make about 60% of sales, the bottom half about 0.1% (VERIFIED, Marketplace Pulse, June 2026). Shopify merchants with at least $1,000 a year in sales: 48.5% say they run at a profit and median platform revenue is about $14,000 a year (VERIFIED, RAND working paper, 2024). Stores that never reach $1,000 are not in that sample.
3. **Regulators have looked inside this exact pitch.** The FTC's complaint against a dropshipping coaching seller says its stores "often lose money" once marketing and fixed costs are counted, including "the stores Defendants tout as success stories" (VERIFIED, raw, complaint paragraph 41). Four of the five FTC ecommerce "AI" cases since 2023 put buyer losses at $14 million to $25 million each (the fifth gives no total), and each says the promised earnings did not arrive for most buyers.
4. **Benchmark cost per purchase on Meta is about $35 to $52 in the categories Dhruv can sell** (Pets $39.23, Home and Garden $48.61, Electronics $51.06; VERIFIED, Triple Whale, 41,000+ brands, Nov 2025 to Oct 2026). Those are established brands. Meta says cost per purchase is "usually" higher during the learning phase, and leaving it takes "about 50 results" in a week per ad set (VERIFIED, raw). A test under $1,000 is very unlikely to leave the learning phase (script to confirm).
5. **He would be launching into the most expensive ad week of the year.** Black Friday is Nov 27, 2026. Meta CPMs ran 16 to 41% above September in Black Friday week 2025, depending on sector (VERIFIED, raw, Supermetrics, 5,000+ retail advertisers). Costs per click fell 11 to 17% below September in Christmas week.
6. **Static image ads are a fair first format, and AI can make them.** Image ads had a slightly lower median cost per purchase than video across 74 DTC brands (VERIFIED, fetch, MHI, small sample, agency source). Text-forward statics and UGC had the highest hit rates in Motion's data. No rigorous public test shows AI-generated statics alone producing profitable cold-traffic sales for a new store. UNKNOWN.
7. **Copying is the fastest way to lose the store.** Angles, formats and facts are free to borrow. Photos, videos, ad copy, brand names, logos, a distinctive look, and patented designs are not. Shopify removes reported content and can close a store for one willful instance (VERIFIED, fetch). Meta bans ads that sell "knockoffs, or replicas" (VERIFIED, fetch).
8. **"$100,000 before the end of the year" is not plausible** for a beginner starting Nov 21 with under $1,000. Section 6 lists ten requirements; at least five fail on evidence.
9. **Realistic week 1 for a first test under $1,000:** first sales within a day or two of ads going live, total week revenue in the low hundreds to about $1,200, and a result between losing most of the ad money and a small profit. No transparent test in `02_youtube_sweep.md` shows every order profitable after ads in week 1. The $2,000 target is a stretch, not a plan.
10. **Fastest path to a first sale is paid-traffic dropshipping. Lowest cash at risk is affiliate or print on demand. Best fit for Dhruv's rules (speed, low refunds, no face on camera, profit per order) is one validated US-stock product with a small fixed Meta test and the repo's kill rules.** That is my reading of the evidence in section 7, not a sourced ranking. No independent head-to-head ranking of these models exists. UNKNOWN.

---

## 1. Base rates

### 1.1 What primary sources say

| Source | What it measures | Figure | Label | Limits |
|---|---|---|---|---|
| Shopify, entrepreneurship report page, published Oct 2026 (https://www.shopify.com/entrepreneur) | Time to first sale | "among newly created Shopify stores that ultimately achieved a sale, half received their first order within approximately three weeks of launching" | VERIFIED, fetch | **[survivor]** Only stores that eventually sold. The share that never sell is not published. |
| Same | First sales per year | "1.2 million stores made their first sale on Shopify in 2025" | VERIFIED, fetch | No denominator. "We do not release absolute merchant count." |
| Same | Speed trend | "43% more stores make their first sale within a single day of signing up, compared to 2022" | VERIFIED, fetch | Relative change only. |
| Same | Store shape | "41% of stores launch with a single product" | VERIFIED, fetch | Platform data, no period given. |
| Shopify blog, "Is dropshipping worth it", updated Aug 15, 2026 (https://www.shopify.com/blog/is-dropshipping-worth-it) | Dropshipping failure rate | "There's no dropshipping-specific failure rate." | VERIFIED, fetch | Shopify earns from every store opened. |
| Same | Gross margin range | "Dropshipping margins tend to sit around 20% to 50%" | VERIFIED, fetch | Before ads. Cites Shopify's own Collective help page. |
| Same | Biggest cost | "Rather than product, marketing tends to be the biggest expense for dropshippers." | VERIFIED, fetch | No figure. |
| Same | Effort | "it takes at least a year of full-time work to recreate the average full-time income through dropshipping" | VERIFIED, fetch | Uncited. |
| RAND working paper, Abraham, Hassler, Master, Phillips, "The Changing Nature of Entrepreneurship in the U.S.: Evidence from Shopify", July 12, 2024 (https://conference.nber.org/conf_papers/f203218/f203218.pdf) | Revenue of active US Shopify businesses | 337,462 businesses with over $1,000 annualized revenue in 2022: median 2022 revenue $13,880, mean $320,304 | VERIFIED, raw | **[survivor]** Excludes every store under $1,000 a year. All merchants, not dropshippers. Data from Shopify, funded by the Kauffman Foundation. |
| Same | Growth and exit, year 1 to year 2 | Of 160,634 businesses opened 2017 to 2022 with more than $1,000 annualized revenue in year 1: 50% grew, 46% stayed the same or fell, 4% stopped using the platform | VERIFIED, raw | Same floor. |
| Same, RAND and Shopify survey, June 2023, 4,000 respondents | Share operating at a profit | 48.5% | VERIFIED, raw | Self-reported, businesses opened 2017 or later with about $1,000 or more in revenue. |
| Same | Median revenue of surveyed businesses | $33,000 total, $10,746 through Shopify | VERIFIED, raw | |
| BLS, Business Employment Dynamics, Jan 12, 2024 (https://www.bls.gov/opub/ted/2024/34-7-percent-of-business-establishments-born-in-2013-were-still-operating-in-2023.htm) | Survival of all US private-sector establishments born March 2013 | 79.6% after 1 year, 50.6% after 5, 34.7% after 10 | VERIFIED, fetch | All industries, employer establishments. Not online stores. |
| Store Leads, updated Nov 13, 2026 (https://storeleads.app/reports/shopify) | Live Shopify stores | 3,298,869 live. Quarterly counts: 2,859,828 (2025 Q4), 2,804,211 (2026 Q1), 2,867,778 (Q2), 3,108,808 (Q3) | VERIFIED, fetch | Third-party crawl. Net counts only, no gross openings or closures. The count fell after the 2025 holiday quarter. |
| Jungle Scout seller survey, fielded Dec 1, 2023 to Jan 3, 2024, 1,064 sellers with live listings (https://www.junglescout.com/resources/articles/how-much-do-amazon-sellers-make/) | Amazon sellers | 13% not yet profitable. 58% profitable within the first year, 22% within 3 months. 31% sell under $500 a month. 25% started with under $1,000, 64% under $5,000. 48% launched within 3 months. | VERIFIED, fetch | **[vendor] [survivor]** Sellers with live listings who answer a tool vendor's survey. The 2025 edition's page did not show these questions. |
| Marketplace Pulse, June 11, 2026 (https://www.marketplacepulse.com/articles/on-tiktok-shop-1-of-sellers-drive-60-of-gmv) | TikTok Shop US seller concentration | Top 1% of nearly 100,000 tracked sellers: about 60% of GMV. Top 0.1% (fewer than 90 sellers): more than a quarter. Bottom half: roughly 0.1%. Amazon for comparison: about 1.6% of sellers make half. | VERIFIED, fetch | Independent research firm. Lifetime GMV estimated from units and price. Calls its own data "early". |
| Motion (now Runneth), Creative Benchmarks 2026 (https://runneth.com/library/research/creative-benchmarks-2026) | Share of Meta ad creatives that become winners | About 5% overall. Micro advertisers (under $10,000 a month): 3.7 to 4.0%. 50.2% of Micro creatives are turned off before day 28. | VERIFIED, raw | **[vendor]** $1.29 billion of spend, 578,750 creatives, 6,015 accounts, Sep 1, 2025 to Jan 1, 2026. "Winner" means at least 10 times the account's median spend and at least $500. It is a spend measure, not a profit measure. |

### 1.2 The popular statistics and where they come from

| Claim | Origin found | Verdict |
|---|---|---|
| "90% of ecommerce startups fail within 120 days" | Marketing Signals, a UK agency, July 2019, a survey of 1,253 owners of **failed** UK start-ups (ESTIMATED; https://internetretailing.net/themes/90-of-e-commerce-start-ups-end-in-failure-within-the-first-120-days-19930 and others, read as search summary today). Original release and method not found. | Weak. The sample is failed owners, so it cannot give a failure rate. |
| "10 to 20% of dropshipping stores are profitable in year 1", "90% fail" | Vendor blogs citing each other. Dropship.io audited the trail on Sep 9, 2026: "We found no verified universal dropshipping success rate in the source trail we audited." (VERIFIED, fetch, https://www.dropship.io/blog/dropshipping-success-rate) **[vendor]** | Weak. No dataset, no denominator, no period. |
| "1 to 5% build a consistently profitable business" | TrueProfit and similar blogs (ESTIMATED, search summary today) **[vendor]** | Weak. |
| "34% of Shopify stores survive their first year", "average store life 143 days" | A Globe and Mail data study, as retold in a blog post of Oct 25, 2022 (ESTIMATED; https://www.sixpixels.com/articles/archives/shopify-a-tale-of-two-cities/). Sample size not stated. Original article not found. | Plausible but unverified and old. |
| "Only 1 in 10 new Shopify stores is active after 90 days", "28% annual merchant churn" | Aggregator blogs (ESTIMATED, search summary today) | Weak. |
| "24% of print-on-demand stores survive three years" | Attributed to Mordor Intelligence by vendor blogs (ESTIMATED, search summary today) | Weak. |

### 1.3 Direct answers to the task questions

- **Share of dropshipping stores that succeed or fail:** UNKNOWN. No primary data exists in public.
- **Time to first sale:** about three weeks at the median for Shopify stores that eventually sell (VERIFIED). With paid ads running, the creator tests in `02_youtube_sweep.md` got a first sale in 20 minutes to about 24 hours (ESTIMATED, self-reported).
- **Share of stores that become profitable:** UNKNOWN for new stores with no revenue floor. For US Shopify merchants above about $1,000 a year, 48.5% (VERIFIED, RAND, 2023 survey).
- **What the hard numbers have in common:** results are concentrated in a small top group on every platform measured (ads, TikTok Shop, Amazon, Shopify revenue). A beginner should plan on the median, not the mean: RAND's median was $13,880 a year against a mean of $320,304.

---

## 2. Testing economics

### 2.1 Meta benchmarks by category (established brands)

Source: Triple Whale, "Facebook Ad benchmarks by industry", page dated Nov 18, 2026, "over 41,000 brands for the period of November 1, 2025 to October 31, 2026" (VERIFIED, raw, https://www.triplewhale.com/blog/facebook-ads-benchmarks). Medians. **[vendor]** The sample is brands that pay for an analytics tool, so it leans toward stores that already have traction. Figures are platform-attributed.

| Category | Cost per purchase | CPM | CTR | Conversion rate | ROAS | AOV |
|---|---|---|---|---|---|---|
| All industries | $39.73 | $15.72 | 2.48% | 1.51% | 1.88 | $74.62 |
| Pets and Animals | $39.23 | $16.89 | 2.44% | 1.60% | 1.58 | $60.37 |
| Home and Garden | $48.61 | $15.06 | 2.46% | 1.22% | 2.29 | $114.14 |
| Electronics | $51.06 | $15.62 | 2.48% | 1.16% | 1.98 | $110.65 |
| Sports and Outdoors | $45.30 | $12.44 | 2.06% | 1.27% | 2.38 | $116.00 |
| Toys, Art and Collectibles | $34.63 | $12.98 | 2.43% | 1.54% | 1.99 | $71.01 |
| Apparel and Accessories | $37.41 | $13.95 | 2.53% | 1.49% | 2.26 | $88.60 |
| Beauty | $40.44 | $19.53 | 2.53% | 1.76% | 1.53 | $62.15 |
| Lifestyle and Boutique | $32.04 | $13.79 | 2.54% | 1.61% | 2.07 | $67.79 |
| Automotive | $35.63 | $10.65 | 2.36% | 1.21% | 2.75 | $110.84 |
| Travel Accessories and Luggage | $52.30 | $17.01 | 2.50% | 1.17% | 2.21 | $121.81 |
| Health and Wellness (excluded category, for context) | $42.30 | $22.44 | 3.08% | 1.43% | 1.42 | $62.52 |

Year over year, all industries: cost per purchase +4.24%, CPM +13.64%, conversion rate -6.10%, CTR +17.22% (VERIFIED, raw). Fourteen of 17 industries got more expensive per purchase.

Cost per click: Triple Whale does not publish it on this page. Other readings:
- Supermetrics: typical cost per click in September 2026 of $0.17 (Electronics and Gaming), $0.19 (Toys and Hobbies), $0.22 (Apparel), $0.24 (Beauty), $0.28 (Home and Kitchen) (VERIFIED, raw, https://supermetrics.com/ebook/black-friday-retail-playbook). **[vendor]** The landing page does not say whether this is all clicks or link clicks; all clicks is likely.
- MHI Media, 74 DTC brands: median link cost per click $1.48 for video and $1.52 for image over 12 months (VERIFIED, fetch, https://mhigrowthengine.com/blog/meta-ads-video-vs-image-benchmarks-2026/). **[vendor]** UK agency, small sample.
- WordStream's 2026 benchmark page was blocked (HTTP 403). UNKNOWN.

**New-store penalty.** No public benchmark isolates brand-new one-product stores. UNKNOWN. What exists:
- Meta: "During the learning phase, ad sets are less stable and usually have a higher CPA." (VERIFIED, raw, https://www.facebook.com/business/help/112167992830700)
- Northbeam, Aug 6, 2026: "Businesses doing more than $50 million in revenue a year generally outperform smaller ones." Median CAC rose 10.34% from H1 2025 to H1 2026; at the 25th percentile it rose 32.57%; CPMs "increased 10%-20% on average starting January 2026" (VERIFIED, fetch, https://themediabuyer.northbeam.io/p/h1-2026-meta-cvrs-are-tanking-as-cacs-skyrocket). **[vendor]** No figures by size in the text.
- Motion: small advertisers find winners at about half the rate of large ones (4.0% against 8.8%).
- The repo's x1.3 "tough" multiplier stays ASSUMED. Nothing found today replaces it.

### 2.2 TikTok ads benchmarks

Source: Triple Whale, "TikTok Ads Benchmarks by Industry", page dated Aug 20, 2026, "over 5,900 brands", Aug 1, 2025 to Jul 31, 2026 (VERIFIED, raw, https://www.triplewhale.com/blog/tiktok-benchmarks). **[vendor]**

| Category | Cost per purchase | CPM | CTR | Conversion rate | ROAS | AOV |
|---|---|---|---|---|---|---|
| All | $17.07 | $4.08 | 0.61% | 1.56% | 1.51 | $50.32 |
| Home and Garden | $19.33 | $4.61 | 0.59% | 1.61% | 2.02 | $61.28 |
| Electronics | $28.90 | $4.40 | 0.64% | 1.46% | 1.98 | $70.72 |
| Sports and Outdoors | $14.67 | $3.46 | 0.54% | 0.99% | 1.44 | $51.96 |
| Toys, Art and Collectibles | $18.37 | $4.40 | 0.55% | 1.71% | 1.57 | $47.43 |
| Apparel and Accessories | $20.64 | $4.16 | 0.74% | 2.08% | 2.70 | $73.79 |
| Pets and Animals | $5.46 | $4.59 | 0.41% | 0.38% | 0.02 | $0.38 |

**The Pets row is broken data.** An AOV of $0.38 and a ROAS of 0.02 cannot be real orders. `data/channel_params.json` currently stores `tiktok_ads_cpa_pets_usd = 5.46` from this table. It should be treated as UNKNOWN (see section 10).

TikTok CPM, later window (Oct 1, 2025 to Sep 30, 2026, "over 6,000 stores", $962.4 million tracked spend): blended median $4.07; Pets $4.50, Home and Garden $4.43, Consumer Electronics $4.30, Sports and Outdoors $3.58. Meta in the same dataset: $15.48 (VERIFIED, raw, https://www.triplewhale.com/blog/tiktok-cpm, Oct 12, 2026).

Reading: TikTok reach costs about a quarter of Meta's, but median ROAS is lower (1.51 against 1.88) and order values are lower. TikTok needs video; statics do not apply. TikTok Shop's own ad product (GMV Max) has no public benchmark; `channel_params.json` already records that as UNKNOWN.

### 2.3 Holiday timing (he would start on Nov 21; Black Friday is Nov 27, Cyber Monday Nov 30)

| Fact | Figure | Label |
|---|---|---|
| Meta CPM in Black Friday week 2025 against September 2025 | 16 to 41% higher, depending on sector | VERIFIED, raw, Supermetrics, "$675M in Meta ad spend from 5,000+ retail advertisers" **[vendor]** |
| Typical cost per click in Christmas week 2025 against September | 11 to 17% lower, in every sector | VERIFIED, raw, same |
| Advertiser spend in Black Friday week against a normal September week | 1.8 to 2.8 times | VERIFIED, raw, same |
| Electronics and Gaming | CPM spike of +26% in the week of Nov 10, then eased | VERIFIED, raw, same |
| Home and Kitchen | "Costs stayed flat until Nov 17" | VERIFIED, raw, same |
| Supermetrics' advice | "Finish testing in October" | VERIFIED, raw, same |
| Triple Whale brands on Meta during BFCM 2025 | Median cost per purchase $34.06, CPM $22.26 (about +7.8% on the year), ROAS 2.26, AOV $77.79 | VERIFIED, raw, https://www.triplewhale.com/blog/facebook-ads-bfcm **[vendor]** |
| Reels placements during BFCM 2025 | CPMs 30 to 40% lower than Feed | VERIFIED, raw, same |
| USPS Christmas cutoffs | Ground Advantage Dec 17, Priority Dec 18 | From `reports/full-synopsis-2026-11-19.md` section 11; not re-checked today |

Reading: buyers convert better in BFCM week (established brands had a lower cost per purchase than their yearly median) but reach costs more, and that conversion lift belongs to brands with offers, reviews and warm audiences. A cold test from a new store in the week of Nov 23 pays peak CPMs without those advantages. The two weeks after Cyber Monday are cheaper per click but run into shipping cutoffs for anything that does not ship from US stock.

### 2.4 The learning phase, and what a small budget can and cannot tell you

Meta's own text (VERIFIED, raw, https://www.facebook.com/business/help/112167992830700):
- "ad sets exit the learning phase as soon as they can deliver stably. This usually occurs after about 50 results in the week after the ad set's last significant edit."
- "During the learning phase, ad sets are less stable and usually have a higher CPA."
- "Avoid high ad volumes. When you create many ads and ad sets, the delivery system learns less about each ad and ad set."
- "Use realistic budgets."
- An ad set that cannot get enough results shows "Learning limited".

Inputs for the script, not computed here: 50 purchases per week per ad set; benchmark cost per purchase $39.23 (Pets), $48.61 (Home and Garden), $51.06 (Electronics); total test budget $500 to $1,000 including apps and a sample. On those inputs a purchase-optimized ad set in this test stays in learning for the whole test (the script should confirm). Consequences:
- Week-1 numbers will be noisy and worse than benchmark. A handful of purchases cannot measure cost per purchase.
- Fewer ads and ad sets is right for this budget. It matches Sergio C and Heath in `02_youtube_sweep.md` and contradicts "10 to 15 creatives in week 1".
- The first test answers "does anyone buy this at this price from this page", as CLAUDE.md milestone 2 already says. It does not answer "is CAC sustainable".

### 2.5 How many creatives per winner (data), and how many products per winner (no data)

Creatives, from Motion (VERIFIED, raw; pages under https://runneth.com/library/research/creative-benchmarks-2026/):

| Advertiser monthly Meta spend | Creatives tested per week | Hit rate | Turned off before day 28 |
|---|---|---|---|
| Micro, under $10,000 | 2.8 | 4.0% (3.7% in the portfolio table) | 50.2% |
| Small, $10,000 to $50,000 | 4.1 | 6.4% | 49.3% |
| Medium, $50,000 to $200,000 | 6.6 | 8.1% | 52.6% |
| Large, $200,000 to $1 million | 11.2 | 8.6% | 53.9% |
| Enterprise, over $1 million | 18.8 | 8.8% | 52.2% |

"~5% of creatives are winners." "55% of total Meta ad spend [is] concentrated on winning creatives." Caveats stated by Motion: the window covers Black Friday; a winner is defined by spend, with no link to ROAS, revenue or conversion.

Products per winner: **UNKNOWN.** No dataset found.
- Vendor blogs say 5 to 10, 5 to 8, or 8 to 15 products per winner, and $100 to $300 or $200 to $500 of ads per product test, one implying a 5 to 10% success rate (ESTIMATED, weak, search summaries today of funnelish.com, dropbuild.com, marksinsights.com, creatify.ai, yakkyofy.com). **[vendor]** None shows data.
- Creators in `02_youtube_sweep.md` imply 2 to 4.
- Reddit, the obvious place for unpaid first-hand reports, blocked every request today.

### 2.6 Static image ads against video and UGC

| Source | Finding | Label |
|---|---|---|
| MHI Media, 74 DTC brands, 12 months to Oct 28, 2026 | Image against video medians: link CTR 1.38% against 1.98%; CPM $19.42 against $27.41; conversion rate 2.71% against 2.48%; cost per purchase $58.66 against $63.15; ROAS 1.64 against 1.45. The author says the ranges overlap heavily and the gap is small. | VERIFIED, fetch. **[vendor]** Agency that sells UGC production; 22% of spend was unclassified; UK-based sample converted from pounds. |
| Motion, asset types | Highest hit rates, in order: text only, product image with text, lifestyle-product image, UGC, high production. Hit rates across types "approximately 4 to 12%". "The fastest-testing, highest-hit-rate asset categories are text-only, product-with-text, and UGC, not high-production." | VERIFIED, raw. **[vendor]** Window includes BFCM, which favors offer-heavy statics. |
| Motion, visual formats | Offer-first banner 8.6% hit rate (21.9% of creatives, 29.3% of spend), demo 8.1%, testimonial 6.5%, unboxing 9.8% | VERIFIED, raw |
| Triple Whale, BFCM 2025 | Reels CPMs 30 to 40% below Feed | VERIFIED, raw |
| Other vendor blogs | Conflict: some put video ROAS well above static, others put static cost per purchase below video | ESTIMATED, weak, search summary today |
| Creators in `02_youtube_sweep.md` | The sales in the transparent tests came from video or AI UGC, not from statics alone | ESTIMATED, self-reported |

Reading: across established accounts, statics hold their own on cost per purchase and are cheaper to reach people with. The creator's claim of "three times cheaper" has no support. For a new store the honest position is: start with a few hand-checked statics (offer or product plus text), add at least one short demo video as soon as the sample arrives, and let the data pick.

### 2.7 AI-generated creative

| Source | Finding | Label |
|---|---|---|
| Meta, "2026: AI Drives Performance", Jan 29, 2026 (https://about.fb.com/news/2026/01/2026-ai-drives-performance.md) | No figure for conversions from AI-generated creative. It reports "the combined revenue run-rate of our video generation tools hit $10 billion" and ranking-model gains such as "a 3.5% lift in ad clicks on Facebook". | VERIFIED, fetch. Meta sells the ads. |
| Meta AI video generation beta | Average gains of 10% in CTR and 8% in conversion rate for advertisers who used it for most ads in a campaign | ESTIMATED, search summary today; original Meta page not found |
| Columbia, Harvard, TU Munich and Carnegie Mellon with Taboola, Jan 2026 | Matched pairs of AI and human ads from the same advertiser, campaign and day; over 500 million impressions. Raw CTR 0.76% for AI against 0.65% for human; comparable under the tightest controls. AI ads that did not look like AI did best. | ESTIMATED, press coverage read as search summary today (https://www.emarketer.com/content/ai-ads-that-feel-human-drive-stronger-engagement and others). **[vendor]** Taboola sells an AI creative tool. Native display ads, clicks only, no purchases, not Meta. |
| Marketing Brew, Apr 7, 2026 | A media buyer said he consistently sees worse results with Meta's creative AI tools than with his own third-party systems | ESTIMATED, search summary today |
| Vendor blogs on "AI against human on Meta" | From 21% lower cost per purchase to 12% higher | ESTIMATED, weak, they conflict |
| Academic work on disclosure | Mixed: some find a disclosed AI label lowers credibility and purchase intent, some find no effect | ESTIMATED, small lab studies, search summary today |
| Meta labeling, post of Feb 3, 2025, updated June 1, 2026 (https://about.fb.com/news/2025/02/gen-ai-transparency-metas-ads-products/) | "AI info" label on ads "created or significantly edited with our generative AI creative tools". It sits next to "Sponsored" when the ad includes an AI-generated photorealistic human, otherwise in the three-dot menu. Meta "will begin automatically detecting ads created or edited using third-party AI tools through industry-standard signals". | VERIFIED, fetch |

Reading: AI images are an accepted, labeled, mainstream way to make ads, and click performance is about equal to human-made creative in the one large controlled study. Whether AI statics of a product Dhruv has not yet held will convert cold US traffic into profitable orders is UNKNOWN. A photorealistic AI person triggers the more visible label and is barred by the repo anyway from claiming to have used the product. A picture that does not match what the supplier ships is what Meta's customer survey punishes (section 4.3).

### 2.8 Conversion rate

- Meta click to purchase, established brands: 1.51% median; Pets 1.60%, Home and Garden 1.22%, Electronics 1.16% (VERIFIED, raw, Triple Whale).
- Shopify stores in general: third-party summaries of Littledata's panel say about 1.4% average; top 20% at 3.2% and above in one summary, 2.7% in a 426-store sample for the 90 days to Oct 3, 2026 in another (ESTIMATED, weak, they conflict; search summary today).
- New one-product store on cold traffic: UNKNOWN. Creator data points in `02_youtube_sweep.md`: 1.54% measured (Mark Builds Brands), 1.9% (Haven, an established brand).

### 2.9 Test budgets and first-week results that practitioners report

Already tabled in `02_youtube_sweep.md` sections 4.3 and 6.2 (ESTIMATED, self-reported, mostly by people paid by tool affiliates). Summary: stated test budgets $100 to $500; $25 to $100 a day per product; first sale within a day in the tests that got one; day-level results from a loss of $130 to a gain of $270; two of seven tests failed outright; only the two-operator, rising-budget test passed $2,000 of sales in a week. One third-party write-up of the Tilbury video puts the 7-day profit at $81 on a $250 budget (ESTIMATED, https://income-reality-check.pages.dev/a/passive-income-i-tried-ai-dropshipping-for-a-week-raw-result/, search summary today); `02` read a caption figure it could not confirm. Either way the result was near break-even.

No independent (non-creator) log of a sub-$1,000 first test was found today. UNKNOWN.

---

## 3. Product-finding and validation methods

Prices are for monthly billing unless stated. "Signal" is what the tool actually observes. "Reliability" is my assessment from the sources named.

| Method | Price and free tier, Nov 2026 | Signal it gives | How reliable | Bias |
|---|---|---|---|---|
| Meta Ad Library (web) | Free, no login to search. The public search page loaded today without login; results did not render in the headless browser (bot block). VERIFIED that it is free to open; results not read today. | Which advertisers are running which ads now, the start date of each ad, how many versions use the same creative, the landing page. No spend, reach or sales for US commercial ads. | Good for "is anyone advertising this, and for how long". Says nothing about profit. A long-running ad is a signal, never proof (CLAUDE.md section 3). | None; it is Meta's transparency tool. |
| Meta Ad Library through the Meta Ads connector | Free; connected in this workspace | Same data by keyword or page | `01_video_decode.md` found keyword search returned unrelated advertisers. Usable with exact page names. | None |
| AdLibrary.io (the video's "Ad Library") | $29 a month after a 3-day trial (VERIFIED in `01_video_decode.md`) | A searchable copy of Meta ads with an MCP server | Same underlying signal as the free library, plus filters | **[affiliate]** The creator is tied to it (see `01`). |
| Winning Hunter | $30, $49 and $90 a month "billed yearly" for Basic, Standard and Enterprise; "Save up to 15% with quarterly, 40% with yearly" (VERIFIED, raw, https://winninghunter.com/pricing). Month-to-month price not readable today: UNKNOWN. Standard shows "Get started free"; trial terms UNKNOWN. | Ads on Meta, TikTok and Pinterest, store traffic and revenue estimates, TikTok Shop data, MCP and API | The vendor itself says sales data "is not 100% exact" and is a ballpark (ESTIMATED, search summary today). | **[vendor] [affiliate]** Runs an affiliate program; most "reviews" are affiliates or rivals. |
| Minea | $49, $99 and $199 a month (Starter, Premium, Business); $39, $79, $158 if paid quarterly (VERIFIED, raw, https://www.minea.com/pricing). "Try for free" button; terms UNKNOWN. | Meta ads, influencer placements, "winning product" lists, shop tracking | Curated lists reach every subscriber at once, so a listed product is by definition already seen by "over 200,000" users (their claim). | **[vendor]** Also sells a course. |
| PiPiADS | Monthly: Basic $49 on a "flash sale" (list $69), Advanced $99 (list $159). Annual promotion to Dec 31: Basic $294 a year, Advanced $594 a year (VERIFIED, raw, https://www.pipiads.com/pricing). Credit-based: 30,000 credits on Basic. | TikTok and Facebook ads with estimated spend and engagement | The vendor calls spend and conversions "estimates"; one reviewer says accuracy "holds up on distinctive products and collapses on generic ones" (ESTIMATED, search summary today, rival-hosted). | **[vendor]** |
| AdSpy | "$149 per month", described as an introductory offer (VERIFIED, raw, https://adspy.com/). No free tier shown. | The largest Facebook and Instagram ad archive, with comment search | Good archive depth; no sales data | **[vendor]** |
| Foreplay | Basic $49, Workflow $149, Agency $389 a month; 7-day free trial (VERIFIED, raw, https://www.foreplay.co/pricing). The Foreplay MCP in this workspace returned HTTP 402, "No active subscription for this user", today. | Saved-ad boards, a 200 million ad database, competitor tracking (Spyder), briefs | Built for creative research, not product discovery; no sales estimates | **[vendor] [affiliate]** "Make over $10k/mo referring Foreplay" on its own menu. |
| Kalodata (TikTok Shop) | Pricing page failed to load today. Third parties report a 7-day free trial and a Starter plan between $38 and $79 a month, conflicting (ESTIMATED, search summary today: koala-apps.io, copyfy.io, toolsurf.com, winninghunter.com). | Estimated TikTok Shop revenue and units by product, shop, creator and video | The only kind of tool here that estimates sales rather than ad activity. Estimates, not platform reports. | **[vendor]** |
| FastMoss (TikTok Shop) | Pricing page errored today. Third parties: $49, $89, $139 a month (Delzonic, checked Sep 2026), others say $59 and up; no permanent free tier (ESTIMATED, search summary today). | Same class of data as Kalodata | Same | **[vendor]** |
| TikTok Creative Center | Free (ESTIMATED; not opened today) | Top ads and trending products by region and category | Shows what gets reach on TikTok, not what makes money | Platform |
| Amazon Movers and Shakers | Free. Page title: "The biggest gainers in Amazon sales rank over the past 24 hours" (VERIFIED, raw) | Rank jumps over 24 hours | Noisy. A small product with modest sales can top it; rank moves day to day (ESTIMATED, seller-tool blogs, search summary today). Use Best Sellers and rank history for anything durable. | None |
| Amazon "bought in past month" on listings | Free on Amazon; read here through DataForSEO | A floor on units sold in the last month, per listing, in buckets (50+, 100+, 1K+) | The best free sales evidence there is: it is Amazon's own count. Buckets are coarse and only shown above a threshold. | None |
| Supplier "winning product" lists (Zendrop, AutoDS, CJ, Sell The Trend, store-builder presets) | Included with the supplier app (Zendrop tiers in `01`) | What the supplier wants listed | Low. The supplier is paid when you sell its item, the same list goes to every user, and StoreBuild alone claims "Over 1.5 Million Stores Created", each with the same kind of 10 preset products (`02`, red flag 5). | **[vendor]** |
| Google Trends | Free | Relative interest over time, scaled "0 to 100"; "a largely unfiltered sample" (VERIFIED, fetch, https://support.google.com/trends/answer/4365533) | Direction and seasonality only. Google: treat it as "one data point among others". No volumes. | None |
| Google Ads search volume and CPC (DataForSEO) | Connected here, cents per call | Absolute monthly searches and what advertisers bid | Reliable for "people look for this" and for seasonality. Says nothing about whether a new store can convert them. | None |

### 3.1 How a careful operator validates before spending

In order. Each step can kill the product for free.

1. **Sales evidence from a platform's own counter**, not from an ad-spy estimate: several Amazon listings with "bought in past month" in the price band, or TikTok Shop sold counts.
2. **The Amazon and Google test** (Fogarty's test in `02`): can the buyer find the same item in one search, cheaper, with Prime delivery and thousands of reviews? If yes, the store needs a real difference (bundle, fit, guarantee, speed) or the product is out.
3. **Ad activity as a second signal**: several unrelated stores advertising it now, some for 30 days or more (Meta Ad Library, free).
4. **A real supplier quote**: unit cost, shipping cost, ship-from location, days to deliver, return terms. Until then cost is UNKNOWN and the gate is blocked (CLAUDE.md section 5).
5. **IP check**: brand names in the listing, design patents on the shape, the supplier's right to its photos (section 4).
6. **`scripts/economics.py`** with the category benchmark cost per purchase and the x1.3 tough case. The cushion rule decides.
7. **A test order to a US address** and one unit in hand. Dhruv approved starting ads the same day as ordering the sample; that is an exception to flag, not a reason to skip the order.
8. **A capped paid test** with the repo's kill rules written down before launch.

### 3.2 Worked illustration: the video's example product

This is the validation the video skipped. All ESTIMATED (DataForSEO, read today, 2026-11-21).

- Google US searches: "dog hair dryer" 8,100 a month on average (9,900 in Oct 2026), CPC $0.86; "dog dryer" 5,400; "high velocity dog dryer" 3,600, CPC $1.23.
- Amazon US, first results page for "dog hair dryer": 67 organic and sponsored results, some repeated. Examples: SHELANDY force dryer $64.59, 18,200 ratings, 3K+ bought in past month, Amazon's Choice; oneisall 8-in-1 vacuum and dryer $97.99, 2,700 ratings, 1K+ bought; a 2-in-1 dryer brush at $26.59, 4,600 ratings, 1K+ bought; a generic 5.2HP dryer at $85.49, 1,700 ratings, 1K+ bought.
- Reading: demand is proven and so is the competition. A shopper sees the same class of product at $27 to $98 with fast delivery and thousands of reviews. A template store selling a supplier's dog dryer has to beat that on price, on a real difference, or on an audience that never checks Amazon. Nothing in the video addresses this.
- Side note: Google US searches for "ai dropshipping" went 14,800 (Aug 2026), 27,100 (Sep), 40,500 (Oct), and advertisers bid a CPC of $19.11 for that phrase. The people paying $19 a click are selling tools, builders and courses to the searcher.

---

## 4. The "copy a winning product" approach: limits and what is fine to borrow

Not legal advice. Primary texts quoted where read.

### 4.1 What the law protects

| Right | What it covers | What it means here | Label |
|---|---|---|---|
| Copyright | "original works of authorship"; it "may protect the way these things are expressed". "Copyright does not protect ideas, concepts, systems, or methods of doing something." "Copyright does not protect names, titles, slogans, or short phrases." | A competitor's photos, videos, ad images, ad copy and page text are protected. The angle, the offer structure and the ad format are not. | VERIFIED, fetch, https://www.copyright.gov/help/faq/faq-protect.html |
| Trademark | Brand names and logos; ads may not confuse people about who is behind the product | No competitor name or logo in ads, product titles, the domain or image prompts that reproduce it. Several ONEISALL trademark applications exist, including for hair dryers; current status needs a USPTO check. | ESTIMATED, https://trademarks.justia.com/owners/shenzhen-shouzheng-chuqi-e-commerce-co-ltd-5798515, search summary today |
| Trade dress | A distinctive, non-functional overall look of a product, package or brand presentation | "Make our ads look like theirs" is the risky instruction. Commentary notes that saved prompts and outputs can show that a competitor pointed the AI at an existing visual identity on purpose. Lack of intent is not a defense for trade dress. | ESTIMATED, https://www.thefashionlaw.com/when-ai-creates-a-lookalike-brand-who-is-doing-the-copying/ and https://www.gtlaw.com/ar/insights/2026/6/forever-rights-or-ticking-time-bomb-non-traditional-trademarks-in-the-age-of-dupe-culture, search summary today |
| Design and utility patents | The look of a product (design) or how it works (utility) | A generic copy of a patented shape infringes even with a different name. A retailer listing says the oneisall dryer carries an "Exclusive Patent"; the number is UNKNOWN. | ESTIMATED, search summary today |
| Supplier photos | Often shot by the original brand, not the supplier | The right to use Zendrop or AliExpress photos is UNKNOWN unless the supplier confirms it in writing. Feeding one to an image model to make "product images" keeps the same question open and can show an item that differs from what ships. | UNKNOWN |

### 4.2 How enforcement reaches a small seller

| Channel | Rule | Label |
|---|---|---|
| Shopify, copyright | On a notice Shopify "will generally remove the reported content". After a valid counter notice "a merchant will generally be allowed to repost the content in 10 to 14 business days". "Shopify has a policy of terminating stores for repeat infringement in appropriate circumstances." "Shopify retains discretion to disable stores for even a single instance of willful or egregious infringement." "all shops that are owned or operated by the same repeat infringer are also subject to termination." | VERIFIED, fetch, https://help.shopify.com/en/manual/compliance/intellectual-property/copyright-policy |
| Shopify, abuse of the process | Competitors also file false notices; Shopify has sued over it. Removal happens in minutes, restoration takes weeks. | ESTIMATED, https://torrentfreak.com/shopify-files-fresh-lawsuit-over-dmca-takedown-harassment-231128/, search summary today |
| Meta ads | "Ads may not contain content that violates the intellectual property rights of any third party". Examples in the May 30, 2024 version: ads that "Promote or sell counterfeits, knockoffs, or replicas of another company's products" or "Are likely to confuse people about the source, sponsorship or affiliation of the goods or services." | VERIFIED, fetch, https://transparency.meta.com/policies/ad-standards/intellectual-property-infringement/third-party-infringement/ |
| Meta, how it is enforced | Mostly on a rights holder's report; an ad can be rejected, and repeated reports put the ad account at risk | ESTIMATED, search summary today of https://transparency.meta.com/policies/ad-standards/intellectual-property-infringement/copyright-and-trademarks |
| Courts, "Schedule A" cases | One rights holder sues hundreds of online sellers in a sealed filing and asks the court, before the sellers are told, to freeze marketplace accounts and payment-processor funds (PayPal and Stripe are named). Filings kept rising in 2025 and spread beyond Chicago. One law firm estimates about 70% end in default judgments. | ESTIMATED, https://www.traverselegal.com/blog/your-amazon-or-paypal-account-was-frozen-by-a-trademark-lawsuit-a-sellers-guide-to-schedule-a-cases/ and https://law360.com/articles/2483634 (May 29, 2026), search summary today. Law firms marketing a defense practice. |
| FTC | Fake or AI-invented reviews and testimonials, made-up "was" prices and unearned "free" claims are separate violations already listed in CLAUDE.md and the synopsis | Repo |

### 4.3 Platform rules that punish the dropshipping version of copying

- Meta has said since 2018 that "people don't like ads that quote inaccurate shipping times or that misrepresent products", and that if feedback does not improve "we will reduce the amount of ads that particular business can run", which "can continue to the point of banning the advertiser" (VERIFIED, fetch, https://about.fb.com/news/2018/06/improving-customer-service/). Third-party guides give the current score bands as a delivery penalty between 1 and 2 and no advertising below 1 (ESTIMATED, search summary today; Meta's live help page was not reached).
- Shopify Payments can hold back "a portion, in some cases a full amount, of transactions". Listed risk factors include "Industries with extended delivery timelines", "Increased refund rate", "Elevated chargeback activity" and "Significant volume surges". The page's examples use 120 days (VERIFIED, fetch, https://help.shopify.com/en/manual/payments/shopify-payments/reserves).
- The FTC's 2025 data: scams starting on social media cost $2.1 billion; shopping was the most reported kind; "Most people said they paid for things that simply never arrived." (VERIFIED, fetch, FTC data spotlight, Apr 27, 2026, https://www.ftc.gov/news-events/data-visualizations/data-spotlight/2026/04/reported-losses-scams-social-media-eight-times-higher-2020). Buyers have reason to distrust an unfamiliar store from an ad, and an honest slow-shipping store sits in the same bucket in their minds.

**Flag on the approved exception.** Starting ads before holding the product is allowed for this test. It carries three specific risks: the page shows something that differs from what ships (Meta feedback, refunds), the delivery promise has no test order behind it (FTC Mail Order Rule, CLAUDE.md section 9), and quality is unknown. The mitigation is the same-day sample order and a delivery window taken from the supplier's written terms, not from the store builder's default.

### 4.4 What is fine to borrow

- The problem and the angle ("drying a wet dog takes an hour").
- The ad format: offer-first banner, demo, before and after, comparison without naming a rival.
- The offer structure: bundles, quantity breaks, guarantee length, price points.
- Page structure, the order of sections, which objections get answered.
- Customer language from public reviews, as research for our own copy (not pasted as our reviews).
- Facts and non-patented functional features.

Not fine: their photos, video, ad images or text; their name or logo; a look close enough to be mistaken for them; invented reviews; a product shape under a design patent. This matches the repo rule: "Creative borrows an angle or a format, never the asset."

---

## 5. Regulators, 2023 to 2026

### 5.1 FTC cases on ecommerce "AI" and dropshipping income claims

FTC complaints are allegations; settlements come without admissions.

| Case, date | What was sold and promised | What buyers paid | What the FTC said about results | Outcome | Label |
|---|---|---|---|---|---|
| Automators AI, Empire Ecommerce, Onyx. Press release Aug 22, 2023 | Managed Amazon and Walmart stores and coaching; "$4k-$6k consistently monthly net profit"; "AI machine learning" | Consumers were lured "to invest $22 million" | "the vast majority of clients did not make the promised earnings or even recoup their investment"; Amazon and Walmart "routinely suspended or terminated the stores" | Settled Feb 2024: about $21.7 million in assets and a ban (ESTIMATED, press, search summary today) | VERIFIED, fetch, https://www.ftc.gov/news-events/news/press-releases/2023/08/ftc-action-stops-business-opportunity-scheme-promised-its-ai-boosted-tools-would-power-high-earnings |
| FBA Machine, Passive Scaling. Complaint June 2024 (filing month from press coverage) | "7-figure business", "risk-free", AI-powered storefront software | "tens of thousands to hundreds of thousands of dollars"; more than $15.9 million in total | Earnings claims "rarely, if ever, materialize" | Settled 2025 with a ban (ESTIMATED, search summary today) | VERIFIED, fetch, FTC release Sep 25, 2024 |
| Ascend Ecom. Sep 25, 2024 | "cutting edge" AI tools, "five-figure monthly income by the second year" | Tens of thousands for the store plus tens of thousands for inventory; at least $25 million in total | "for nearly all consumers, the promised gains never materialize" | Proposed order June 23, 2025: ban, assets turned over | VERIFIED, fetch, https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes and the case page |
| Ecommerce Empire Builders. Complaint filed Sep 18, 2024 | "AI-powered Ecommerce Empire"; a **dropshipping** model using "cheap products from Chinese dropshipping companies"; "$10,000 a month" | Courses at almost $2,000; done-for-you stores at $10,000 to $35,000 | Paragraph 41: "Defendants understate the actual costs required to run and maintain a dropshipping business, especially ongoing marketing costs. After accounting for fixed costs needed to run and maintain EEB-built ecommerce stores, Defendants' online stores often lose money, even the stores Defendants tout as success stories." Paragraph 35: "By their own admission, Defendants lack substantiation for their earnings claims". Their own fine print: "my results are not typical." | Stipulated order May 9, 2025: ban, assets for refunds | VERIFIED, raw, complaint PDF https://www.ftc.gov/system/files/ftc_gov/pdf/2423027ecommercebuilderscomplaint.pdf and the case page. (The quote's dash is replaced by a comma here.) |
| Click Profit. Mar 18, 2025 | "guaranteed passive income using cutting-edge AI technology"; stores on Amazon, Walmart and TikTok | A "management fee" of at least $45,000 plus inventory; at least $14 million in total | "Amazon has blocked, suspended, or terminated about 95% of Click Profit's stores." "more than one-fifth of the company's stores on the platform earn no money at all"; "another third earns less than $2,500 in gross lifetime sales" | Aug 25, 2025: permanent ban, assets for redress | VERIFIED, fetch, https://www.ftc.gov/news-events/news/press-releases/2025/03/ftc-acts-stop-click-profit-online-business-opportunity-has-cost-consumers-least-14-million |
| Growth Cave. Action Mar 2025, settlement Jan 27, 2026 | Coaching and credit-repair business opportunities, "false promises of significant income" | Nearly $50 million | The opportunities "regularly failed to deliver the promised results while costing consumers thousands of dollars" | Bans; judgments totaling $48,597,538, partly suspended; the orders also bar misleading claims about artificial intelligence | VERIFIED, fetch, https://www.ftc.gov/news-events/news/press-releases/2026/01/ftc-secures-settlement-banning-growth-cave-defendants-marketing-selling-business-opportunities. Not ecommerce. |
| Air AI. Complaint Aug 2025, settlement Mar 24, 2026 | AI sales-calling tool sold as a business opportunity | Not stated on the page | "Falsely claimed that people who purchase their services will or are likely to make substantial earnings" | $18 million judgment, largely suspended; $50,000 paid; ban | VERIFIED, fetch, FTC release Mar 24, 2026. Not ecommerce. |

A new ecommerce-store or dropshipping case filed in 2026: none found. The FTC's business-opportunity listing for 2026 (read today through Oct 5, 2026) shows Air AI, Growth Cave, a trucking "automation" scheme, franchises and Amway (VERIFIED, fetch, https://www.ftc.gov/industry/franchises-business-opportunities-and-investments).

### 5.2 Other regulator facts

- FTC, Apr 27, 2026: "One in three people who reported losing money to a job or business opportunity scam in 2025" said it started on social media (VERIFIED, fetch).
- Reported losses to business and job opportunity scams: $750.6 million in 2024 (ESTIMATED, FTC release of Mar 2025 read as search summary today). The 2025 category figure was not found: UNKNOWN.
- Rule-making: in January 2025 the FTC proposed extending the Business Opportunity Rule to "money-making opportunities", including business coaching. As of a June 2026 law-firm note it was still pending (ESTIMATED, https://ftc.gov/news-events/news/press-releases/2025/01/ftc-proposes-rule-changes-new-rule-deter-deceptive-earnings-claims-multilevel-marketers-money-making, search summary today). Current status: UNKNOWN.
- No FTC consumer alert specific to dropshipping was found.

### 5.3 What this means for the video

- The FTC cases are about people who paid $2,000 to $75,000 for coaching or a managed store. The video sells no course; it earns from partner links (`01_video_decode.md`). The legal exposure is different. The pattern of the pitch is the same: an AI label, a large revenue number from a different business, and no data on typical results.
- What the FTC found when it could see inside (Empire's own stores, Click Profit's 230 stores, Automators' clients) is the nearest thing to a base rate for "follow the system" ecommerce: most made little or nothing, and marketing cost was the part left out.
- An income line such as "$100,000 before the end of the year" needs a reasonable basis and typical-result evidence under FTC advertising law. `01` could not find where the line appears, and found no disclaimer on the funnel pages it read.

---

## 6. Is "$100,000 before the end of the year" plausible?

Start Nov 21, 2026. Year end is 40 days away. Budget under $1,000. A first-time store owner with 1 to 3 hours a day.

### 6.1 What it would take

| # | Requirement | Evidence | Verdict |
|---|---|---|---|
| 1 | Sales of about $2,500 a day on average from day one (simple division of $100,000 by 40 days) | Haven, the creator's four-year-old stocked brand, reported $125,463.94 for the whole of September 2026 (`02`, section 6.1, ESTIMATED) | Requires out-earning the creator's mature brand per day, immediately |
| 2 | An ad budget in proportion | Median Meta ROAS for established brands: 1.88 (VERIFIED, Triple Whale). Haven: $68,886.10 of Meta spend behind that month, "around a two ROAS" (ESTIMATED, `02`). The script should compute the spend implied; on these inputs it is a five-figure sum. | Fails on a budget under $1,000 |
| 3 | An ad account allowed to spend that much | Third-party guides report daily spending limits of about $25 to $50 on new ad accounts, rising with payment history (ESTIMATED, weak; Jon Loomer notes he has not seen the figure in Meta's documentation; search summary today). Dhruv's own limit: UNKNOWN. | Likely fails in the first weeks |
| 4 | Cash to float the gap | Shopify: "payouts for new merchants can take up to 5 business days" (VERIFIED, fetch, https://help.shopify.com/en/manual/finance/shopify-balance/payouts/payout-accounts). Reserves can hold part or all of sales; "Significant volume surges" and "extended delivery timelines" are listed triggers (VERIFIED). The supplier and Meta are paid before the payout lands. | Fails without outside cash |
| 5 | A winning product and ad on the first or second try | About 4% of small advertisers' creatives become winners (VERIFIED, Motion). Creators imply 2 to 4 product tests (`02`). The budget covers two or three small tests at most. | Unlikely |
| 6 | Profit per order at peak-season ad prices | Black Friday week CPMs 16 to 41% above September (VERIFIED). Meta: higher cost per purchase while learning (VERIFIED). Benchmark cost per purchase about $35 to $52 by category (VERIFIED) against a dropship margin that is UNKNOWN until a quote exists. | Unproven |
| 7 | A supplier that ships hundreds to thousands of orders in time for Christmas | USPS cutoffs Dec 17 and 18 (repo). Supplier stock depth and delivery days: UNKNOWN. | Unproven |
| 8 | No interruptions | New ad accounts get reviewed and sometimes disabled (`02`, red flag 19). Payment holds (section 4.3). Takedowns if the store copies (section 4.2). | Each one costs days out of 40 |
| 9 | The time to run it | Orders, tracking questions and refunds at that volume, on 1 to 3 hours a day | Fails |
| 10 | Someone comparable having done it | No beginner result of any size is shown in the video or funnel (`01`). The FTC has repeatedly found that claims of this kind had no substantiation (section 5). | No evidence |

**Verdict: not plausible.** Requirements 2, 3, 4, 9 and 10 fail on evidence and the rest are unproven. The line is marketing. And even at face value, $100,000 is revenue: the creator's own brand kept about 10% of revenue in its latest reported month (`02`, section 6.1, ESTIMATED).

### 6.2 The realistic range for week 1 of a first test under $1,000

From the transparent tests in `02_youtube_sweep.md` section 6.2 (all ESTIMATED, self-reported) and the benchmarks above:

| Outcome | What it looks like | Seen in |
|---|---|---|
| Poor (common) | A few sales or none; most of the ad money gone; product paused on the kill rule | Mohsin's first product, Juodkunaitis, Ant's first product |
| Middle (common) | First sale within a day or two; a few hundred dollars to about $1,200 of sales in the week; near break-even after ads, goods, fees and samples | Tilbury's expert ($855.75 of sales on $249.66 of ads over 4 ad days), Wold in the UK ($1,147 on $510), Mohsin's second product |
| Good (uncommon) | A second product catches; single days of $500 to $1,000 in sales; a few hundred dollars of profit for the week | Ant's second product |
| Outlier | More than $2,000 of sales in the first week | Persse only: two experienced operators, budget rising from $50 to $200 a day, a children's product that Dhruv excludes |

Against Dhruv's stated goals:
- "First sales and clear data": realistic. This is what a sub-$1,000 test can deliver.
- "About $2,000 in sales in week 1": a stretch. One of seven transparent tests did it, and not under these constraints.
- "Each order profitable after ad cost": not supported as a week-1 expectation. No transparent test shows it, and Meta says cost per purchase runs higher during learning. The workable form of the rule is the repo's: a fixed loss limit for the test, a pause at break-even CAC with zero purchases, and no scaling until 3-day blended CAC is at or under target.

---

## 7. Which model is easiest and fastest to a first profitable sale under $1,000?

No independent head-to-head ranking was found. The comparison articles are written by vendors of one of the models (ESTIMATED, weak, search summary today). The table assembles the evidence; the last column is my judgment.

| Model | Cash before first sale | Time to first sale | Evidence on profit | Main risks | Fit for Dhruv (judgment) |
|---|---|---|---|---|---|
| Generic dropshipping, China-shipped | Lowest for a store: $1 a month trial plus app plus ads | Hours to a day once ads run (`02`) | No base rate. Gross margin "around 20% to 50%" before ads (Shopify). FTC on a dropshipping coaching seller's own stores: they "often lose money". | Long delivery: Meta feedback penalty, payment reserves, FTC shipping rule; duty on every parcel since 2025 (repo); refunds; out of scope under CLAUDE.md section 2 | Fast, but the highest refund and account risk. Conflicts with "low risk". |
| US-stock dropshipping | Same as above; unit cost higher | Same | No independent profitability data: UNKNOWN. The reference creator's own advice is a US warehouse and 2 to 3 day delivery (`01`). Repo example: the same extender at $76.99 from US stock against $47.50 China-shipped (synopsis, section 7), so speed is paid for in margin. | Thinner margin; US stock can run out; resold catalog items are also on Amazon | **Best fit for speed with fewer refunds**, if a product passes `economics.py` at US-stock cost |
| TikTok Shop seller | $0 monthly fee (repo, ESTIMATED); samples for creators | UNKNOWN; depends on creators posting | Top 1% of sellers make about 60% of sales; the bottom half about 0.1% (VERIFIED, Marketplace Pulse) | New-seller order caps (third parties report 50 to 100 orders a day at the first tier, conflicting; ESTIMATED); settlement about 31 days after delivery for new sellers (repo, ESTIMATED); US shipping rules changed in 2026 and sources conflict (UNKNOWN); needs video and creators | Not a week-1 channel. A second step once a product sells. |
| TikTok Shop affiliate (creator) | Near zero | UNKNOWN; needs an account with followers and regular video | Vendor roundups: the top 0.5% of creators drive 38% of affiliate GMV; mid-tier creators (10,000 to 100,000 followers) have median earnings of $680 a month (ESTIMATED, weak, search summary today). Average commission about 13% (repo, ESTIMATED). | Needs a follower threshold and on-camera style content; Dhruv does not appear on camera; daily posting limits since May 2026 (ESTIMATED) | Lowest cash risk, slowest and least predictable. Poor fit. |
| Print on demand | Near zero; a sample | UNKNOWN for the first sale. Printify: sellers average 165 days to their first $1,000 of revenue and publish about 67 listings before reaching it (VERIFIED, fetch, https://printify.com/blog/print-on-demand-statistics/) **[vendor]** | Printify says new sellers often start at margins of 5 to 10%. The repo's own print-on-demand gift test passes the base case and fails the low case (synopsis, section 11). | Made-to-order lead time; holiday cutoffs in mid-December; the design is the whole difference | US-made and no stock, so low risk of refunds from slow delivery. With paid ads it behaves like dropshipping with slower production. A fair second lane. |
| Amazon (own listing, FBA) | 25% of surveyed sellers started under $1,000; 64% under $5,000 (Jungle Scout, **[vendor] [survivor]**) | 48% launched within 3 months | 58% profitable within a year, 22% within 3 months, 13% not yet (same survey). Amazon PPC cost per purchase median $13.98 (repo, ESTIMATED). | Needs stock on hand, so not a no-inventory test; no reviews at launch; the "automation" version is what the FTC keeps shutting down | Cheapest ads, but cannot start before Christmas without stock. Later lane. |
| Own brand with stock (Barkfare) | About $6,976 for the first 150 kits (synopsis, section 8) | Weeks to months | Best unit profit if it works (repo money math). Haven, the creator's real business, is this model and kept about 10% in a weak month after four years. RAND: half of active Shopify businesses grow from year 1 to year 2; 48.5% report a profit. | Cash, time, inventory risk | The slow lane, as already decided. It is also what the creator actually does. |

**Reading.** Paid-traffic dropshipping is the only model here that can produce a sale within days of starting, which is why every creator teaches it. It is also the model with the least evidence of profit and the most platform risk. Choosing US stock removes the biggest known cause of refunds, bans and holds, at the price of margin. So the question for the fast lane is narrow: is there a US-stock product whose verified landed cost leaves a pre-ad contribution above the category's benchmark cost per purchase with the cushion? If no candidate passes, the evidence says do not run the test, and "zero winners is an acceptable result" (CLAUDE.md section 3).

---

## 8. US stock or China-shipped: what this file adds

- Meta's customer survey penalizes "inaccurate shipping times" and can end in a ban (VERIFIED).
- Shopify Payments lists "extended delivery timelines" as a reason to hold funds (VERIFIED).
- The most common social-media shopping complaint to the FTC in 2025 was goods that "never arrived" (VERIFIED).
- Shopify: "Shoppers now expect delivery in days rather than weeks." (VERIFIED, fetch)
- A measured refund or chargeback rate by shipping speed: still UNKNOWN. No source found, same as `02`.
- Visa's dispute-monitoring threshold was reported lowered to 1.5% from April 1, 2026, applying above 1,500 monthly fraud and dispute cases (ESTIMATED, vendor blog https://redo.com/resources/articles/chargebacks/vamp-2026-shopify, search summary today). The count floor means it does not bite a small test, but processors apply their own stricter judgment to new accounts.
- NRF: 19.3% of online sales expected to be returned in 2025 (ESTIMATED, NRF release read as search summary today). All retail, heavy on apparel. Keep the repo's 5% and 10% refund scenarios as ASSUMED.

Reading: every piece of platform and regulator evidence points the same way as Dhruv's preference. US stock for the test.

---

## 9. Inputs collected for the scripts (no math done here)

| Input | Value | Label for `data/` | Source |
|---|---|---|---|
| Meta cost per purchase, all industries | $39.73 | ESTIMATED | Triple Whale, Nov 2025 to Oct 2026, read 2026-11-21 |
| Meta cost per purchase, Pets and Animals | $39.23 | ESTIMATED | same |
| Meta cost per purchase, Home and Garden | $48.61 | ESTIMATED | same |
| Meta cost per purchase, Electronics | $51.06 | ESTIMATED | same |
| Meta cost per purchase, Sports and Outdoors | $45.30 | ESTIMATED | same |
| Meta cost per purchase, Toys, Art and Collectibles | $34.63 | ESTIMATED | same |
| Meta cost per purchase, Beauty | $40.44 | ESTIMATED | same |
| Meta cost per purchase, Automotive | $35.63 | ESTIMATED | same |
| Meta cost per purchase, Apparel and Accessories | $37.41 | ESTIMATED | same |
| Meta cost per purchase, Travel Accessories and Luggage | $52.30 | ESTIMATED | same |
| Meta CPM, all, Pets, Home and Garden, Electronics | $15.72, $16.89, $15.06, $15.62 | ESTIMATED | same |
| Meta CTR, all | 2.48% | ESTIMATED | same |
| Meta conversion rate, all, Pets, Home and Garden, Electronics | 1.51%, 1.60%, 1.22%, 1.16% | ESTIMATED | same |
| Meta ROAS, all | 1.88 | ESTIMATED | same |
| Meta AOV, all, Pets, Home and Garden, Electronics | $74.62, $60.37, $114.14, $110.65 | ESTIMATED | same |
| Black Friday week CPM uplift against September | 16% to 41% by sector | ESTIMATED | Supermetrics, 2025 data |
| Christmas week cost per click against September | 11% to 17% lower | ESTIMATED | same |
| BFCM 2025 median cost per purchase and CPM on Meta | $34.06 and $22.26 | ESTIMATED | Triple Whale BFCM page |
| New-store multiplier | 1.3 | ASSUMED | CLAUDE.md; nothing found to replace it |
| Results needed to leave Meta's learning phase | about 50 per ad set per week | VERIFIED (platform documentation) | Meta Business Help Center |
| Creative hit rate, advertisers under $10,000 a month | 3.7% to 4.0% | ESTIMATED | Motion |
| Share of creatives turned off before day 28 | about 50% | ESTIMATED | Motion |
| TikTok ads cost per purchase, all, Home and Garden, Electronics | $17.07, $19.33, $28.90 | ESTIMATED | Triple Whale, Aug 2025 to Jul 2026 |
| TikTok ads cost per purchase, Pets | set to UNKNOWN | UNKNOWN | broken row, section 2.2 |
| TikTok CPM blended | $4.07 | ESTIMATED | Triple Whale, Oct 2025 to Sep 2026 |
| Shopify Payments payout delay, new merchants | up to 5 business days | VERIFIED (platform documentation) | Shopify Help Center |
| Shopify Payments reserve | possible; part or all of sales; examples of 120 days | VERIFIED (platform documentation) | Shopify Help Center |
| Dropshipping gross margin range | 20% to 50% | ESTIMATED | Shopify blog; not a substitute for a quote |
| Tool costs for a test month, if bought | AdSpy $149; Foreplay $49; Minea $49; PiPiADS $49; Winning Hunter from $30 billed yearly; AdLibrary.io $29 | VERIFIED (vendor pricing pages, 2026-11-21) | section 3 |
| Free validation stack | Meta Ad Library, Amazon listing counts, Google Trends, DataForSEO | n/a | section 3 |
| Product cost, shipping cost, delivery days, return terms for any fast-lane product | not available | UNKNOWN | needs a supplier quote; blocks G5 |
| Refund rate | 5% and 10% scenarios | ASSUMED | CLAUDE.md section 4 |

---

## 10. Things in the repo this research suggests updating (not changed by me)

1. `data/channel_params.json`, Meta cost per purchase values. They were taken from search snippets on Nov 14 because the page was blocked. The page is readable with the headless browser and was updated Nov 18, 2026. New medians: all $39.73 (stored 38.99), Pets $39.23 (38.51), Home and Garden $48.61 (47.93), Electronics $51.06 (51.86), Sports and Outdoors $45.30 (44.53), Toys $34.63 (34.85), Beauty $40.44 (39.31). The window is now Nov 2025 to Oct 2026, 41,000+ brands.
2. `data/channel_params.json`, `tiktok_ads_cpa_pets_usd = 5.46`. The same source table shows a Pets AOV of $0.38 and ROAS of 0.02. Treat as UNKNOWN. Any score that used $5.46 as a pets acquisition cost on TikTok is too optimistic.
3. The Foreplay MCP now returns "No active subscription for this user" (HTTP 402), not just "out of credits". CLAUDE.md section 6 lists it as the first tool for competitor ads; the fallback (Meta Ad Library, Meta Ads connector) is the working route.

---

## 11. Biggest unknowns

1. The true success rate of new dropshipping stores. No primary data exists in public.
2. Cost per purchase and conversion rate for a brand-new one-product store on cold Meta traffic in late 2026. Only established-brand medians exist.
3. How many product tests a beginner needs per winner. Creators imply 2 to 4; blogs say 5 to 15; nobody shows data.
4. Whether AI-generated static ads alone can carry a profitable cold test for a product in an allowed category.
5. Refund and chargeback rates by delivery speed.
6. The daily spending limit and review risk on Dhruv's own new ad account.
7. The real unit cost, shipping cost and delivery time of any candidate from a US-stock source. Without it no script can say whether an order is profitable after ads.
8. Current TikTok Shop rules for a new US seller (shipping, probation caps, settlement timing): third-party sources conflict; Seller Center is the only authority.
9. Whether oneisall or others hold design patents on common dog-dryer shapes, and the status of the ONEISALL trademark filings.
10. The current status of the FTC's proposed rule on money-making opportunities.
11. Month-to-month prices for Winning Hunter, Kalodata and FastMoss (pages unreadable or failing today).

---

## 12. Sources that blocked or failed

- Reddit: HTTP 403 by request and "blocked by network security" in the headless browser. No practitioner threads read.
- WordStream Facebook benchmarks 2026: HTTP 403.
- Triple Whale pages: HTTP 403 to WebFetch; read in full with the headless browser.
- Kalodata pricing: "Page loading failed". FastMoss pricing: client-side application error.
- Meta Ad Library web search: the page opened without login but showed no results in the headless browser (first request returned HTTP 403).
- transparency.meta.com parent page for intellectual property: HTTP 404; the child policy page was read.
- Meta's live help page for the customer feedback score: not found; 2018 newsroom post used.
- Foreplay MCP: HTTP 402, "No active subscription for this user". One call made.
- FTC complaint PDF and the RAND working paper PDF: unreadable through WebFetch; text extracted locally with `pdftotext`.
- Winning Hunter pricing toggle (monthly against yearly): not operable in the headless browser.
- Jungle Scout's 2025 State of the Amazon Seller page: does not show profitability or start-up cost questions; the 2024 survey was used.
- The Globe and Mail study of Shopify store survival: original not found.
- motionapp.com now redirects to runneth.com.
- Amazon Movers and Shakers: only the page title and header rendered.
- Not attempted by rule: anything behind a login or signup.

---

## 13. Source list (all accessed 2026-11-21)

Primary and read directly:
- https://www.shopify.com/entrepreneur
- https://www.shopify.com/blog/is-dropshipping-worth-it
- https://help.shopify.com/en/manual/compliance/intellectual-property/copyright-policy
- https://help.shopify.com/en/manual/payments/shopify-payments/reserves
- https://help.shopify.com/en/manual/finance/shopify-balance/payouts/payout-accounts
- https://conference.nber.org/conf_papers/f203218/f203218.pdf (RAND working paper)
- https://www.bls.gov/opub/ted/2024/34-7-percent-of-business-establishments-born-in-2013-were-still-operating-in-2023.htm
- https://www.facebook.com/business/help/112167992830700
- https://transparency.meta.com/policies/ad-standards/intellectual-property-infringement/third-party-infringement/
- https://about.fb.com/news/2018/06/improving-customer-service/
- https://about.fb.com/news/2025/02/gen-ai-transparency-metas-ads-products/
- https://about.fb.com/news/2026/01/2026-ai-drives-performance.md
- https://www.copyright.gov/help/faq/faq-protect.html
- https://support.google.com/trends/answer/4365533
- https://www.ftc.gov/news-events/news/press-releases/2023/08/ftc-action-stops-business-opportunity-scheme-promised-its-ai-boosted-tools-would-power-high-earnings
- https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes
- https://www.ftc.gov/system/files/ftc_gov/pdf/2423027ecommercebuilderscomplaint.pdf
- https://www.ftc.gov/legal-library/browse/cases-proceedings/ecommerce-empire-builders
- https://www.ftc.gov/legal-library/browse/cases-proceedings/ascend-ecom
- https://www.ftc.gov/news-events/news/press-releases/2025/03/ftc-acts-stop-click-profit-online-business-opportunity-has-cost-consumers-least-14-million
- https://www.ftc.gov/legal-library/browse/cases-proceedings/click-profit-llc
- https://www.ftc.gov/news-events/news/press-releases/2026/01/ftc-secures-settlement-banning-growth-cave-defendants-marketing-selling-business-opportunities
- https://www.ftc.gov/news-events/news/press-releases/2026/03/air-ai-its-owners-will-be-banned-marketing-business-opportunities-settle-ftc-charges-company-misled
- https://www.ftc.gov/industry/franchises-business-opportunities-and-investments
- https://www.ftc.gov/news-events/data-visualizations/data-spotlight/2026/04/reported-losses-scams-social-media-eight-times-higher-2020

Vendor data read directly:
- https://www.triplewhale.com/blog/facebook-ads-benchmarks
- https://www.triplewhale.com/blog/tiktok-benchmarks
- https://www.triplewhale.com/blog/tiktok-cpm
- https://www.triplewhale.com/blog/facebook-ads-bfcm
- https://runneth.com/library/research/creative-benchmarks-2026 and its pages `testing-volume-by-tier`, `portfolio-breakdown-by-tier`, `top-visual-formats`, `top-asset-types`
- https://supermetrics.com/ebook/black-friday-retail-playbook
- https://mhigrowthengine.com/blog/meta-ads-video-vs-image-benchmarks-2026/
- https://themediabuyer.northbeam.io/p/h1-2026-meta-cvrs-are-tanking-as-cacs-skyrocket
- https://www.marketplacepulse.com/articles/on-tiktok-shop-1-of-sellers-drive-60-of-gmv
- https://storeleads.app/reports/shopify
- https://www.junglescout.com/resources/articles/how-much-do-amazon-sellers-make/
- https://www.junglescout.com/resources/reports/amazon-seller-report-2025/
- https://printify.com/blog/print-on-demand-statistics/
- https://www.dropship.io/blog/dropshipping-success-rate
- https://www.sixpixels.com/articles/archives/shopify-a-tale-of-two-cities/
- Pricing pages: https://winninghunter.com/pricing , https://www.minea.com/pricing , https://www.pipiads.com/pricing , https://adspy.com/ , https://www.foreplay.co/pricing
- DataForSEO: Amazon products for "dog hair dryer" (US) and Google Ads search volume for 13 keywords (US)

Secondary, read as search summaries (ESTIMATED): the URLs given inline in each row.
