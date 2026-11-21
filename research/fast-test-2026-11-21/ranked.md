# Fast-test product ranking (2026-11-21)

Produced by `scripts/fast_test_rank.py`. Own store on Shopify, Meta ads, supplier ships from US stock to the customer.
Before ads = price minus supplier cost, card fee and a 6% refund allowance. Tough = benchmark ad cost x 1.3 (new store).
Costs are marketplace card prices read on the date above: ESTIMATED until a real order confirms them.
Order: green first (earns money at the tough ad cost), then amber (only at the benchmark ad cost), then red; by score inside each tier.

Products: 30. Earn money in the tough case with US stock: 3. Still earn money if cost is 20% higher and refunds are 10%: 0. Pass the cushion rule: 2.

## Overall

| # | Product | Sell | US cost | Before ads | Ad cost (tough) | Profit (benchmark) | Profit (tough) | If cost +20% | Amazon/mo | Score | Tier | Start now? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | japanese-style-knife-set | $99.00 | $26.49 | $63.40 | $63.19 | $14.79 | $0.21 | -$5.09 | 23,100 | 73.9 | green | yes, thin (caution) |
| 2 | heated-gloves-7v | $97.99 | $25.89 | $63.08 | $58.89 | $17.78 | $4.19 | -$0.99 | 19,250 | 65.8 | green | yes, thin (caution) |
| 3 | rechargeable-wall-sconce-pair | $109.99 | $36.69 | $63.21 | $63.19 | $14.60 | $0.02 | -$7.32 | 20,950 | 63.6 | green | yes, thin (caution) |
| 4 | cordless-tire-inflator | $59.99 | $15.02 | $39.33 | $46.32 | $3.70 | -$6.99 | -$9.99 | 77,850 | 70.8 | amber | no, loses money (caution) |
| 5 | portable-carplay-screen-kit | $129.99 | $54.99 | $63.13 | $66.38 | $12.07 | -$3.25 | -$14.25 | 26,300 | 65.8 | amber | no, loses money |
| 6 | filtered-shower-head-kit | $79.00 | $12.95 | $58.72 | $63.19 | $10.11 | -$4.47 | -$7.06 | 23,150 | 64.2 | amber | no, loses money |
| 7 | mini-smart-projector | $99.99 | $36.39 | $54.40 | $66.38 | $3.34 | -$11.98 | -$19.26 | 54,150 | 63.0 | amber | no, loses money |
| 8 | small-dog-booster-car-seat | $69.99 | $21.88 | $41.58 | $51.00 | $2.35 | -$9.42 | -$13.79 | 16,000 | 58.2 | amber | no, loses money |
| 9 | lightweight-pet-stroller | $84.99 | $37.89 | $39.24 | $51.00 | $0.01 | -$11.76 | -$19.34 | 10,200 | 56.4 | amber | no, loses money |
| 10 | mattress-vacuum-uv | $99.99 | $34.83 | $55.96 | $63.19 | $7.35 | -$7.23 | -$14.20 | 14,150 | 55.9 | amber | no, loses money (caution) |
| 11 | portable-carplay-screen | $79.99 | $44.44 | $28.13 | $66.38 | -$22.93 | -$38.25 | -$47.14 | 27,200 | 64.2 | red | no, loses money |
| 12 | stainless-steel-litter-box-kit | $58.99 | $30.69 | $22.75 | $51.00 | -$16.48 | -$28.25 | -$34.39 | 54,850 | 64.0 | red | no, loses money |
| 13 | digital-night-vision-binoculars | $72.67 | $41.79 | $24.11 | $58.89 | -$21.19 | -$34.78 | -$43.14 | 15,150 | 60.6 | red | no, loses money |
| 14 | handheld-vacuum-sealer-kit | $69.99 | $18.89 | $44.57 | $63.19 | -$4.04 | -$18.62 | -$22.40 | 24,850 | 57.4 | red | no, loses money |
| 15 | hd-galaxy-projector | $59.99 | $28.06 | $26.29 | $63.19 | -$22.32 | -$36.90 | -$42.51 | 10,600 | 57.4 | red | no, loses money |
| 16 | waterless-scent-diffuser-kit | $79.95 | $40.41 | $32.12 | $63.19 | -$16.49 | -$31.07 | -$39.15 | 37,200 | 54.3 | red | no, loses money |
| 17 | ai-translation-earbuds | $69.95 | $37.79 | $25.63 | $66.38 | -$25.43 | -$40.74 | -$48.30 | 7,200 | 54.0 | red | no, loses money |
| 18 | foam-dog-stairs-for-bed | $69.99 | $56.39 | $7.07 | $51.00 | -$32.16 | -$43.93 | -$55.21 | 21,250 | 53.0 | red | no, loses money |
| 19 | heated-vest-powerbank-kit | $79.99 | $34.34 | $38.23 | $58.89 | -$7.07 | -$20.66 | -$27.53 | 27,600 | 52.7 | red | no, loses money (caution) |
| 20 | electric-spin-scrubber-kit | $59.99 | $22.22 | $32.13 | $63.19 | -$16.48 | -$31.06 | -$35.51 | 4,100 | 51.5 | red | no, loses money |
| 21 | heated-socks-app | $62.99 | $24.59 | $32.49 | $58.89 | -$12.81 | -$26.40 | -$31.31 | 11,450 | 50.2 | red | no, loses money (caution) |
| 22 | wireless-carplay-adapter | $59.99 | $26.29 | $28.06 | $66.38 | -$23.00 | -$38.32 | -$43.58 | 9,350 | 50.0 | red | no, loses money |
| 23 | wireless-cat-water-fountain | $74.95 | $31.29 | $36.69 | $51.00 | -$2.54 | -$14.31 | -$20.57 | 17,250 | 49.6 | red | no, loses money |
| 24 | compact-digital-camera-kit | $79.99 | $33.69 | $38.88 | $66.38 | -$12.18 | -$27.50 | -$34.24 | 17,600 | 49.2 | red | no, loses money |
| 25 | architect-desk-lamp | $69.99 | $32.53 | $30.93 | $66.38 | -$20.13 | -$35.45 | -$41.95 | 14,350 | 45.9 | red | no, loses money |
| 26 | waterproof-pet-throw-blanket | $79.00 | n/a | n/a | n/a | n/a | n/a | n/a | 4,850 | 20.5 | red | no US stock |
| 27 | jump-starter-air-compressor | $99.99 | $33.49 | $57.30 | $46.32 | $21.67 | $10.98 | $4.28 | 82,050 | 79.0 | green | BLOCKED on safety |
| 28 | dog-force-dryer | $109.99 | $52.42 | $47.48 | $51.00 | $8.25 | -$3.52 | -$14.00 | 9,250 | 49.0 | amber | BLOCKED on safety |
| 29 | towel-warmer-bucket | $109.99 | $51.90 | $48.00 | $63.19 | -$0.61 | -$15.19 | -$25.57 | 33,350 | 51.3 | red | BLOCKED on safety |
| 30 | cordless-heated-blanket | $119.99 | n/a | n/a | n/a | n/a | n/a | n/a | 26,900 | 29.6 | red | BLOCKED on safety |

