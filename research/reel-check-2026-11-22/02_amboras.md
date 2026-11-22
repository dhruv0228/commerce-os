# Reel check 2026-11-22, topic 02: the Amboras tool

Researched 2026-11-22. Public pages only. Nothing was signed up for, logged into, bought or sent.

Labels used here:
- VERIFIED: I read it on a primary page today (Amboras's own site, Y Combinator's directory, Trustpilot's profile page).
- ESTIMATED: third-party or self-reported, with link. A vendor's own marketing number is ESTIMATED even when I read it on the vendor's page. In those cases I write "VERIFIED wording" for the fact that the page says it.
- ASSUMED: my own reading or inference.
- UNKNOWN: not found. I say what I tried.

Quotes are copied from the pages. Long dashes inside quotes were replaced with commas or hyphens.

## Short answer

- Amboras is a real, young company. It is a Y Combinator Spring 2026 startup that hosts stores on its own platform. It is not a Shopify app.
- The reel's testimonial matches a paid, scripted creator campaign. Several other reels use the same lines. There is no independent, measured evidence for the conversion claims.
- Three of the four checks that made us leave Amboras now have an answer on Amboras's own pages (pixel and Conversions API, order routing, export). None was tested. The fourth (API access for an AI agent) is still not documented, and the terms forbid automated access without written consent.
- Amboras's own pages contradict each other in several places (plan names, refunds, fees wording, Stripe setup). A third-party review says there is a 1% fee per sale. Amboras's FAQ says there is none.
- For our store, Amboras would add built-in A/B testing, bundles and reviews. It would take away Shopify's supplier apps, TikTok Shop sync, a documented Admin API and a long track record. The Nov 18 switch to Shopify Basic still looks right on today's evidence. That is a recommendation for Dhruv, not a decision.

## What the repo already said (grep for "Amboras", 27 files)

- `reports/decisions.md` line 10: Amboras chosen on 2026-11-13, pay at Gate 6 after four checks. Pricing came from an ecomm.design review, marked unverified.
- `reports/decisions.md` lines 49 and 52: switched to Shopify Basic on 2026-11-18 because the four checks were never confirmed. Dhruv's condition: the store must convert as well as Amboras would.
- `research/platform-winners-2026-11-15/platforms.json`: "Amboras is not Shopify". One-click Shopify supplier apps do not work with it.
- `data/channel_params.json` and several research files used "Amboras 1% platform fee". That number came from the third-party review, not from Amboras.
- `research/business-models-2026-11-14.json` already noted: amboras.com/pricing "shows plan prices, no transaction-fee %".

## 1. What Amboras is

| Fact | Label | Source |
|---|---|---|
| Legal name Amboras, Inc., "a Delaware C Corporation", "with offices at 1111B S Governors Ave, STE 84587, Dover, DE 19904". Terms "Last updated: July 2026". | VERIFIED | https://www.amboras.com/terms |
| Y Combinator directory: tagline "AI Native Shopify", batch Spring 2026, founded 2025, team size 3, San Francisco, status Active, primary partner Aaron Epstein. | VERIFIED | https://www.ycombinator.com/companies/amboras |
| Founders: Imad Mokadem (CEO) and Amin Mokadem (CTO), brothers, both ETH Zurich per their YC bios. | VERIFIED | https://www.ycombinator.com/companies/amboras and https://www.amboras.com/team |
| Team page lists 15 named people, including a "Go-to-Market" person who "Focuses on creator partnerships and user-generated content". | VERIFIED | https://www.amboras.com/team |
| Founders say they grew an educational board game brand to "$200K/month" and that an earlier product, EcomCoder ("a Shopify dev tool"), "grew to over 1,000 users". | ESTIMATED (self-reported) | https://www.ycombinator.com/launches/QRm-amboras-your-self-improving-online-store |
| Amboras looks like a rename of EcomCoder. The site footer's LinkedIn link goes to linkedin.com/company/ecomcoder. A YouTube channel named "Ecomcoder AI" posted "Amboras (YC P26) Launch Video". | VERIFIED (footer link); ASSUMED (rename) | https://www.amboras.com/ |
| A Whop community page "Amboras Inc." shows "Frankfurt am Main, DE", "Created by" Amin, "904 joined", no posts. Its purpose is not stated. | VERIFIED | https://whop.com/amboras-inc/ |
| It hosts the store itself. "Amboras hosts the storefront and backend." FAQ: "It hosts your storefront, runs your products and orders, processes payments, sends transactional and marketing emails". | VERIFIED | https://amboras.com/what-is-amboras and https://www.amboras.com/faq |
| It does not sit on top of Shopify. It imports from Shopify, WooCommerce, BigCommerce, Magento and Squarespace. | VERIFIED | https://www.amboras.com/faq |
| Stack named on its own pages: Medusa (commerce engine), Stripe Connect (payments), Supabase (auth and database), AWS (hosting). "the storefront is exportable as a Next.js project". | VERIFIED | https://www.amboras.com/bundles , https://www.amboras.com/subscriptions , https://www.amboras.com/security , https://www.amboras.com/faq |
| How a store is built: "Type one sentence describing what you sell. Amboras names the brand, generates three products with photo-real images and copy, applies branding, sets up promotions, and gives you a live storefront URL, usually inside two minutes." | VERIFIED wording | https://www.amboras.com/faq |
| "A polished, ready-to-sell store with your own domain, products, and brand is usually live the same day." | VERIFIED wording; ESTIMATED as a fact | https://www.amboras.com/faq |
| "AI co-founder": the homepage says "Your store, one cofounder." and "Your personal Ecom agent". | VERIFIED | https://www.amboras.com/ |
| "Optimize for conversion" button: not described on any public Amboras page I read. It appears only in creator videos. | UNKNOWN | Pages listed in the sitemap, https://www.amboras.com/sitemap.xml |
| Homepage stats: "Stores built 100K", "To first sale <7 days". No method. No count of live or paying stores. | ESTIMATED (self-reported) | https://www.amboras.com/ |
| AI models: "A mix of frontier models including Anthropic Claude and OpenAI GPT". Terms name Anthropic as an AI subprocessor. | VERIFIED | https://www.amboras.com/faq and https://www.amboras.com/terms |

Note for our house rules. The default build "generates three products with photo-real images". Our rule is that hero and ad images use photos of the real sample. AI product images would have to be replaced.

## 2. Pricing, fees and payments today

| Fact | Label | Source |
|---|---|---|
| Basic: $49 monthly, or $39 per month billed yearly. 1 store, 1 seat, 1 domain. "Generates 2 complete themes". | VERIFIED | https://www.amboras.com/pricing |
| Pro: $105 monthly, or $84 per month billed yearly. 5 stores, 10 seats, 5 domains. | VERIFIED | https://www.amboras.com/pricing |
| Advanced: $299 monthly, or $239 per month billed yearly. Plus: "from $2,499/mo". | VERIFIED | https://www.amboras.com/pricing |
| Every plan lists "AI A/B/n testing", "Advanced analytics", "Email campaigns and flows", "Multi-currency and automatic tax". | VERIFIED | https://www.amboras.com/pricing |
| Building uses "store editing tokens". Basic's allowance is described only as about 2 complete themes. "AI agent usage is unlimited and does not use store editing tokens." | VERIFIED | https://www.amboras.com/pricing |
| Free tier: "You can build a complete store on the free tier, no credit card. Pay only when you decide to publish on a custom domain or unlock paid features." | VERIFIED wording | https://www.amboras.com/faq |
| "30-day launch guarantee on Basic, Pro & Advanced". The page does not say what the guarantee covers. | VERIFIED wording; terms UNKNOWN | https://www.amboras.com/pricing |
| Transaction fee, Amboras's version: "Are there any transaction fees? No. Amboras never charges a transaction fee on top of payment processing." | VERIFIED wording | https://www.amboras.com/faq |
| Checkout page: "We take a flat platform fee, never a cut of each sale." | VERIFIED wording | https://www.amboras.com/checkout |
| Transaction fee, third-party version: "Amboras charges a platform fee of 1% on Basic and Pro, or 0.5% on Advanced", plus card processing. Published October 28, 2026. | ESTIMATED | https://ecomm.design/amboras-ai-alternatives/ |
| The two versions conflict. The pricing page shows no fee line. The true per-sale fee is not settled. | UNKNOWN | Above |
| Card processing: "Processing fees are pass-through, typically 2.9% + 30¢ for cards in the US". | VERIFIED wording | https://www.amboras.com/faq |
| Payments run on Stripe Connect. "your money lands in your own bank account", "on a daily payout schedule by default. Amboras never holds your funds." | VERIFIED wording | https://www.amboras.com/faq |
| Payment methods claimed: cards, Apple Pay, Google Pay, PayPal, Klarna, Affirm, AfterPay and more, "over 125 methods globally". | VERIFIED wording | https://www.amboras.com/faq |
| Terms: "Amboras is not a payment processor" and "is not responsible for payment processing, payouts, reserves, holds, account suspensions, chargebacks, refunds, or fees imposed by any payment provider". | VERIFIED | https://www.amboras.com/terms |
| Terms: "We may modify pricing and plan features on 30 days' notice". A free plan can be changed or ended "at any time". | VERIFIED | https://www.amboras.com/terms |
| Third-party review says the free tier is a 14-day trial with 200 AI credits per month and that AI actions pause when credits run out. | ESTIMATED | https://ecomm.design/amboras-ai-alternatives/ |

Input for `scripts/economics.py` if Amboras is ever modeled again. If the FAQ is right, `payment_pct` is 0.029 with $0.30 per order, the same as Shopify Payments. If the third-party review is right, add 0.01. Do not rely on either until Amboras confirms in writing.

## 3. The funding claim: "backed by the same investors as OpenAI and SpaceX"

What Amboras itself says:
- "Backed by Y Combinator, A*, and operator angels." VERIFIED wording. https://www.amboras.com/backed
- Nine names under "Our investors": Y Combinator, A*, Cherry Ventures, Liquid 2 Ventures, Twenty Two Ventures, RTP Global, Spot VC, Robinhood Ventures, Founders Capital Nominees. VERIFIED that the page lists them. That each one invested is ESTIMATED (self-reported). https://www.amboras.com/backed
- Under Y Combinator: "Backed Airbnb, Stripe, DoorDash, Coinbase, and OpenAI." Under A*: "Backed Airbnb, DoorDash, Notion, Ramp, SpaceX, and Square." Under Robinhood Ventures: "Invested through Fund I in private companies including Canva and SpaceX." VERIFIED wording.
- About page: "Backed by the firm behind Airbnb, Stripe, and OpenAI. Y Combinator accepted us into the Spring 2026 batch." VERIFIED wording. https://www.amboras.com/about
- No amount raised, round name or date appears on the Amboras site. UNKNOWN.

What outside sources say:
- Y Combinator lists Amboras in its own directory. VERIFIED. https://www.ycombinator.com/companies/amboras
- Aggregators list a pre-seed of $500k in June 2026 with Y Combinator. ESTIMATED, low quality. https://fundediq.co/amboras-amboras-com-funding/ and https://www.vcbacked.co/company/amboras
- Y Combinator and OpenAI: OpenAI was seeded by YC Research in 2016. A May 2026 report put YC's stake at about 0.6%, from one unnamed source. ESTIMATED. https://daringfireball.net/2026/05/y_combinators_stake_in_openai . YC's company directory has no OpenAI page at /companies/openai (HTTP 404 today).
- A* and SpaceX: third-party databases list SpaceX among A*'s holdings, and co-founder Kevin Hartz is described as an early SpaceX investor. ESTIMATED. https://techcrunch.com/2024/06/21/kevin-hartzs-a-raises-its-second-oversubscribed-fund-in-three-years
- Robinhood Ventures Fund I: its Q2 2026 update is reported to list holdings in OpenAI and SpaceX. ESTIMATED (search summary of Robinhood's PDF, not opened by me). https://cdn.robinhood.com/app_assets/rhv/updates/rvi_q2_2026_update.pdf
- No press release, SEC filing or investor page was found that confirms A*, Cherry, RTP Global or Robinhood Ventures invested in Amboras. UNKNOWN.

Verdict: loosely true. Some of the backers Amboras lists also hold or held stakes in OpenAI or SpaceX. Only the Y Combinator link to Amboras is confirmed by a second primary source. The claim says nothing about whether the product works. Accelerators and funds back many companies, and most startups do not last.

## 4. The product claims in the reel

| Reel claim | What Amboras itself says | Independent, measured evidence |
|---|---|---|
| Paste a URL, press "optimize for conversion", get a store in 20 minutes | Migration from Shopify is supported. "A starter store is live in under two minutes." No "optimize for conversion" button on public pages. (VERIFIED wording, FAQ) | None found. |
| It "researched the largest brands in my niche" and made a store "better than theirs" | Not claimed on amboras.com. The "Amboras Academy" YouTube channel has videos titled "I Copied a Brand That Makes $300M/Year With Claude Opus 5.5" and "The Art of Cheating In Ecommerce". (VERIFIED titles via YouTube search) | None found. "Better" is not measured anywhere. |
| It "extracted the A/B tests they were running" | Not claimed on any Amboras page I read. | None. ASSUMED: an outsider can see page variants a competitor serves. An outsider cannot see the competitor's test results or winners. |
| It runs A/B tests for you | Yes. "Agents set up variants and split traffic; you review the results and promote the winner." Pricing lists "AI A/B/n testing" on every plan. (VERIFIED wording) | None found. |
| Bundles "are gonna rip" | Six bundle components. "Median bundle take rate 31%". No method. (VERIFIED wording, ESTIMATED number) | None found. |
| "Look at the difference in my conversion rate" | See below. | None found. |

Amboras's own numbers, all without method, named merchants or sample sizes:
- YC launch post: "early merchants are already seeing over 80% CVR lift on the first version Amboras puts live." Same post: "Our A/B testing engine is in beta." ESTIMATED. https://www.ycombinator.com/launches/QRm-amboras-your-self-improving-online-store
- A/B page: "3.2 days, vs. 14 days for fixed-horizon tests", "38% of variants beat control by ≥ 95% confidence", "< 5% across 4,200 shipped experiments". ESTIMATED. https://www.amboras.com/ab-testing
- Changelog, May 14: "A/B testing for storefronts. First pass of native experiments." VERIFIED wording. https://www.amboras.com/changelog
- Changelog, May 24: "the new checkout lifts paid conversion by roughly 20%". ESTIMATED. Same page.
- Reviews page: "Median conversion lift in 4 weeks 31%". ESTIMATED. https://www.amboras.com/reviews
- No case study with a named merchant and numbers was found on amboras.com. VERIFIED absence on the pages in the sitemap that I read.

Amboras's own terms, section 5.5: "We do not guarantee that ... A/B testing, optimization, or any other feature will improve, or will not temporarily or permanently reduce, your conversion rate, traffic, search ranking, deliverability, sales, revenue, or any other business metric". VERIFIED. https://www.amboras.com/terms

Terms, section 5: autonomous features "may act on prices, promotions, product copy, SEO metadata, and email campaigns" and "All changes made by Autonomous Features are deemed made by you". VERIFIED. This matters for our rule that Dhruv approves every price change.

ASSUMED, about our own case. A split test needs enough orders per variant to reach a decision. Our first test is sized for about 10 customers. That is far too few for any A/B tool to pick a winner, on Amboras or on Shopify. Any sample-size number must come from a script, not from prose.

### Independent reviews and reviewer incentives

- Trustpilot: a profile for www.amboras.com exists. It is unclaimed and has 0 reviews. VERIFIED. https://www.trustpilot.com/review/amboras.com
- G2, Capterra, Product Hunt: a Google search limited to those sites returned no Amboras review page. UNKNOWN beyond that.
- YouTube search for "Amboras review": the top results are Amboras's own channels ("Amboras AI", "Amboras Academy", "Ecomcoder AI") and one tutorial with a signup link. No independent tested review was found. VERIFIED search result via DataForSEO.
- ecomm.design, "Best Amboras AI Alternatives for 2026", October 28, 2026. Critical of Amboras. It does not say the author tested Amboras hands-on. It recommends Shopify and routes product links through its own /go/ paths, with no stated affiliate disclosure. ESTIMATED. https://ecomm.design/amboras-ai-alternatives/
- yctierlist.com reportedly rates Amboras "C" and calls the space crowded. ESTIMATED (search summary only). https://yctierlist.com/s26/amboras/
- Reddit: threads exist but Reddit blocked this session (HTTP 403 and a "blocked by network security" page). Google snippets only, so ESTIMATED:
  - r/dropshipping, about August 21, 2026, "Does anyone have experience with Amboras?": "I've seen alot of videos pass by if Amboras, I'm currently on the free trial but it's shit. But it also only uses the worst possible model."
  - "Amboras in 2026, Is It Actually Usable Now?": "Are they improving? Is it actually usable?"
  - "Shopify or Amboras?" in r/dropshipping, and "Shopify vs Amboras, which is better for a 40 product store".
  - Replies were not read. Their content is UNKNOWN.

Evidence that creators are paid and scripted (all ESTIMATED from Google snippets unless marked):
- Reddit post title: "Hiring UGC Creators, Amboras Campaign (Large Budget ...)". Snippet: "I provide full scripts, hooks, and formats, you just post."
- r/UGClickHub post "Hiring creators for Amboras". Snippet: "Pay starts at $1200/mo plus bonuses".
- A creator's own post: "amboras doesn't post jobs, they send me scripts and pay per view".
- The hashtag #amboraspartner appears on several Instagram reels and YouTube shorts.
- Amboras's team page lists a person who "Focuses on creator partnerships and user-generated content". VERIFIED. https://www.amboras.com/team
- Other reels repeat this reel's lines. Snippets include: "I dropped Shopify URL into this AI co-founder and checked Optimize for conversion in 20 ...", "comment 'store' before Black Friday to receive access", "How I Sold My E-Commerce Business for $50M in 26 Days", "$50M deal at 22??", "made 41k then found the thing everyone's gatekeeping", and "1.1% on Shopify vs 2.7% on Amboras (+145.5%)".
- Whether the specific reel from the handle "masondoesecom" was paid is UNKNOWN. I did not view the reel. The pattern above fits a paid script. Paid endorsements must be disclosed under the FTC Endorsement Guides. Whether this one was disclosed is UNKNOWN.

Reading: the testimonial voice in the reel is advertising copy, not a customer result. That is a description of the evidence, not an accusation against any person.

## 5. The four checks

| Check | What Amboras's own pages say today | Status |
|---|---|---|
| (a) Meta pixel and Conversions API | Integrations page, tagged Built-in: "Meta Pixel + Conversions API, full-funnel ad attribution with server-side dedup and Advanced Matching for the highest possible EMQ." Changelog, Apr 28: "Meta Pixel + Conversions API. Server-side Purchase events with phone-level matching". Terms 6.6 name "the Meta Pixel, Meta Conversions API". | VERIFIED that Amboras documents it. Not tested. Which events fire (ViewContent, AddToCart, InitiateCheckout, Purchase) and dedup quality are UNKNOWN until seen in Meta Events Manager. |
| (b) Routing orders to a supplier | Built-in: "AliExpress Dropshipping: Source products from AliExpress and forward orders for fulfillment. You must pay each forwarded order in AliExpress before the supplier ships it." Built-in: Printful, Printify, ShipStation, ShipBob, Shippo. Built-in "Workflow Automation: Trigger replyable emails, order tags, CSV exports, and live Google Sheets rows when orders are placed." FAQ: "Custom 3PLs can be wired in via webhook." | Partly VERIFIED. An order-triggered email, CSV or Google Sheets row would be enough to forward orders by hand or by our own script. No public spec for the webhook or any order API. CJdropshipping: the changelog (Apr 25) says "CJ Dropshipping, phase 2", but CJdropshipping is not in today's integration list. UNKNOWN. |
| (c) Data export | FAQ: "Can I export my data? Yes. Products, customers, orders, content, and assets all exportable as CSV, JSON, or as a complete archive." FAQ: "the storefront is exportable as a Next.js project." Terms 12.4: after termination "we will retain your account data for 90 days, during which you may request an export". | VERIFIED that Amboras states it. Not tested. The third-party review says Amboras "has no documented bulk export tool for leaving" (ESTIMATED). |
| (d) API access for an AI agent | No developer documentation found. docs.amboras.com, developers.amboras.com, help.amboras.com, api.amboras.com, /docs, /developers, /api and /mcp all returned HTTP 404 today. The sitemap lists no docs. Terms 3.2(h): you agree not to "access or monitor the Services using any robot, spider, scraper, or other automated means without our prior written consent". | NOT confirmed. UNKNOWN whether any merchant API exists. Automated access needs written consent. This check still fails. |

Sources for the table: https://www.amboras.com/apps-and-integrations (rendered in a headless browser), https://www.amboras.com/changelog , https://www.amboras.com/faq , https://www.amboras.com/terms , https://www.amboras.com/sitemap.xml .

## 6. Integrations that matter to us

About the integrations page. Its header says "Every integration below is already built into Amboras" and shows "All 420". Only 58 entries carry the tag "Built-in". The rest have no tag, and several read like Shopify app descriptions (for example Postscript: "SMS marketing platform built exclusively for Shopify"). The cards do not open a detail page. I treat only the 58 tagged entries as claimed-available. VERIFIED counts from the rendered page.

| Item | Finding | Label |
|---|---|---|
| Meta pixel and Conversions API | Built-in (see check a). Also "Facebook & Instagram Shop" catalog sync, Built-in. | VERIFIED wording |
| TikTok pixel | "Tiktok Ads", Built-in: "TikTok Pixel + Conversions API for accurate, ad-blocker-resistant conversion tracking." | VERIFIED wording |
| TikTok Shop sync | Listed under Sales Channels with no Built-in tag. | UNKNOWN |
| Google | Google Analytics 4, Google Ads Pixel, Google Shopping Feed, Google Merchant Center: all Built-in. | VERIFIED wording |
| Payments | Stripe Connect under the hood. PayPal, Klarna, Affirm, AfterPay named as methods. Shop Pay is not mentioned. Shopify Payments does not apply. | VERIFIED wording (FAQ) |
| Checkout ownership | Hosted by Amboras. Your own Stripe account. "colors, logo, fields, language, and the order-summary layout" are editable. | VERIFIED wording |
| Print on demand | Printful and Printify, Built-in. | VERIFIED wording |
| CJdropshipping | Not in today's list. Only a changelog line from Apr 25. | UNKNOWN |
| Zendrop, DSers, AutoDS, Spocket, Syncee | Not in the list at all. | VERIFIED absence |
| AliExpress | Built-in, pay each forwarded order in AliExpress. Mostly China-direct, which fails our 2 to 8 day rule. | VERIFIED wording; ASSUMED on fit |
| US-stock supplier that is not one of the above | Only by email, CSV, Google Sheets row or a webhook that has no public spec. | VERIFIED wording; details UNKNOWN |
| Subscriptions | "Native subscriptions ship with flexible billing intervals, dunning, and customer self-service portals". | VERIFIED wording |
| Reviews | Native reviews with photo and video, plus a "Fake-review filter". Trustpilot widget, Built-in. | VERIFIED wording |
| Email | Native campaigns and flows. Klaviyo, Omnisend and Mailchimp, Built-in. | VERIFIED wording |
| Bundles and upsells | Native. "Fixed bundles, mix-and-match bundles, and BOGO promotions". One-click thank-you upsell claimed. | VERIFIED wording |
| Custom domain | Connect your own or buy one. Needs a paid plan to publish on it. | VERIFIED wording |
| Zapier and Make | Listed with no Built-in tag. | UNKNOWN |
| Export and migration off | See check (c). Moving off Amboras is not described anywhere on the site. | UNKNOWN |

## 7. Complaints and risks

Complaints found:
- Trustpilot has 0 reviews, so no complaint record exists there. VERIFIED.
- Reddit shows doubt about quality on the free trial (snippets above). ESTIMATED. Threads not read.
- No reports of payout holds, account closures or outages were found. That is absence of evidence from a thin record, not evidence of a clean record. UNKNOWN.

Risks from Amboras's own documents (all VERIFIED on https://www.amboras.com/terms unless noted):
- Young vendor. Founded 2025 per Y Combinator. If the company stops, the store goes offline. Data is kept 90 days after termination.
- No uptime promise. "Amboras does not commit to any uptime level, service level, or support response time".
- Status page. The FAQ says "Status, RPO, and RTO are published on status.amboras.com". That address returned HTTP 404 today. VERIFIED 404 from this environment.
- Suspension. Amboras may "take your storefront offline, immediately" if the store "poses a legal, security, fraud, or reputational risk". It may also "terminate for convenience on 30 days' notice".
- Liability cap: the greater of fees paid in the prior 12 months or $100. No liability for "reduced conversion or sales" from AI output or autonomous features.
- Refunds conflict. FAQ: "Unused days on annual plans are refunded prorated." Terms: "all fees are non-refundable" and no refund "for any unused portion of your subscription". The terms would govern.
- Plan names conflict. The FAQ lists "Starter", "Studio", "Team" and "Plus". The pricing page lists Basic, Pro, Advanced and Plus. The FAQ says annual billing "saves about two months". The pricing page says "Save 20%".
- Stripe setup conflict. FAQ: "You never set up Stripe yourself". Checkout page: "Connect Stripe" and "Stripe Connect OAuth".
- Security page lists "SOC 2 Type II", "ISO 27001", "PCI DSS" and "HIPAA Ready". No certificate, auditor or report link is shown. ESTIMATED (self-reported). https://www.amboras.com/security
- Public changelog. The newest entry on the page is dated Jun 1. No later entry is shown as of today. Other pages are newer (terms July 2026, a guide "Reviewed October 22, 2026"). VERIFIED.
- Payout holds. Any hold would come from Stripe, under an agreement between the merchant and Stripe. Amboras disclaims responsibility.
- Lock-in. The store runs on Amboras's stack. Export is claimed but untested. There is no documented API.
- Arbitration in Delaware with a class waiver. Opt-out is possible within 30 days of accepting the terms.
- Compliance risk from the marketing around it. Amboras's own Academy videos promote copying a named brand's store. Our rule (CLAUDE.md section 7) forbids copying competitors' branding, images, text, claims or designs.

## Comparison with Shopify Basic for our case

Our case: one product, US customers, a US-stock supplier that ships blind, Meta ads, a $1,800 budget and a first test of about 10 customers. Shopify figures below are the repo's own (CLAUDE.md section 0), still marked "verify at signup".

| Topic | Shopify Basic (repo figures) | Amboras Basic (today) |
|---|---|---|
| Monthly price | About $39, or $1 for the first 3 months | $49 monthly or $39 per month billed yearly. VERIFIED |
| Fee per sale | 2.9% + $0.30 with Shopify Payments, no extra fee | "typically 2.9% + 30¢" and "never charges a transaction fee" per its FAQ. A third party says 1% extra. UNKNOWN |
| Meta pixel and Conversions API | Yes | Claimed Built-in. Untested |
| Supplier apps for US stock | Many one-click apps | AliExpress, Printful, Printify and 3PLs only. Others by CSV, email or undocumented webhook |
| TikTok Shop sync | Apps exist | Not confirmed |
| A/B testing, bundles, upsells, reviews, email | Mostly paid apps or our own code | Included in the plan |
| API for an AI agent | Admin API (once Dhruv grants access) | None documented. Terms need written consent for automated access |
| Export | Standard exports | Claimed (CSV, JSON, archive, Next.js project). Untested |
| Track record and reviews | Long, public | Founded 2025. 0 Trustpilot reviews. Most online praise is paid creator content |
| Status page and uptime terms | Public | No uptime commitment. Stated status page not reachable today |

What Amboras would add:
- A store built by prompt in minutes, with native A/B/n testing, bundles, upsells, reviews, email and subscriptions in one price.
- Fewer app subscriptions. ASSUMED saving. No app cost was priced here.

What it would take away:
- One-click connection to US-stock suppliers. We would route orders by hand or by our own script.
- A documented API for Claude. This is Dhruv's software edge, and it is the one check that still fails.
- TikTok Shop sync (unconfirmed), Shop Pay, a public status page and a deep record of independent reviews.
- Certainty about fees and refunds, because Amboras's own pages disagree with each other.

What is still unknown:
- Whether Amboras stores convert better than Shopify stores. No independent measurement exists. Dhruv's condition ("must convert as well as Amboras would") cannot be benchmarked against any verified Amboras number.
- The real per-sale fee, the free-tier limits and what the "30-day launch guarantee" covers.
- Whether a merchant API or MCP exists, and whether Amboras would give written consent for an agent.
- Whether the CAPI events and order webhooks work as described.
- Payout timing and hold behavior for a brand-new Stripe Connect account on Amboras.

What we can take from it without switching (ASSUMED, for Dhruv to weigh):
- The useful ideas are bundles with tiered pricing, a one-click post-purchase upsell, native reviews and simple split tests of headline, offer and free-shipping threshold. All can be done on Shopify.
- With about 10 customers in the first test, no split test will reach a decision on any platform. Testing tools matter later, at Milestone 2 traffic levels.
- If Dhruv wants to revisit Amboras, the cheap path is to build on its free tier without a card and email its support four written questions: per-sale fee, merchant API and agent consent, order webhook spec, and export format. Signing up and emailing need his approval first (CLAUDE.md section 10).

## What I tried and could not access

- Reddit: search JSON returned HTTP 403. A headless browser got "You've been blocked by network security." WebSearch cannot query reddit.com. Thread content is from Google snippets via DataForSEO.
- SEC EDGAR full-text and company search for "Amboras" and "EcomCoder": HTTP 403 ("Undeclared Automated Tool"). No Form D could be checked. EDGAR asks for contact details in the User-Agent, which project rules do not allow me to send.
- Foreplay (to see Amboras's own ads): the connector returned "Insufficient credits". Not checked.
- Crunchbase and PitchBook: not opened. Funding amount is from low-quality aggregators only.
- The reel itself and the Instagram account were not viewed. Its content is as transcribed by the owner.
- a-star.co: the fetched HTML showed no portfolio text. A*'s investment in Amboras could not be confirmed there.
- Amboras's admin, free tier and integration settings: not opened, because that needs a signup.
- Meta Ad Library and TikTok Creative Center for Amboras ads: not checked.
- status.amboras.com, docs.amboras.com, developers.amboras.com, help.amboras.com: HTTP 404 from this environment.

## Source list

Amboras pages read today:
- https://www.amboras.com/
- https://amboras.com/what-is-amboras
- https://www.amboras.com/pricing
- https://www.amboras.com/faq
- https://www.amboras.com/terms
- https://www.amboras.com/backed
- https://www.amboras.com/about
- https://www.amboras.com/team
- https://www.amboras.com/apps-and-integrations
- https://www.amboras.com/ab-testing
- https://www.amboras.com/checkout
- https://www.amboras.com/bundles
- https://www.amboras.com/subscriptions
- https://www.amboras.com/upsells
- https://www.amboras.com/reviews
- https://www.amboras.com/analytics
- https://www.amboras.com/migrate
- https://www.amboras.com/security
- https://www.amboras.com/changelog
- https://www.amboras.com/guides/ecommerce-platform-checklist
- https://www.amboras.com/llms.txt
- https://www.amboras.com/sitemap.xml
- https://www.amboras.com/robots.txt

Other sources:
- https://www.ycombinator.com/companies/amboras
- https://www.ycombinator.com/launches/QRm-amboras-your-self-improving-online-store
- https://www.trustpilot.com/review/amboras.com
- https://ecomm.design/amboras-ai-alternatives/
- https://whop.com/amboras-inc/
- https://yctierlist.com/s26/amboras/
- https://fundediq.co/amboras-amboras-com-funding/
- https://www.vcbacked.co/company/amboras
- https://daringfireball.net/2026/05/y_combinators_stake_in_openai
- https://techcrunch.com/2024/06/21/kevin-hartzs-a-raises-its-second-oversubscribed-fund-in-three-years
- https://cdn.robinhood.com/app_assets/rhv/updates/rvi_q2_2026_update.pdf
- https://www.youtube.com/@Amboras and https://www.youtube.com/@AmborasAcademy (titles seen in YouTube search results)
- Google and YouTube search results through DataForSEO, 2026-11-22 (queries: "amboras site:reddit.com", "\"amboras\" review", "Amboras review" on YouTube, and three follow-ups)
