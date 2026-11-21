# 02. YouTube sweep: "agentic AI dropshipping" and the credible operators of 2026

Research date: 2026-11-21. Research only: nothing was bought, signed up for, logged into or contacted.

## 0. How to read this file

**Labels**

- VERIFIED: I read it today on the primary source. For a video that means the video's own transcript (auto captions) or description, pulled through DataForSEO's YouTube endpoints, or a web page I loaded today. For a creator statement, VERIFIED means "the creator said this in the video", not "this is true".
- ESTIMATED: a number about the real world that comes from a third party. Here that is mostly a creator's own self-reported sales or profit, given with the video link and publish date. None of these were independently checked.
- UNKNOWN: not found or not checkable.

**Limits of this sweep**

- I read transcripts, not the picture. When a creator says "as you can see on my screen", I could not see the screen. "Proof shown" below means "the creator says a dashboard is on screen"; whether the dashboard is real is UNKNOWN.
- Auto captions drop decimal points and misspell names (for example "$8577" for $85.77, "Team Drop" for TeemDrop, "Clod" for Claude). Where a number is ambiguous I say so.
- View counts and dates are VERIFIED as of 2026-11-21 (YouTube data via DataForSEO). Dates written "about N months ago" come from the search result only and are approximate.
- No margins, CAC, ROAS or profit were computed by me. Where a creator states one, it is quoted as their statement. Raw inputs for the repo scripts are in section 6.

**Method**

- 21 YouTube searches through `serp/youtube/organic/live/advanced` (US, English): 371 distinct videos, about 200 of them published in the last 6 months.
- Subtitles and descriptions pulled for 28 videos (`serp/youtube/video_subtitles` and `video_info`). 15 core videos from 15 different creators are recorded in section 2, plus 13 supporting videos in section 3.
- DataForSEO cost reported by the API: $0.002 per search and $0.006 per subtitle or info call, about $0.38 in total.

**Sources that blocked or failed**

- Foreplay MCP: one call tried (`search_discovery_brands`, "Haven Golf"). Error 402, "Insufficient credits", remaining credits 0. Not used.
- `app.storebuild.ai/page/new-desk` returned an empty page to WebFetch (JavaScript only). Read with the headless browser instead.
- `zendrop.com/?p=4464` ("Special Offer From Austin Rabin" in search results) returned HTTP 404.
- Named operators with no recent video in the top 20 results of a search on their name: Sebastian Ghiorghiu, Chris Wane, Camille. They are not covered.
- TikTok's own seller policy pages were not reached; only third-party articles came up (see section 4.6).

---

## 1. Executive summary

1. **The video Dhruv watched sells a funnel, and the creator's real business is not run that way.** Austin Rabin's "Haven" is Haven Golf Company, a branded golf polo company that holds stock in its own North Carolina warehouse and ships in "about 2 to 3 days" (VERIFIED, his video `gXVbZLlcPYA`, Oct 29, 2026). The "agentic AI dropshipping" tutorial builds a different thing: a templated store with 10 pre-loaded Zendrop products. The tutorial never runs an ad, shows no sale, states no ad budget, no kill rule and no delivery time (VERIFIED, transcript of `lJtgRzCBePM`).
2. **His own disclosed month is thin.** For September 2026 he reports revenue $125,463.94, Facebook ad spend $68,886.10, cost of goods $28,868.40, and net profit $12,596.51, which he calls "just over a little bit of a 10% net profit margin" and "around a two ROAS, which is pretty low for us" (ESTIMATED, self-reported in `gXVbZLlcPYA`). That is an established brand with a warehouse, nine years of Facebook ads experience and repeat customers.
3. **The phrase "$100,000 before the end of the year if you start today" is not in the video transcript, the description, or the two StoreBuild pages I loaded** (VERIFIED absent today). Where it appears (a later funnel step, an email, a thumbnail) is UNKNOWN.
4. **Almost every video in this space is paid by the same four things**: a free "AI store builder" funnel (buildyourstore.ai with AutoDS, storebuild.ai with Zendrop), the Shopify $1 affiliate link, a supplier app, and an ad-spy tool. Jordan Welch says it out loud: "they are paying us for every single person we get to sign up" (VERIFIED, `9zh3Raq4FVc`). Of the 15 core videos, 13 carry affiliate links, a sponsor, the creator's own software, or a paid program. The two exceptions are Shopify's own channel and one agency owner who sells his agency.
5. **Transparent small-budget tests end near break-even in week 1.** With stated costs: +$52 in 24 hours on $57 of ads (Nazareth), "$54.01" after 7 days on $249.66 of ads by a sponsor-side expert (Tilbury video, caption ambiguous), +$217 on $510 of ads to the UK (Wold), a failed $250 test (Mohsin), a failed week on about $100 a day (Juodkunaitis), +$349.39 on about $776 of ads across two products (Ant). All ESTIMATED, self-reported. None reached $2,000 of week-1 sales on a total budget of $500 to $1,000 with every order profitable. The one that passed $2,000 of sales in a week (Persse, $3,239 by day 8) made about $85 profit on its first $1,000 day and ran $50 to $200 a day of ads.
6. **What credible creators agree on**: sell what already sells, check the margin before building, run one simple broad Meta sales campaign at $25 to $100 a day, judge after about 3 days, expect the first product or two to fail, raise order value with bundles, and track profit, not revenue.
7. **AI today is good at the build and the paperwork, not at the outcome.** It builds pages, writes copy, summarizes competitor ads, writes image prompts and makes product images fast. In the reference video itself Claude could not edit the theme's hero text, had not seen the rendered page, and could not add reviews (VERIFIED). No video shows an agent running ads to a profit on its own.
8. **Shipping time is mostly not mentioned.** In the "AI dropshipping" videos the delivery promise is usually skipped. The few who state it say 3 to 9, 5 to 9, 5 to 8 or 5 to 15 days, quoted from supplier apps and agents they are paid to recommend; where the stock sits is not stated. The only creator with a disclosed real P&L ships from US stock in 2 to 3 days and tells viewers to do the same.

---

## 2. Core videos (15 videos, 15 creators)

Format for each: link, views and date (VERIFIED) / method / numbers claimed and proof / money links.

### 2.1 Austin Rabin: "$4.2M With Agentic Ai Dropshipping Full Guide (Just Copy Me)"

- https://www.youtube.com/watch?v=lJtgRzCBePM , 13,065 views, Nov 11, 2026, 38 min. This is the video Dhruv described.
- **Method (VERIFIED)**: (1) storebuild.ai funnel creates a Shopify store ($1 a month for 3 months after a 3-day trial; needs a brand new Shopify email) with a Zendrop theme and 10 products. Zendrop is free for 0 to 10 products, then "up to $79 per 30 days". A one-time upsell is offered (12 months of Zendrop tools, "$200 in order credits"). (2) Claude Project "AI drop shipping manager" with two roles. (3) Ad research role uses the AdLibrary.io MCP to pull 3 to 5 static image ads from a named competitor (oneisall.com) and writes ChatGPT image prompts. (4) ChatGPT (free plan) makes the ad image from the supplier's product photo. (5) Store manager role audits the store, rewrites the product description, FAQ and SEO text through the Shopify connector after approval.
- **Product research, validation rule, test budget, kill and scale rules, fulfillment time**: none given (VERIFIED absent). The demo product (dog hair dryer) was simply one of the 10 pre-loaded items. Claude noted the reference competitor "is not running any dog dryer ads right now".
- **Creative claim**: "Static ads perform a lot better than video. They're three times on average cheaper" (VERIFIED said; no data given, so the claim itself is UNKNOWN).
- **AI limits shown in the video (VERIFIED)**: Claude "hasn't seen the rendered pages, fonts and colors, and mobile layout"; "we can't change the heading ... We have to do that manually. It doesn't have access to it"; reviews could not be added on a new store. His prompts tell Claude "Do not invent reviews" and not to change "shipping speeds, performance claims".
- **Numbers**: "$4.2 million in the last year and a half" for Haven (ESTIMATED, self-reported, no proof in the audio). No result from the demo store.
- **Money links (VERIFIED, description)**: app.storebuild.ai, storebuild.ai/austinrabin ("I am a partner with Shopify", said on camera), adlibrary.io/austin, go.zendrop.com/affiliate/austin-rabin-bfcm. Says "I don't have a course to sell" in a sister video, which also links a Launchpass Discord group (paid or free: UNKNOWN).
- **Related videos by the same creator (VERIFIED)**: "$3.9M with a.i. dropshipping (free method)" (`3fg_NwHN2vY`, 130,143 views, Aug 5, 2026), "$4.1M Shopify Ai Dropshipping Automation With Claude & Chatgpt" (`IlAbicMXo1I`, 48,844 views, Sep 2, 2026), "$125K in 30 days branded Shopify A.i. dropshipping" (`gXVbZLlcPYA`, 13,470 views, Oct 29, 2026). All four use the same store builder funnel. The last one contains the Haven P&L in section 6.1.

