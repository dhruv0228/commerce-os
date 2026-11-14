# Supplier validation: dog car travel kit (2026-11-14)

Product: `dog-car-travel-kit` (rigid back-seat platform kit, $149). Stage set to `gate1_approved` in `data/candidates.csv` per Dhruv's Gate 1 universe decision A (reports/decisions.md, Nov 14).
Facts live in `data/suppliers.csv` (rows `dog-car-trav-h1` to `h10`). Scores come from `scripts/score.py` (`reports/ranked_suppliers.md`). Nothing has been sent, ordered or paid.

## Executive summary

- 10 sources are on file: 8 Chinese sellers on Made-in-China.com plus 2 US delivery options. 2 of the 8 are new today (Suzhou Offer Gifts, Ningbo Haishu Mango). No supplier offers our own-brand hero from US stock, so the delivery plan stays the same: air-ship a small batch to Dhruv's home and post orders by USPS. That meets the 2 to 8 day rule only after the stock lands.
- **Every supplier fails the scorecard for now**, because `legitimacy_verified` is `unknown` for all of them. Platform badges and audit IDs are claims until we confirm them and place a sample or test order. Pre-sample scores run from 19 to 41 out of 100, and quality is capped at 15 until a sample is reviewed. This is what the skill expects before samples.
- **No listing matches our spec yet.** Nobody lists a 3-panel rigid board with a sag test, and nobody lists a folded carton of 20 in or less. Every listed package is either unknown or too long or bulky for $14 USPS shipping. The inquiries ask about both.
- **Recommended samples: Nanjing Fav Pet Sup (`h6`) and Suzhou Offer Gifts (`h9`).** Fav Pet lists a 7-layer hard plate rated at 400 lb, has an SGS audit ID and 61 reviews, a $15 sample and a 5-piece tier. Offer Gifts lists a platform of about 52 x 25 in (our Standard size), a TÜV Rheinland audit ID, a $30 sample, MOQ 10, DDP and 20-day production. Sample fees total $45 (ESTIMATED from the listings). Express courier is UNKNOWN; ASSUMED at $40 to $70 per sample. Total about $125 to $185, inside the $250 samples line.
- Qingdao Meilianjia (`h1`) ranks first on score only because it is the cheapest and its package size is unknown, so the script assumed our target carton. It is the third choice if either recommended sample fails the spec in writing.

## 1. Supplier comparison (from reports/ranked_suppliers.md)

| Supplier | Type | Quality /30 | Price /25 | US ship /15 | Response /10 | Packaging /10 | Tech /10 | Total | Basis | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| h1 Qingdao Meilianjia International Trading Co. (qdulinkc) | Trading co.; claims own moulding | 6 | 25 | 3 | | 6 | 1 | **41** | proxy | fail: legitimacy not verified |
| h6 Nanjing Fav Pet Sup Ltd. (favpet) | Trading co. / says manufacturer; est. Aug 2024 | 9 | 21.5 | 4 | | 5 | 1 | **40.5** | proxy | fail: legitimacy not verified |
| h9 Suzhou Offer Gifts Co. (new) | Promotional goods supplier | 7 | 19.3 | 6 | | 6 | 1 | **39.3** | proxy | fail: legitimacy not verified |
| h10 Ningbo Haishu Mango Import & Export (new) | Trading co. | 6 | 21.1 | 5 | | 4 | 1 | **37.1** | proxy | fail: legitimacy not verified |
| h3 WOR-BIZ Industrial Product (mokofuwa) | Trading co. | 5 | 20.5 | 3 | | 4 | 1 | **33.5** | proxy | fail: legitimacy not verified |
| h2 Puyang Selfaiding Industrial | Manufacturer (claim) | 7 | 13 | 7 | | 5 | 1 | **33** | proxy | fail: legitimacy not verified |
| h4 Shengzhou Tuoke Industry and Trade (copperwu) | Factory (claim) | 8 | 15 | 3 | | 4 | 1 | **31** | proxy | fail: legitimacy not verified |
| h5 Xiamen Furvorite Pet Supplies (rongtengpet) | Manufacturer (claim) | 5 | 16.5 | 2 | | 5 | 1 | **29.5** | proxy | fail: legitimacy not verified |
| h7 Amazon Multi-Channel Fulfillment | US 3PL, not a product supplier | | | 12 | | 3 | 8 | **23** | proxy | fail: legitimacy not verified |
| h8 US-warehouse resellers (IBSPOT / SucceBuy, Lehni) | Other brands from US stock | 6 | | 12 | | 0 | 1 | **19** | proxy | fail: legitimacy not verified |

