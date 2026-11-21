# 03. Fulfillment and money: how supply and cash really flow in the "agentic dropshipping" model

Research date: 2026-11-21. Research only: nothing was contacted, bought, signed up for or logged into.

Labels used in this file:

- **VERIFIED**: read today on the primary source (the vendor's, platform's or agency's own page). When the primary source is a vendor describing itself, the label means "the vendor says this today", not "independently tested". Those rows say "vendor claim".
- **ESTIMATED**: third-party figure, with URL and date. Bias is flagged where known.
- **UNKNOWN**: not found, or behind a login we did not use.

No margins, CAC, ROAS or profit are computed here. Section 2 contains cash-timing arithmetic only (how much cash is out before a payout lands), run in a scratch script on ASSUMED placeholder cost shares.

Fast-lane flags (Dhruv's approved exceptions, noted, not rejected): selling before holding the product; generic catalog products instead of an own-brand hero; no sample approval before ads.

---

## 0. The ten findings that matter

1. **No stock is bought up front, but every order is paid for before the customer's money arrives.** Zendrop charges the card on file when an order is fulfilled. Shopify Payments in the US pays out after a settlement time of at least 3 business days, "longer" for new accounts, typically 3 to 5 business days plus 24 to 72 bank hours (VERIFIED, Shopify). Community reports put the first payout of a new account at 7 to 14 days (ESTIMATED).
2. **Float for $2,000 of sales in one week is the whole week's supplier bill plus the week's ad spend.** At ASSUMED supplier cost shares of 30 to 60 percent that is $600 to $1,200 of supplier charges before any payout lands (script output, section 2). That is as large as the entire $500 to $1,000 test budget, so the test only works on a credit card with room, or at a smaller sales target.
3. **Zendrop is not free for a live store.** The Shopify App Store listing says the Free plan allows "No linked products" and 1 to 20 linked products costs $29 per month (VERIFIED). Zendrop's own pricing page shows Free, Pro $49 and Plus $79 (VERIFIED). The two pages disagree; the App Store one is what Shopify bills.
4. **US stock on Zendrop means 4 to 8 business days by Zendrop's own numbers, up to 10 in Q4**: processing 1 to 3 business days (up to 5 in peak season) plus 3 to 5 business days transit. China stock is 10 to 15 business days transit after processing (VERIFIED, vendor claim, help articles updated Nov 19, 2026).
5. **US-supplier products on Zendrop cannot carry custom branding, and Zendrop does not accept returns** at its warehouse. Returns go to the seller's own address or the store runs a no-return policy (VERIFIED).
6. **TikTok Shop US cannot be used with China-shipped dropshipping at all, and is slow to pay.** US-based sellers "cannot use international third-party suppliers", third-party fulfillment is allowed only if the seller "maintain[s] ownership of the inventory", orders must be in transit within 2 business days and delivered within 6, and new sellers are paid 31 days after delivery (all VERIFIED on TikTok's Seller University today).
7. **Meta's "customer feedback score" thresholds are stale.** Meta now calls it the customer experience score and says "there's no fixed score threshold that determines ad delivery"; the score changes auction costs, and the survey asks buyers about "shipping delays" (VERIFIED, Meta help text). The widely repeated "below 2 is penalised, below 1 is banned" comes from third-party blogs (ESTIMATED, possibly outdated).
8. **A $500 to $1,000 test will never leave Meta's learning phase.** Meta says ad sets exit learning "after about 50 results in the week after the ad set's last significant edit" and that during learning ad sets "usually have a higher CPA" (VERIFIED).
9. **Launching next week means buying ads in the most expensive week of the year with no account history.** Median established brand paid 59 percent more per thousand impressions in Black Friday week 2025 than in September, 84 percent more on the day (ESTIMATED, Lebesgue, vendor data on its own large customers).
10. **Christmas cutoffs**: USPS recommends Ground Advantage by Thu Dec 17 (VERIFIED). With Zendrop's Q4 processing of up to 5 business days, a US-stock order must be placed by about Thu Dec 10 (peak case) to Mon Dec 14 (typical case). China-shipped orders placed after about Nov 25 to Dec 9 miss Christmas on Zendrop's own stated times (script output, section 6).

Verdict (section 7): **US stock for this test.** China-shipped only as a later fallback, on the own store only, with the real delivery window stated.

---

## 1. Dropship sources for a Shopify store

### 1a. Comparison table

Rating figures are the Shopify App Store listing read today. "bd" means business days. Product cost versus AliExpress is UNKNOWN for every source unless stated: all catalogs with prices sit behind a login, and no controlled same-product comparison was found.

| Source | Plans and free tier | US stock: how much, which categories | Stated processing + delivery to a US customer | Cost versus AliExpress | Branding / packaging | Returns handling | MCP / API |
|---|---|---|---|---|---|---|---|
| **Zendrop** (the video's supplier) | Own site: Free $0 (no automated fulfillment), Pro $49/mo or $399/yr, Plus $79/mo or $549/yr; Black Friday: Plus Annual $197/yr plus $300 order credits. App Store listing: Free = "No linked products allowed"; Beginner $29/mo (1 to 20 linked products); Pro $49 (21 to 100); Plus $79 (101+). VERIFIED, both pages; they conflict. | "Ships from US" suppliers; categories listed: pet, tech gadgets, home goods and decor, health and beauty, apparel. Count: UNKNOWN ("smaller than the China-based catalog"). VERIFIED vendor claim. | US: 1 to 3 bd processing (up to 5 bd in Q4) + 3 to 5 bd transit. China: 10 to 15 bd transit after processing. VERIFIED vendor claim (help articles, one updated Nov 19, 2026). Third-party: 4.1 days US, 10 to 15 days China, n=180 orders, method not published (ESTIMATED, ecommerce-times.com, Aug 10, 2026). | UNKNOWN versus AliExpress. "5 to 12% premium over equivalent CJ listings" (ESTIMATED, same article, no method). | "Custom branding and private labeling are not available for U.S. supplier products." Branded packaging needs Zendrop Fulfillment (China) plus the Private Agent program. VERIFIED. | Zendrop "does not accept product returns at its warehouse". Refunds "only when we're at fault". Damaged: report within 30 days of delivery with photo or video. Lost US orders: considered after 45 days from shipping (60 global). No refund if tracking shows delivered. "Return shipping costs are your responsibility." VERIFIED. | MCP server: product search, import, list orders, tracking, trigger fulfillment (asks for confirmation), revocable scoped token. VERIFIED. Public order API: none documented. |
| **CJdropshipping** | Free to use. Optional memberships: Free $0, Plus $15.99, Prime $19.99, Advanced $59.99 per month (ESTIMATED, easync.io, Oct 14, 2026; sources conflict; CJ's membership page blocked us). | Four US fulfillment centers: California, New Jersey, Texas, Indiana (VERIFIED, CJ blog); a second New Jersey warehouse of 120,000 sq ft announced Nov 13, 2026 (VERIFIED, CJ blog). US SKU count: UNKNOWN. One indicator: a "hair brush" search fell from 574 results to 54 with the US ship-from filter (ESTIMATED, easync.io). | US stock: "as fast as 2 to 7 days" (VERIFIED vendor claim). CJ calculator for a 500 g parcel: US stock 3 to 8 days, $9.79 (UniUni) or $13.66 (USPS); China CJPacket Ordinary $12.07, "62% in 4 to 9 days, 93% within 12 days" per CJ's own data (ESTIMATED, easync.io quoting CJ, Oct 2026). Third-party: 5.2 days US, 12 to 18 days China (ESTIMATED, ecommerce-times.com). | UNKNOWN. Qualitative only: "some items cost less" on AliExpress (ESTIMATED, easync.io). | Custom packaging and inserts, but they must be pre-stocked. Moving your own stock into a US warehouse: at least 10 pieces per variant and 100 in total (ESTIMATED, easync.io). | Undelivered-order disputes accepted only 60 days after the parcel leaves the warehouse; product complaints within 30 days of delivery; return shipping is the seller's cost (ESTIMATED, easync.io summarising CJ policy). | Official MCP server (search_products, calculate_freight, get_logistics_timeliness, get_warehouses, create_order, add_to_cart, get_pay_order_list; no pay tool listed). VERIFIED. Public REST API with per-warehouse inventory (VERIFIED Nov 15). |
| **Spocket** | Starter $39.99/mo (25 products), Professional $59.99 (250), Empire $99.99, Unicorn $299.99; 7-day trial. App Store also lists a Free plan that only gives chat support. VERIFIED. | "7+ Million US/EU Products" (VERIFIED vendor claim). US share: UNKNOWN. | Supplier-set. "Majority of suppliers" 1 to 3 bd processing, about 4 to 7 bd US delivery (ESTIMATED, avada.io and dodropshipping.com). Spocket's blog says 2 to 5 bd (vendor claim). | UNKNOWN. | Branded invoice from Professional up. Product branding depends on supplier. VERIFIED. | Set by each supplier (ESTIMATED; Spocket's help article was not readable). | None found. UNKNOWN. |
| **AutoDS** | No free plan. Import $26.90/mo (200 products), Starter $39.90 (500), Advanced $66.90 (1,000); $0.99 to $1 three-day trial. Add-ons: auto ordering $9.90/mo, product finding $14.97/mo. VERIFIED. | An automation layer over other suppliers (AliExpress, Amazon, Walmart, CJ, "private suppliers"). US stock depends on the supplier chosen. | Vendor claims: private suppliers 1 to 3 days (US), CJ US warehouse 3 to 7, AliExpress 2 to 15, China 7 to 15 (VERIFIED as vendor claims, AutoDS blog Dec 29, 2025; no test behind them). | Supplier-dependent. UNKNOWN. | Supplier-dependent. | "Fulfilled by AutoDS": returns only for delivered orders above $10; requests auto-denied at a 5% return rate. VERIFIED. | "Connects directly to AI assistants like Claude via MCP" (VERIFIED, App Store listing). |
| **Syncee** | Free (browse; App Store says 25 products to import), Basic $39.99/mo (100 products, 1 supplier), Pro $59.99 (250), Business $99.99; 3-day trial. VERIFIED. | Supplier marketplace with US, CA, UK, EU, AU suppliers. US count: UNKNOWN. | "Each supplier sets their own conditions"; no standard time (VERIFIED, Syncee help, dated Sep 16, 2024). | UNKNOWN. | Supplier-dependent. | Handled by each supplier under its own policy (ESTIMATED, search summary of help.syncee.com). | In-app "Syncee AI Agent". No MCP or public API found. |
| **DSers + AliExpress** | Basic free (3 stores, 3,000 products); Advanced $19.90/mo; Pro $49.90; Enterprise $499.90; 14-day trials. VERIFIED. | Only AliExpress listings that ship from the US. Share: UNKNOWN. | US-stocked AliExpress listings: 3 to 10 bd or 2 to 7 days (ESTIMATED, vendor blogs, conflicting). China: 15 to 30 days, "usually 2 to 6 weeks" (ESTIMATED, fforder.com, May 13, 2026). "Ships from US" labels can be wrong: check the first tracking scan (ESTIMATED). | This is the AliExpress baseline. Our own Nov 17 data point: a US-stock extender at $76.99 versus $47.50 China-shipped (repo, `data/suppliers.csv`). | None. Seller's packaging. | AliExpress buyer protection. Details not re-read today. | "MCP Connection" on paid plans, "Unavailable" on Basic. VERIFIED. |
| **Doba** | No free plan. Prices shown billed quarterly: Limited $28.67/mo, Basic $57.00/mo ($0.99 seven-day trial), Standard $142.67/mo. VERIFIED. | "Ship from US ... 450K+" (VERIFIED vendor claim). | No figures on the pricing page. UNKNOWN. | "Wholesale prices are often higher" than other platforms (ESTIMATED, third-party review summary). | UNKNOWN. | Return policy URL returned 404. UNKNOWN. | Retailer API on Standard and up. VERIFIED. |
| **TopDawg** | Start-Up $0 (browse only). Business $34.99/mo billed annually, or $49.99 monthly, plus $1.50 per order; Scale $69.99 annual or $99.99 monthly, $1.25 per order; Premier $139.99 annual or $199.99 monthly, $0.75 per order. Per store integration. VERIFIED. | US only: "3,000+ verified U.S. dropshippers", "500,000+ wholesale products"; pet, home, fashion, electronics, health and beauty (VERIFIED vendor claim). | "2 to 5 day U.S. shipping"; "carrier tracking in 1 business day" (VERIFIED vendor claim). | UNKNOWN. US wholesalers, not AliExpress goods. | Branded packing slips from Scale. | UNKNOWN. | API on Premier. |
| **Trendsi** (fashion only) | Free (500 listings); Pro $29.90/mo. VERIFIED. | "US and overseas warehouses", 40K+ products, apparel and accessories. | US products 2 to 5 bd, overseas 5 to 10 bd; shipped within 2 to 10 bd (VERIFIED vendor claim). | UNKNOWN. | Branded invoice, custom branding, private label. | Returns within 7 days of delivery, unworn with tags; swimwear, intimates, jewelry and beauty are final sale. VERIFIED. | In-app assistant. No MCP found. Listed by TikTok as a dropshipping integration. |
| **DropCommerce** | Free (25 products, no fulfillment), Basic $29/mo, Growth $55, Pro $95. VERIFIED. | US and Canadian suppliers only; "real brands". | "Delivery 2 to 7 days" (VERIFIED vendor claim). | Resells other brands. | Branded invoicing from Growth. | UNKNOWN. | None found. |
| **USAdrop** | Free, Pro $29.99/mo, Plus $45.99. VERIFIED. | US warehouse and China. | "US warehouse (2 to 5 days)"; headline "5 to 12 Day Delivery" (VERIFIED vendor claim). | UNKNOWN. | Private label and custom packaging, "no MOQ" (vendor claim). | UNKNOWN. | None found. |
| **AppScenic** | Free (no push to store), Standard $39/mo, Pro $79, Elite $99. VERIFIED. | US, UK, EU, CA, AU suppliers. | UNKNOWN. | UNKNOWN. | UNKNOWN. | UNKNOWN. | None found. |
| **Shopify Collective** | Free app. | Other Shopify brands in the same country. | Supplier-set. | Resells other brands (allowed by CLAUDE.md for add-ons only). | Supplier's brand. | "Returns are seamlessly automated" (vendor claim). | Native Shopify. Retailer needs Shopify Payments "with active payouts" and to meet "trust and fraud criteria" (VERIFIED). Whether a brand-new store passes: UNKNOWN. |

App Store ratings read today (VERIFIED): Zendrop 4.5 (1,303 reviews, 92 one-star); Spocket 3.7 (624, 87 one-star); AutoDS 4.6 (1,392); Syncee 4.2 (559); DSers 5.0 (6,446); Trendsi 4.8 (1,858); TopDawg 5.0 (21 only); DropCommerce 4.7 (134); USAdrop 4.1 (97); AppScenic 3.9 (48); Dropshipman 4.4 (324); HyperSKU 4.9 (316); Shopify Collective 4.5 (500).

Recent one-star themes read today (VERIFIED that the reviews exist; the claims in them are not verified):

- Zendrop, Nov 18, 2026: "delays, lost shipment, product unavailable after placing the order". Nov 10, 2026 (US merchant, 9 months): "Around 85% of our orders were affected by stock availability issues", no reliable inventory sync.
- Spocket, Sep to Nov 2026: four consecutive one-star reviews about unauthorized or hard-to-cancel subscription charges.

### 1b. How each source takes your money (matters for float)

| Source | When the seller pays the supplier | Label |
|---|---|---|
| Zendrop | Card on file is charged wholesale cost plus shipping when the order is fulfilled: on clicking Fulfill (manual), immediately on arrival (auto), or in a daily batch at 7 PM EST. Order credits are applied first if enabled. | ESTIMATED (search summary of support.zendrop.com articles "Order flow explained" and "Fulfillment FAQs"; articles not opened) |
| CJdropshipping | Each order sits in "Awaiting Payment" until the seller pays it. The MCP server can create orders but lists no pay tool. | ESTIMATED (easync.io) for the manual step; VERIFIED for the MCP tool list |
| AutoDS, "Fulfilled by AutoDS" | Prepaid "Managed Balance" that you load yourself ("no automatic recharge"), minimum top-up $50, card or PayPal top-up fee 5%, plus separate "Auto-Order Credits". Cash goes out before the sale. | VERIFIED (AutoDS help article) |
| DSers + AliExpress | Seller pays AliExpress per order with a card. | ESTIMATED (general knowledge of the flow; not re-read today) |
| TopDawg | Product cost plus a $0.75 to $1.50 order processing fee per order. | VERIFIED (App Store listing) |
| Shopify Collective | "Payments are automatically processed when they ship." | VERIFIED (App Store listing) |

### 1c. Corrections and additions versus `research/platform-winners-2026-11-15/platforms.json`

That file was left untouched (it is a dated snapshot). Differences found today:

- Zendrop: a $29 Beginner tier exists on Shopify billing and the Free plan allows zero linked products. The Nov 15 entry listed only Free, Pro and Plus.
- Zendrop: China transit is stated as 10 to 15 business days; refund and return terms are now recorded (above).
- CJdropshipping: an official MCP server exists (Nov 15 recorded the REST API only). US warehouse states are now named.
- AutoDS: plan prices are now readable ($26.90, $39.90, $66.90) and MCP is advertised (Nov 15: "not mentioned").
- Spocket: a Free tier exists on the App Store listing (chat support only); rating is 3.7 with billing complaints.
- HyperSKU: today's App Store listing shows sourcing location China only and "5 to 12 days" worldwide; the Nov 15 entry reported US forward stock from a third party.
- New rows: Doba, TopDawg, Trendsi, DropCommerce, USAdrop, AppScenic, Shopify Collective.

### 1d. Bias notes for this section

- Every "vendor claim" row is marketing. No independent, method-disclosed delivery test was found for any source.
- easync.io sells competing software. ecommerce-times.com shows no disclosure and links to Zendrop pages repeatedly. AutoDS's speed article names AutoDS the winner. fforder.com is a fulfillment vendor.
- The video's creator is a Zendrop partner (see `01_video_decode.md`), which explains why Zendrop is the default in that method. On the facts above, Zendrop is a reasonable choice for US stock, but CJdropshipping (free, MCP, four US warehouses) is the main alternative to price-check for any chosen product.

---

## 2. Does Dhruv need to buy products up front?

**No inventory is bought. But he pays for each order, and for the ads that produced it, before he receives the customer's money.**

### 2a. One order, step by step

| Step | What happens | Timing | Label and source |
|---|---|---|---|
| 1 | Customer pays on the Shopify store by card. Shopify Payments captures the payment. | Day 0 | Card rate 2.9% + $0.30 on Basic is ESTIMATED from `data/channel_params.json`; Shopify's US page did not show rates today ("depend on the subscription plan"). |
| 2 | The order appears in Zendrop. On fulfillment, Zendrop charges Dhruv's card for wholesale cost plus shipping. With "approve every change", this is when he clicks or approves Fulfill. | Day 0 (or next approval) | ESTIMATED (Zendrop help summaries, section 1b) |
| 3 | Meta bills his card for ad spend as it accrues (threshold billing). | Rolling, during the week | ESTIMATED: third-party guides say new accounts are billed at a low threshold such as $25 that rises with history (get-ryze.ai, read 2026-11-21) |
| 4 | Supplier processes and ships. Tracking syncs back to Shopify. | US stock: 1 to 3 bd, up to 5 in Q4 | VERIFIED vendor claim (Zendrop) |
| 5 | Shopify Payments releases the money. "In the United States, the minimum settlement time is 3 business days." "When you begin receiving payouts, your settlement time is longer, but as you reliably fulfill orders on time..." it shortens. "Payouts typically arrive in your bank account within 3 to 5 business days." Banks then need "24 to 72 hours". | Typical: 3 to 5 bd + 1 to 3 bank days. New account: "longer", not quantified. | VERIFIED: https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries/united-states/payouts (read 2026-11-21) |
| 6 | Shopify also says "payouts for new merchants can take up to 5 business days". | | VERIFIED: https://help.shopify.com/en/manual/finance/shopify-balance/payouts/payout-accounts |
| 7 | Community reports: first payout of a new account 7 to 14 days; some new accounts show a "Temporary New-Account Payout Hold"; some stores report holds of weeks. | Anecdotal | ESTIMATED: Shopify Community threads 570994, 646493, 644134 (search summaries, 2026-11-21). The one thread opened had a user statement only, no staff reply. |
| 8 | Customer receives the parcel. | US stock: day 4 to 8 bd (up to 10 in Q4) | VERIFIED vendor claim |
| 9 | Refund or dispute window. A refund comes out of his Shopify balance. Zendrop refunds him only when Zendrop is at fault. | Up to months later | VERIFIED (Zendrop policy) |

Ways to shorten step 5 that Shopify itself names: reliably fulfil on time, and use Shopify Balance as the payout account ("payouts can arrive ... in as little as 1 business day" from the processing date). VERIFIED, same pages. Connecting the bank through Plaid and turning on two-step authentication to reach a 2-day pay period is reported in the community and in older help text (ESTIMATED; today's US page says the minimum is 3 business days).

### 2b. Reserves and holds on a new US store

- "A reserve is a temporary hold on a portion, in some cases a full amount, of transactions processed through Shopify Payments for a specified period." Two types: a fixed amount, or a percentage of transactions. Shopify's own examples: $1,000 held for 120 days; 10% held for 120 days. VERIFIED: https://help.shopify.com/en/manual/payments/shopify-payments/reserves
- Risk factors Shopify lists: extended billing cycles, elevated chargeback activity, increased refund rate, "industries with extended delivery timelines" (events, custom orders, pre-orders), and "significant volume surges". Dropshipping is not named. VERIFIED, same page.
- A brand-new store going from zero to $2,000 in a week during Black Friday is a volume surge by any reading. Whether Shopify would reserve it: UNKNOWN. Community posts describe a 20% reserve placed "because of dropshipping" (ESTIMATED, Shopify Community thread 347340, anecdotal).
- Chargeback: $15 fee in the US, returned if the merchant wins; 7 to 21 days to answer; a decision "can take up to 75 days". VERIFIED: https://help.shopify.com/en/manual/payments/chargebacks/chargeback-process

### 2c. Cash float for about $2,000 of sales in one week

Scratch script: `/tmp/claude-0/-home-user-commerce-os/c2389654-3ee7-5e31-ba87-8e168cf76207/scratchpad/float_and_dates.py` (cash-timing arithmetic only; move into `scripts/` if it is to be kept). Inputs: $2,000 spread evenly over 7 days (Dhruv's target); supplier cost share of revenue is an ASSUMED placeholder range because real Zendrop costs are UNKNOWN.

When the first payout lands, by sale date (script output; VERIFIED Shopify inputs of 3 to 5 bd settlement and 1 to 3 bank days; Thanksgiving Nov 26 is not a business day):

| Sale captured | 3 bd + 1 bank day | 5 bd + 1 bank day | 5 bd + 3 bank days |
|---|---|---|---|
| Mon Nov 23 | Mon Nov 30 (7 days) | Wed Dec 2 (9 days) | Fri Dec 4 (11 days) |
| Fri Nov 27 (Black Friday) | Thu Dec 3 (6 days) | Mon Dec 7 (10 days) | Wed Dec 9 (12 days) |
| Mon Nov 30 (Cyber Monday) | Fri Dec 4 (4 days) | Tue Dec 8 (8 days) | Thu Dec 10 (10 days) |

Because even the best case is about a week, **the whole selling week is paid for before any customer money arrives.** Supplier charges out of pocket (script output):

| Supplier cost share of revenue (ASSUMED) | One $2,000 week | If sales continue at $2,000/week and the first cash lands on day 10 | ...on day 14 | ...on day 21 |
|---|---|---|---|---|
| 30% | $600 | $857 | $1,200 | $1,800 |
| 40% | $800 | $1,143 | $1,600 | $2,400 |
| 50% | $1,000 | $1,429 | $2,000 | $3,000 |
| 60% | $1,200 | $1,714 | $2,400 | $3,600 |

Add to that: the week's ad spend (billed by Meta during the week), the Zendrop subscription ($29/month on Shopify billing, VERIFIED), Shopify ($1/month promo, per CLAUDE.md, verify at signup), the sample, and any refunds. If Shopify applied its example 10% reserve, $200 of a $2,000 week would be locked for 120 days (script output on Shopify's example figure; not a predicted rate).

Plain reading:

- The stated budget of $500 to $1,000 "including ads, apps and samples" cannot also carry the supplier bill for $2,000 of sales in cash. One of three things has to give: the sales target for week 1, the budget, or the payment method.
- The usual way this is bridged is a credit card: supplier and ad charges land on a card whose statement is due after the payouts arrive. That makes the card limit, not the test budget, the real float. This is our reading of the mechanics, not a sourced statistic.
- The risk case is a payout hold. If payouts are held for 2 to 4 weeks while orders keep coming, the card balance grows by the supplier and ad cost of every new order. A hard rule that pauses ads when unpaid supplier and ad charges exceed a set figure would cap this.

---

## 3. Risk mechanics

### 3a. Chargebacks and disputes

| Item | Fact | Label and source |
|---|---|---|
| Shopify chargeback fee, US | $15, returned if you win | VERIFIED, Shopify chargeback process page |
| Visa VAMP, merchant "excessive" level | Ratio 1.5% and at least 1,500 counted disputes plus fraud reports in a month (US and most regions; 2.2% in CEMEA). Shopify: "If you have an extended period of enrollment in VAMP, then your use of Shopify Payments might be restricted." | VERIFIED, https://help.shopify.com/en/manual/payments/chargebacks/monitoring-programs. The drop from 2.2% to 1.5% on April 1, 2026 is ESTIMATED (fraud.net, merchantriskcouncil.org). |
| Mastercard Excessive Chargeback Merchant | 100 to 299 chargebacks and 1.5% to 2.99%; fines from month 2 ($1,000) | VERIFIED, same Shopify page |
| Mastercard MATCH list, code 4 | Chargebacks above 1% of Mastercard sales transactions in a month and totalling $5,000 or more. "Shopify generally can't process for businesses listed on MATCH." | VERIFIED, same page |
| Shopify's own trigger for a reserve or review | No number published. "Elevated chargeback activity" and "increased refund rate" are listed risk factors. | VERIFIED (absence of a number), reserves page |
| "Stay under 1%" | Common advice | ESTIMATED, chargeflow.io and others (vendors of chargeback tools) |
| PayPal dispute fees | Standard $15; High Volume $30; chargeback fee $20. Page "Last Updated: November 4, 2026". | VERIFIED, https://www.paypal.com/us/business/paypal-business-fees |
| PayPal high-volume rule | More than 100 sales transactions in the previous 3 full months and a dispute rate of 1.5% or more. Rate = disputed claim amounts (not received, not as described) over net sales for the previous 3 months. | VERIFIED, PayPal help article help350 |
| PayPal fees for checkout | PayPal Checkout 3.49% + $0.49; standard cards 2.99% + $0.49 | VERIFIED, same fees page |
| PayPal holds for new sellers | "If you have a new PayPal account, it can take time to build up a positive reputation as a seller." Holds of up to 21 days, released about a day after confirmed delivery when tracking is added. | First sentence VERIFIED (PayPal help126). The 21-day figure is ESTIMATED (search summary of PayPal help pages; the article we tried was unpublished). |

What this means at test scale: the card-network programs need 100 to 1,500 disputes a month, so they cannot be triggered by a 30 to 60 order test. The live risk is Shopify's own unpublished review, where one or two disputes on 40 orders is already 2.5% to 5%. Small numbers make the ratio jumpy.

### 3b. Meta: customer feedback and delivery-time rules

- Meta's current name is **customer experience score**. "Customer experience score is one of several signals used in the ad auction... Businesses may see increased costs or improved competitiveness in the auction depending on their score." Dissatisfied or neutral buyers "are asked about issues ... such as unexpected charges, shipping delays, or product quality concerns, as well as any refund attempts and outcomes". VERIFIED: Meta Business Help Center article 1491186119412011 (text returned by Meta's help-article tool, 2026-11-21).
- "There's no fixed score threshold that determines ad delivery." VERIFIED: Meta help article 2281317572404281. The insights dashboard is "rolling out gradually to some verified businesses", so a new unverified business may not be able to see its own score.
- The older scheme (score 0 to 5, delivery penalty between 1 and 2, no advertising below 1) is ESTIMATED from third-party blogs (dodropshipping.com, revealbot.com, bir.ch, read via search 2026-11-21) and may be outdated. One blog reports a rename to "business portfolio feedback score" applied to all advertisers (single source).
- Meta's daily-limit page still says the limit may be readjusted for "low ad quality rankings or low feedback scores on your page or app". VERIFIED, article 563129151097553.
- Delivery-time rule: Meta publishes no maximum number of days. Its best-practice page says "the shipping information you provide should be inclusive of the full amount of time it takes to ship, including handling and processing times, item availability", tracking should be provided, and "if you source goods from suppliers or operate a dropship business, it's important that you maintain quality control". VERIFIED: Meta help article 108127923199330.
- Enforcement for heavy negative feedback "could include ad restrictions, financial penalties or disabling accounts". ESTIMATED: Meta Newsroom post of March 2022 (search summary; not re-read).

### 3c. How shipping time feeds refunds and disputes

- No rigorous study of "refund rate per extra shipping day" was found. UNKNOWN.
- Delayed delivery was the reason most often given by consumers who admitted disputing a real purchase, 18% of them. ESTIMATED: Sift Q4 2025 Digital Trust Index as cited by dropship.io (read via search 2026-11-21; vendor blog).
- One seller anecdote: chargebacks near 1.3% at 16 to 19 day delivery, under 0.5% at about 8 days. ESTIMATED: fulfillment-vendor blog (eboxman.com or dailyfulfill.com, via search summary; single case, vendor with an interest).
- Supplier terms make slow shipping expensive for the seller: Zendrop considers a lost US order only after 45 days from shipping (60 days global), and CJ accepts an undelivered dispute only 60 days after dispatch, while a card dispute or a customer's patience runs out far sooner. So the seller refunds first and recovers later, if at all. VERIFIED (Zendrop) and ESTIMATED (CJ, via easync.io).
- Shopify lists "delayed product delivery" as a chargeback cause and says on-time fulfillment shortens settlement time. VERIFIED.

### 3d. FTC Mail, Internet or Telephone Order Merchandise Rule (16 CFR 435)

All VERIFIED: https://www.ftc.gov/business-guidance/resources/business-guide-ftcs-mail-internet-or-telephone-order-merchandise-rule (read 2026-11-21; FTC notes the page was edited January 2025 for penalty amounts).

- The seller must have "a reasonable basis to expect that it will be able to ship" within the time it states.
- If no time is stated "clearly and conspicuously", the seller must ship "within thirty (30) days after receipt of a properly completed order".
- "Ship" means the parcel "is physically placed in the possession of the carrier". The rule is about shipment, not delivery.
- The clock starts when the order is complete and paid; a card authorization counts.
- If the time cannot be met, a delay notice must go out before the promised date, with a definite revised date (or a statement that none can be given), and a free way to cancel for a "full, prompt refund".
- Delay of 30 days or less: silence counts as consent. Longer or indefinite: the order is cancelled automatically unless the customer agrees.
- A second delay needs a renewed notice, and this time silence is not consent.
- Refunds are due "within seven (7) working days" for card payments.
- Dropshipping does not move the duty: "the person soliciting the order, not the agent fulfilling it, is the seller under the Rule."
- Penalties: "up to $53,088 per violation" (confirm the current figure).

Delivery-time claims (as opposed to ship-time claims) fall under the FTC Act's general ban on deception and under Meta's and the card networks' rules, so both the ship time and the delivery window need a basis.

### 3e. What a compliant shipping policy says

Draft wording only, for Dhruv's approval. The numbers must come from the supplier's stated times for the exact product and be confirmed by his own test order before they are published.

**US stock (Zendrop US supplier, today's stated times):**

> Orders ship from a US warehouse. We hand your order to the carrier within 1 to 3 business days (up to 5 business days between Nov 23 and Dec 31). Delivery then takes 3 to 5 business days. Most orders arrive 4 to 8 business days after you order. You get a tracking number by email when the order ships. If we cannot ship within the time above, we will email you a new date and you can cancel for a full refund.

Notes: Zendrop's own numbers total 4 to 8 business days, not 2 to 8. A "2 to 8 days" promise has no reasonable basis yet. A Christmas-delivery claim needs an order-by date (section 6).

**China-shipped (Zendrop Fulfillment, today's stated times):**

> This item ships from our international warehouse. We hand your order to the carrier within 1 to 5 business days. Delivery takes 10 to 15 business days after that. Most orders arrive 11 to 20 business days after you order. This item will not arrive before Dec 25 if ordered after [date]. If we cannot ship within 5 business days, we will email you a new date and you can cancel for a full refund.

The window must appear on the product page near the buy button and at checkout, not only on a policy page ("clearly and conspicuously"). Every claim in the ad must match it.

---

## 4. TikTok Shop US in late 2026

Primary source for almost everything below: TikTok Shop US Seller University (seller-us.tiktok.com/university), pages read today with their "Updated at" dates.

| Topic | Fact | Label and source |
|---|---|---|
| Who can register | New email and phone; owner 18+; valid US passport, driver license, state ID or green card; "primary business address in the United States". Sole proprietors without an EIN register as Individual Seller with SSN. A tax form is requested by entity type (the page lists Form 1040 for a single-member LLC). The separate "Corporation or Partnership" registration page, which an LLC would use, was not read. | VERIFIED, "How to register as a Sole Proprietorship", updated 05/13/2026 |
| Bank account | Account holder name must "match exactly" the name used at onboarding ("zero-tolerance policy"). | VERIFIED, "Finance & Settlement 101", updated 08/10/2026 |
| Approval time | "Most complete US applications are approved in 1 to 3 business days", 5 to 10 days if documents are incomplete | ESTIMATED, hubfluence.io (undated 2026 guide; a TikTok Shop tool vendor) |
| Probation | Every new shop starts in the New Shop Probation Program. Beginner: up to 50 orders a day and 100 products. Standard 100 and 200. Premium 200 and 1,000. "There is no fixed timeline." The daily cap can be set "significantly lower ... including an OVL of 5" during routine checks. | VERIFIED, "New Shop Probation Program Requirements", updated 08/10/2026 |
| Dropshipping | "You may use third-party fulfillment providers to pack and ship your items, provided that you maintain ownership of the inventory." "U.S.-based sellers cannot use international third-party suppliers or consolidation services." "Do not purchase products from another online retailer and have the order shipped directly to a TikTok Shop customer." No invoices or packaging that identify another seller or supplier. | VERIFIED, "Best Practices for Order Fulfillment" and "Order Packaging Requirements" (updated 09/03/2026) |
| Dropship apps TikTok itself lists | Under "Drop Shipping" in its shipping-app list: CJ dropshipping, Supliful, Trendsi. Zendrop's App Store listing says it "works with TikTok Shop US" (vendor claim). | VERIFIED, "How to Ship TikTok Shipping Orders", updated 08/25/2026 |
| How those two fit together | TikTok names dropship apps as integrations yet requires the seller to own the inventory. Whether a per-order purchase from a US supplier counts as owning it: UNKNOWN. Needs a written answer from TikTok or the supplier before use. | UNKNOWN |
| Dispatch deadline | Regular orders "must be marked as In Transit (for example, scanned by carriers) within 2 business days of Awaiting Shipment". In force since January 26, 2026. | VERIFIED, "Fulfillment Policy", updated 09/28/2026 |
| Auto-cancel | If tracking is not added "within 5 business days of Awaiting Shipment". | VERIFIED, same |
| Delivery deadline | "Delivered within 6 business days of Awaiting Shipment" (Standard and Economy). Express: 3 business days. 95% on time needed to keep a shipping option. | VERIFIED, "Fulfillment Policy" and "Seller Shipping: Overview and Services" (updated 08/12/2026) |
| Late Dispatch Rate | Recommended at or below 4%; "greater than 10%, enforcement actions may be applied". Valid Tracking Rate at least 95%. | VERIFIED, "Fulfillment Policy" |
| US warehouse | No rule says the seller must run a warehouse. Options: Fulfilled by TikTok ("supports most sellers with no minimum requirement"), TikTok Shipping from "their own or third-party warehouses", or Seller Shipping "if you are currently eligible". | VERIFIED, "TikTok Shop US Logistics Services Overview", updated 07/06/2026 |
| Referral fee | TikTok's category page, updated 10/08/2026, still shows 6% for most categories, on (customer payment + platform discount minus tax), shipping fee included in the base. | VERIFIED. Conflict: `data/channel_params.json` carries 8% "since Aug 4, 2026" from delzonic.com (ESTIMATED). Unresolved; the TikTok page is titled "in 2024" and may be stale. Check the Seller Center fee page after signup. |
| When TikTok pays | Clock starts at delivery. Introductory tier ("new or probationary sellers"): 31 days after delivery. Standard 8 days, Accelerated 5 (SPS 3.5+), Express 1 (SPS 4.0+). A reserve portion of each order is also held "for 30 days from the delivery date". | VERIFIED, "Finance & Settlement 101" and "Dynamic Settlement and Reserve Policy" (updated 07/31/2026) |
| Shop Performance Score | Needs "at least 30 orders in 90 calendar days" to exist at all. | VERIFIED, probation page |
| Affiliate samples, free | Open to creators "who have generated sales on TikTok Shop within the last 120 days"; the seller can "approve, reject, or ignore"; the creator must post "within 14 days of receiving the product". The seller pays for the unit and shipping (ESTIMATED, yotpo.com and others). | VERIFIED, "Guide to Samples: Free and Refundable", updated 11/20/2026 |
| Affiliate samples, refundable | The creator buys the product and is refunded if they post within 14 days and reach the seller's sales goal ("usually ... 1 to 3 orders") by day 54. "No seller approval needed." | VERIFIED, same guide |

**Is a first sale within 7 days realistic for a new seller?** Our reading of the VERIFIED rules:

- Account approval plus first listing takes about 1 to 5 business days (ESTIMATED), so a shop can exist inside a week.
- A sale from Dhruv's own videos or from TikTok ads is possible in week 1. A sale driven by affiliates is unlikely in week 1: a creator has to request a sample, receive it (4 to 8 business days from a US dropship source) and then has up to 14 days to post.
- For a dropshipper, every free sample is a full-price supplier order.
- Cash is the bigger problem. An order placed Mon Nov 30 and delivered on the deadline (Tue Dec 8) settles on about Fri Jan 8, 2027 (script output). TikTok Shop therefore cannot recycle cash during a one-week or even one-month test.
- A US-supplier dropship flow has to hit a 2-business-day carrier scan. Zendrop's stated processing is 1 to 3 business days, up to 5 in Q4, so late dispatches are likely in December.

Conclusion for the fast test: TikTok Shop is not the week-1 channel. It is a possible second step once a US source with reliable 1-day dispatch and a clear answer on the inventory-ownership rule exists.

---

## 5. Meta ads for a brand-new store and ad account

| Topic | Fact | Label and source |
|---|---|---|
| Daily spending limit | "Meta sets this limit for most advertisers based on their advertising and payment history." It "typically increases automatically as you build your advertising history, follow our advertising policies, [and] spend up to or near your limits". Meta "may readjust" it if "you have a new business portfolio, ad account, page or app", after a policy violation, or with "low feedback scores". It resets at midnight in the ad account's time zone. The amount is shown under current balance in payment settings. | VERIFIED, Meta help article 563129151097553 |
| Typical starting amounts | $25, $50 or $250 a day for new accounts; one vendor model says about $50 in week one and $250 by week four | ESTIMATED: primescalemedia.com, adadvisor.ai, jonloomer.com (read via search 2026-11-21). Not Meta figures. |
| Learning phase | "This usually occurs after about 50 results in the week after the ad set's last significant edit." During learning, "ad sets are less stable and usually have a higher CPA". Editing during learning resets it. | VERIFIED, https://www.facebook.com/business/help/112167992830700 (read 2026-11-21) |
| Time to stable delivery | No Meta figure beyond the 50-results rule. With a $500 to $1,000 total budget, 50 purchases in 7 days in one ad set will not happen, so the whole test runs in learning or "learning limited". | Our reading of the VERIFIED rule |
| Ad account limit | "New business portfolios can only create one ad account. This goes up to 3 when a campaign delivers and a payment is made." An ad account created in a portfolio "will permanently be a part of that portfolio". | VERIFIED, Meta help article 915885887059947 |
| Business verification | "Required to access certain advertising, developer, billing and spending features." It can only be started when the portfolio is eligible. Needs legal name, address, phone and a working https website that match the legal entity. "A decision ... may take up to 14 business days." Verified status can be revoked for policy violations. | VERIFIED, Meta help articles 2058515294227817 and 1294735268952297 |
| Is dropshipping banned? | No policy names it. Meta's own guidance addresses dropship businesses (quality control, honest shipping times). | VERIFIED for the guidance (article 108127923199330); "no formal ban" is ESTIMATED (agrowth.io and others) |
| Common ban and restriction reasons reported for dropshippers | Misleading or exaggerated claims; product not as described; refund, chargeback and "not received" complaints feeding negative feedback; payment failures; a new account ramping spend fast; and "circumventing systems", which includes opening new accounts or moving assets after a restriction. New accounts linked to a banned one are reported to be disabled within days. | ESTIMATED: dodropshipping.com, leadsie.com, relevantaudience.com, agrowth.io (vendor and affiliate blogs, read via search 2026-11-21). No Meta data. |

### What Dhruv can and cannot reuse from his client work

Can reuse:

- His own Facebook profile and its two-factor login. That profile's standing is the base trust signal for anything he creates.
- His skill: campaign setup, pixel and Conversions API setup, reading results, creative testing.
- A business portfolio he personally owns, if he has one with history. A new ad account there is still a new ad account, but the portfolio is not new. Whether it has a free slot is shown under Business info, "ad account creation limit" (VERIFIED, article 1253008271714847).

Cannot reuse:

- The client's ad account, payment method, Page, pixel or dataset, domain or catalog. They belong to the client's business. Running his own store's ads there would mix billing, policy history and the customer experience score of two businesses.
- The client account's spending limit, learning history or audience data. A new ad account, a new Page and a new pixel all start from zero, and Meta says it may set a lower daily limit for exactly that combination.

Risk to protect: his profile is the common link between the client's assets and the new store. Reported practice is that restrictions follow connections between accounts (ESTIMATED, blogs above). A policy strike on the dropship store is therefore a risk to his client work, not only to the test. That argues for conservative claims, honest delivery windows and keeping the test product well inside the exclusions.

---

## 6. Holiday timing

### 6a. Ad prices around Black Friday (Nov 27) and Cyber Monday (Nov 30), 2026

All ESTIMATED. Every source sells analytics or agency services, and the samples are established brands with holiday offers.

| Source | Sample | Finding |
|---|---|---|
| Lebesgue, posted Oct 16, 2026 (https://lebesgue.io/facebook-ads/are-meta-ads-worth-it-black-friday) | $22.6M of Meta spend by its largest customers, Sep to Nov 2025 | Median brand CPM versus September: +13% by Nov 10, +27% by Nov 20, +53% on Thanksgiving, +84% on Black Friday, +59% for Black Friday week, +71% on Cyber Monday, +48% the next day, +20% two days after. In the same week: conversion rate +48%, cost per purchase 20% lower, Meta-reported ROAS +19%. Home and decor CPM +116%. Range across brands: 51% lower to 172% higher. |
| Triple Whale (via search summary) | Its customer base | Average Meta CPM across BFCM 2025 of $22.26, up 7.6% on 2024; Meta ROAS 2.26 |
| Supermetrics, 2026 retail playbook (via search summary) | 5,000+ retail advertisers | Typical CPMs rose 16% to 41% by Black Friday week, by sector |
| January | Conflicting | Vendor posts say January is the cheapest month (stackmatix.com: November $28.09 falling to $17.12 in January 2026; "November 2025 CPMs 38% above January"). Northbeam's review says CPMs rose 10% to 20% from January 2026. Direction for January 2027: UNKNOWN. |

Reading for a new store: the established brands in that data bought more expensive impressions but converted far better, because they had offers, reviews, returning visitors and trained pixels. A new store has none of those, so it pays the higher CPM without the conversion lift. That is our inference, not a measured fact. The one firm point is that prices fall back fast: by two days after Cyber Monday the premium was down to about 20%.

### 6b. Christmas delivery cutoffs

Carrier dates for the lower 48 states:

| Carrier and service | Send by, for delivery by Dec 25 | Label and source |
|---|---|---|
| USPS Ground Advantage | Thu Dec 17 | VERIFIED, https://www.usps.com/holiday/holiday-shipping-dates.htm ("recommended" dates) |
| USPS First-Class Mail | Thu Dec 17 | VERIFIED |
| USPS Priority Mail | Fri Dec 18 | VERIFIED |
| USPS Priority Mail Express | Sat Dec 19 | VERIFIED |
| FedEx Ground Economy | Dec 15 | ESTIMATED, news roundups of FedEx's 2026 chart (krdo.com/Stacker, Nov 18, 2026); FedEx's PDF refused access |
| FedEx Ground / Home Delivery | Dec 17 (5-day lanes), Dec 18 (4-day), Dec 21 (3-day) | ESTIMATED, same |
| UPS Ground | Not found; reported as not yet published | UNKNOWN |

A dropship order needs the supplier's processing time in front of the carrier date. Script output, using Zendrop's stated times:

| Case | Customer must order by |
|---|---|
| US stock, 1 bd processing, in USPS hands Dec 17 | Wed Dec 16 |
| US stock, 3 bd processing | Mon Dec 14 |
| US stock, 5 bd processing (Zendrop's Q4 peak figure) | Thu Dec 10 |
| US stock, delivered by Dec 24 on "3 bd + 5 bd" | Mon Dec 14 |
| US stock, delivered by Dec 24 on "5 bd + 5 bd" | Thu Dec 10 |
| China stock, 1 bd + 10 bd | Wed Dec 9 |
| China stock, 3 bd + 15 bd | Mon Nov 30 |
| China stock, 5 bd + 15 bd | Wed Nov 25 |

So for a US-stock product a "by Christmas" promise is safe for orders through about **Thu Dec 10**, arguable through Mon Dec 14, and should be dropped after that. For China stock the safe date is effectively already gone for a store that opens next week.

After Christmas, late-December orders run into carrier backlogs and the heaviest return and "where is my order" period, with a new store's first payouts still settling.

---

## 7. Conclusion: US stock versus China-shipped for this test

**US stock.** The evidence, in order of weight:

1. **Channel rules.** TikTok Shop US bars international third-party suppliers for US-based sellers and requires delivery within 6 business days (VERIFIED). China-shipped is own-store only.
2. **Money.** Shopify shortens payout time "as you reliably fulfill orders on time" and lists extended delivery timelines, refunds and chargebacks as reserve triggers (VERIFIED). Suppliers only compensate a lost parcel after 45 days (Zendrop, US) or 60 days (Zendrop global; CJ), so on slow lanes the seller funds the refund for weeks (VERIFIED for Zendrop).
3. **Ad account.** Meta's survey asks buyers about shipping delays and the result changes auction cost (VERIFIED). The ad account is tied to the profile Dhruv uses for client work.
4. **Calendar.** China-shipped orders taken after about Nov 25 to Dec 9 miss Christmas on Zendrop's own numbers; US stock works until about Dec 10 to 14 (script output on VERIFIED carrier dates and vendor times).
5. **The sample.** A US-stock sample ordered on launch day arrives in about 4 to 8 business days, inside the test. A China-shipped sample arrives after the test's first two to four weeks of sales, so the whole test would run blind.
6. **Duties.** Duty-free entry for low-value China parcels ended May 2, 2025; each China parcel now carries duty, while US stock is already landed (ESTIMATED: flexport.com, avalara.com, branvas.com, via search 2026-11-21).
7. **Refund behaviour.** Delayed delivery is the top self-reported reason for disputing a real purchase (ESTIMATED, Sift via vendor blog). Direction is consistent across sources; the size of the effect is UNKNOWN.

What US stock costs:

- A much smaller catalog. One CJ search kept about 54 of 574 results with the US filter (ESTIMATED, single example).
- Higher unit cost. No measured premium was found; our own Nov 17 data point for the extender was $76.99 US-stock against $47.50 China-shipped (repo). Treat the premium as UNKNOWN per product until the actual listing is read.
- No custom branding on Zendrop's US-supplier products, and no supplier-side returns (VERIFIED).
- Stock-outs after the order is placed appear in recent Zendrop one-star reviews (VERIFIED that they are reported).
- "2 to 8 days" is not what the supplier states. It is 4 to 8 business days, and up to 10 in Q4.

When China-shipped is acceptable: only on the own store, for a product with no US stock, outside the Christmas window, with an 11 to 20 business-day window stated on the page and at checkout, and with a per-product check that the stated transit time is real.

Checks that must happen before any delivery promise is published (they need Dhruv's own account, so they are outside this research):

1. For the chosen product: Zendrop and CJ unit cost, shipping cost, ship-from state, stock count and stated processing time, read from the logged-in catalog.
2. One test order to a US address, timed from order to carrier scan to delivery, and opened to check for supplier invoices or branding in the box.
3. Shopify Payments identity and bank verification finished before ads start, and the first payout date read from the admin.
4. The daily spending limit shown in the new ad account's payment settings.

---

## 8. Biggest unknowns

1. Real product cost, shipping cost and stock depth for any specific product on Zendrop or CJ (login required). Without these the float and every later script are placeholders.
2. How long Shopify Payments will take to pay a brand-new store its first payout, and whether a reserve or hold is applied. Official text says "longer"; community says 7 to 14 days; neither is a promise.
3. The actual Meta daily spending limit on Dhruv's new ad account.
4. TikTok Shop referral fee: 6% on TikTok's page (updated Oct 8, 2026) versus 8% reported by third parties.
5. Whether TikTok accepts a US-supplier dropship flow under its inventory-ownership wording.
6. Independent delivery-time tests for US-stock dropship apps: none found with a disclosed method.
7. Product cost premium of US stock over China stock and over AliExpress: no controlled comparison found.
8. January 2027 ad prices: sources conflict.
9. UPS 2026 ground cutoff; FedEx dates are second-hand.
10. Whether a no-return policy on a dropshipped item (Zendrop's suggestion) is acceptable to Dhruv given the "premium" rules and the refund reserve.

## 9. Sources that blocked or failed

- help.shopify.com: headless browser got a Cloudflare 403. WebFetch worked but several guessed URLs (payout schedule, account holds, pay periods) resolved to an overview page; the "account holds" article was not read.
- spocket.co/pricing: WebFetch 403; read with the headless browser.
- doba.com/pricing: headless browser 403; WebFetch worked. doba.com/return-policy: 404.
- cjdropshipping.com/membership: "Human verification" wall. CJ's Shopify App Store URL returned 404.
- FedEx 2026 "Last Day to Ship" PDF: permission error.
- PayPal: the "release payments on hold" article is unpublished; the hold page did not show the 21-day text.
- Meta Business Help Center: the learning-phase page was read in the headless browser; the other Meta articles were read as text returned by Meta's own help-article tool (Meta Ads connector), with the article URLs given above.
- hereweship.com (TikTok dispatch guide): HTTP 500.
- Triple Whale benchmark page: not retried (Cloudflare on Nov 14).
- Zendrop and CJ product catalogs, Zendrop pricing inside the app, Shopify admin, TikTok Seller Center, Meta payment settings: behind logins, not accessed by rule.
- Foreplay: not used; this section did not need ad data.

## 10. Source list

Primary, read 2026-11-21:

- Shopify: https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries/united-states/payouts ; https://help.shopify.com/en/manual/finance/shopify-balance/payouts/payout-accounts ; https://help.shopify.com/en/manual/payments/shopify-payments/reserves ; https://help.shopify.com/en/manual/payments/chargebacks/chargeback-process ; https://help.shopify.com/en/manual/payments/chargebacks/monitoring-programs ; https://help.shopify.com/en/manual/online-sales-channels/shopify-collective/retailers/requirements-and-considerations
- Shopify App Store listings: apps.shopify.com/zendrop , /spocket , /autods , /syncee-1 , /dsers , /trendsi , /topdawg , /dropcommerce , /usadrop , /appscenic , /aliexpress-dropshipping-master , /hypersku , /collective ; one-star review pages for Zendrop and Spocket
- Zendrop: https://www.zendrop.com/pricing ; https://zendrop.com/mcp-server/ ; https://support.zendrop.com/en/articles/14792358 ; https://support.zendrop.com/en/articles/8487356 ; https://support.zendrop.com/en/articles/12088853 ; https://support.zendrop.com/en/articles/10454772
- CJdropshipping: https://cjdropshipping.com/blogs/cj-news/CJ-s-Global-Warehouses ; https://cjdropshipping.com/blogs/business-insights/CJdropshipping-Updates--New-Jersey-Warehouse--TikTok-Shop-Fulfillment---and-Cost-Planning ; https://developers.cjdropshipping.com/en/api/api2/mcp.html
- Other vendors: https://www.spocket.co/pricing ; https://www.autods.com/pricing/ ; https://intercom.help/autods---new/en/articles/12700443 ; https://syncee.com/pricing/ ; https://help.syncee.com/en/articles/8949214 ; https://www.dsers.com/pricing ; https://www.doba.com/pricing ; https://topdawg.com/ ; https://www.trendsi.com/pricing
- TikTok Shop US Seller University (https://seller-us.tiktok.com/university/essay?knowledge_id=...): 7741109863761707 (registration), 3238037484062465 (probation), 4069705271658253 (order volume limit), 3995852763301633 (fulfillment policy), 6179821974439723 (fulfillment best practices), 7131013343053575 (packaging), 8308896260065025 (seller shipping), 6734735776089869 (logistics overview), 2334828973737741 (shipping apps), 5988482086864682 (referral fees), 3995852763531009 (settlement and reserve), 1167036928444174 (finance 101), 5764641632306946 (samples), 2251207540770573 (sample quota), 2960632903649066 (3-day delivery), and the Late Dispatch Rate FAQ
- Meta Business Help Center articles: 112167992830700 (learning phase), 563129151097553 (daily spending limits), 141820733085330 and 764293677236889 (account spending limit), 1491186119412011 (customer experience score), 2281317572404281 (customer experience insights), 108127923199330 (customer feedback best practices), 2058515294227817 and 1294735268952297 (business verification), 915885887059947 and 1253008271714847 (ad account limits)
- FTC: https://www.ftc.gov/business-guidance/resources/business-guide-ftcs-mail-internet-or-telephone-order-merchandise-rule
- USPS: https://www.usps.com/holiday/holiday-shipping-dates.htm
- PayPal: https://www.paypal.com/us/business/paypal-business-fees ; https://www.paypal.com/us/cshelp/article/when-is-the-dispute-rate-applied-and-how-is-it-calculated-help350 ; https://www.paypal.com/us/cshelp/article/why-is-my-payment-on-hold-or-unavailable-help126

Third-party (ESTIMATED), read or summarised 2026-11-21:

- https://easync.io/articles/cj-dropshipping-review/ (Oct 14, 2026; competitor of CJ tools)
- https://ecommerce-times.com/cj-dropshipping-vs-zendrop-in-2026-which-supplier-platform-actually-delivers/ (Aug 10, 2026; no disclosure)
- https://www.autods.com/blog/fulfillment-speed-reliability-autods-zendrop/ (Dec 29, 2025; vendor)
- https://www.fforder.com/post/dropshipping-suppliers (May 13, 2026; vendor)
- https://www.hubfluence.io/tiktok-shop-registration (2026; vendor)
- https://lebesgue.io/facebook-ads/are-meta-ads-worth-it-black-friday (Oct 16, 2026; vendor)
- Shopify Community threads 570994, 646493, 644134, 347340 (anecdotal)
- Search summaries only (pages not opened): avada.io and dodropshipping.com on Spocket times; chargeflow.io; dropship.io citing Sift; stackmatix.com and Northbeam on January CPMs; Triple Whale and Supermetrics BFCM figures; krdo.com/Stacker on FedEx dates; get-ryze.ai, primescalemedia.com, adadvisor.ai and jonloomer.com on Meta limits; dodropshipping.com, leadsie.com, relevantaudience.com and agrowth.io on ad account bans; flexport.com, avalara.com and branvas.com on de minimis; fraud.net and merchantriskcouncil.org on Visa VAMP dates.
