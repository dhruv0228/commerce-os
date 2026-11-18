# Skip agents, message low-MOQ factories directly

Research date: 2026-11-18. Built from the notes in `research_notes/How sellers contact suppliers/`. Labels follow CLAUDE.md section 5. Nothing here is a supplier quote, and no message has been sent.

Experienced sellers still find factories the plain way. They search Alibaba and Made-in-China, send one short template to 10 to 30 suppliers, and use free US customs records (ImportYeti) to find the factory behind a competitor once they are ready for bulk. For Barkfare's 5-kit first order, the best route is to message the factories already found with MOQs of 2 to 5 (listed at about $12 to $22 a unit, ESTIMATED), post one free Alibaba request for quotation (RFQ) at the same time, and pay by card through Trade Assurance. Sourcing agents and dropship apps are poor fits right now: agent fees start around $100 per order, about the same as five kits of goods, and CJ's US warehouse needs about 100 stocked units. The first message should be about 130 words: who you are, the product link, a 5-unit trial with an honest next order of 50 to 100, and six questions. Checking a supplier is mostly free: look up the business license, do a live video call, keep every term and payment on the platform, and treat the first kit as the test. The real unknowns are cost, not trust. Every parcel from China now pays duty, the tariff code for a rigid extender is not confirmed, and express freight for a bulky kit has not been quoted. No channel gives own brand, US stock and delivery in under 10 days at 5 units, so speed has to come from paid express shipping, not from the choice of channel.

## Direct platform messaging beats every other channel at 5 units