## home

| # | Product | Sell | US cost | Before ads | Ad cost (tough) | Profit (benchmark) | Profit (tough) | If cost +20% | Amazon/mo | Score | Tier | Start now? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | japanese-style-knife-set | $99.00 | $26.49 | $63.40 | $63.19 | $14.79 | $0.21 | -$5.09 | 23,100 | 73.9 | green | yes, thin (caution) |
| 2 | rechargeable-wall-sconce-pair | $109.99 | $36.69 | $63.21 | $63.19 | $14.60 | $0.02 | -$7.32 | 20,950 | 63.6 | green | yes, thin (caution) |
| 3 | filtered-shower-head-kit | $79.00 | $12.95 | $58.72 | $63.19 | $10.11 | -$4.47 | -$7.06 | 23,150 | 64.2 | amber | no, loses money |
| 4 | mattress-vacuum-uv | $99.99 | $34.83 | $55.96 | $63.19 | $7.35 | -$7.23 | -$14.20 | 14,150 | 55.9 | amber | no, loses money (caution) |
| 5 | handheld-vacuum-sealer-kit | $69.99 | $18.89 | $44.57 | $63.19 | -$4.04 | -$18.62 | -$22.40 | 24,850 | 57.4 | red | no, loses money |
| 6 | hd-galaxy-projector | $59.99 | $28.06 | $26.29 | $63.19 | -$22.32 | -$36.90 | -$42.51 | 10,600 | 57.4 | red | no, loses money |
| 7 | waterless-scent-diffuser-kit | $79.95 | $40.41 | $32.12 | $63.19 | -$16.49 | -$31.07 | -$39.15 | 37,200 | 54.3 | red | no, loses money |
| 8 | electric-spin-scrubber-kit | $59.99 | $22.22 | $32.13 | $63.19 | -$16.48 | -$31.06 | -$35.51 | 4,100 | 51.5 | red | no, loses money |
| 9 | towel-warmer-bucket | $109.99 | $51.90 | $48.00 | $63.19 | -$0.61 | -$15.19 | -$25.57 | 33,350 | 51.3 | red | BLOCKED on safety |

