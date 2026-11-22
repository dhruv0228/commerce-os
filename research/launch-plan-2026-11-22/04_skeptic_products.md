# Skeptic check: the nine shortlisted products (2026-11-22)

Role: skeptic. I re-opened the sources behind each scout's top 3 and tried to break the case on
four points: is the selling price one that other sellers really get, is the US-stock cost real and
repeatable, is the demand real, and is there a safety, patent, trademark or house-rule problem.
I did not edit the candidate files. Corrected values are listed per product and in the answer to
the workflow.

Labels: VERIFIED means I read it on a primary page or platform data today (AliExpress search cards,
DataForSEO Amazon data, store product JSON, Printful API). ESTIMATED means a third-party figure or a
Google result snippet I did not open. ASSUMED means our own placeholder. UNKNOWN means not found.
No margins are computed here. All math stays in `scripts/economics.py`.

## How I checked (all read 2026-11-22, about 15:00 to 15:10 UTC)

- AliExpress US: 8 fresh searches with the ship-from-United-States filter in headless Chromium
  (same method as the scouts). I matched the scouts' cited item ids on the cards. Item pages were not
  opened (captcha on 2026-11-21), so stock depth and shipping come from card tags only.
- Amazon: DataForSEO `amazon/products/live/advanced` on 9 keywords (100 results each) and
  `amazon/asin/live/advanced` on 9 cited ASINs. The ASIN endpoint returns price, ratings and Best
  Sellers Rank but no "bought in past month", so badge counts come only from the keyword scans.
- Google search volume: DataForSEO Google Ads search volume for 11 keywords (ESTIMATED by nature).
- Temu, TikTok Shop and patents: Google result snippets through DataForSEO SERP. Temu and TikTok
  pages were not opened.
- Store JSON: crownandpaw.com, hatoriknives.com, 4knines.com (two products); Printful public API
  `api.printful.com/products/3` and printful.com/shipping.

What blocked me:
- Google Patents pages and its query endpoint returned a "Sorry..." bot page. FreePatentsOnline reset
  the connection. So patent facts come from Google snippets only (ESTIMATED), not from the patent
  documents. This is not a clearance.
- Temu prices: only a few snippets carried a price. TikTok Shop: snippets only; I could not reproduce
  the scouts' larger sold counts.
- Printful medium-canvas US shipping rate did not parse from the page, so the scout's $10.79 was not
  re-read.
- Four SERP queries came back with no organic items (HORL and Tumbler patent searches, one Temu and
  one TikTok query).

## Pattern across all nine

In every case, the price used as "proven" belongs to a brand with reviews or a TV story (4Knines,
Ruff Liners, Kurgo, Quntis, ThermoMaven, Crown & Paw, Hatori, Gbnryg). The same generic item sells
with volume on Amazon, TikTok Shop or Temu for about one third to one half of that price, often
close to our US-stock cost. Three of the cited US-stock costs are not repeatable today (1 to 3 units
left, or a new-shopper price only). Two candidates sit next to live patent portfolios (4Knines,
K9 Sport Sack).

## barkfare-addons

### waterproof-dog-hammock-seat-cover

| Question | Verdict | What I found |
|---|---|---|
| Price ($69 proposed kit) | Partly holds | 4Knines Dog Rear Seat Cover with Hammock, Regular, $79.99 in all three colors (VERIFIED, 4knines.com product JSON). Amazon B00DQFZGZ0 (4Knines Heavy-Duty Rear Seat Cover) $79.99 with 300+ bought past month, 6,168 ratings, #61 in Dog Car Seat Covers (VERIFIED). Ruff Liners B0DSK1Y9J6 $109.99, 403 ratings, title "As Seen on Shark Tank" (VERIFIED price; its 500+ badge was not in my scan). Generic twins: URPOWER $23.98 with 9,000+ (47,000 ratings), URPOWER $33.99 with 1,000+, Mancro $18.04 with 2,000+ (VERIFIED). TikTok Shop snippet "58 sold, $24.00"; Temu snippet "$16.49" (ESTIMATED). A $69 no-name kit has no seller proving it. |
| US-stock cost ($24.58) | Partly holds | Cited card 3256812679473069 now shows $16.58 only as "New shoppers save $47.86" (473 sold, free shipping, 6-day tag). The $24.58 non-promo price could not be reproduced, so the repeat price is UNKNOWN. Other non-promo US cards: 3256812347350787 $21.75, 20 sold, free shipping, 6 days; 3256813271434686 $27.60, 5 sold, free shipping (VERIFIED cards). The two seat belts in the kit are still not costed (UNKNOWN). |
| Demand | Holds | "dog car seat cover" 12,100 a month, "dog hammock for car" 4,400 (ESTIMATED, Google Ads). Amazon volume is large, but almost all of it is under $40. |
| Rules and IP | Flag | Google Patents snippets list 4Knines, LLC as owner of design patents titled "Seat cover with floor hammock", "Split bench seat cover", "Split cover for a vehicle interior" (USD1116542S1), "Cover adaptable to foldable vehicle seats" and "Vehicle door guard", cited from USD851963S1 and USD904798S1 (ESTIMATED, pages not opened). US7677662B2 covers a hammock-style seat cover (status UNKNOWN). Ruff Liners US 12,221,024 (door protection) was already noted. Pick a supplier design that does not look like a 4Knines split or floor-hammock layout. No battery, no heat. |

