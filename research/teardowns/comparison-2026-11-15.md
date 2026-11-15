# Competitor store comparison (2026-11-15)

Covers our two products: the dog back-seat extender kit ($149, Gate 1 approved) and the dash cam (about $105, product 2). Brand files are in this folder: `ruffliners.md`, `ruffrover.md`, `4knines.md`, `urpower.md`, `rove.md`, `redtiger.md`, `viofo.md` and `vantrue.md`. The per-store JSON and screenshot paths are in `stores/stores.json` in the session scratchpad.

All competitor figures are ESTIMATED (third-party pages read on 2026-11-15) unless marked UNKNOWN. Our own kit contents are ASSUMED until supplier quotes and a sample exist. This file holds no economics; margins and CAC come only from `scripts/economics.py`.

## 1. Executive summary

- **Extender, the leaders' weak points:**
  - Ruff Liners leads on volume and ads (1,133 active Meta ads), but its warranty is only 90 days and its door guards hang from window inserts, the category's most-cited complaint.
  - RuffRover runs the closest kit to ours, but its price display is built on a $363.99 reference price and a return clause that excludes "sale items".
  - 4Knines has the best fit tooling and was on sale at $132.59 at capture, below our $149.
- **Extender, our best angle:** "Fits your car, or we tell you before you buy." A measured fit check, strap-hung door guards that never touch the window, a published sag test and a 1-year warranty with no registration. We do not try to win on price.
- **Dash cam, the leaders' weak points:**
  - REDTIGER leads on volume and ads (85 active Meta ads), but sells the card and hardwire kit separately and states its discount and warranty inconsistently.
  - ROVE promises 1 to 3 day delivery against a 5 to 7 day policy.
  - VIOFO and Vantrue are priced above us and speak to enthusiasts.
- **Dash cam, our best angle:** "Everything in the box" (an install time such as 20 minutes is claimed only after we time it on the sample). Camera, card and hardwire kit in one kit at about $105, a step-by-step install video, and plain-English choice help. The kit specification itself is UNKNOWN until the dash cam deep dive.
- **Confidence:** medium. Prices, policies and page structure were read directly. Review provenance and ad performance are inferences, labeled as such below.

## 2. Dog back-seat extender: side by side

| | Ruff Liners | RuffRover | 4Knines | URPOWER (Amazon) | Us (ASSUMED plan) |
|---|---|---|---|---|---|
| Hero price | $169.99 (compare-at $189.99); XL $189.99 | $159.95 vs "$363.99, save 56%" | $169.99 list, $132.59 sale (22% sitewide) | $39.99; PU version $65.99 | $149 kit |
| Kit or bundle | Bed bundle, 20% off both: $191.98 | Tether and bowl in box; "Complete Setup" with bed $199.92 | No bundle shown | Cover and seat belt | Extender, 2 strap-hung door guards, tether, fur tool, fit card, bag (per hero deep dive) |
| Door protection | Window-insert panels (patent 12,221,024) | Zip-up side walls; DoorGuard 2-pack $39.95 | Patent-pending EZ Open, one zip, no inserts | Zip-on flaps | Standalone strap-hung guards, no window inserts |
| Fit tooling | Vehicle-class picker, 2 sizes | "Universal fit", "email us"; dimensions conflict | Find My Fit, fit quiz, vehicle icons, fit guide | "Measure before ordering" | Year/make/model finder plus a 2-measurement check |
| Shipping | Free; ships in 1-2 days, transit 2-5 days | US warehouses; 3-7 days after order; free threshold UNKNOWN | Free over $99; 5-7 days | Prime | Free; only times we can meet (FTC Mail Order Rule) |
| Returns | 30 days, no questions | 30 days, but "no returns on sale items" in policy | 30 days, buyer pays label unless protection bought | Amazon | 30 days, prepaid label on fit problems (to price in economics.py) |
| Warranty | 90 days (1 year if registered) | Lifetime (defects) | Limited lifetime | 6 months | 1 year, no registration (ASSUMED; set after supplier terms) |
| Reviews | 4.5 / 2,109, Amazon importer | Loox 4.8 / 3,771 (counts differ by page) | Loox 182 | 4.4 / 5,548 | 0 at launch; earned only |
| Trust | Patent, Car and Driver, "100,000 owners" | Lifetime warranty, US stock | Own research, automaker logos, US phone | Amazon's Choice | Published sag test, real-sample video, fit guarantee |
| BNPL | None seen | Afterpay | None seen | Amazon | Shop Pay Installments or equivalent if Amboras supports it (UNKNOWN) |
| Email popup | 10% off | Scratch card, +5% and early access | "Mystery discount", asks vehicle | n/a | Fit check as the capture ("get your fit result by email") |
| Meta ads (Foreplay) | 1,133 active, 2026-11-14 | 69 active, 2,198 inactive | UNKNOWN | n/a | First test after G7 |