## auto-outdoor

| # | Product | Sell | US cost | Before ads | Ad cost (tough) | Profit (benchmark) | Profit (tough) | If cost +20% | Amazon/mo | Score | Tier | Start now? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | heated-gloves-7v | $97.99 | $25.89 | $63.08 | $58.89 | $17.78 | $4.19 | -$0.99 | 19,250 | 65.8 | green | yes, thin (caution) |
| 2 | cordless-tire-inflator | $59.99 | $15.02 | $39.33 | $46.32 | $3.70 | -$6.99 | -$9.99 | 77,850 | 70.8 | amber | no, loses money (caution) |
| 3 | portable-carplay-screen | $79.99 | $44.44 | $28.13 | $66.38 | -$22.93 | -$38.25 | -$47.14 | 27,200 | 64.2 | red | no, loses money |
| 4 | digital-night-vision-binoculars | $72.67 | $41.79 | $24.11 | $58.89 | -$21.19 | -$34.78 | -$43.14 | 15,150 | 60.6 | red | no, loses money |
| 5 | heated-vest-powerbank-kit | $79.99 | $34.34 | $38.23 | $58.89 | -$7.07 | -$20.66 | -$27.53 | 27,600 | 52.7 | red | no, loses money (caution) |
| 6 | heated-socks-app | $62.99 | $24.59 | $32.49 | $58.89 | -$12.81 | -$26.40 | -$31.31 | 11,450 | 50.2 | red | no, loses money (caution) |
| 7 | jump-starter-air-compressor | $99.99 | $33.49 | $57.30 | $46.32 | $21.67 | $10.98 | $4.28 | 82,050 | 79.0 | green | BLOCKED on safety |
| 8 | cordless-heated-blanket | $119.99 | n/a | n/a | n/a | n/a | n/a | n/a | 26,900 | 29.6 | red | BLOCKED on safety |

## tech-desk

| # | Product | Sell | US cost | Before ads | Ad cost (tough) | Profit (benchmark) | Profit (tough) | If cost +20% | Amazon/mo | Score | Tier | Start now? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | portable-carplay-screen-kit | $129.99 | $54.99 | $63.13 | $66.38 | $12.07 | -$3.25 | -$14.25 | 26,300 | 65.8 | amber | no, loses money |
| 2 | mini-smart-projector | $99.99 | $36.39 | $54.40 | $66.38 | $3.34 | -$11.98 | -$19.26 | 54,150 | 63.0 | amber | no, loses money |
| 3 | ai-translation-earbuds | $69.95 | $37.79 | $25.63 | $66.38 | -$25.43 | -$40.74 | -$48.30 | 7,200 | 54.0 | red | no, loses money |
| 4 | wireless-carplay-adapter | $59.99 | $26.29 | $28.06 | $66.38 | -$23.00 | -$38.32 | -$43.58 | 9,350 | 50.0 | red | no, loses money |
| 5 | compact-digital-camera-kit | $79.99 | $33.69 | $38.88 | $66.38 | -$12.18 | -$27.50 | -$34.24 | 17,600 | 49.2 | red | no, loses money |
| 6 | architect-desk-lamp | $69.99 | $32.53 | $30.93 | $66.38 | -$20.13 | -$35.45 | -$41.95 | 14,350 | 45.9 | red | no, loses money |

## pets

| # | Product | Sell | US cost | Before ads | Ad cost (tough) | Profit (benchmark) | Profit (tough) | If cost +20% | Amazon/mo | Score | Tier | Start now? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | small-dog-booster-car-seat | $69.99 | $21.88 | $41.58 | $51.00 | $2.35 | -$9.42 | -$13.79 | 16,000 | 58.2 | amber | no, loses money |
| 2 | lightweight-pet-stroller | $84.99 | $37.89 | $39.24 | $51.00 | $0.01 | -$11.76 | -$19.34 | 10,200 | 56.4 | amber | no, loses money |
| 3 | stainless-steel-litter-box-kit | $58.99 | $30.69 | $22.75 | $51.00 | -$16.48 | -$28.25 | -$34.39 | 54,850 | 64.0 | red | no, loses money |
| 4 | foam-dog-stairs-for-bed | $69.99 | $56.39 | $7.07 | $51.00 | -$32.16 | -$43.93 | -$55.21 | 21,250 | 53.0 | red | no, loses money |
| 5 | wireless-cat-water-fountain | $74.95 | $31.29 | $36.69 | $51.00 | -$2.54 | -$14.31 | -$20.57 | 17,250 | 49.6 | red | no, loses money |
| 6 | waterproof-pet-throw-blanket | $79.00 | n/a | n/a | n/a | n/a | n/a | n/a | 4,850 | 20.5 | red | no US stock |
| 7 | dog-force-dryer | $109.99 | $52.42 | $47.48 | $51.00 | $8.25 | -$3.52 | -$14.00 | 9,250 | 49.0 | amber | BLOCKED on safety |