Corrected values: repeatable US cost UNKNOWN; best non-promo US cards $21.75 (20 sold) to $27.60
(5 sold), plus seat belts UNKNOWN. Price proven for a generic hammock: $23.98 to $33.99.

### suv-cargo-liner-dog

| Question | Verdict | What I found |
|---|---|---|
| Price ($69 proposed) | Does not hold for the costed item | 4Knines Cargo Liner for SUVs, Small, $79.99 (VERIFIED JSON; no sales count). Amazon volume for liners sits at $27.99 to $45.89: B08LPJB9KK $33.23 with 1,000+; ALLANSING $39.94 with 700+ and B0GG8TXTY6 $45.89 with 500+ (the scouts' "top listing", not a $90 liner); B0755DRHSL $27.99 with 400+ (VERIFIED). The $90.09 (RYNVALE XL, 200+) and $95.99 (XL with foam side walls, 200+) listings exist (VERIFIED) but are XL liners with cushioned or foam walls, a different spec from a $21 Oxford trunk mat. |
| US-stock cost ($21.42) | Does not hold | Card 3256813379906952: $21.42, 0 sold, "Early bird deal, only 1 left", 6-day tag, and no "Free shipping" tag on my read (VERIFIED card). The backup $32.46 card also says "only 1 left". No repeatable US source. |
| Demand | Partly holds | "cargo liner for dogs" 320 a month, flat (ESTIMATED). Real Amazon demand, but at $28 to $46. |
| Rules and IP | Flag | 4Knines design patent family includes "Cover adaptable to foldable vehicle seats"; USD703116S1 "Zippered vehicle rear bumper protector" (owner not read). Both ESTIMATED from snippets. Fit returns by SUV size. |

Corrected values: US cost UNKNOWN (only source has 1 unit and 0 sales). Proven generic price
$27.99 to $45.89.

### front-bucket-seat-cover-dog

| Question | Verdict | What I found |
|---|---|---|
| Price ($44.99) | Partly holds | Amazon B00KAFYNTE 4Knines front bucket cover $44.99, 1,890 ratings, #108 in Automotive Seat Covers (VERIFIED). Its 200+ badge was not in my scan, so not re-verified. Generic front covers sell with volume far lower: $13.59 with 900+, $11.04 with 500+, a 900D cover with side flaps $23.79 with 700+, a 2-pack $26.58 with 1,000+ (VERIFIED). $44.99 is a 4Knines brand price. |
| US-stock cost ($15.45) | Holds as displayed | Card 3256812250169844: $15.45, 3 sold, "Save $31.37", free shipping, 6-day tag (VERIFIED). It costs more than several generic Amazon retail prices. |
| Demand | Partly holds | "front seat dog cover" 590 a month (ESTIMATED). Add-on only. |
| Rules and IP | Minor flag | Same 4Knines design-patent family. Generic design otherwise. |

Corrected values: proven generic price $11.04 to $23.79.

## holiday-gifts

### rolling-knife-sharpener-kit

| Question | Verdict | What I found |
|---|---|---|
| Price ($69 proposed) | Partly holds | Amazon AIERLIAN B0CRDK541R $33.99 (list $39.99), 6,000+ bought past month, #3 in Knife Sharpeners (VERIFIED). But near-identical kits sell lower with volume: $18.99 with 300+ (1,200 ratings), $15.99 with 200+ (two listings), $29.99 with 400+, $31.99 with 2,000+ (VERIFIED). TikTok Shop snippets: "388 sold, $16.99", "322 sold, $18.89", "132 sold, $26.99" (ESTIMATED). I could not reproduce the "10,783 sold, $39" snippet. Hatori $79.95 with compare-at $199.95 (VERIFIED JSON); its 1,307 reviews are a vendor figure. Tumbler sells at $103.20 on Amazon with 1,000+ (VERIFIED), but that is a brand. |
| US-stock cost ($13.07) | Partly holds | Card 3256812688812619: $13.07, 10 sold, "Early bird deal, only 3 left", 6-day tag; no "Free shipping" tag on my read, so the shipping fee is UNKNOWN (VERIFIED card). Card 3256812646672190: $15.15, 4 sold, free shipping (VERIFIED). Strop and gift box not costed. |
| Demand | Holds | "rolling knife sharpener" 8,100 a month, 22,200 in Dec 2025, 9,900 in Oct 2026 (ESTIMATED). Strong December lift and Amazon volume. |
| Rules and IP | Flag | Google Patents snippet for HORL family DE102016009482A1 (Otmar Horl, Freiburg) shows a "family litigation" marker (ESTIMATED). US12654275B2 "Magnetic sharpening jig" exists, owner not read. One Amazon listing is titled "The Original Patented Knife Sharpener Kit". Tumbler uses a ™ on "The Original Tumbler Rolling Knife Sharpener". A US patent check against HORL and Tumbler is needed before buying stock. No battery, no blade. |

Corrected values: repeatable US cost $15.15 (4 sold), plus strop and box UNKNOWN. Proven generic
price $15.99 to $33.99.

### monitor-light-bar-desk-kit

| Question | Verdict | What I found |
|---|---|---|
| Price ($44.99 proposed) | Does not hold | Quntis B08DKQ3JG1 $33.96 (to $39.95), 4,000+, 13,978 ratings, #1 in USB Reading Lamps (VERIFIED). That is a brand. Generic bars sell with volume at a fraction: B0GSPZ797T $13.59 with 2,000+, B0FW43JPNG $11.89 with 1,000+, RGB bar B0G4ZYSP7J $13.59 with 500+ (VERIFIED). No seller proves $44.99 for a generic. |
| US-stock cost ($8.85) | Holds as displayed | Card 3256812455029377: $8.85, 10 sold, "Save $22.75", free shipping, no new-shopper tag (VERIFIED). Remote and bar length still UNKNOWN. The $11.55 backup card says "only 4 left". |
| Demand | Holds | "monitor light bar" 6,600 a month, flat at 8,100 in recent months (ESTIMATED). Amazon volume large. |
| Rules and IP | Flag | Design patents for screen bar lamps exist: USD946803S1 "Screen bar lamp", USD952236S1 cited with it (ESTIMATED, owners not read). Choose a shape that is not a BenQ ScreenBar copy. USB 5 V, no battery. No eye-health claims. |

Corrected values: proven prices are $33.96 (Quntis brand) and $11.89 to $13.59 (generic). The
$8.85 cost holds.

### electric-salt-pepper-grinder-set

| Question | Verdict | What I found |
|---|---|---|
| Price ($39.97) | Partly holds | ThermoMaven B0D7Q7LNNY $39.97 (list $49.99), 3,000+, #1 in Salt & Pepper Shaker Sets (VERIFIED). Generic sets outsell it at about half: $18.98 with 10,000+, $21.65 with 10,000+, CIRCLE JOY gravity set $16.14 with 8,000+, $18.56 with 5,000+ (VERIFIED). |
| US-stock cost ($10.55) | Does not hold | Card 3256813400886540: $10.55, 0 sold, "Early bird deal, only 1 left" (VERIFIED). The $9.75 card also says "only 1 left"; the $5.21 card is a new-shopper price. Most US results for this search are grain mills. No repeatable US source. |
| Demand | Holds | "electric salt and pepper grinder" 12,100 a month, 40,500 in Dec 2025 (ESTIMATED). |
| Rules and IP | Minor flag | Small lithium battery inside a kitchen tool (not worn). Food-contact papers needed. US11910959B2 "Electric grinder" exists, owner not read. |

Corrected values: US cost UNKNOWN. Proven generic price $16.14 to $21.65.

## high-margin

### dog-carrier-backpack-kit

| Question | Verdict | What I found |
|---|---|---|
| Price ($79.99) | Does not hold for this item | Kurgo G-Train B09KMJCSNP $79.99, 1,341 ratings, #37 in Dog Carrier Backpacks, made by Radio Systems Corporation (VERIFIED). Its 200+ badge was not in my scan. The cited AliExpress item is a mesh "bubble" or box backpack. That type sells on Amazon at $21.24 (300+), Texsens $21.79 (2,000+, 12,500 ratings) and an expandable mesh backpack at $33.99 (900+) (VERIFIED). TikTok Shop snippet "421 sold, $16.99" for a backpack carrier (ESTIMATED). |
| US-stock cost ($25.99) | Holds as displayed | Card 3256813153502270: $25.99, 0 sold, free shipping, 6-day tag, no promo (VERIFIED). No reviews; quality unknown. It costs more than the Amazon retail price of the same type. Kit extras UNKNOWN. |
| Demand | Holds | "dog backpack carrier" 12,100 a month (ESTIMATED). Amazon volume is real, at $10 to $34. |
| Rules and IP | Serious flag | Google Patents snippets list K9 Sport Sack, LLC as owner of US10617096B2 "Pet carrying backpack" (top collar opening for the dog's head), US12453333B2 "Convertible pet-carrying and backpacking backpack" (granted 2025-10-28), USD1013285S1 "Pet backpack" and USD876826S1 (ESTIMATED). A head-out design like Kurgo or K9 Sport Sack is risky. A load-bearing product also needs strap and buckle test data. |

Corrected values: proven price for the costed type $21.24 to $33.99; $79.99 is Kurgo brand only.

### custom-pet-portrait-canvas-large

| Question | Verdict | What I found |
|---|---|---|
| Price ($99.95) | Partly holds | Crown & Paw "Penelope" product JSON: 16x24 unframed $99.95 (compare-at $109.95), 24x36 unframed $159.95, 12x18 unframed $79.95 (VERIFIED, updated today). No sales count. The page says each portrait is "hand-illustrated by our artists". Amazon custom pet portrait canvases sell at $16.99 to $32.99 (watercolor portrait $19.97 with 200+; NWT pet canvas $32.99 with 100+) (VERIFIED). |
| US cost ($44.45) | Holds | Printful API: 18x24 $33.66 and 24x36 $52.02, in stock in the US (VERIFIED). New: the "Canvas (in)" 16x24 variant 19303 is $31.11, an exact size match to Crown & Paw's 16x24 (VERIFIED). Printful shipping page shows the $0.40 US surcharge from Oct 15, 2026 to Jan 17, 2027 (VERIFIED); the medium-canvas rate itself did not parse, so $10.39 was not re-read. Art cost $5 is ASSUMED. |
| Demand | Partly holds | "custom pet portrait" 5,400 a month, 12,100 in Dec 2025, 3,600 in Oct 2026 (ESTIMATED). High-price demand is proven only for the leading brand. |
| Rules and IP | Flag | AI art must not be called hand-illustrated. Do not copy Crown & Paw costume scenes or names. Get a photo licence from the customer. Christmas cut-off risk from art approval plus 2 to 5 business days to fulfill. |

Corrected values: 16x24 cost $31.11 plus shipping (instead of 18x24 at $33.66). Proven price outside
Crown & Paw $16.99 to $32.99.

### metal-detector-kit

| Question | Verdict | What I found |
|---|---|---|
| Price ($104.49) | Partly holds | Gbnryg B0D3C25SX8 $104.49 (list $129.99), 1,000+, 1,663 ratings, #10 in Metal Detectors, 5.8 lb (VERIFIED). But adult detectors with LCD sell with volume lower: SUNPOW $55.65 (500+), GoGonova $56.98 (1,000+), a "2026 Latest Professional Metal Detector for Adults with LCD" $67.98 (800+), Bounty Hunter TK4 $71 (1,000+) (VERIFIED). Temu snippet shows professional detectors at $74.85 (ESTIMATED). |
| US-stock cost ($48.45) | Partly holds | Cited card 3256811850573305 now shows $46.69 with "New shoppers save $129.25" (116 sold), so still a first-order price. A sibling card 3256811951167885 "Professional Underground Metal Detector Multi-Mode" shows $48.39, 51 sold, free shipping, 6-day tag, no promo tag (VERIFIED). Whether it matches the Gbnryg spec is UNKNOWN. |
| Demand | Holds | "metal detector" 90,500 a month, 110,000 in Dec 2025 and Oct 2026 (ESTIMATED). "metal detector for adults" only 260. The best Amazon seller is a National Geographic kids' kit (10,000+), and kids are out of scope. |
| Rules and IP | Flag | Many listings say "for Adults & Kids"; we must sell to adults only. SUNPOW lists a 1,500 mAh lithium battery (handheld, not worn). Ask for FCC papers. 17-inch box. |

Corrected values: non-promo US cost $48.39 (different listing). Proven volume price $55.65 to $71;
$104.49 is one seller.

## What this means for the ranking

- No candidate clears the "one third of a price other sellers prove" rule once generic twins are
  counted. Each passes only against a brand's price.
- The rolling knife sharpener is the strongest of the nine on demand and creator fit, and its
  repeatable US cost ($15.15) is under half of the $33.99 Amazon price. It needs a US patent check
  against HORL and Tumbler first.
- The pet portrait canvas has the most solid cost data (Printful API) but its high price is proven
  only by Crown & Paw.
- The cargo liner and the salt and pepper grinder have no repeatable US source today. The dog carrier
  backpack has a price-variant mismatch and a K9 Sport Sack patent risk.

Working files (scratch, not facts of record): AliExpress, Amazon, SERP and store reads are in
`/tmp/claude-0/-home-user-commerce-os/c2389654-3ee7-5e31-ba87-8e168cf76207/scratchpad/skeptic/data/`.
