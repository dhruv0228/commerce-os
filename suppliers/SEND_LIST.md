# Supplier send list (Barkfare extender kit)

Status: ready to send once Dhruv says go. Nothing has been sent. Claude never sends supplier messages (CLAUDE.md section 8); Dhruv pastes each one himself.

## How to send (about 15 minutes)

1. Create or log in to a free buyer account on Made-in-China.com (and Alibaba.com for any Alibaba listing).
2. For each row below, open the listing link, click **Contact Supplier** / **Send Inquiry**, and paste the message from the draft file (everything above the `---` line).
3. Replace `[HOME ZIP]` with your ZIP and `[Business email]` with the email you chose.
4. Tell Claude when they are sent. Replies usually arrive in 1 to 3 days; paste or forward them back and Claude logs them in `data/suppliers.csv` and reruns the numbers.

Order matters least; the two recommended sample suppliers are h6 and h9.

| # | Supplier | Where to send | Draft | Sample | MOQ |
|---|---|---|---|---|---|
| 1 | Qingdao Meilianjia International Trading Co., Ltd. (Made-in-China shop qdulinkc) | Made-in-China.com inquiry on listing https://qdulinkc.en.made-in-china.com/product/srHUSGClHJYe/ | `suppliers/dog-car-trav-h1/inquiry.md` | available; price UNKNOWN ("sample costs and shipping may apply") | 50 (ESTIMATED: $8.14 at 50-499, $7.62 at 500-999, $6.24 at 1 |
| 2 | Ningbo Haishu Mango Import & Export Co., Ltd. | Made-in-China.com inquiry on listing https://int-mango.en.made-in-china.com/product/lAYUIhmcgSWC/ | `suppliers/dog-car-trav-h10/inquiry.md` | $50 per piece (ESTIMATED) | 200 ($16.99 at 200-999, $14.99 at 1,000+) |
| 3 | Puyang Selfaiding Industrial Co., Ltd. | Made-in-China.com inquiry on listing https://selfaiding.en.made-in-china.com/product/GgbYqMcTsthr/ | `suppliers/dog-car-trav-h2/inquiry.md` | free existing-style sample under 3 pcs; freight paid by buyer (ESTIMATED) | conflicting: 2 (tiers), 1 (profile), 200 for standard styles |
| 4 | WOR-BIZ Industrial Product Co., Ltd. (Anhui) (Made-in-China shop mokofuwa) | Made-in-China.com inquiry on listing https://mokofuwa.en.made-in-china.com/product/DdSEmVkYHHcL/ | `suppliers/dog-car-trav-h3/inquiry.md` | listing shows $0 (garbled; UNKNOWN) | 500 ($15.00 at 500-999, $14.50, $14.00 at 2,000+) |
| 5 | Shengzhou Tuoke Industry and Trade Co., Ltd. (Made-in-China shop copperwu) | Made-in-China.com inquiry on listing https://copperwu.en.made-in-china.com/product/wZIfmWHJslGT/ | `suppliers/dog-car-trav-h4/inquiry.md` | $30, sample in 3-5 days (ESTIMATED; earlier read said refundable on order) | conflicting 100 or 300 (1 if in stock); price $9.99-39.80, $ |
| 6 | Xiamen Furvorite Pet Supplies Co., Ltd. (Made-in-China shop rongtengpet) | Made-in-China.com inquiry on listing https://rongtengpet.en.made-in-china.com/product/KdLtvznyESfo/ | `suppliers/dog-car-trav-h5/inquiry.md` | $20 per piece (ESTIMATED, garbled text) | 2 ($12.50 at 2-14, $11.00 at 15-29, $9.90 at 30+) |
| 7 | Nanjing Fav Pet Sup Ltd. (Made-in-China shop favpet) (recommended sample) | Made-in-China.com inquiry on listing https://favpet.en.made-in-china.com/product/XxVYTFKPZsRW/ | `suppliers/dog-car-trav-h6/inquiry.md` | $15 per piece (ESTIMATED) | 5 on tiers ($12.40 at 5-99, $12.25 at 100-999, $10.25 at 1,0 |
| 8 | IBSPOT.COM Inc. (Elkins Park, PA), seller of the SucceBuy/LumaCS hard-bottom back-seat extender | contact form or customer service email on ibspot.com | `suppliers/dog-car-trav-h8/inquiry.md` | buy retail | UNKNOWN |
| 9 | Suzhou Offer Gifts Co., Ltd. (recommended sample) | Made-in-China.com inquiry on listing https://szoffer-gifts.en.made-in-china.com/product/MgqYybkEXmVe/ | `suppliers/dog-car-trav-h9/inquiry.md` | $30 per piece (ESTIMATED) | 10 ($19.30 at 10-49, $18.50 at 50-99, $17.72 at 100-199, $16 |

## After replies

- Claude compares quotes, flags red flags and recommends the 2 samples (target: h6 Nanjing Fav Pet, sample about $15, and h9 Suzhou Offer Gifts, sample about $30, plus express shipping; total cap $200, paid through platform escrow or PayPal).
- Dhruv approves the sample orders (a separate approval).
- Samples arrive in about 1 to 2 weeks. Dhruv tests fit in the car, kneels on the platform (sag test), checks the 20-inch fold and films it.


## Added 2026-11-17 (send these too)

| # | Supplier | Where to send | Draft | Why |
|---|---|---|---|---|
| 10 | Guangzhou Doglemi | Alibaba message on its listing | `suppliers/doglemi/inquiry.md` | Minimum order 5: fastest own-brand option |
| 11 | Huizhou Ouqi Intelligent Technology | Alibaba message on its listing | `suppliers/huizhou-ouqi/inquiry.md` | Minimum order 2: fast own-brand option |
| 12 | Ningbo Inbest Homeware | search the company name on Alibaba or Made-in-China | `suppliers/ningbo-inbest/inquiry.md` | Customs records show it supplies 4Knines: proven, for the bigger order |
| 13 | Zhejiang Treasureland Auto | Alibaba message on its listing | `suppliers/zhejiang-treasureland/inquiry.md` | Customs records show it supplies Ruff Liners: proven, for the bigger order |
| 14 | AliExpress seller with US stock (item 3256812096596227) | AliExpress "Message" button | `suppliers/ali-us-76/inquiry.md` | Fast lane: ships from the US, but only 9 sold, so buy 1 to inspect |

Alibaba needs a free buyer account, like Made-in-China.