### How we beat them

- **Price position:**
  - $149 sits under Ruff Liners' $169.99 and RuffRover's bed bundle.
  - 4Knines' sale ($132.59) and URPOWER ($39.99) are cheaper, so we cannot win on price. The kit must justify the gap with what's in the box and a fit promise.
  - Do not discount to match 4Knines before `economics.py` shows the cushion rule still passes.
- **Offer:** the kit includes the door guards that Ruff Liners builds in, RuffRover sells for $39.95 and 4Knines sells separately. The guarantee: "If it doesn't fit the car you told us about, we pay return shipping." That is a cost line to model, not a free promise.
- **Fit finder:**
  - Year/make/model plus 2 measurements.
  - A clear "not for" list: captain's chairs unless proven, heated seats in use.
  - The verdict goes by email, and the address also feeds the list.
  - This is Dhruv's software edge, and none of the four do measurement-based fit.
- **Shipping promise:** state only what the US source can meet, confirmed by a test order (CLAUDE.md section 2). Show an order, ships and delivered timeline like RuffRover's, built from real carrier data.
- **Reviews strategy (FTC 16 CFR Part 465):**
  - Ask every buyer, not only happy ones, after delivery.
  - Publish negative reviews.
  - Any incentive is disclosed and never tied to a positive rating.
  - No imported reviews of other products (the rule bars reviews of a substantially different product).
  - No staff or family reviews without disclosure.
  - No AI personas. Paid UGC creators are disclosed as paid (16 CFR Part 255).
  - Until reviews exist, use our sag test, install video and fit data as proof.
- **Page sections (proposed PDP order):**
  1. Gallery of the real sample in 3 body styles.
  2. One-line promise.
  3. Fit check, inline.
  4. Size result and price.
  5. What's in the box, with each item's job.
  6. Order-to-delivery timeline.
  7. Guarantee row.
  8. Sag test video against a generic board.
  9. Door guard install, 3 steps.
  10. Reviews (when they exist).
  11. "Not for" list and FAQ.

### 5 concrete things to do better (extender)

1. Ship a measured fit check before add to cart, with a written fit guarantee. Ruff Liners and RuffRover offer only vehicle class or "email us".
2. Use door guards that never go in the window seal, and say why, citing the category complaint with its source. Do not name a competitor or copy 4Knines' research wording.
3. Publish one honest reference price (no compare-at until we have actually sold at it) and no fake countdowns. This avoids RuffRover's FTC 16 CFR 233 exposure.
4. Give a 1-year warranty with no registration step, written into the supplier terms (CLAUDE.md section 2).
5. Publish a sag test and real-weight number filmed on our sample, instead of the 280 lb and 400 lb marketing claims.

## 3. Dash cam: side by side

| | ROVE | REDTIGER | VIOFO | Vantrue | Us (ASSUMED plan) |
|---|---|---|---|---|---|
| Hero near our price | R2-4K front, $119.99 (IMX335); Dual $199.99 | F7NA 4K + 1080P rear, $159.99 vs $189.99 ("-30%" badge on a $30 cut) | A229 Plus 2K+2K, $229.99 on PDP ($159.99 on homepage card) | E1 Pro S 4K front, $129.99 vs $199.99 (meta: $119.99 vs $299.99) | Kit at about $105 (spec UNKNOWN) |
| Card in box | No (Dual: free 128GB) | No; +128GB bundle $199.99 | No; card from $39.99 | No | Yes (ASSUMED) |
| Hardwire kit | Sold separately, $29.99-39.99 | "Free hardwire kit" variant option | $25.99 extra | In bundles only | Yes (ASSUMED) |
| Shipping | "1 to 3 days" banner vs 5-7 business days in policy; no refunds for late shipments | Free over $50; 3-5 business days | Policy: postal, 8-12 business days, duties possible | Ships within 1 business day; 3-5 days; free threshold UNKNOWN | Only verified times |
| Returns | 30 days; who pays return shipping contradicts itself | 14 days no-reason, 30 days "unsatisfied" | 14 days | 30 days, buyer pays return shipping | 30 days |
| Warranty | 1 year | 18 months (homepage says 2 years) | 12 months (18 if registered) | 12 months (18 if registered) | Set after supplier terms (UNKNOWN) |
| Reviews | Ryviu, count not shown; claims 40,000+ | Loox 4.7 / 35; claims 3,500+ five-star | Yotpo 4.9 / 31 | Judge.me, 0 on hero | 0; earned only |
| Choice help | Spec table | 5-question quiz (email gate), compare table, installers | Spec compare, wiring diagram | None | 3-question quiz plus a "will it hardwire in my car" check |
| BNPL | Afterpay | Klarna | None seen | None seen | If Amboras supports it (UNKNOWN) |
| Email popup | R4 waitlist with countdown | Quiz 5%, Black Friday 5% | Expert chat | 5% off | Install guide by email |
| Meta ads (Foreplay) | UNKNOWN | 85 active, 2026-11-15 | UNKNOWN | UNKNOWN | After G7 |