### 2.2 Mark Tilbury (with a guest "AI dropshipping expert"): "I Tried AI Dropshipping For 7 Days, Copy Every Step"

- https://www.youtube.com/watch?v=mUz_tHYLhUs , 641,338 views, Nov 3, 2026, 3 h 51 min. The most viewed AI dropshipping video of the last month.
- **Method (VERIFIED)**: rules were $300 total budget, 7 days, random niche (office). Product rules: sell under $80 ("customers are not going to dish out $200, $300 on a store that they don't really know"), 2 to 3 times markup, lightweight, safe. Built with buildyourstore.ai plus AutoDS. Chose a general "beginner store", not a one product store, "because if that one product flops" the test is over. Tilbury says the sample units came from Amazon with next day delivery so videos could be filmed, and that normally you should order the exact units you will sell. Self-filmed videos, two per product. Meta: three campaigns (one per product), $40 a day each, broad US, sales objective. After day 1 kept $40 a day on the product with sales and cut the other two to $7.30 a day each. Shipping policy written as "up to 10 business days"; "not have the customers wait 14 days or more".
- **Numbers (ESTIMATED, self-reported, read out on camera)**: revenue $855.75, 25 sales, product cost and shipping $472.84, transaction fees $28.90, ad spend $249.66, samples $48.35, software $1.99. Captions give the final profit as "$541" and total costs as "$81.74"; captions in this video drop decimals, so the profit figure is most likely $54.01, but treat it as UNKNOWN until read on screen or run through the scripts. The $1,000 profit target was missed. Day 1: 2 sales and a loss.
- **Money links (VERIFIED)**: buildyourstore.ai/lpco, autods.com/lctf, "Some of the links in this description are affiliate links that I get a commission from."

### 2.3 Baxter Persse: "I Tried AI Dropshipping for 7 Days (Realistic Results)"

- https://www.youtube.com/watch?v=8Oi5CWTfQFs , 262,476 views, Nov 13, 2026, 22 min.
- **Method (VERIFIED)**: two experienced people (his partner "made hundreds of thousands of dollars with drop shipping"). Product research by a burner Instagram account that only engages with product ads, and by TikTok Shop sales data tools. Product: a kids' art display frame (a children's product, excluded for Dhruv). Store from Build Your Store plus AutoDS. Images and 12 AI video ads in an hour from Higgsfield driven by Claude. Meta ads $50 a day, raised to $100, then $200. Price raised by $5, $10 and $15 on the 1, 2 and 3 packs mid-test.
- **Numbers (ESTIMATED, self-reported)**: first sales on day 1 or 2. Day 5: about $200 spent on ads, "down around $170 today". Day 7: $1,000 in sales, "we only made like $85 today ... That's why you never trust fake gurus who only show their revenue numbers." By day 8: $3,239 sales in 7 days. Day 10: over $1,300 sales, profit "over $180". Day 14: profit $482 for the day. Day 21: "just under $22,000 in sales". Total profit over the period is not stated (UNKNOWN). Fulfillment time not stated.
- **Money links (VERIFIED)**: "Build Your Store actually partnered with us on this video", "Higgsfield also partnered with us on this video", AutoDS link, free course on Whop. "We may earn a commission from affiliate links."

### 2.4 Jordan Welch: "Claude + Dropshipping = $12,784/Month"

- https://www.youtube.com/watch?v=9zh3Raq4FVc , 100,155 views, Sep 3, 2026, 14 min.
- **Method (VERIFIED)**: four product rules: recently trending and already selling, not available in stores, "over 25 or $30 in profit per order", a wow factor. TrendTrack filter: ads active, created in the last 30 days, "shop now" button, English, brands with 10 to 50 live ads ("less than 10 ... not doing anything", "more than 50 ... much harder for you to compete with"). TrendTrack MCP connected to Claude Cowork for a validation report. Then "clone our competitor's store" with the Clone Store app, which "pulled all the images from our competitor".
- **Numbers**: "$424 in sales on day one" (ESTIMATED, self-reported, revenue only). Example unit cost $2, sold in 2 and 4 packs with "$35" and "almost $40" profit per order (self-reported). The "$12,784/Month" in the title is not supported anywhere in the transcript (VERIFIED absent). No ad budget, kill rule or shipping time.
- **Money links (VERIFIED)**: course.aicom.co ("my $5,000 AI Course For FREE"), clone.store affiliate code, Shopify affiliate link, TrendTrack link. Said on camera: "I partnered with Shopify and a billion-dollar company called Base 44, and they are paying us for every single person we get to sign up."
- **Risk**: copying a competitor's images and page is the opposite of the repo's research rule (section 7 of CLAUDE.md).

### 2.5 AC Hampton: "How to Actually Start Shopify Dropshipping in 2026"

- https://www.youtube.com/watch?v=wDBcYlt_DZU , 299,002 views, Jun 25, 2026, 28 min. Supporting video by the same creator: "How to ACTUALLY Start Dropshipping with Claude AI in 2026 (FULL COURSE)", https://www.youtube.com/watch?v=PPde3fFttE0 , 47,224 views, Sep 5, 2026.
- **Method (VERIFIED)**: product check in AutoDS (TikTok top sellers over 7 to 30 days). "Four lights" in the Claude video: kills a pain, people already buying, sells year-round, the math works (example: source $12.70, sell about $42). Fulfillment through TeemDrop: "deliver in 3 to 9 days instead of the month-long waits". AI UGC videos from EcomBos. Meta: sales campaign, CBO, $25 to $50 a day, one ad set per angle, purchase event, broad, turn off multi-advertiser ads and enhancements, "10 to 15 creatives, three angles, and real data ... inside of the first week".
- **Benchmarks he states (VERIFIED said; ESTIMATED as facts)**: CTR 2.5% or higher, cost per click under $1, CPM $15 to $25, ROAS above 2.0; "below a 1.1 or 1.2 means that you're probably going to be losing money".
- **Kill and scale (VERIFIED said)**: turn off any ad "burning spend with a high cost per purchase and nothing to show for it"; do not scrap everything in a panic, "ads just need time and data". Scale after "two to three days of consistency below break even first, then double the budget ... at the start of the day", then move the best 3 to 4 ads into their own campaign. His Claude demo analyses an account where one creative "burned $600 and it never came back above break even" and another had "almost $700 spent and 64 sales", so the demo test spent well over $1,000.
- **Numbers**: "over $10 million" himself, students "over $50 million combined", a 14-year-old student "$60,000 in his first 3 months" (ESTIMATED, self-reported, no proof in the audio).
- **Money links (VERIFIED)**: Shopify affiliate, buildyourstore.ai, AutoDS, Tailor Brands, EcomBos (code ALEX), .store domains, Vitals, TeemDrop coupon link, 1-on-1 mentorship at supremeecom.com.

### 2.6 Nathan Nazareth: "I Started a Dropshipping Store in 24 Hours Using ONLY AI"

- https://www.youtube.com/watch?v=_dTKOXlvdZ8 , 65,932 views, Jun 29, 2026, 15 min.
- **Method (VERIFIED)**: rules: under $100 total, store built in under 60 minutes. Build Your Store plus AutoDS. Product picked with a ChatGPT research prompt (criteria: mass demand, impulse buyers, many angles; cross-check on TikTok and the Meta Ad Library). Product: neck and shoulder massager, AliExpress about $25, sold at $70, buy-two bundle. 14-day money-back guarantee. Page says 5 to 9 business days. AI UGC ads made with Arcads and edited by hand. Meta: broad, "leaving Meta's algorithm to do all the heavy lifting"; "Anyone who tries to sell you on some fancy or flashy ad strategy is completely capping".
- **Numbers (ESTIMATED, self-reported)**: 24 hours: revenue $188.98, 3 units, product plus shipping about $75, fees about $5, ads $57, total expenses $137, profit $52. First sale after $9 of spend.
- **His own caveats (VERIFIED)**: "this isn't exactly passive income"; "I just did a 7-day challenge and it went horribly"; "we're not going to make tens of thousands of dollars overnight".
- **Red flag (VERIFIED)**: the page carries "AI videos of testimonials from previous happy customers. And I know, these aren't real, of course". That is a fake testimonial under the FTC rule the repo already cites.
- **Money links (VERIFIED)**: buildyourstore.ai, his "Full Free Program", Shopify affiliate, AutoDS referral. Description: "Most people make little to no money."

### 2.7 Davie Fogarty: "I Helped a Complete Stranger Build an AI Ecom Store"