## Rule review (ASSUMED: our reading of CLAUDE.md section 2; Dhruv can overrule)

- japanese-style-knife-set: CAUTION. The $26.49 cost is a 15-piece block set with 12 sold, not the gift set the $99 price is based on. Meta's ad rules on bladed items do not clearly allow kitchen knives. Never call it Japanese-made unless it is.
- heated-gloves-7v: CAUTION. Lithium packs and a heating element worn on the body; battery paperwork (UL, ETL or UN38.3) UNKNOWN; sizing returns; season ends by March. The cost is a listing with 3 sold.
- rechargeable-wall-sconce-pair: CAUTION. Amazon sells sets of 2 at $45 to $57 with Prime, about half our price. The cost is one listing with 12 sold.
- cordless-tire-inflator: CAUTION. Lithium battery with a motor; certification UNKNOWN; two giant brands.
- mattress-vacuum-uv: CAUTION. UV light: no germ-killing or health claims allowed without proof.
- heated-vest-powerbank-kit: CAUTION. Heating element worn on the body; two sellers and two parcels; sizing returns.
- heated-socks-app: CAUTION. Lithium packs worn against the leg; certification UNKNOWN; sizing returns.
- jump-starter-air-compressor: BLOCKED. High-current lithium pack clamped to a car battery; certification UNKNOWN. The scout flagged it as a likely fail on safety.
- dog-force-dryer: BLOCKED. Mains-powered heated appliance used on animals; electrical certification UNKNOWN; over 10 lb.
- towel-warmer-bucket: BLOCKED. Mains-powered heating appliance; electrical certification UNKNOWN; over 9 lb.
- cordless-heated-blanket: BLOCKED. Battery-heated textile; certification UNKNOWN; no US stock found.

## Re-check at the cost of a better-proven US listing

| Product | Cheapest listing | Profit (tough) | Better-proven listing | Profit (tough) |
|---|---|---|---|---|
| japanese-style-knife-set | $26.49 | $0.21 | $33.39 (next US block set) | -$6.69 |
| heated-gloves-7v | $25.89 | $4.19 | $48.69 (the US listing with 110 sold) | -$18.61 |
| rechargeable-wall-sconce-pair | $36.69 | $0.02 | $47.15 (style closer to the Amazon best sellers ($45.91 to $52.89)) | -$10.44 |

## First week on a small budget (top 10 overall, tough ad cost, no payout yet)

| Product | Budget | Orders the cash covers | Sales | Profit after setup and sample | Orders for $2,000 | Cash needed for $2,000 |
|---|---|---|---|---|---|---|
| japanese-style-knife-set | $500.00 | 5 | $495.00 | -$41.46 | 21 | $1,925.83 |
| japanese-style-knife-set | $1,000.00 | 10 | $990.00 | -$40.43 | 21 | $1,925.83 |
| heated-gloves-7v | $500.00 | 5 | $489.95 | -$20.95 | 21 | $1,822.27 |
| heated-gloves-7v | $1,000.00 | 11 | $1,077.89 | $4.19 | 21 | $1,822.27 |
| rechargeable-wall-sconce-pair | $500.00 | 4 | $439.96 | -$52.62 | 19 | $1,950.47 |
| rechargeable-wall-sconce-pair | $1,000.00 | 9 | $989.91 | -$52.53 | 19 | $1,950.47 |
| cordless-tire-inflator | $500.00 | 7 | $419.93 | -$79.94 | 34 | $2,116.55 |
| cordless-tire-inflator | $1,000.00 | 15 | $899.85 | -$135.84 | 34 | $2,116.55 |
| portable-carplay-screen-kit | $500.00 | 3 | $389.97 | -$80.73 | 16 | $2,012.88 |
| portable-carplay-screen-kit | $1,000.00 | 7 | $909.93 | -$93.72 | 16 | $2,012.88 |
| filtered-shower-head-kit | $500.00 | 6 | $474.00 | -$55.79 | 26 | $2,008.67 |
| filtered-shower-head-kit | $1,000.00 | 12 | $948.00 | -$82.64 | 26 | $2,008.67 |
| mini-smart-projector | $500.00 | 4 | $399.96 | -$100.30 | 21 | $2,210.52 |
| mini-smart-projector | $1,000.00 | 9 | $899.91 | -$160.18 | 21 | $2,210.52 |
| small-dog-booster-car-seat | $500.00 | 6 | $419.94 | -$94.39 | 29 | $2,151.37 |
| small-dog-booster-car-seat | $1,000.00 | 13 | $909.87 | -$160.32 | 29 | $2,151.37 |
| lightweight-pet-stroller | $500.00 | 5 | $424.95 | -$112.71 | 24 | $2,187.23 |
| lightweight-pet-stroller | $1,000.00 | 10 | $849.90 | -$171.52 | 24 | $2,187.23 |
| mattress-vacuum-uv | $500.00 | 4 | $399.96 | -$79.76 | 21 | $2,109.31 |
| mattress-vacuum-uv | $1,000.00 | 9 | $899.91 | -$115.92 | 21 | $2,109.31 |