### How we beat them

- **Price position:**
  - About $105 sits below every 2-channel STARVIS 2 option on these sites ($159.99 and up) and below ROVE's front-only $119.99.
  - Amazon prices for the same brands are lower than their DTC prices and were not checked today (UNKNOWN).
  - The test must show buyers accept our kit against Amazon, not against these DTC pages.
- **Offer:** a complete kit, so the customer buys nothing else: camera, card, hardwire kit, trim tool, cable clips and a 12V fuse-tap guide. All four competitors upsell the card and the hardwire kit. Bundle only what passes the cushion rule in `economics.py`.
- **Fit and choice finder:**
  - Three plain-English questions: rear camera? parking mode? rideshare?
  - Then a car-specific install check: fuse box location and cable route video by body style.
  - REDTIGER's quiz shows people use quizzes. Ours ends in a kit, not a model number.
- **Shipping promise:**
  - US stock only, with the promise taken from test orders.
  - Never a banner that contradicts the policy (ROVE).
  - A late-order email offering cancellation, as the FTC Mail Order Rule requires (CLAUDE.md section 9).
- **Reviews strategy:**
  - The same FTC 16 CFR Part 465 rules as the extender.
  - Add customer-submitted footage, with permission, as REDTIGER does.
  - Never present Amazon or other-brand ratings as ours.
- **Page sections (proposed PDP order):**
  1. Real-sample day and night footage clip.
  2. "Everything in the box" price card.
  3. 3-question chooser.
  4. Install-in-20-minutes video, if verified on the sample.
  5. Day and night plate-reading samples from our own unit.
  6. Delivery timeline.
  7. Guarantee row.
  8. Spec table, kept short.
  9. Reviews.
  10. FAQ (SD card care, parking-mode battery drain).

### 5 concrete things to do better (dash cam)

1. Put card, hardwire kit and install tools in one box at one price, so there is no accessory upsell at checkout.
2. Show real footage from our sample (day, night, plate at distance). Never use renders or stock footage (CLAUDE.md section 2).
3. Use one honest price with no inflated "-30%" badges and no auctions, and the same price on every page (REDTIGER, VIOFO and Vantrue all slip here).
4. Make one shipping promise that matches the policy, backed by test orders (ROVE's banner contradicts its policy).
5. Write install help for first-timers (fuse tap, cable routing, parking-mode voltage cut-off) instead of sensor jargon (VIOFO and Vantrue).

## 4. Which business model fits us

**Extender:** RuffRover's model fits a new supplier-direct brand with limited capital:
- one hero kit from a US warehouse,
- a short add-on list (bed, guards, stairs),
- a lifetime-style warranty,
- Afterpay at a $150 to $200 basket.

Its pricing tactics do not fit. Ruff Liners' model (patents, Amazon-first, over 1,000 live ads) and 4Knines' wide vehicle catalog need capital we do not have.

**Dash cam:** a kit-first DTC page plus marketplace or TikTok affiliates fits. The holistic analysis already ranks TikTok affiliates as the dash cam's best channel. REDTIGER-scale SKU breadth and installer networks do not fit an $1,800 budget.

## 5. Risks and unknowns

- Our kit contents, costs, shipping times and warranty terms are ASSUMED or UNKNOWN until supplier quotes and samples exist. Gates G4 and G5 still apply.
- Review provenance at Ruff Liners is inferred from app code and review text, not confirmed.
- Ad counts show activity, not profit or CAC (CLAUDE.md section 3).
- **Access gaps:**
  - Amazon blocked headless browsing (URPOWER data via DataForSEO).
  - Checkout pages were not opened, so payment options come from page code.
  - Foreplay returned no analytics for VIOFO and Vantrue and no brand for 4Knines or ROVE.
- Black Friday pricing (Nov 15 to Dec 1) distorts every price above. Re-check in January before the first paid test.

## 6. Recommended next action

Turn the two angles into drafts for Dhruv's review:
- the extender fit-check spec (questions, measurements, "not for" list),
- the dash cam kit spec, inside the dash cam deep dive.

Then run both through `economics.py`, including the fit-guarantee return cost and the kit's extra parts, before Gate 5.

**Decision for Dhruv (one letter):**
- **A (recommended):** adopt the positioning in this file. Extender: fit guarantee, strap-hung guards, 1-year warranty, $149 with no compare-at price. Dash cam: complete kit at about $105. Feed both into supplier inquiries and economics.
- **B:** same as A, but lower the extender to about $135 to match 4Knines' sale, rerunning the cushion rule first.
- **C:** do the dash cam deep dive before fixing any positioning.
- **D:** revisit the extender because 4Knines' sale price undercuts us.