- https://www.youtube.com/watch?v=MxjwiA7cCpI , 214,572 views, Sep 29, 2026, 30 min. (His "$1M a month" video was already covered in `research/video-davie-2026-11-18/`; not repeated.)
- **Method (VERIFIED)**: ad-spy filters, then a "Google test": if the product is in Kmart or on Google Shopping "for half the price of what you can probably source it for, just don't bother". Shortlist of five products from AliExpress and Zendrop prices. "I have never been able to pick out of a batch of products which one's going to be the best ... let's launch all of the products." Images: Pinterest reference to Claude to a JSON style prompt to Higgsfield, then in-paint the real product; image ads laid out in Canva. Store pages built with Claude Code. Meta: broad, one campaign per product, all creatives in. First read: "how much does it cost to get an add to cart or a purchase".
- **On image ads (VERIFIED)**: "The creativity of your marketing when you're just using image ads needs to be really, really powerful ... which is much harder cuz you've got movement with the videos." And: "make sure it is what the actual supplier is going to send the person because the last thing we want to do is mislead customers."
- **What happened (ESTIMATED, self-reported)**: first product (anti-theft bag) "spent just under 100 bucks. It just wasn't converting", no add to carts. She then made 7 or 8 AI UGC video ads through the Higgsfield connector. "Tested a couple of products ... it just wasn't hitting the mark." Then a winner: launch at about $100 a day, raised to "just over $250 a day", $1,000 total sales and 23 orders by day 2, and "$42,159.88 in 8 days". Profit, the winning product and total spend before the winner are not stated (UNKNOWN). Timeline was "longer than we planned". One ad took nearly all the budget.
- **Effort (VERIFIED)**: "I've been at it for 14 hours" on build day; "it is quite technical"; "The Shopify theme is really doing my head in." The student already worked in paid ads ("That's like my money maker") and had Davie beside her.
- **Money links (VERIFIED)**: lp.dailymentor.co (his paid program), Xero referral.

### 2.8 The Ecom King (Kamil Sattar): "How I Find $1K/Day Winning Dropshipping Products Using Claude AI (FREE METHOD)"

- https://www.youtube.com/watch?v=IgkDbdcjQhk , 44,770 views, Aug 26, 2026, 25 min.
- **Method (VERIFIED)**: a Claude "skill" file (ecom product evidence researcher) that scores products on demand signal, market gap, supplier, compliance and creative proof, using the Meta Ad Library, TikTok Creative Center, Reddit and Google Trends. Know the margin first: his example is a $69 order with about $39 margin, so "I can spend $20 and still make profit". Supplier: USAdrop, "within 5 to 15 days".
- **Numbers (ESTIMATED, self-reported)**: a store doing "just over 1k a day for the last month" at "20% profit" (says the Shopify dashboard is on screen); a student "from zero to $7 million" (no proof in the audio).
- **Money links (VERIFIED)**: ecomstackai.io (his own sign-up), USAdrop, Winning Hunter, Shopify, .store, Omnisend, Airwallex. "Some links are affiliate links." Prompts are gated behind "500 likes".

### 2.9 Sergio C (agency owner): "How to Scale Facebook Ads on a Low Budget (Post-Andromeda)"

- https://www.youtube.com/watch?v=rBD9xJswb5k , 269,116 views, Aug 23, 2026, 27 min. Not a dropshipper; runs ads for brands.
- **Method (VERIFIED)**: at $30 to $100 a day, do the opposite of "upload 15 to 20 creatives and let Meta decide", because "a handful of ads will steal the spend" and the rest never get data. Step 1, creative test: one CBO campaign, broad, and force each ad to a fixed number of impressions (1,000 minimum, 2,000 to 3,000 better), then switch it off, so every ad gets an equal read. He cites "an average CPM is about $28, $30". Compare CTR, link CTR, CPM, cost per landing page view, cost per purchase; keep 2 to 5. "When I say a winner, I do not mean an ad with a five times return on ad spend after spending just $12." Step 2, landing page test with equal budget per ad set. Step 3, a simple Advantage+ sales campaign plus one interest test with only the winners.
- **Scale (VERIFIED)**: "performance doesn't scale one-to-one"; add about $20 a day at a time; rerun the creative test on the side for each new batch.
- **Funnel checks (VERIFIED said; ESTIMATED as facts)**: at least 10% of product page views should add to cart; no more than a 50% drop from add to cart to checkout started.
- **Finding relevant to AI statics (VERIFIED)**: for his example client, "A product image style ad didn't really work."
- **Numbers**: client examples (a $6M brand up 45% on the same spend; first-month campaigns at 6.7 times return on $500) are ESTIMATED, self-reported, and from brands with an average order near $250.
- **Money links (VERIFIED)**: his agency (advt-media.net). No tool affiliates.

### 2.10 Henrik Wold: "I Tried Dropshipping with Low Budget - Profitable?"

- https://www.youtube.com/watch?v=gHXQRWvnlI8 , 35,877 views, Aug 18, 2026, 27 min.
- **Method (VERIFIED)**: "I do not have the budget to be testing 10 different products ... that would just be gambling. I'm going to have to find a 10 out of 10 product." Winning Hunter TikTok Shop section, skip the biggest trends, look deep in the list for stores under about $150,000 revenue. Product: handheld turbo blower sold as a leaf blower, AliExpress $30 with free shipping, sold at 52 pounds. Sold to the UK "cuz the advertising is just way cheaper". Atlas app builds the store; photos taken from competitor stores; ads are videos downloaded from the ad-spy tool ("this ad actually has a TikTok URL on it") plus three ChatGPT image ads ("having some image ads in the rotation is never going to be a bad idea"). Meta: one campaign, one ad set, about 10 ads, $50 a day, purchase event, multi-advertiser ads off. Raised to $200 a day after the first profitable days. Upsell added later.
- **Numbers (ESTIMATED, self-reported)**: first sale after about 24 hours and 47 sessions with none. Total: 847 pounds, stated as $1,147; ad spend $510; product cost $420; profit stated as $217. About $40 of tools, payment fees and refunds are not in his sum. Stated cost per purchase "closer to maybe 25" early on.
- **Red flags (VERIFIED)**: reviews written by hand ("We put in Randy from Texas"), competitor photos and videos reused, a different market than the US.
- **Money links (VERIFIED)**: his paid program (breakoutecom.com), Atlas code, Winning Hunter, Shopify affiliate.

### 2.11 Alex Robinson: "I make $10k/day dropshipping using static ads (just copy me)"

- https://www.youtube.com/watch?v=_COh_Rm4UqA , 17,845 views, Oct 10, 2026, 50 min.
- **Method (VERIFIED)**: statics are used "to validate and test" and work best at the "solution to product aware" level; "native" ads drive his top of funnel. Test: one CBO at $50 a day, one ad set, one country (US), 5 to 10 statics aimed at one avatar and one desire. "I'll like to spend $150 to $160 before I conclude any data." Cut rule: "An ad set has to spend a minimum of three times the target CPA before it's a sign to cut it." Winner: profitable for three or more days in a row and still profitable when spend goes up. Avatars come from manual Reddit research.
- **On AI statics (VERIFIED)**: his own AI skill's first batch: "the designs look solid, but the messaging is horrible ... The messaging isn't clear and direct enough." He gives an illustrative result for running such a batch as is (3 days, $162 spent, $3.75 cost per click, $76 CPM, ROAS 0.38; his example, not a measured test), then rebuilds from competitors' best statics found in TrendTrack.
- **Numbers (ESTIMATED, self-reported)**: "$10,000 a day in revenue", "around $3,000 a day" profit, "30% net profit margins"; says a Triple Whale dashboard is on screen.
- **Money links (VERIFIED)**: paid Skool community (the static-ad skill is inside it), TrendTrack (20% off link), TeemDrop invitation code ("My Private Supplier").

### 2.12 Dara Denney (creative strategist): "How I Make AI Static Ads (in minutes)"

- https://www.youtube.com/watch?v=5C5VhqW9HCc , 96,285 views, Jun 25, 2026, 25 min. Not a dropshipper; has worked on brand ad accounts for about 10 years.
- **Method (VERIFIED)**: myths she rejects: statics are only for retargeting; "video is the only thing that works for my brand"; statics are only for cheap message tests. Strategy first: one goal per ad, one persona, one awareness level. Use real customer review text ("golden nugget testimonials") by feeding a review export to an LLM. Formats to test: educational infographic, benefit call-out, us versus them, transformation, text-only or founder letter. Workflow: a "brand brain" document written in Claude, then an AI ad tool; start with 3 variations.
- **Caveat she gives (VERIFIED)**: she does not like the tool's review-collage outputs and reviews every output by hand.
- **Money links (VERIFIED)**: "Super Scale has actually partnered with me on this video" (get.superscale.ai/dara); her consulting form.

### 2.13 Learn With Shopify (official): "How to Use Claude to Build and Run a Shopify Store"