## Capped test plan: $350.00 of ads on one product (top 8 with US stock)

| Product | Orders (benchmark to tough) | Sales | Net after setup and sample | Cash out before any payout | Stop an ad with no sale at |
|---|---|---|---|---|---|
| japanese-style-knife-set | 7.2 to 5.5 | $712.82 to $548.32 | $63.99 to -$41.35 | $583.22 to $539.21 | $63.40 |
| heated-gloves-7v | 7.7 to 5.9 | $757.10 to $582.38 | $95.47 to -$16.99 | $591.92 to $545.76 | $63.08 |
| rechargeable-wall-sconce-pair | 7.2 to 5.5 | $791.95 to $609.19 | $52.44 to -$52.59 | $666.86 to $605.90 | $63.21 |
| cordless-tire-inflator | 9.8 to 7.6 | $589.29 to $453.30 | $5.33 to -$83.82 | $528.56 to $494.52 | $39.33 |
| portable-carplay-screen-kit | 6.9 to 5.3 | $891.04 to $685.42 | $11.75 to -$88.11 | $797.93 to $710.94 | $63.13 |
| filtered-shower-head-kit | 7.2 to 5.5 | $568.81 to $437.55 | $43.84 to -$53.73 | $472.19 to $450.67 | $58.72 |
| mini-smart-projector | 6.9 to 5.3 | $685.40 to $527.23 | -$29.49 to -$115.54 | $651.83 to $594.27 | $54.40 |
| small-dog-booster-car-seat | 8.9 to 6.9 | $624.43 to $480.33 | -$16.91 to -$102.52 | $583.09 to $538.04 | $41.58 |

## The $100,000 by year end claim on benchmark numbers

- Orders needed at a $74.62 average order: 1,341 in 40 days (34 a day).
- Ad spend at the all-industry benchmark: $53,277.93 ($1,331.95 a day); at new-store cost: $69,261.31.
- That is 53 times a $1,000 budget for ads alone.
- Supplier payments at the median cost share in our candidates (42% of price): $42,303.25.
- The creator's own reported month: ads were 55% of revenue and profit 10%. At that margin $100,000 of sales leaves $10,039.94.

## China-shipped comparison (where a China cost was found; 10% refund allowance ASSUMED)

| Product | US cost | China cost | Profit tough, US | Profit tough, China |
|---|---|---|---|---|
| japanese-style-knife-set | $26.49 | $20.89 | $0.21 | $1.85 |
| heated-gloves-7v | $25.89 | $54.99 | $4.19 | -$28.83 |
| portable-carplay-screen-kit | $54.99 | $58.39 | -$3.25 | -$11.85 |
| mini-smart-projector | $36.39 | $58.79 | -$11.98 | -$38.38 |
| mattress-vacuum-uv | $34.83 | $31.89 | -$7.23 | -$8.29 |
| hd-galaxy-projector | $28.06 | $15.45 | -$36.90 | -$26.69 |
| ai-translation-earbuds | $37.79 | $11.69 | -$40.74 | -$17.44 |
| heated-socks-app | $24.59 | $37.89 | -$26.40 | -$42.22 |
| wireless-carplay-adapter | $26.29 | $13.33 | -$38.32 | -$27.76 |
| compact-digital-camera-kit | $33.69 | $19.59 | -$27.50 | -$16.60 |
| jump-starter-air-compressor | $33.49 | $41.39 | $10.98 | -$0.92 |

## Ad spend needed to leave Meta's learning phase (50 purchases in a week)

- pets: $1,961.50
- home: $2,430.50
- tech: $2,553.00
- outdoor: $2,265.00
- beauty: $2,022.00
- auto: $1,781.50
- all: $1,986.50