The common advice in seller guides is simple: start on Alibaba, search the product name plus "manufacturer", and check whether each seller is a factory or a trading company. One 2026 guide puts it bluntly: **"Alibaba is where most Amazon sellers find manufacturers"** ([SellerSprite](https://cn.sellersprite.com/en/blog/amazon-fba-alibaba-supplier-guide-2026)). Jungle Scout's founder messaged **10 to 20 suppliers with the same template** and logged every reply ([Jungle Scout](https://www.junglescout.com/blog/how-to-find-alibaba-suppliers/)). Alibaba's RFQ adds a second, free path: you post one spec, and suppliers who want the job send quotes. Free accounts get **10 RFQ quotes** ([Wise, 2022](https://wise.com/us/blog/alibaba-rfq)). Direct messages let you pick who you contact, while the RFQ brings in suppliers you missed. Operators use both, then shortlist 2 or 3.

The low-MOQ suppliers already in the repo fit a 5-unit order: Nanjing Fav Pet (MOQ 5, $12.40), Xiamen Furvorite (MOQ 2, $12.50), Huizhou Ouqi (MOQ 2, $17.88 to $26.87) and Guangzhou Doglemi (MOQ 5, $21.67). All are listing prices, ESTIMATED, and only "reference" prices until a supplier quotes (`suppliers/SEND_LIST.md`, `research/sourcing-2026-11-17/README.md`). None showed US stock.

Customs records are the standard way to find the factory behind a known brand. You find the brand's legal importer, search it on **ImportYeti (free)**, and review its suppliers and shipment volume ([MyWifeQuitHerJob](https://mywifequitherjob.com/importyeti/)). The data covers only US sea imports, importers can hide their records, and contact details are often missing, so operators then look up the factory on Alibaba or its own site ([Bellingcat toolkit](https://bellingcat.gitbook.io/toolkit/more/all-tools/importyeti)). The repo already used this to find Ningbo Inbest (behind 4Knines) and Zhejiang Treasureland (behind Ruff Liners). These are good private-label partners for bulk, but big-brand factories are unlikely to accept 5 units.

US options are fast but not ours. A hard-bottom extender on IBSPOT costs **$70.45 and ships from a US warehouse in 3 to 7 business days**, but it is someone else's product ([IBSPOT](https://ibspot.com/products/succebuy-dog-back-seat-extender-with-hard-bottom-mesh-window-storage-pocket)). US makers on Maker's Row quote typical MOQs of **25 to 500+** ([Maker's Row](https://makersrow.com/blog/best-small-batch-manufacturers-usa/)), and Faire sells other brands' finished goods ([Faire](https://faire.com/blog/buying/retailer-guide-to-buying-on-faire)).

| Rank | Channel | Fit for the 5-kit order | Private label later | Verdict |
|---|---|---|---|---|
| 1 | Alibaba and Made-in-China direct messages to MOQ 2 to 5 factories | Free; MOQ already fits | Yes, same supplier | Use now |
| 2 | One Alibaba RFQ | Free; widens the field | Yes, if you say so in the spec | Use now, in parallel |
| 3 | US-stock resale (IBSPOT, AliExpress US-ship) | 3 to 7 days, but $66 to $77 a unit | No | Only for a fit check |
| 4 | Customs-record factories | MOQ likely too high | Best fit | Save for bulk |
| 5 | CJdropshipping | US stock needs about 100 units | Packaging, then volume | Later |
| 6 | Sourcing agents | Fee about equals the goods | Strong at bulk | Later |
| 7 | Zendrop, Spocket, Syncee | No sign they carry this product | Packaging only | Skip |
| 8 | US makers, Faire, trade shows | MOQ, cost or travel too high | Varies | Skip |

This ranking is judgment from the notes, not a `score.py` output.

## Agents and dropship apps cost more than five kits

Sourcing agents earn their fee on bulk orders, not tiny ones. Jingsourcing's Basic plan charges **5% with a $100 minimum**, plus **$25 per product** under $500 ([Jingsourcing](https://jingsourcing.com/pricing/)). Leeline charges a **$100 flat fee under $1,000**, paid upfront ([Leeline, 2023](https://www.leelinesourcing.com/pricing/)). Industry minimums run **$150 to $450 per order**, and many agents refuse commission work under $5,000 ([Maple Sourcing](https://maplesourcing.com/china-sourcing-agent-fees-complete-cost-breakdown.html)). Five kits at the listed prices are roughly $60 to $110 of goods, so the fee would match or exceed the product cost. Agent-run sites themselves say a small test order "may not be cost-effective" and that you should try factories yourself first ([Supplyia](https://www.supplyia.com/what-is-a-sourcing-agency/)). Agents become useful at the 50 to 100 unit order: factory checks, inspections and access to 1688, which is claimed to be **10% to 40% cheaper** than Alibaba but is in Chinese only ([SellerSprite](https://cn.sellersprite.com/en/blog/amazon-fba-alibaba-supplier-guide-2026)).

CJdropshipping claims **3 to 6 day** US delivery from its US warehouses ([CJ blog](https://blog.cjdropshipping.cn/detail/Unlock-3-Day-Delivery-with-CJ-s-New-US-Warehouses)), but stocking your own branded goods there usually needs **about 100 units, 10 per variant** ([Super-DS](https://super-ds.com/blog/cjdropshipping-review-2026)). Reviewers report agents not replying "in days" ([Trustpilot](https://ca.trustpilot.com/review/cjdropshipping.com?page=5)). CJ's catalog search was blocked by a bot check in this session, so whether CJ stocks a hard-bottom extender in the US is UNKNOWN. Zendrop, Spocket and Syncee resell catalog items; no source showed them custom-sourcing a product at 5 units.

## A 130-word message with six questions gets usable replies

Templates from 2015 to 2026 share one shape: a one-line business intro, the product link or photo, and a short numbered list of commercial questions ([Jungle Scout](https://www.junglescout.com/blog/evaluate-alibaba-suppliers/); [Sourcing Pioneer](https://sourcingpioneer.com/the-ultimate-alibaba-for-beginners-guide/)). A current guide says **"A strong first message is usually 120 to 180 words, plus a short numbered question list"** ([SellerSprite](https://www.sellersprite.com/en/blog/How-To-Reach-Out-To-Alibaba-Suppliers-Like-A-Pro)). Alibaba says to share everything up front because of time zones ([Alibaba](https://activity.alibaba.com/ggs/how_to_send_an_effective_inquiry_on_alibaba.html)). Sourcing agents disagree: suppliers answer only a few points, so hold the rest for round two ([Cosmo Sourcing](https://www.cosmosourcing.com/blog/questions-to-ask-suppliers-on-alibaba)). The fix is to give full product details but ask only the questions that decide whether to continue.

Asking for prices at three quantities does double duty. A small price drop between tiers suggests a reseller; a steep drop suggests a real production line ([Sourcing Pioneer](https://sourcingpioneer.com/the-ultimate-alibaba-for-beginners-guide/)). What to leave out matters just as much. Calling yourself a small startup signals tiny orders and price pressure ([Global From Asia](https://globalfromanywhere.com/getting-factory-responses)). A target price belongs after the first quotes, not before ([QualityInspection.org](https://qualityinspection.org/target-price-chin/)). Instead of hiding the small order, operators **name it as a trial and offer a higher unit price** for it, tied to a realistic next order ([Sourcing Pioneer](https://sourcingpioneer.com/the-ultimate-alibaba-for-beginners-guide/)). One guide says to type 1,000 units in Alibaba's quantity box ([SellerSprite](https://www.sellersprite.com/en/blog/How-To-Reach-Out-To-Alibaba-Suppliers-Like-A-Pro)), but on a $1,800 budget that would overpromise; 50 or 100 is honest. Sign as a business with a name and role ([SaleHoo](https://www.salehoo.com/blog/why-dont-suppliers-reply-to-my-emails-and-how-to-fix-it)). "Founder" is accurate; "Purchasing Agent," which Jungle Scout once used, is not for a one-person company. A brand-domain email is best practice, and a personal email works until the domain exists. Do not put a home address, ZIP or phone number in a first message; "Florida, USA" is enough to price shipping.

None of the published templates were written for a DTC brand, so they skip US stock and US delivery time. Those come first for Barkfare because CLAUDE.md section 2 requires US delivery. The draft below is for Dhruv's approval and has not been sent.

> Hi [contact name],
>
> I'm Dhruv, founder of Barkfare, a US dog-travel brand selling online. We're interested in your [product name] ([link]) as a kit under our own brand.
>
> We'd start with a 5-unit trial order, then 50 to 100 units per order if the trial goes well.
>
> Could you tell me:
> 1. Unit price at 5, 50 and 100 units
> 2. MOQ, and whether a 5-unit trial is possible (we can pay a higher unit price for it)
> 3. Do you have US warehouse stock? Shipping cost and time to Florida, USA (express, duties paid if possible)
> 4. Can you add our logo, and the MOQ for that?
> 5. Production lead time
> 6. Are you the factory or a trading company?
>
> We're comparing a few suppliers and will decide within 2 weeks.
>
> Thanks,
> Dhruv Patel, Barkfare

Round two, only for suppliers who answer well, covers blind shipping and packaging, payment terms, return and defect terms, carton size and weight, certifications, and whether the sample fee is refunded on a bulk order. Cosmo Sourcing also suggests asking for a photo of one specific detail, which forces the supplier to shoot a real unit ([Cosmo Sourcing](https://www.cosmosourcing.com/blog/questions-to-ask-suppliers-on-alibaba)).

Expect few useful replies. In Jungle Scout's case, **21 factories were messaged, 14 replied and only 3 were worth pursuing** ([Jungle Scout](https://www.junglescout.com/blog/evaluate-alibaba-suppliers/)). A vendor calls a 30% to 60% reply rate normal, with no data behind it ([SellerSprite](https://www.sellersprite.com/en/blog/How-To-Reach-Out-To-Alibaba-Suppliers-Like-A-Pro)). A 5-unit ask will likely do worse, so 15 to 20 messages for 3 to 5 good answers is a fair target. Send during China office hours, about 9am to 6pm there ([Sourcing Pioneer](https://sourcingpioneer.com/the-ultimate-alibaba-for-beginners-guide/)), which is about 8pm to 5am in Florida. No source tested follow-up timing; practitioners suggest a nudge after 2 to 3 days ([Owl Sourcing](https://owlsourcing.com/chinese-suppliers-ignore-your-inquiries/)) and a last try within a week ([Supplyia](https://www.supplyia.com/?p=3168)). A one-line nudge on the same thread works: "Hi [name], following up on my message. Could you answer questions 1, 3 and 6? Thanks, Dhruv." Then drop the supplier.

Many suppliers reply faster on WhatsApp or WeChat, and moving there is not a scam signal by itself. The risk is paying off the platform ([Supplyia](https://www.supplyia.com/?p=3168)). Alibaba says disputes rely on evidence from its own chat ([Alibaba seller blog](https://seller.alibaba.com/blogs/2026/southeast-asia/b2b-trade/trade-assurance-complete-guide-alibaba-secure-payment)), so copy any agreed price, spec or date back into the Alibaba thread and the order.

## Verification is free until the bulk order

Trade Assurance holds the money **"in escrow and released to the supplier after the product is received and confirmed"**, and covers defects, wrong items, non-shipment and late shipment ([Alibaba](https://tradeassurance.alibaba.com/)). It protects only what is written in the on-platform order and only money paid through Alibaba. Wires to other accounts, WeChat Pay and similar are not covered ([Epic Sourcing](https://www.epicsourcing.co/post/24-04-how-to-use-alibaba-trade-assurance-a-buyers-safety-guide)). Third-party guides say buyers have **about 30 days from delivery** to open a dispute and pay **about 2.99%** for card payment (both ESTIMATED) ([Jingsourcing](https://jingsourcing.com/b-how-to-use-alibaba-trade-assurance/)). It is mediation, not a promised refund: one seller got a different product and no refund ([Cosmo Sourcing](https://www.cosmosourcing.com/blog/12-common-supplier-scams-how-to-avoids-fraud-when-sourcing)). Made-in-China's version holds payment too, but its buyer terms state no dispute window and no late-shipment cover ([Made-in-China terms](https://m.made-in-china.com/trade/agreement.html)), so prefer Alibaba when a supplier is on both.

Badges mean less than they look. Gold Supplier is a paid membership ([Alibaba seller blog](https://seller.alibaba.com/blogs/2026/southeast-asia/dried-fruit/gold-supplier-10-years-partnership-guide-alibaba-b2b)). Verified Supplier means an inspector such as **Bureau Veritas or TUV Rheinland** confirmed the company exists and its stated business type ([Alibaba](https://activities.alibaba.com/alibaba/buyer/ab/safety_security/products/verification_services.php)). It does not prove the company makes this product, and a trading company can hold the same badge. Ask for the audit report PDF itself. The stronger check is the business license: look up its 18-character code on China's official registry, **gsxt.gov.cn** (Chinese, with a CAPTCHA), or on Qichacha or Tianyancha, and match the legal name, status, address and business scope ([Hicom Asia](https://www.hicom-asia.com/how-to-check-chinese-company-necips/); [Sino Shipping](https://www.sino-shipping.com/th/sourcing-procurement-china/compliance/how-to-verify-supplier-business-licenses/)). The registration date shows true company age. Any mismatch between license, contract and bank name is a reason to stop ([New Buying Agent](https://www.newbuyingagent.com/resources/how-to-read-a-chinese-business-license-and-verify-a-supplier)).

The red flags that recur across sources are: a request to pay off the platform or to a personal account, a **late change of bank details**, a payee name that differs from the licensed company, urgency, a price far below other quotes, and refusal to sell a sample ([Epic Sourcing](https://www.epicsourcing.co/post/how-to-avoid-alibaba-scams-red-flags-us-importers); [Cogoport](https://www.cogoport.com/en/blogs/how-to-avoid-china-supplier-scams); [Cosmo Sourcing](https://www.cosmosourcing.com/blog/12-common-supplier-scams-how-to-avoids-fraud-when-sourcing)). Small first orders fail more often from **quality fade** (good sample, worse bulk), price hikes after ordering and surprise shipping charges than from outright theft ([Cosmo Sourcing](https://www.cosmosourcing.com/blog/alibaba-scams-common-scams-when-fba-product-sourcing)). For this product, also distrust "fits all cars", load ratings with no test report, and "US warehouse" with no address. A live video call showing this exact product is our own rule (ASSUMED), not a sourced one, but it costs nothing and CLAUDE.md already requires photos of the real sample.

| Check | When | Cost |
|---|---|---|
| License lookup, audit PDF, video call, payee name match | Before any money | Free |
| Specs, kit contents, plain packaging, ship-by date written in the Alibaba order | Before paying | Free |
| Pay by card through Trade Assurance | 5-kit order | About 2.99% (ESTIMATED) |
| Unboxing video, measure, load test; keep one kit unopened as the "golden sample" | Week of arrival | Free |
| Dated photos and video of packed goods before paying the balance | 50 to 100 unit order | Free |
| Third-party inspection, one man-day | 50 to 100 unit order, new factory | About $200 to $350 (ESTIMATED) |

The inspection estimate comes from third-party sources; QIMA only quotes on request ([QIMA](https://qima.com/consumer-products/product-inspections); [Supplyia](https://www.supplyia.com/inspection-company-in-china/)). It is not worth it at 5 units. For a US supplier there is no escrow, so the checks are a state business-registry search, a real warehouse address, a test order with tracking, and paying by credit card.

## Every parcel from China now pays duty, and the tariff code is unknown

Duty-free entry for small parcels ended for China on **May 2, 2025** ([UPS](https://www.ups.com/cn/en/shipping/international-shipping/tariffs)) and for all countries on **August 29, 2025** ([CBP](https://content.govdelivery.com/accounts/USDHSCBP/bulletins/3f01456)). So even a 5-kit express box to Florida is a dutiable entry with a brokerage fee. After the Supreme Court struck down the IEEPA tariffs on February 20, 2026, Chinese goods carry the normal duty, the original Section 301 duties (25% on Lists 1 to 3), and a **12.5% Section 301 tariff in force since July 24, 2026** ([China Briefing](https://www.china-briefing.com/news/us-china-tariff-rates-2025/)). The latest source is from July 2026, so any November changes are UNKNOWN.

The tariff code decides the rate. CBP classed a fabric rear-seat protector under **8708.99.8180**, at 2.5% plus 25% Section 301 ([CBP ruling N325857](https://open-gov.usebase.io/rulings/N325857)). If the rigid kit lands there, the stack is about 40% of declared value before brokerage (ESTIMATED). A rigid platform could class differently, and some 8708 codes may fall under Section 232 programs ([Federal Register](https://public-inspection.federalregister.gov/2025-15819.pdf)). The code is UNKNOWN until a customs broker reviews the spec. Ask each supplier for an express quote with duties paid (DDP) and a second quote without duties (DAP), and never accept an under-declared invoice value, since that legal risk falls on the importer.

## Dhruv's decision: send, widen, or wait

No `economics.py` run is possible yet. Landed cost needs real unit quotes, express freight and the duty rate, and all three are UNKNOWN. Confidence in this report is **medium**: the advice is consistent across sources, but most sources are agent or tool vendors with something to sell, Reddit and YouTube could not be reached, and no source measured reply rates.

A (recommended). Approve the short message above for the low-MOQ suppliers already drafted in `suppliers/SEND_LIST.md`, plus one free Alibaba RFQ. Ask a customs broker for the tariff code at the same time. No money moves.
B. Do A, and also buy one US-stock extender (about $66 to $77, ESTIMATED) for a 3 to 7 day fit check. Faster hands-on test, but it spends sample money on a product we would not sell and departs from the "first kit is the sample" plan.
C. Hire a sourcing agent now. Not advised at 5 units.
D. Hold all outreach until the tariff code and express cost are known.

## Conclusion

Finding a supplier is the easy part. The project already has four factories whose listed MOQs fit, and the free channels work. The hard part is the landed cost of a rigid, bulky kit sent by express into a market where every parcel now pays duty. That makes question 3 in the first message the most important one, and it means the broker check should run alongside outreach, not after it.

A 5-unit order is far below the 100 to 200 units most sellers start with ([Helium 10](https://www.helium10.com/project-x/sourcing-product-for-amazon-fba/)), so suppliers will treat it as samples at sample prices. That is fine if the supplier who says yes to 5 can also do the logo at 50 to 100. Asking about logo MOQ now, rather than later, turns the trial into the first step of private label instead of a dead end. At the bulk stage the playbook changes: customs-record factories, a paid inspection and possibly an agent start to earn their cost.