Response points stay blank until suppliers reply. Price points are relative to the cheapest estimated landed cost (h1).

**The best 5 for comparison:** h6, h9, h1, h10 and h2. h2 makes the five despite its score: it has the strongest legitimacy signals (SGS audit, 33 reviews, a free sample under 3 pieces, DDP and FBA experience) but no rigid board and a very bulky package.
**Dropped:** h3 (MOQ 500, 180 lb rating), h4 ($39.80 at MOQ 100 and a 30 to 45 day lead time), h5 (hammock with mattress, lead time up to 3 months).
**Seen but not added:** Anhui Xianwei E-Commerce. Its company profile is lighting and sports products, it lists a placeholder HS code, and its spec does not match. Ningbo Zero Point Co. sells dog door protectors at $4.29 a pair with MOQ 1,000 pairs (ESTIMATED; [listing](https://zeropoint.en.made-in-china.com/product/DFGJudcHZEkZ/China-Car-Accessory-Dog-Car-Door-Protector-for-Car-Pack-of-2.html)). The listing doesn't say how they attach. It is a door-guard price benchmark only, and it supports the $4 assumption. 4Knines sells wholesale on Faire ($100 minimum, $189.99 MSRP), but it is another brand and the 4Knines patents are what we design around. Not a hero source.

## 2. Evidence of legitimacy (all ESTIMATED: listing claims read 2026-11-14, none verified)

| ID | Identity and evidence | Link |
|---|---|---|
| h1 | Qingdao, Shandong. Diamond Member since 2025, "Audited Supplier" (agency not named), verified licence badge, claims 15+ years. No certifications or reviews visible. | [listing](https://qdulinkc.en.made-in-china.com/product/srHUSGClHJYe/China-Pet-Travel-Backseat-Bed-Waterproof-Foldable-Hard-Bottom-Back-Mat-Seat-Extender-for-Dogs.html) |
| h2 | Puyang, Henan (the listing's origin field says Zhejiang, a conflict). Est. 2016. SGS audit QIP-ASR2491747. ISO9001:2015 and CE listed. 5.0 from 33 reviews. | [listing](https://selfaiding.en.made-in-china.com/product/GgbYqMcTsthr/China-Dog-Car-Seat-Cover-Back-Seat-Extender-Large-Space-Pet-Car-Mat.html) |
| h3 | WOR-BIZ Industrial Product Co., Anhui. Diamond Member since 2020, audited (agency not named). | [listing](https://mokofuwa.en.made-in-china.com/product/DdSEmVkYHHcL/China-Factory-Customized-Car-Back-Seat-Extender-Pet-Dog-Car-Seat-Cover-Hammock.html) |
| h4 | Shengzhou, Zhejiang. Gold Member since 2023. SGS audit QIP-ASR253816. ISO14001, BSCI and ISO/TS16949 listed. 5.0 from 3 reviews. | [listing](https://copperwu.en.made-in-china.com/product/wZIfmWHJslGT/China-100-Waterproof-Hard-Bottom-Dog-Car-Seat-Cover-with-Mesh-Window-and-Storage-Pockets-for-Truck-SUV-Car.html) |
| h5 | Xiamen Furvorite Pet Supplies Co., Jimei, Xiamen. SGS audit QIP-ASR237544. Founding year (2018 or 2023) and output figures conflict. | [listing](https://rongtengpet.en.made-in-china.com/product/KdLtvznyESfo/China-Oxford-Leather-Dog-Car-Seat-Cover-Waterproof-Dog-Hammock-Strong-Support-Non-Slip-Printed-Back-Seat-Extender-Animal.html) |
| h6 | Nanjing Fav Pet Sup Ltd., Pukou, Nanjing. Est. 2024-08-22, which conflicts with its "10+ years" claim. SGS audit QIP-ASI2442110. ISO9001, amfori BSCI and CE listed. 5.0 from 61 reviews. | [listing](https://favpet.en.made-in-china.com/product/XxVYTFKPZsRW/China-Waterproof-Premium-Durable-Hard-Bottom-Pet-Dog-Booster-Car-Seat-Cover-for-Back-Seat.html) |
| h9 | Suzhou Offer Gifts Co., Kunshan, Jiangsu. Exporting since 2017, Diamond Member since 2018. TÜV Rheinland audit MIC-ASR2441327. CE listed. 5.0 from 9 reviews. | [listing](https://szoffer-gifts.en.made-in-china.com/product/MgqYybkEXmVe/China-Hard-Bottom-Dog-Car-Seat-Extender-Hammock-Cover.html) |
| h10 | Ningbo Haishu Mango Import & Export Co., Zhejiang. Diamond Member since 2011, audited (agency not named). ISO 9000 and BSCI on the search card. | [listing](https://int-mango.en.made-in-china.com/product/lAYUIhmcgSWC/China-Hard-Bottom-Waterproof-Dog-Pet-Car-Seat-Cover-for-Back-Seat.html) |
| h7 | Amazon MCF. Fees from a third-party table. | [amzprep](https://amzprep.com/amazon-mcf-fees/) |
| h8 | IBSPOT.COM Inc., Elkins Park PA. Retail listing of a SucceBuy/LumaCS honeycomb extender: $70.45, 350 lb (supplier-listed), ships from US. No wholesale terms found. | [listing](https://ibspot.com/products/succebuy-dog-back-seat-extender-with-hard-bottom-mesh-window-storage-pocket) |

To move any supplier to `legitimacy_verified=yes`, we need three things: the SGS or TÜV audit report confirmed on the agency's site, the business licence name matched to the payee, and a protected sample order received as described.

## 3. Scorecards (pre-sample, proxy)

- **Quality (proxy, capped at 15).** h6 scores 9: a 400 lb 7-layer plate, double 600D fabric, an SGS audit and 61 reviews. h4 scores 8: 250 lb, 600D, BSCI/ISO, but only 3 reviews. h2 and h9 score 7. h1 and h10 score 6: hard bottom in the title only. h3 and h5 score 5.
- **US shipping (15).** No factory holds US stock. Points reward a short lead time and a DDP offer: h2 7 (15 workdays, DDP); h9 6 (20 days, DDP); h10 5; h6 4; h1, h3 and h4 3; h5 2. The US delivery options score 12 but cannot supply our brand.
- **Packaging (10).** Points are for listed logo and packaging customization: h1 and h9 6, h2, h5 and h6 5, the rest 4 or lower.
- **Tech (10).** The factories score 1, because we place orders by message and Dhruv ships. Amazon MCF has an order API: 8 (ESTIMATED).

## 4. Landed cost per order (ESTIMATED / ASSUMED; computed per row, not a quote)

Formula, recorded in each row's `landed_source`:
- Hero listing price at the ~50-unit or MOQ tier (ESTIMATED)
- \+ premium-spec uplift $8.50 (ASSUMED)
- \+ add-ons $6.70 (ASSUMED)
- \+ tariff at 27% of FOB (ESTIMATED; HTS classification UNKNOWN)
- \+ air freight of $14 per kit at our target carton, scaled up by chargeable weight for bulky listed packages (ASSUMED)
- \+ packaging $2.50 (ASSUMED)
- \+ USPS Ground Advantage zone 5 (ESTIMATED, Notice 123): $14.30 if the carton fits our target, $18.80 if it is over 22 in long, $23.96 or more if it is over 1,728 cu in.

| ID | Hero listing price | Listed package | Landed per order |
|---|---|---|---|
| h1 | $8.14 (50-499) | UNKNOWN (target assumed) | $60.44 |
| h6 | $12.40 (5-99) | 63 x 44 x 6 cm, 3 kg (24.8 in long) | $70.35 |
| h10 | $16.99 (MOQ 200) | UNKNOWN (target assumed) | $71.68 |
| h3 | $15.00 (MOQ 500) | 56 x 45 x 10 cm (22.05 in long) | $73.65 |
| h9 | $18.50 (50-99) | 60 x 43 x 5 cm (23.6 in long) | $78.10 |
| h5 | $9.90 (30+) | 50 x 40 x 30 cm (3,661 cu in) | $91.67 |
| h4 | $39.80 (MOQ 100) | UNKNOWN (target assumed) | $100.65 |
| h2 | $11.44 (50-199) | 40 x 50 x 50 cm (7,600 cu in) | $115.85 |
| h7, h8 | n/a | n/a | UNKNOWN |

The carton matters more than the unit price. A $3 to $4 difference in hero price is small next to the $5 to $40 swing between a 20-inch fold and the packages as listed. `data/economics_inputs.csv` is unchanged because no supplier has quoted yet. `economics.py` was rerun and the base case is still preliminary: pre-ad contribution $62.37, cushion 1.21, pass. Those inputs assume sea freight and our target carton, not the air-batch costs above. Both get replaced at G5 with real quotes.

## 5. Shipping and return terms

- **Single-order US fulfillment:** no factory offers it. Path: a 15 to 50 kit air batch to Dhruv's home, then USPS Ground Advantage at 2 to 5 days. That meets the 2 to 8 day rule only if we ship from stock already in hand. h2, h9 and Anhui Xianwei list DDP. Air DDP cost and transit are UNKNOWN (the inquiries ask).
- **Blind shipping:** UNKNOWN for all. It matters less for the air batch, since Dhruv repacks, but it applies to any later supplier-to-3PL flow.
- **Returns and defects:** UNKNOWN for all, except h4, which claims a 1-year warranty with no terms given. Every inquiry asks for written terms.
- **Lead times (claims):** h2 15 workdays; h10 about 15 days; h9 20 days; h6 about 1 month; h4 30 to 45 days; h5 up to 3 months in peak season. A Jan 4 test needs samples by early December and the batch landed before Jan 4.

## 6. Sample recommendations (2)

1. **h6 Nanjing Fav Pet Sup.** Its listed spec is closest (7-layer plate, 400 lb, double 600D). Sample $15, a 5-piece price tier, SGS audit ID, 61 reviews. Main doubts: the company is young, the MOQ conflicts (5, 100 or 500), and the 24.8-inch pouch must shrink to 20 in.
2. **h9 Suzhou Offer Gifts.** Its platform is about 52 x 25 in (our Standard size). MOQ 10, 20 days, DDP, TÜV audit ID, sample $30. Main doubts: it is a promotional-goods trader, the board and load rating are not stated, and its 23.6-inch fold is too long.

Order a sample only after a written reply confirms a rigid 3-panel (or comparable) board, a fold of 20 in or less (or a credible change to reach it), and standalone door guards. If either one fails, fall back to h1 (Qingdao Meilianjia: claims its own moulding, which could produce a PP board) or h2 (Selfaiding: free sample, fastest lead time).

Sample cost: listing fees of $15 + $30 = $45 (ESTIMATED). Express courier to the US is UNKNOWN; ASSUMED at $40 to $70 per sample. Expected total about $125 to $185, inside the $250 samples line. Each sample should include the add-ons so the whole kit can be judged.

## 7. Risks and missing information

- **Legitimacy:** every row is `unknown`. The audit IDs are not yet checked on SGS or TÜV sites.
- **Spec:** no listing proves a 3-panel rigid board, a sag test or a 20-inch fold. Expect a custom build and possibly tooling for honeycomb PP panels. Its cost is UNKNOWN.
- **Most sellers here are traders,** not factories (h1, h3, h6, h9 and h10 by their own listings). The real factory and the backup supplier stay unidentified until the replies come in.
- **Cash:** a 15 to 50 kit batch at roughly $60 to $80 landed per order (before USPS) exceeds the $300 working-capital line. This is the heads-up already pending in decisions.md (Nov 13). Dhruv decides at G5.
- **IP:** stock factory designs may copy a Chinese-owned US design patent (USD1005742 and others; see the deep dive). Compare each sample with those figures. 4Knines US 2025/0121780 is pending and broad, so dropping the door guards removes that risk. A patent attorney FTO before production is still advised (not legal advice).
- **Tariffs and HTS:** the listings use 9404.90.40 (h1), 4201 (h4, h5) and 6304.93 (h3). Our estimate assumes 6307.90.98. Classification is UNKNOWN until a broker or ruling confirms it.
- **Not accessible today:** Alibaba product and showroom pages (HTTP 410 or empty), Global Sources (no results via search), 1688 (not reachable without login), CJdropshipping (no listing found via search). Claude in Chrome was not used in this session.

## 8. Draft outreach (status: draft, not sent)

- `suppliers/dog-car-trav-h1/inquiry.md` (Qingdao Meilianjia)
- `suppliers/dog-car-trav-h2/inquiry.md` (Puyang Selfaiding)
- `suppliers/dog-car-trav-h3/inquiry.md` (WOR-BIZ / mokofuwa)
- `suppliers/dog-car-trav-h4/inquiry.md` (Shengzhou Tuoke)
- `suppliers/dog-car-trav-h5/inquiry.md` (Xiamen Furvorite)
- `suppliers/dog-car-trav-h6/inquiry.md` (Nanjing Fav Pet Sup), recommended sample 1
- `suppliers/dog-car-trav-h9/inquiry.md` (Suzhou Offer Gifts), recommended sample 2
- `suppliers/dog-car-trav-h10/inquiry.md` (Ningbo Haishu Mango)
- `suppliers/dog-car-trav-h8/inquiry.md` (IBSPOT, US-stock wholesale; only if Dhruv allows another brand's platform for a test)
- No draft for h7 (Amazon MCF is self-serve with public fees; relevant only once stock exists).

Every factory draft carries the kit spec and asks for:
- unit price at 15, 50, 200 and 500 kits
- sample price, lead time and DDP courier cost
- folded carton dimensions and weight
- load rating and sag test
- materials
- logo and custom carton MOQ
- DDP air to a US home address, with the HTS code
- written defect and return terms
- whether the full kit can be packed as one SKU
- written confirmation that the door guards are standalone

**Answer these before sending (Dhruv):**
1. Brand name and the business email or Made-in-China account to send from, plus the US ZIP for sample quotes. Every draft has placeholders for these. h2 also needs a trademark authorization letter for logos, and our brand isn't registered yet.
2. First batch size to quote and fund: 15 or 50 kits. Will you release contingency above the $300 working-capital line if samples pass? Suppliers will anchor on the quantity we name.
3. Keep the two door guards in the kit, accepting the pending 4Knines application risk with standalone strap-hung guards, or swap them for a travel bowl. Also: may a US-stock other-brand platform (h8) be used for a first test, given CLAUDE.md section 1 says other brands are never the hero?

## 9. Recommended primary supplier

**h6 Nanjing Fav Pet Sup Ltd.,** provisionally, pending its written reply and sample. It has the closest listed spec, the cheapest sample, a low MOQ and the most reviews of the 8.

## 10. Recommended backup supplier

**h9 Suzhou Offer Gifts Co.,** provisionally: the size matches, MOQ is 10 and DDP is offered. h1 Qingdao Meilianjia is next in line. A scale-up backup should be an actual factory; ask h6 and h9 to name theirs.

## Confidence

Medium-low. Every price is a listing claim for a product below our spec, nobody has replied, and no legitimacy is verified.

## Gate 4 decision (appended to reports/decisions.md as pending)

Approve supplier outreach and samples for the dog car travel kit?

- **A (recommended):** Answer the 3 pre-send questions, then send the 8 factory inquiries. Order samples from h6 and h9 only after their written replies confirm the board, the 20-inch fold and standalone door guards. Sample spend capped at $200 from the $250 samples line.
- **B:** Send the inquiries now, but decide on samples only after all replies are in (slower, about a week).
- **C:** Same as A, plus the h8 IBSPOT US-stock inquiry and one retail benchmark unit (~$70) for a no-inventory test path.
- **D:** Pause the extender. No outreach.