- https://www.youtube.com/watch?v=Ih5RapM8XKw , 203,102 views, premiered Jul 13, 2026, 7 min. Primary source for what the connector does.
- **What Shopify says it does (VERIFIED)**: create a store from Claude chat ("Now connect this to Shopify and create my store"), install the Shopify Claude Connector app; or connect an existing store under Customize, Connectors. Then: read live products, orders and sales; rewrite all product titles and descriptions in one voice; a daily check-in ("best and worst selling ... which products are running low on stock"); pricing and bundle suggestions. Free Claude plan is enough for the steps shown.
- **Shopify's own warnings (VERIFIED)**: "The connector asks for broad access to your store, so make sure you're comfortable with that." "Remember to review everything before you publish. Claude is fast, but the final call should always be yours." "Claude Chat ... on its own cannot take payments, register your domain, or ship a single order."
- **Not shown**: ads, fulfillment, theme editing. No income claims. No affiliate links.

### 2.14 Mark Builds Brands: "ZERO to $1k/day in 3 days with ai dropshipping. [full case study]"

- https://www.youtube.com/watch?v=1XhpB0-vckw , 115,138 views, Jul 30, 2026, 25 min.
- **Method (VERIFIED)**: product rules: a painful problem in a passionate market; at least $25 gross margin per order and a price at least 3 times landed cost; fits in a shoe box; some room for upsells. "You shouldn't be spending more than like 2 hours on product research." Warns against products that need a break-even ROAS of 1.7 to 2.0: "Do you have any idea how hard it is to maintain a 3x return on ad spend on Facebook at high levels of spend?" Found the product with Claude plus the GetHookd MCP. Store on the free Debut theme, direct to product page. Place test orders before running ads. Meta: one campaign, four ad sets, each one format (AI animation, native statics, founder ads, mini podcast), 3 to 5 ads each, fully broad, US only, Audience Network excluded, every enhancement off. Split traffic 50/50 between two product pages on day 1 and killed one after "the first like $300, $400 in spend".
- **Numbers (ESTIMATED, self-reported, revenue only)**: day 1 $850, day 3 over $1,000, day 4 $1,200. Store conversion rate 1.54% (he believes 2 to 2.5% after bot traffic). Order value only about $14 above the base price. Profit not stated (UNKNOWN).
- **What went wrong (VERIFIED)**: "Ad account got shut down" on day 2, back the next day. Every asset was new (pixel, ad account, store).
- **Money links (VERIFIED)**: GetHookd is "my software" (said on camera), paid mentorship, email list.

### 2.15 Sharif Mohsin: "I Tried Dropshipping for 14 Days (Realistic Results)"

- https://www.youtube.com/watch?v=jRVYT9hag64 , 55,098 views, Oct 19, 2026, 19 min.
- **Method (VERIFIED)**: hard cap of $250 for everything. Store built by pasting an Amazon listing URL into the Store Launch app. Second product chosen from Amazon "bought in past month" counts (700 to 1K a month across several new listings). Meta ads left to run without changes.
- **Numbers (ESTIMATED, self-reported)**: product 1 failed and used about half the budget ($124 or $125 left). Product 2 (squishy toys): day 1 $109 sales on $67 of ads, profit $4; day 2 about $60 sales on $104 of ads, loss $65; day 3 $164 sales on $101 of ads, loss $2; day 4 $136 sales on $76 of ads, profit $17. His verdict: "this challenge didn't look too successful ... Not every product is going to work."
- **Money links (VERIFIED)**: his free course funnel, storelaunch.ai referral.

---

## 3. Supporting videos (shorter notes)

| Video | Views, date (VERIFIED) | What it adds | Money links (VERIFIED) |
|---|---|---|---|
| Ben Heath, "$100 vs $100,000 Facebook Ads Strategy" (`du6rDgRf06g`) | 24,263, Aug 12, 2026 | Tiny budgets: one campaign, one ad set, one offer, broad; Meta "ideally wants ... 50 plus conversions per week"; separate testing campaigns only make sense at large budgets; a test "might take 2 weeks, a month" at small spend; big percentage budget jumps are fine at small budgets, not at large ones | Skool community, his agency, Hyros |
| Jensen Tung, "Easiest Way To Find Winning Products For Beginners In 2026" (`lsDlihWbg9I`) | 490,921, Jul 23, 2026 | Problem first, then product, then several supplier quotes and a sample; "Don't be surprised if your first few products flop"; shows an Alibaba AI tool that sends and answers supplier messages by itself (the repo forbids sending) | Accio Work (sponsor link), Shopify, Printful and many other affiliate links, paid coaching calls |
| Alexander Shenton, "How To Find Dropshipping Suppliers With 3-7 Day Delivery" (`_tmfG_WOtE0`) | 2,519, Sep 18, 2026 | Test a new product with AliExpress-style sourcing; switch to a private agent "the moment you start seeing consistent sales"; slow shipping means "refund requests, chargebacks"; Fulfillman lists US delivery "5 to 8 days" | Fulfillman, ZIK Analytics, Shopify, his paid course |
| Elliott Prendy, "How to Start Dropshipping on TikTok Shop (2026)" (`8Tj3wn6gVuw`) | 15,213, May 31, 2026 | Setup only: AutoDS import to TikTok Shop, own address entered as the warehouse, auto order. UK based. No results, no mention of TikTok Shop US shipping rules | AutoDS |
| James Pelton, "I Let AI Run My Dropshipping Business for a Month, Here's What Happened" (`LquhZ4A9hkQ`) | 49,390, Jun 29, 2026 | Shows day 1 only: Doba's agent builds a store and lists 10 products priced at cost times 1.2 plus shipping. No sales, no ads, no 30-day result despite the title | "This video is sponsored by Doba" |
| Lukas Juodkunaitis, "I Tried Dropshipping With $500 for 7 Days (HONEST RESULTS)" (`zDu5bV_MYVw`) | 13,056, Apr 25, 2026 (just outside 6 months) | The closest match to Dhruv's budget. About $100 a day, 5 or 6 copied videos at about $20 each, private supplier. Day 1: 3 sales, $177 revenue, $89.71 ads, $68 goods, +$8. Day 2: 0 sales, loss $130. Day 3: 1 sale, loss $95.10. Day 4: 0 sales. Day 5: 10 sales, $385 revenue, $137.39 ads, loss $12 because the free-gift offer cost too much. Challenge failed. "It gets more and more competitive. People run the same products with the same offer." | Paid mentorship, Shopify, Atlas |
| Ant, "I Tried A.I. Dropshipping Until I Made $1,000/Day (REAL RESULTS)" (`z451fon1rz4`) | 81,832, Apr 27, 2026 (just outside 6 months) | Product 1: $153 then $102 of ads over 2 days, 3 orders, loss about $168, dropped. Product 2 (a festival-trend shirt): day 1 $519 revenue on $138 ads, +$247.54; day 2 $1,059 revenue on $383 ads and $371.20 goods, +$270. Overall +$349.39 in 4 days. Ads were other people's TikTok videos | Paid coaching, Shopify, Zendrop, tool resale on Whop |
| Romas Ecom, "how to literally print money while you sleep with AI dropshipping" (`ScF0pi6FSLQ`) | 454,804, Aug 16, 2026 | Contrarian: bulk-imported catalog stores on Google Shopping ads, not Meta. Claims "$3.7 million" and "one or two hours a week" with no proof in the audio | Says "I'm not sponsored by any AI store builder" but the description has a Higgsfield affiliate link and a paid mentorship |
| Perry Xie, "how i made $200k in 30 days with shopify stores i built in 10 minutes" (`b43_Gs64mYM`) | 188,772, Sep 10, 2026 | Claude-built product pages. Claims "$197,000 in 50 days" and "$143,000 in 30 days", revenue only | Paid Skool, TrendTrack, Atlas, "$3,500+ worth of tools ... for $29" on Whop |
| Austin Rabin, three sister videos (see 2.1) | see 2.1 | Same funnel each time; one contains the real Haven P&L | Same links |

---

## 4. Synthesis

### 4.1 Where the credible creators agree

"Credible" here means they either show a full cost breakdown, are not paid by a store-builder funnel, or state their own limits.

1. **Start from proven demand.** Pick a product other stores are already advertising and selling now (Welch, Hampton, Wold, Tilbury's expert, Fogarty, Mark Builds Brands, Mohsin). Nobody credible lets a chatbot invent the product from nothing; the AI is pointed at ad-library, TikTok Shop or Amazon sales data.
2. **Check the margin before building anything.** Stated floors: "over 25 or $30 in profit per order" (Welch); at least $25 gross margin and a price 3 times landed cost (Mark Builds Brands); about 3 times cost (Hampton, Nazareth); 2 to 3 times cost and a price under $80 for an unknown store (Tilbury's expert). All ESTIMATED as rules of thumb.
3. **Meta is the default paid channel**, with a plain setup: sales objective, purchase event, broad targeting, one CBO campaign, enhancements and multi-advertiser ads switched off (Hampton, Wold, Mark Builds Brands, Nazareth, Robinson, Heath, Fogarty).
4. **The creative and the product page decide the result, not ad-manager tricks** (Nazareth, Mark Builds Brands, Sergio C, Fogarty, Denney).
5. **Test small and read early**: $25 to $100 a day per product, a verdict after about 3 days or about $150 (Robinson), or after spending three times the target cost per purchase (Robinson).
6. **Expect losers.** Fogarty's student tested "a couple of products" that failed first; Tilbury's expert had two of three products with no day-1 sales; Mohsin's and Ant's first products failed; Tung: "your first few products flop"; Juodkunaitis failed the week.
7. **Raise order value with quantity bundles and upsells** (Nazareth, Persse, Wold, Welch, Mark Builds Brands).
8. **Keep a human approval step on every AI change** (Rabin, Shopify, Fogarty).
9. **Revenue is not profit.** Persse ($85 on a $1,000 day), Tilbury (near break-even), Rabin's own brand (about 10% net in his words) all say it with numbers.

### 4.2 Where they disagree

| Topic | One side | Other side |
|---|---|---|
| Static image ads | Rabin: "three times on average cheaper" than video. Robinson and Denney: statics can win, including on cold audiences | Fogarty: stopping the scroll with an image "is much harder". Sergio C's client: "A product image style ad didn't really work." Wold uses images only as filler in the rotation. Persse, Nazareth, Hampton and Fogarty's student all got their sales from video or AI UGC |
| How many creatives | Hampton: 10 to 15 creatives in week 1 | Sergio C and Heath: at small budgets fewer ads, each forced to get enough impressions |
| Store type | One product page (Rabin, Welch, Nazareth, Wold, Mark Builds Brands) | General "beginner store" with 3 products so one flop does not end the test (Tilbury's expert); "launch all five" (Fogarty) |
| When to kill | Mark Builds Brands: "ruthless", cuts on day 1 | Hampton: beginners kill too early. Robinson: wait for 3 times target CPA. Tilbury's expert: reduce budget, do not stop |
| How fast to scale | Hampton: double after 2 to 3 good days. Wold: 4 times overnight | Sergio C: about $20 a day at a time. Persse doubled and wrote "pushing up the ad spend to chase the momentum really hurt us" |
| Product research tool | Paid ad-spy (TrendTrack, Winning Hunter, GetHookd, AdLibrary.io, PiPiAds, Kalodata) | Free: burner social account, Meta Ad Library, Amazon "bought in past month" (Persse, Nazareth, Mohsin) |
| Channel | Meta (nearly everyone) | Google Shopping only (Romas Ecom). TikTok Shop appears only in setup tutorials with no results |
| Reviews and copied assets | Rabin's prompts: "Do not invent reviews". Fogarty: do not mislead customers | Nazareth: AI testimonial videos he admits "aren't real". Wold: invented reviewer. Welch: clones a competitor's store and images |

### 4.3 Budgets and timelines they state for a first profitable product

All ESTIMATED (self-reported). Inputs only; see section 6.2 for the raw numbers.

- Stated test budgets: $100 (Nazareth), about $150 planned (Wold; he actually spent $510 on ads), $250 (Mohsin), $300 (Tilbury), about $500 (Juodkunaitis), $50 to $200 a day with no cap (Persse), $100 to $250 a day (Fogarty's student).
- Daily ad budget per product at launch: $25 to $50 (Hampton), $40 (Tilbury's expert), $50 (Persse, Wold, Robinson), about $100 (Juodkunaitis, Fogarty's student).
- Time to first sale in the tests that got one: 20 minutes to about 24 hours.
- Time to a clearly profitable day: Persse about day 10 to 14; Ant day 3 (second product); Wold day 2 to 3; Tilbury's expert days 2 to 4 at single or double digit dollars; Mohsin and Juodkunaitis never.
- Nobody with a transparent cost sheet shows a first week where every order was profitable after ad cost. Day 1 is a loss in most of them ("if you are making profit on day number one, you should consider yourself kind of lucky", Tilbury video).
- Time cost: Fogarty's student worked 14 hours on build day; Tilbury's expert filmed and edited all ads in one day and "didn't get that much sleep". Dhruv's 1 to 3 hours a day is less than any of them spent.

### 4.4 How many products you must test

No creator gives a tested number. What they did or said:

- Fogarty: shortlist five and launch them all; the student still needed "a couple" of failures before the winner.
- Tilbury's expert: three at once on $300.
- Ant: winner on product 2. Mohsin: two products, budget gone. Juodkunaitis: one, failed, started a second.
- Wold: with a low budget, one carefully chosen product, because testing ten "would just be gambling".
- Hampton hands out a "top 10 winning products list" to test from.
- Practical reading: plan for 2 to 4 product tests. The repo's stop rule (review after two failed tests in a row) is stricter than what these creators imply, which fits a $500 to $1,000 budget.

### 4.5 AI-generated image ads versus video and UGC

- **For**: cheap and fast; five formats that are known to work (Denney); good for a clear message to people who already know the problem (Robinson). Rabin's "3 times cheaper" has no data behind it (UNKNOWN).
- **Against, or with conditions**: the first AI batch has weak messaging and loses money if run as is (Robinson); the picture must match the item the supplier ships (Fogarty); imitating a competitor's ad style closely ("This looks so much like their ads", Rabin) invites trade dress and copyright trouble and is against the repo's research rule.
- **What actually produced the sales in the transparent tests**: video. Persse (AI video from Higgsfield plus Claude), Nazareth (AI UGC), Fogarty's student (AI UGC after image ads got no add to carts on product 1), Tilbury's expert (self-filmed), Wold and Ant (other people's videos). Robinson is the only one who says statics carry a large share, and he pairs them with "native" ads.
- **Fair summary**: statics are a cheap first read on message and angle and a useful second format; no transparent test in this sweep won on AI statics alone. For the repo: an AI person must not claim to have used the product, so AI UGC "testimonials" as used by Nazareth and Hampton's tool are out; AI product demos and voiceover are allowed.

### 4.6 US stock versus China-shipped

What creators say (VERIFIED said; the delivery times themselves are ESTIMATED vendor or affiliate claims):

| Source | Statement |
|---|---|
| Rabin, own brand (`gXVbZLlcPYA`) | US warehouse in North Carolina, "about 2 to 3 days", "about $6.50 per order". "I highly recommend getting a high-quality supplier or having a warehouse in the United States ... cuz everyone is so used to Amazon" |
| Rabin, agentic video | No delivery time stated for the Zendrop products |
| Tilbury's expert (AutoDS side) | Policy "up to 10 business days"; never suppliers "that take 3 to four weeks"; "if I ship from the US to the US, even better ... a day or two" |
| Nazareth (AutoDS, AliExpress) | "between 5 to 9 business days", says it usually arrives sooner |
| Hampton (TeemDrop, paid link) | "3 to 9 days" |
| Ecom King (USAdrop, paid link) | "within 5 to 15 days" |
| Shenton (Fulfillman, paid link) | US "5 to 8 days" on a private line; test on AliExpress, switch once sales are daily |
| Welch, Persse, Mark Builds Brands, Wold, Mohsin | No delivery time stated |

- Agreement among those who mention it: slow shipping causes refunds and chargebacks; get under about 10 days; move to faster fulfillment as soon as a product sells.
- No creator gives a measured refund or chargeback rate by shipping speed. UNKNOWN.
- No creator compares conversion rate for US stock against China-shipped. UNKNOWN.
- TikTok Shop: the one tutorial (Prendy, UK) does not cover US rules. Third-party articles from January and February 2026 report that TikTok Shop moved to end seller-arranged shipping in the US and then paused or softened it, and they conflict with each other (ESTIMATED; easyship.com/blog/tiktok-shop-reverses-us-shipping-mandate, modernretail.co article of Jan 28, 2026, ordoro.com update of Feb 2026; read as search summaries on 2026-11-21). The current rule for a new US seller is UNKNOWN and must be read in Seller Center before any TikTok Shop plan.
- Reading for Dhruv: the evidence from this sweep supports his preference for US stock. It is what the reference creator does in his real business, and it is the only option that fits the FTC shipping-time rule in the repo without long stated windows.

### 4.7 What AI agents really do well today, and what is hype

**Shown working on camera (VERIFIED as shown or described in more than one video)**

- Scaffolding a store and a product page in minutes (store builder funnels, Atlas, Store Launch, Claude Code). Note the "AI store builders" are mostly a theme plus 10 preset products, not research.
- Rewriting product titles, descriptions, FAQ, SEO text and alt text through the Shopify connector, with approval (Rabin, Shopify).
- Reading store data for a daily summary and pricing ideas (Shopify).
- Summarizing a competitor's ads through an ad-library MCP and naming angles (Rabin, Welch, Mark Builds Brands).
- Writing image prompts and producing product and lifestyle images (ChatGPT, Higgsfield) and short AI videos.
- Reading exported ad results and listing what to cut and keep (Hampton).
- Scheduling a recurring research task (Rabin).

**Limits shown in the same videos (VERIFIED)**

- The Shopify connector could not change theme text and had not seen the rendered or mobile page (Rabin). Theme work was still manual and painful (Fogarty's student).
- AI statics need a human to fix the message (Robinson). AI tools produce outputs the expert rejects (Denney).
- Generated product images can drift from the real item (Fogarty).
- A chatbot with no live sales data cannot validate demand; every credible method wires it to an ad-library or marketplace source first.
- Ad account bans, payment holds and supplier quality are untouched by AI (Mark Builds Brands lost his ad account for a day).

**Hype (claims with nothing shown)**

- "A team of AI agents working 24/7 ... while you just sit there or sleep and rake in all the cash", "fulfill your orders, do customer service" (Rabin intro): not shown in the video.
- "Fully automated", "one or two hours a week" (Romas Ecom).
- An agent that runs a store for 30 days (Pelton): only day 1 exists in the video.
- No video in this sweep shows an agent creating, launching and managing ads to a profit without a person.

Dhruv already has the pieces the reference video sells: Claude, a Shopify connector path (Shopify's own), a Meta Ads connector, Higgsfield, and an ad library (Foreplay, currently out of credits). The paid AdLibrary.io plan and the store builder funnel add little beyond a theme.

---

## 5. Consensus playbook (what most credible creators would agree on)

Written as their consensus, with the repo's rules noted where a common tactic breaks them.

1. **Choose from live demand.** Shortlist products that several stores started advertising in the last 30 days and that show marketplace sales (Amazon "bought in past month", TikTok Shop sold counts). Skip anything a shopper finds cheaper on Amazon or Google Shopping in one search (Fogarty's Google test). Stay inside Dhruv's allowed categories; most creator examples are health-adjacent or children's items and do not transfer.
2. **Gate on unit numbers before building.** Creator floors: at least $25 to $30 gross margin per order, price about 3 times landed cost, price under about $80 for an unknown store, small and light. Feed real costs to `scripts/economics.py`; do not accept a creator's rule as a pass.
3. **Lock fulfillment and the delivery promise first.** Prefer a US-stock source. Order one unit the same day (the approved exception) and state only a delivery window the source can meet.
4. **Build one clean product page in a day.** Free theme, supplier facts only, a quantity bundle, clear shipping and returns, no invented reviews, images that match the shipped item. Use Claude for structure and copy with approval on every write.
5. **Place a test order through checkout before any ad** (Mark Builds Brands).
6. **Make 5 to 10 creatives in at least two formats.** A few statics with a hand-checked message and at least a few short videos. Borrow angles, never assets.
7. **Run one simple Meta sales campaign.** CBO, broad, US, purchase event, about $50 a day, one ad set per angle, enhancements off. If the budget is spread too thin, use Sergio C's equal-impression test so each ad gets a fair read.
8. **Read it on a fixed rule.** Wait for about 3 days or about $150, or three times the target cost per purchase with no sale (Robinson), and watch CTR, cost per click, CPM and add-to-cart rate as early signals. The repo's own kill rules (pause an ad at break-even CAC with zero purchases; pause the test at half the budget if blended CAC is above break-even) are stricter and should govern.
9. **Fix the offer before adding spend.** If the page gets clicks but few add to carts, change price, bundle or page first (Sergio C, Fogarty, Persse).
10. **Scale in steps only after 2 to 3 good days in a row**, and expect profit to dip when the budget jumps (Persse, Sergio C).
11. **Count profit every day with every cost** (goods, shipping, fees, ads, samples, apps, refunds). Juodkunaitis lost money on his best sales day because the offer was not costed.
12. **Plan for 2 to 4 product tests and stop on the rule.** When a product sells daily, move it to faster, controlled fulfillment and real customer content.

---

## 6. Raw inputs for the scripts (no math done here)

### 6.1 Haven Golf Company, September 2026, as read out by the owner

ESTIMATED (self-reported; https://www.youtube.com/watch?v=gXVbZLlcPYA , Oct 29, 2026). Says Shopify analytics and the finance summary are on screen.

| Input | Value as stated |
|---|---|
| Revenue | $125,463.94 |
| Orders | 1,382 |
| Average order value | $86.91 |
| Store conversion rate | 1.9% |
| Facebook ad spend | $68,886.10 ("around a two ROAS, which is pretty low for us") |
| Cost per purchase, new product campaign | $30.88 average |
| Cost of goods | $28,868.40 |
| Shopify plan and apps | "about $3,000 a month" |
| Payment processing | $3,871.97 |
| Shipping to customers | "about $6.50 per order", $8,983 |
| Returns | $4,299 (he adds back $742.04 of goods) |
| Net profit as he states it | $12,596.51, "just over a little bit of a 10% net profit margin" |
| Fulfillment | Own warehouse in North Carolina, "about 2 to 3 days" |

### 6.2 Small-budget tests with stated costs

All ESTIMATED (self-reported in the linked video). "Profit" is the creator's own figure and usually leaves out some costs.

| Creator, date | Market | Days | Revenue | Ad spend | Goods and shipping | Other stated costs | Profit as stated | Notes |
|---|---|---|---|---|---|---|---|---|
| Nazareth, Jun 29, 2026 | US | 1 | $188.98 (3 units) | $57 | about $75 | about $5 | $52 | Price $70, cost about $25 |
| Tilbury's expert, Nov 3, 2026 | US | 4 ad days in a 7-day test | $855.75 (25 sales) | $249.66 | $472.84 | fees $28.90, samples $48.35, software $1.99 | caption says "$541", most likely $54.01 (UNKNOWN until checked) | 3 products at $40 a day |
| Wold, Aug 18, 2026 | UK | about 5 | $1,147 | $510 | $420 | tools about $40, not in his sum | $217 | Unit cost $30, price 52 pounds |
| Mohsin, Oct 19, 2026 | US | 4 on product 2 | $109, about $60, $164, $136 by day | $67, $104, $101, $76 by day | not itemized | not itemized | +$4, -$65, -$2, +$17 by day | Product 1 used about $125 and failed |
| Juodkunaitis, Apr 25, 2026 | US | 6 | $177, 0, 1 sale, 0, $385 by day | $89.71 on day 1, $137.39 on day 5 | $68 on day 1 | not itemized | +$8, -$130, -$95.10, loss, -$12 by day | Failed |
| Ant, Apr 27, 2026 | US | 4 | $104 and 1 sale (product 1); $519 and $1,059 (product 2) | $153, $102, $138, $383 | $25.30, $15, $116.30, $371.20 | fees $3.40, $0.17 (as captioned), $34; domain $15; Shopify $1 | -$94.46, -$73.79, +$247.54, +$270; total +$349.39 | Trend product |
| Persse, Nov 13, 2026 | US | 21 | $3,239 in the first 7 days of sales; "just under $22,000" by day 21 | $50, then $100, then $200 a day, later more | not itemized | not itemized | about $85 on the first $1,000 day; $324 on day 11; $482 on day 14 | Children's product; two experienced operators; sponsors |

### 6.3 Creator benchmarks (ESTIMATED; use only as cross-checks against `data/channel_params.json`)

| Metric | Value | Who |
|---|---|---|
| Meta CPM | "$15 to $25" healthy | Hampton |
| Meta CPM | "about $28, $30" average | Sergio C |
| CTR (all) | 2.5% or higher | Hampton |
| Cost per click | under $1 | Hampton |
| Product view to add to cart | 10% or more | Sergio C |
| Add to cart to checkout started | no more than a 50% drop | Sergio C |
| Store conversion rate | 1.54% measured, 2 to 2.5% after bots | Mark Builds Brands |
| Store conversion rate | 1.9% | Rabin (Haven) |
| Spend before judging statics | $150 to $160 over 3 days | Robinson |
| Cut rule | 3 times target cost per purchase | Robinson |
| Zendrop plan | free for 0 to 10 products, "up to $79 per 30 days" | Rabin |
| AutoDS | $0.99 or $1 trial; import plan "just under $20 per month" | Tilbury video, Prendy |

---

## 7. Red flags

**About the reference video and funnel**

1. The headline revenue belongs to a different business model. Haven Golf Company is a stocked apparel brand with a US warehouse; the tutorial is a Zendrop template store. VERIFIED from his own videos.
2. His own stated net margin for the latest reported month is about 10%, on a mature brand. VERIFIED said, ESTIMATED as a fact.
3. The tutorial shows no ad running, no sale, no budget, no kill rule, no delivery time.
4. "Static ads ... three times on average cheaper": no data.
5. The StoreBuild page claims "Over 1.5 Million Stores Created" and gives every user "a ready-to-sell store with 10 products" (VERIFIED on the page today). If true, a great many stores hold the same preset products.
6. The "$100,000 before the end of the year" line could not be found in the video or on the pages loaded. If it is in the funnel, it is an earnings claim with no disclaimer on the pages I saw.
7. "I don't have a course to sell" while every link in the description is a paid partner link.

**Across the space**

8. Undisclosed or lightly disclosed pay: the store builder, Shopify, supplier and ad-spy links are affiliate links in nearly every video. Disclosure ranges from clear (Welch on camera, Pelton, Persse, Tilbury, Ecom King) to none in the description text (Rabin, Hampton, Wold, Nazareth, Robinson).
9. Titles with money claims the video does not support: Welch "$12,784/Month" (video shows $424 of day-1 sales); Pelton "Here's What Happened" (day 1 only); Hampton "$10 million" and students "$50 million"; Ecom King student "$7 million"; Romas "$3.7 million"; Perry Xie "$200k in 30 days".
10. Revenue shown without profit: Welch, Mark Builds Brands, Fogarty's $42,159.88, Perry Xie.
11. "Not sponsored" said on camera with an affiliate link and a paid mentorship in the description (Romas Ecom).
12. Fake social proof taught as normal: AI testimonial videos (Nazareth), invented reviewers (Wold). These break FTC 16 CFR 465 and the repo rules.
13. Copying taught as normal: cloning a competitor's store and images (Welch), reusing competitors' and creators' videos as ads (Wold, Ant, Juodkunaitis), imitating a named competitor's ad style (Rabin).
14. Example products sit in categories Dhruv excludes: health-adjacent (lymphatic brush, massager, clay mask, arch support, tooth powder, heating belt, low-sugar snacks) and children's (art frame, squishy toys).
15. Results from cheaper ad markets (Wold: UK, considered Australia) do not transfer to US costs.
16. Results come from people with years of ad experience, warm ad accounts or a mentor beside them. The sponsor-side expert in the most viewed video still landed near break-even.
17. Supplier delivery times are quoted only by creators paid by that supplier (TeemDrop, USAdrop, Fulfillman, AutoDS).
18. Tool resale ("$3,500+ worth of tools ... for $29", Perry Xie; "PiPi Ads/Kalodata for Cheap", Ant): shared-login schemes.
19. New ad accounts get shut down (Mark Builds Brands, day 2). Not an AI problem and not mentioned in the funnel videos.
20. TikTok Shop dropshipping tutorials skip the US shipping rules, which changed in 2026 according to third-party reports.

---

## 8. Biggest unknowns

- Whether Haven's $4.2M and the monthly P&L are real: UNKNOWN (self-reported, screen not checked).
- Where the "$100,000 before the end of the year" claim appears: UNKNOWN.
- Real delivery times for Zendrop, AutoDS, TeemDrop and USAdrop to a US address: UNKNOWN until a test order.
- Refund and chargeback rates for China-shipped versus US-stock orders: UNKNOWN; no creator gives one.
- Whether AI static image ads can carry a cold test on their own for an allowed product: UNKNOWN; no transparent example found.
- How many product tests a first-timer needs: UNKNOWN; creators imply 2 to 4.
- The current TikTok Shop US fulfillment rule for a new seller: UNKNOWN.
- Total profit across the full period in the Persse and Fogarty videos: UNKNOWN.
- On-screen proof in any video: not checked (transcripts only).

---

## 9. Top videos of the last 6 months from the 21 searches

Views VERIFIED on 2026-11-21 through DataForSEO. Dates with "about" are approximate.

Queries: 1 agentic AI dropshipping; 2 AI agents dropshipping 2026; 3 Claude Shopify MCP dropshipping; 4 ChatGPT dropshipping store; 5 AI dropshipping automation; 6 dropshipping product research 2026; 7 one product store 2026; 8 dropshipping Facebook ads 2026 testing strategy; 9 TikTok Shop dropshipping 2026; 10 dropshipping US suppliers fast shipping; 11 Claude Code Shopify store ads; 12 AI image ads dropshipping static ads; 13 how to start dropshipping 2026; 14 dropshipping with $500 challenge 2026; 15 Sebastian Ghiorghiu dropshipping 2026; 16 Chris Wane dropshipping 2026; 17 Camille dropshipping 2026 beginners; 18 Davie Fogarty dropshipping 2026; 19 dropshipping realistic results honest failed; 20 US vs China dropshipping suppliers shipping times 2026; 21 dropshipping is dead 2026 truth.

| # | Video (ID) | Channel | Views | Published | Found by query # |
|---|---|---|---|---|---|
| 1 | I Tried Shopify Dropshipping For 7 Days (Realistic Results) (`rhuYy9LP72M`) | Mark Tilbury | 5,268,463 | about 6 months ago | 4, 14, 19 |
| 2 | I Tried AI Dropshipping For 7 Days, Copy Every Step (`mUz_tHYLhUs`) | Mark Tilbury | 641,338 | Nov 3, 2026 | 1 |
| 3 | I Tried Dropshipping for 7 Days as a Student  (With Zero Experience) (`CNtkNxLmGj8`) | Manish Creates | 592,804 | about 5 months ago | 14 |
| 4 | Beginners Guide To AI Dropshipping (5+ Hour FREE Course) (`DNdBJ5tgyjI`) | Jordan Welch | 506,310 | about 4 months ago | 2, 13, 17, 18 |
| 5 | Easiest Way To Find Winning Products For Beginners In 2026 (`lsDlihWbg9I`) | Jensen Tung | 490,921 | Jul 23, 2026 | 6 |
| 6 | how to literally print money while you sleep with AI dropshipping (just copy me) (`ScF0pi6FSLQ`) | Romas Ecom | 454,804 | Aug 16, 2026 | 5 |
| 7 | How to Actually Start Shopify Dropshipping in 2026 (`wDBcYlt_DZU`) | Ac Hampton | 299,002 | Jun 25, 2026 | 13, 14, 17 |
| 8 | How to Scale Facebook Ads on a Low Budget (Post-Andromeda) (`rBD9xJswb5k`) | Sergio C | 269,116 | Aug 23, 2026 | 8 |
| 9 | I Tried AI Dropshipping for 7 Days (Realistic Results) (`8Oi5CWTfQFs`) | Baxter Persse | 262,476 | Nov 13, 2026 | 14, 19 |
| 10 | How to Build a Full Shopify Store using AI (Claude Code) (`HsMGvW2TE64`) | Metics Media | 228,145 | about 4 months ago | 3, 11 |
| 11 | I Helped a Complete Stranger Build an AI Ecom Store (`MxjwiA7cCpI`) | Davie Fogarty | 214,572 | Sep 29, 2026 | 18 |
| 12 | How to Use Claude to Build and Run a Shopify Store (`Ih5RapM8XKw`) | Learn With Shopify | 203,102 | Premiered Jul 13, 2026 | 3, 11 |
| 13 | how i made $200k in 30 days with shopify stores i built in 10 minutes.. (w/ claude ai) (`b43_Gs64mYM`) | Perry Xie | 188,772 | Sep 10, 2026 | 11 |
| 14 | Facebook Ads Tutorial - 2026 Full Guide for Beginners (`h839wnSKZXs`) | Davie Fogarty Mentors | 176,162 | about 3 months ago | 8, 18 |
| 15 | What You NEED To Know To Get Started With Facebook Ads (`p8pthMjKKXk`) | Ben Heath | 167,816 | about 3 months ago | 8 |
| 16 | The SIMPLEST Way To Make Money Online With Claude AI in 2026 (`XSehihyKFqw`) | Nate Herk | AI Automation | 153,140 | about 5 days ago | 2 |
| 17 | How to Start Dropshipping on eBay in 2026 (Full Course for Beginners) (`_CRIPwLLATg`) | AutoDS - Build Your Online Income | 152,233 | about 5 months ago | 13, 17 |
| 18 | Full Guide to Start Ai Dropshipping in 2026 (MASTER CLASS) (`vy7XsVPy_kA`) | Baddie In Business | 150,352 | about 6 months ago | 2, 5, 13, 17 |
| 19 | Claude AI + Dropshipping = $300/Day (Beginner-Friendly) (`F-Xbf3OhqsE`) | Travis Marziani | 148,857 | about 1 month ago | 11 |
| 20 | $3.9M with a.i. dropshipping (free method) literally just copy my store. (`3fg_NwHN2vY`) | Austin Rabin | 130,143 | Aug 5, 2026 | 2, 5 |
| 21 | How to Start Dropshipping THE LAZY WAY (Step By Step) FREE COURSE (`5mh20SuL3Lc`) | Baddie In Business | 128,358 | about 4 months ago | 17 |
| 22 | How To Find Winning DropShipping Products In 2026 (My Exact Process) (`8n7LQAuwfR8`) | Nishkarsh Sharma | 127,899 | about 4 months ago | 6 |
| 23 | The ONLY Way to Start Dropshipping in 2027 (For Beginners) (`OlDS58i5_ps`) | Ac Hampton | 121,920 | about 1 month ago | 13, 17 |
| 24 | f*ck it. ZERO to $1k/day in 3 days with ai dropshipping. [full case study] (`1XhpB0-vckw`) | Mark Builds Brands | 115,138 | Jul 30, 2026 | 5 |
| 25 | How to Set Up AI Agents in 2026 (Use this FREE AI Tool) (`qfXxWLxNGuM`) | Youri van Hofwegen | 110,888 | about 2 months ago | 2 |
| 26 | Claude Can Now Do EVERYTHING on Shopify (`EpPuU9k6Ahg`) | Brendan Gillen | 109,232 | about 6 months ago | 3, 11 |
| 27 | Claude + Dropshipping = $12,784/Month (`9zh3Raq4FVc`) | Jordan Welch | 100,155 | Sep 3, 2026 | 3, 11 |
| 28 | How I Make AI Static Ads (in minutes) (`5C5VhqW9HCc`) | Dara Denney | 96,285 | Jun 25, 2026 | 12 |
| 29 | The COMPLETE Shopify Tutorial 2026 (`_1caEZ7t3UY`) | Learn With Shopify | 92,833 | about 6 months ago | 7 |
| 30 | $1,084,935/Sales with CLAUDE CODE - 0 to $100k Dropshipping Challenge (`T2sxUoS6-4Y`) | Ecom with Simo | 90,876 | about 5 months ago | 11 |
| 31 | How To Start Dropshipping With $0 (For Beginners) (`bpxNL18GVEg`) | Jordan Welch | 82,754 | about 12 days ago | 2, 13, 17 |
| 32 | Build a Shopify Store With AI (Claude Code Tutorial) (`YpMaB2S2xcs`) | Davie Fogarty Mentors and Davie Fogarty | 82,236 | about 5 months ago | 3, 11 |
| 33 | I Tried A.I. Dropshipping Until I Made $1,000/Day (REAL RESULTS) (`z451fon1rz4`) | Ant | 81,832 | Apr 27, 2026 | 19 |
| 34 | How to Start AI Dropshipping in 2026 (FULL 6-Hour Full Course, A-Z) (`EBj5aaiXQ68`) | Reetu Maz  | 77,082 | about 2 months ago | 17 |
| 35 | Claude Design Just Changed Shopify Dropshipping Forever (`393t6rWLz5A`) | THE ECOM KING | 76,248 | about 6 months ago | 3 |
| 36 | $1,134,935 Sales with HIGGSFIELD on ChatGPT - 0 to $100k Dropshipping Challenge (`YJvdgFDeAos`) | Ecom with Simo | 68,759 | about 1 month ago | 4 |
| 37 | The NEW Way to Start Dropshipping in 2026 (Step by Step) (`_DSA83JfpJk`) | Andy Stauring | 68,371 | about 4 months ago | 13, 17 |
| 38 | I Started a Dropshipping Store in 24 Hours Using ONLY AI (`_dTKOXlvdZ8`) | Nathan Nazareth | 65,932 | Jun 29, 2026 | 4 |
| 39 | $1,137,935 Sales with HIGGSFIELD on ChatGPT - 0 to $100k Dropshipping Challenge (`sboQcUJxmCA`) | Ecom with Simo | 64,283 | about 2 months ago | 4 |
| 40 | Claude Code + Shopify = $130,000/Month (`8O_69fP_WZc`) | Money Talk With Leon | 62,527 | about 5 months ago | 11 |
| 41 | Beginners Guide To A.I Dropshipping In 2027 (Full Course) (`5uI98Gy7B5o`) | Sharif Mohsin | 60,938 | about 2 weeks ago | 2 |
| 42 | If I Wanted to Hit $1M/Month in Ecommerce, I'd Do This (`AdCZUaxu1VA`) | Davie Fogarty Mentors | 60,411 | about 6 days ago | 18 |
| 43 | Full Guide to Escape the Trenches with Dropshipping (A-Z in 8+ Hours) (`tkZnXOPad00`) | Nathan Miller | 57,516 | about 5 months ago | 13 |
| 44 | I Tried Dropshipping for 14 Days (Realistic Results) (`jRVYT9hag64`) | Sharif Mohsin | 55,098 | Oct 19, 2026 | 14, 19 |
| 45 | How to Start Dropshipping With AI in 2026 (AutoDS + Shopify) (`aRCgyeyitdc`) | James Blue | 52,707 | about 2 months ago | 2, 5 |
| 46 | How to Start an AI Dropshipping Business in 2026 (Step-by-Step) (`ALMz11FwbSQ`) | Mikey No Code | 52,469 | about 10 days ago | 2, 4, 5, 6, 13, 14, 16, 17, 18 |
| 47 | The NEW Way to Start AI Dropshipping in 2027 (`Dt1BHy9EYMY`) | Ac Hampton | 51,984 | about 2 weeks ago | 5 |
| 48 | I Let AI Run My Dropshipping Business for a Month / Here's What Happened (`LquhZ4A9hkQ`) | James Pelton | 49,390 | Jun 29, 2026 | 1 |
| 49 | $4.1M Shopify Ai Dropshipping Automation With Claude & Chatgpt (Just Copy Me) (`IlAbicMXo1I`) | Austin Rabin | 48,844 | Sep 2, 2026 | 2, 3, 4, 5 |
| 50 | I Let Claude AI Run My Entire Dropshipping Business (Full Guide) (`NbfZ9uj0jJk`) | Lex AI | 48,653 | about 2 months ago | 5 |
| 51 | How to ACTUALLY Start Dropshipping with Claude AI in 2026 (FULL COURSE) (`PPde3fFttE0`) | Ac Hampton | 47,224 | Sep 5, 2026 | 2 |
| 52 | How I Find $1K/Day Winning Dropshipping Products Using Claude AI (FREE METHOD) (`IgkDbdcjQhk`) | THE ECOM KING | 44,770 | Aug 26, 2026 | 6 |
| 53 | How I’d Turn a Winning Dropshipping Product Into a $100M Brand (`cXiJSppvaRw`) | Davie Fogarty Mentors | 43,641 | about 1 month ago | 18 |
| 54 | Starting Dropshipping From $0 in 2026 is Simple, Actually (`sfIekgD2-4E`) | Ac Hampton | 41,959 | about 3 months ago | 17 |
| 55 | The TikTok Shop Strategy Nobody Talks About (`1Xq8ulHYKI4`) | Neil Patel | 38,546 | about 4 months ago | 9 |
| 56 | How to Win with Facebook Ad Creatives in 2027 (DO THIS) (`jDt1eCJpfO0`) | Chase Chappell | 38,177 | about 4 months ago | 8 |
| 57 | Claude FULLY Runs This Dropshipping Store By Itself.. (`ODqTAPf9PR0`) | Jordan Bown | 38,128 | about 1 month ago | 3, 4 |
| 58 | Speedrunning a Shopify Store to $400k/Month With Claude AI (`uQES8APlsM0`) | Andrew Yu | 38,086 | about 3 months ago | 3, 11 |
| 59 | I Tried Dropshipping with Low Budget - Profitable? (`gHXQRWvnlI8`) | Henrik Wold | 35,877 | Aug 18, 2026 | 14 |
| 60 | How to Start Shopify Dropshipping in 2027 (FOR BEGINNERS) (`XCYAtRXQc3w`) | Ac Hampton | 34,776 | about 5 days ago | 13, 17 |

---

## 10. Other sources loaded today

- https://app.storebuild.ai/page/new-desk (rendered in a headless browser, 2026-11-21): "Awarded #1 Partner in Americas", "Create your Shopify store for FREE in just 5 minutes and start selling today", "Choose your niche and get a ready-to-sell store with 10 products", "Over 1.5 Million Stores Created", "Real People. Real Results. Your Store. Your Profits.", "© 2025 Storebuild.ai". No income figure and no earnings disclaimer on this page.
- https://storebuild.ai/austinrabin/ (WebFetch, 2026-11-21): "Launch your Shopify store today"; "3-day free trial and just $1/month for your first 3 months"; footer "© 2025 StoreBuild, Inc."; no income claims, no mention of Zendrop.
- https://www.buildyourstore.ai/ (WebFetch, 2026-11-21): "AI store builder to create your online store"; "loads your store with 10 proven winning products"; free .store domain; "Our records show clients getting their first sales within the first 48 hours up to a week"; "The earnings are depending on you."; footer link "Dropship with AutoDS".
- Web search on "Austin Rabin Haven" (2026-11-21): no independent confirmation of the store's revenue found.
- Web search on TikTok Shop US shipping policy (2026-11-21): third-party articles only, conflicting; see 4.6.

Raw transcripts and search results are in the session scratchpad only (not kept in the repo): `/tmp/claude-0/-home-user-commerce-os/c2389654-3ee7-5e31-ba87-8e168cf76207/scratchpad/yt/`.
