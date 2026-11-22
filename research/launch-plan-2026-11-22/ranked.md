# Fast-test product ranking (2026-11-22)

Produced by `scripts/fast_test_rank.py`. Own store on Shopify, Meta ads, supplier ships from US stock to the customer.
Before ads = price minus supplier cost, card fee and a 6% refund allowance. Tough = benchmark ad cost x 1.3 (new store).
Costs are marketplace card prices read on the date above: ESTIMATED until a real order confirms them.
Order: green first (earns money at the tough ad cost), then amber (only at the benchmark ad cost), then red; by score inside each tier.

Products: 52. Earn money in the tough case with US stock: 4. Still earn money if cost is 20% higher and refunds are 10%: 1. Pass the cushion rule: 4.

## Overall

| # | Product | Sell | US cost | Before ads | Ad cost (tough) | Profit (benchmark) | Profit (tough) | If cost +20% | Amazon/mo | Score | Tier | Start now? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | barkfare-extender-cheaper-listing | $149.00 | $54.01 | $81.43 | $51.00 | $42.20 | $30.43 | $19.63 | 5,500 | 78.8 | green | YES, robust (caution) |
| 2 | japanese-style-knife-set | $99.00 | $26.49 | $63.40 | $63.19 | $14.79 | $0.21 | -$5.09 | 23,100 | 73.9 | green | yes, thin (caution) |
| 3 | rechargeable-wall-sconce-pair | $109.99 | $36.69 | $63.21 | $63.19 | $14.60 | $0.02 | -$7.32 | 20,950 | 63.6 | green | yes, thin (caution) |
| 4 | barkfare-extender-us-stock | $149.00 | $83.69 | $51.75 | $51.00 | $12.52 | $0.75 | -$15.99 | 5,500 | 58.5 | green | yes, thin (caution) |
| 5 | cordless-tire-inflator | $59.99 | $15.02 | $39.33 | $46.32 | $3.70 | -$6.99 | -$9.99 | 77,850 | 70.8 | amber | no, loses money (caution) |
| 6 | filtered-shower-head-kit | $79.00 | $12.95 | $58.72 | $63.19 | $10.11 | -$4.47 | -$7.06 | 23,150 | 64.2 | amber | no, loses money |
| 7 | mini-smart-projector | $99.99 | $36.39 | $54.40 | $66.38 | $3.34 | -$11.98 | -$19.26 | 54,150 | 63.0 | amber | no, loses money |
| 8 | small-dog-booster-car-seat | $69.99 | $21.88 | $41.58 | $51.00 | $2.35 | -$9.42 | -$13.79 | 16,000 | 58.2 | amber | no, loses money |
| 9 | portable-carplay-screen-kit | $119.99 | $54.99 | $54.02 | $66.38 | $2.96 | -$12.36 | -$23.36 | 26,300 | 56.7 | amber | no, loses money (caution) |
| 10 | lightweight-pet-stroller | $84.99 | $37.89 | $39.24 | $51.00 | $0.01 | -$11.76 | -$19.34 | 10,200 | 56.4 | amber | no, loses money |
| 11 | mattress-vacuum-uv | $99.99 | $34.83 | $55.96 | $63.19 | $7.35 | -$7.23 | -$14.20 | 14,150 | 55.9 | amber | no, loses money (caution) |
| 12 | rolling-knife-sharpener-kit | $69.00 | $13.07 | $49.49 | $63.19 | $0.88 | -$13.70 | -$16.32 | 16,050 | 51.7 | amber | no, loses money |
| 13 | suv-cargo-liner-dog | $69.00 | $21.42 | $41.14 | $51.00 | $1.91 | -$9.86 | -$14.14 | 1,900 | 38.1 | amber | no, loses money |
| 14 | cocktail-smoker-kit | $33.24 | $22.11 | $7.87 | $51.65 | -$31.86 | -$43.78 | -$48.20 | 32,000 | 64.2 | red | no, loses money |
| 15 | portable-carplay-screen | $79.99 | $44.44 | $28.13 | $66.38 | -$22.93 | -$38.25 | -$47.14 | 27,200 | 64.2 | red | no, loses money |
| 16 | stainless-steel-litter-box-kit | $58.99 | $30.69 | $22.75 | $51.00 | -$16.48 | -$28.25 | -$34.39 | 54,850 | 64.0 | red | no, loses money |
| 17 | mini-car-vacuum-blower | $39.99 | $24.68 | $11.45 | $46.32 | -$24.18 | -$34.87 | -$39.80 | 72,350 | 61.9 | red | no, loses money |
| 18 | wireless-meat-thermometer | $33.99 | $30.42 | $0.24 | $63.19 | -$48.37 | -$62.95 | -$69.03 | 52,350 | 61.0 | red | no, loses money |
| 19 | digital-night-vision-binoculars | $72.67 | $41.79 | $24.11 | $58.89 | -$21.19 | -$34.78 | -$43.14 | 15,150 | 60.6 | red | no, loses money |
| 20 | electric-salt-pepper-grinder-set | $39.97 | $10.55 | $25.56 | $63.19 | -$23.05 | -$37.63 | -$39.74 | 25,900 | 59.9 | red | no, loses money |
| 21 | music-boxing-machine | $69.99 | $37.29 | $26.17 | $58.89 | -$19.13 | -$32.72 | -$40.18 | 18,450 | 58.5 | red | no, loses money (caution) |
| 22 | folding-dog-car-ramp | $75.98 | $54.19 | $14.73 | $51.00 | -$24.50 | -$36.27 | -$47.11 | 17,100 | 57.8 | red | no, loses money |
| 23 | handheld-vacuum-sealer-kit | $69.99 | $18.89 | $44.57 | $63.19 | -$4.04 | -$18.62 | -$22.40 | 24,850 | 57.4 | red | no, loses money |
| 24 | hd-galaxy-projector | $59.99 | $28.06 | $26.29 | $63.19 | -$22.32 | -$36.90 | -$42.51 | 10,600 | 57.4 | red | no, loses money |
| 25 | cordless-pressure-washer-gun | $69.99 | $32.49 | $30.97 | $58.89 | -$14.33 | -$27.92 | -$34.42 | 9,050 | 56.2 | red | no, loses money |
| 26 | monitor-light-bar-desk-kit | $44.99 | $8.85 | $31.84 | $66.38 | -$19.22 | -$34.54 | -$36.31 | 10,250 | 54.5 | red | no, loses money |
| 27 | waterless-scent-diffuser-kit | $79.95 | $40.41 | $32.12 | $63.19 | -$16.49 | -$31.07 | -$39.15 | 37,200 | 54.3 | red | no, loses money |
| 28 | ai-translation-earbuds | $69.95 | $37.79 | $25.63 | $66.38 | -$25.43 | -$40.74 | -$48.30 | 7,200 | 54.0 | red | no, loses money |
| 29 | smart-bird-feeder-camera | $51.29 | $58.79 | -$12.36 | $58.89 | -$57.66 | -$71.25 | -$83.01 | 10,650 | 53.4 | red | no, loses money |
| 30 | foam-dog-stairs-for-bed | $69.99 | $56.39 | $7.07 | $51.00 | -$32.16 | -$43.93 | -$55.21 | 21,250 | 53.0 | red | no, loses money |
| 31 | electric-spin-scrubber-kit | $59.99 | $22.22 | $32.13 | $63.19 | -$16.48 | -$31.06 | -$35.51 | 4,100 | 51.5 | red | no, loses money |
| 32 | wireless-carplay-adapter | $59.99 | $26.29 | $28.06 | $66.38 | -$23.00 | -$38.32 | -$43.58 | 9,350 | 50.0 | red | no, loses money |
| 33 | wireless-cat-water-fountain | $74.95 | $31.29 | $36.69 | $51.00 | -$2.54 | -$14.31 | -$20.57 | 17,250 | 49.6 | red | no, loses money |
| 34 | compact-digital-camera-kit | $79.99 | $33.69 | $38.88 | $66.38 | -$12.18 | -$27.50 | -$34.24 | 17,600 | 49.2 | red | no, loses money |
| 35 | architect-desk-lamp | $69.99 | $32.53 | $30.93 | $66.38 | -$20.13 | -$35.45 | -$41.95 | 14,350 | 45.9 | red | no, loses money |
| 36 | waterproof-dog-hammock-seat-cover | $69.00 | $24.58 | $37.98 | $51.00 | -$1.25 | -$13.02 | -$17.94 | 2,500 | 35.9 | red | no, loses money |
| 37 | backseat-dog-car-bed | $59.49 | $48.09 | $5.81 | $51.00 | -$33.42 | -$45.19 | -$54.81 | 3,450 | 34.9 | red | no, loses money |
| 38 | custom-pet-portrait-canvas | $62.00 | $35.38 | $20.80 | $51.00 | -$18.43 | -$30.20 | -$37.27 | n/a | 28.5 | red | no, loses money |
| 39 | front-bucket-seat-cover-dog | $44.99 | $15.45 | $25.24 | $51.00 | -$13.99 | -$25.76 | -$28.85 | 300 | 25.0 | red | no, loses money |
| 40 | waterproof-pet-throw-blanket | $79.00 | n/a | n/a | n/a | n/a | n/a | n/a | 4,850 | 20.5 | red | no US stock |
| 41 | dog-car-door-covers-2pack | $29.99 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 16.0 | red | no US stock |
| 42 | jump-starter-air-compressor | $99.99 | $33.49 | $57.30 | $46.32 | $21.67 | $10.98 | $4.28 | 82,050 | 79.0 | green | BLOCKED on safety |
| 43 | leg-air-compression-massager-heat | $119.99 | $44.29 | $64.72 | $58.89 | $19.42 | $5.83 | -$3.03 | 24,900 | 76.4 | green | BLOCKED on safety |
| 44 | heated-gloves-7v | $97.99 | $25.89 | $63.08 | $58.89 | $17.78 | $4.19 | -$0.99 | 19,250 | 65.8 | green | BLOCKED on safety |
| 45 | cordless-neck-shoulder-kneading-massager | $89.99 | $23.29 | $58.39 | $58.89 | $13.09 | -$0.50 | -$5.16 | 14,050 | 64.6 | amber | BLOCKED on safety |
| 46 | dog-force-dryer | $109.99 | $52.42 | $47.48 | $51.00 | $8.25 | -$3.52 | -$14.00 | 9,250 | 49.0 | amber | BLOCKED on safety |
| 47 | heated-vest-powerbank-kit | $79.99 | $34.34 | $38.23 | $58.89 | -$7.07 | -$20.66 | -$27.53 | 27,600 | 52.7 | red | BLOCKED on safety |
| 48 | shiatsu-foot-massager-machine | $109.99 | $64.49 | $35.41 | $58.89 | -$9.89 | -$23.48 | -$36.38 | 34,300 | 52.1 | red | BLOCKED on safety |
| 49 | cordless-heated-hand-massager | $79.99 | $31.69 | $40.88 | $58.89 | -$4.42 | -$18.01 | -$24.35 | 14,700 | 51.7 | red | BLOCKED on safety |
| 50 | towel-warmer-bucket | $109.99 | $51.90 | $48.00 | $63.19 | -$0.61 | -$15.19 | -$25.57 | 33,350 | 51.3 | red | BLOCKED on safety |
| 51 | heated-socks-app | $62.99 | $24.59 | $32.49 | $58.89 | -$12.81 | -$26.40 | -$31.31 | 11,450 | 50.2 | red | BLOCKED on safety |
| 52 | cordless-heated-blanket | $119.99 | n/a | n/a | n/a | n/a | n/a | n/a | 26,900 | 29.6 | red | BLOCKED on safety |

## barkfare-hero

| # | Product | Sell | US cost | Before ads | Ad cost (tough) | Profit (benchmark) | Profit (tough) | If cost +20% | Amazon/mo | Score | Tier | Start now? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | barkfare-extender-cheaper-listing | $149.00 | $54.01 | $81.43 | $51.00 | $42.20 | $30.43 | $19.63 | 5,500 | 78.8 | green | YES, robust (caution) |

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

## barkfare

| # | Product | Sell | US cost | Before ads | Ad cost (tough) | Profit (benchmark) | Profit (tough) | If cost +20% | Amazon/mo | Score | Tier | Start now? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | barkfare-extender-us-stock | $149.00 | $83.69 | $51.75 | $51.00 | $12.52 | $0.75 | -$15.99 | 5,500 | 58.5 | green | yes, thin (caution) |

## auto-outdoor

| # | Product | Sell | US cost | Before ads | Ad cost (tough) | Profit (benchmark) | Profit (tough) | If cost +20% | Amazon/mo | Score | Tier | Start now? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | cordless-tire-inflator | $59.99 | $15.02 | $39.33 | $46.32 | $3.70 | -$6.99 | -$9.99 | 77,850 | 70.8 | amber | no, loses money (caution) |
| 2 | portable-carplay-screen | $79.99 | $44.44 | $28.13 | $66.38 | -$22.93 | -$38.25 | -$47.14 | 27,200 | 64.2 | red | no, loses money |
| 3 | digital-night-vision-binoculars | $72.67 | $41.79 | $24.11 | $58.89 | -$21.19 | -$34.78 | -$43.14 | 15,150 | 60.6 | red | no, loses money |
| 4 | jump-starter-air-compressor | $99.99 | $33.49 | $57.30 | $46.32 | $21.67 | $10.98 | $4.28 | 82,050 | 79.0 | green | BLOCKED on safety |
| 5 | heated-gloves-7v | $97.99 | $25.89 | $63.08 | $58.89 | $17.78 | $4.19 | -$0.99 | 19,250 | 65.8 | green | BLOCKED on safety |
| 6 | heated-vest-powerbank-kit | $79.99 | $34.34 | $38.23 | $58.89 | -$7.07 | -$20.66 | -$27.53 | 27,600 | 52.7 | red | BLOCKED on safety |
| 7 | heated-socks-app | $62.99 | $24.59 | $32.49 | $58.89 | -$12.81 | -$26.40 | -$31.31 | 11,450 | 50.2 | red | BLOCKED on safety |
| 8 | cordless-heated-blanket | $119.99 | n/a | n/a | n/a | n/a | n/a | n/a | 26,900 | 29.6 | red | BLOCKED on safety |

## tech-desk

| # | Product | Sell | US cost | Before ads | Ad cost (tough) | Profit (benchmark) | Profit (tough) | If cost +20% | Amazon/mo | Score | Tier | Start now? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | mini-smart-projector | $99.99 | $36.39 | $54.40 | $66.38 | $3.34 | -$11.98 | -$19.26 | 54,150 | 63.0 | amber | no, loses money |
| 2 | portable-carplay-screen-kit | $119.99 | $54.99 | $54.02 | $66.38 | $2.96 | -$12.36 | -$23.36 | 26,300 | 56.7 | amber | no, loses money (caution) |
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

## holiday-gifts

| # | Product | Sell | US cost | Before ads | Ad cost (tough) | Profit (benchmark) | Profit (tough) | If cost +20% | Amazon/mo | Score | Tier | Start now? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | rolling-knife-sharpener-kit | $69.00 | $13.07 | $49.49 | $63.19 | $0.88 | -$13.70 | -$16.32 | 16,050 | 51.7 | amber | no, loses money |
| 2 | cocktail-smoker-kit | $33.24 | $22.11 | $7.87 | $51.65 | -$31.86 | -$43.78 | -$48.20 | 32,000 | 64.2 | red | no, loses money |
| 3 | mini-car-vacuum-blower | $39.99 | $24.68 | $11.45 | $46.32 | -$24.18 | -$34.87 | -$39.80 | 72,350 | 61.9 | red | no, loses money |
| 4 | wireless-meat-thermometer | $33.99 | $30.42 | $0.24 | $63.19 | -$48.37 | -$62.95 | -$69.03 | 52,350 | 61.0 | red | no, loses money |
| 5 | electric-salt-pepper-grinder-set | $39.97 | $10.55 | $25.56 | $63.19 | -$23.05 | -$37.63 | -$39.74 | 25,900 | 59.9 | red | no, loses money |
| 6 | cordless-pressure-washer-gun | $69.99 | $32.49 | $30.97 | $58.89 | -$14.33 | -$27.92 | -$34.42 | 9,050 | 56.2 | red | no, loses money |
| 7 | monitor-light-bar-desk-kit | $44.99 | $8.85 | $31.84 | $66.38 | -$19.22 | -$34.54 | -$36.31 | 10,250 | 54.5 | red | no, loses money |
| 8 | smart-bird-feeder-camera | $51.29 | $58.79 | -$12.36 | $58.89 | -$57.66 | -$71.25 | -$83.01 | 10,650 | 53.4 | red | no, loses money |

## barkfare-addons

| # | Product | Sell | US cost | Before ads | Ad cost (tough) | Profit (benchmark) | Profit (tough) | If cost +20% | Amazon/mo | Score | Tier | Start now? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | suv-cargo-liner-dog | $69.00 | $21.42 | $41.14 | $51.00 | $1.91 | -$9.86 | -$14.14 | 1,900 | 38.1 | amber | no, loses money |
| 2 | folding-dog-car-ramp | $75.98 | $54.19 | $14.73 | $51.00 | -$24.50 | -$36.27 | -$47.11 | 17,100 | 57.8 | red | no, loses money |
| 3 | waterproof-dog-hammock-seat-cover | $69.00 | $24.58 | $37.98 | $51.00 | -$1.25 | -$13.02 | -$17.94 | 2,500 | 35.9 | red | no, loses money |
| 4 | backseat-dog-car-bed | $59.49 | $48.09 | $5.81 | $51.00 | -$33.42 | -$45.19 | -$54.81 | 3,450 | 34.9 | red | no, loses money |
| 5 | custom-pet-portrait-canvas | $62.00 | $35.38 | $20.80 | $51.00 | -$18.43 | -$30.20 | -$37.27 | n/a | 28.5 | red | no, loses money |
| 6 | front-bucket-seat-cover-dog | $44.99 | $15.45 | $25.24 | $51.00 | -$13.99 | -$25.76 | -$28.85 | 300 | 25.0 | red | no, loses money |
| 7 | dog-car-door-covers-2pack | $29.99 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | 16.0 | red | no US stock |

## beauty-fitness

| # | Product | Sell | US cost | Before ads | Ad cost (tough) | Profit (benchmark) | Profit (tough) | If cost +20% | Amazon/mo | Score | Tier | Start now? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | music-boxing-machine | $69.99 | $37.29 | $26.17 | $58.89 | -$19.13 | -$32.72 | -$40.18 | 18,450 | 58.5 | red | no, loses money (caution) |
| 2 | leg-air-compression-massager-heat | $119.99 | $44.29 | $64.72 | $58.89 | $19.42 | $5.83 | -$3.03 | 24,900 | 76.4 | green | BLOCKED on safety |
| 3 | cordless-neck-shoulder-kneading-massager | $89.99 | $23.29 | $58.39 | $58.89 | $13.09 | -$0.50 | -$5.16 | 14,050 | 64.6 | amber | BLOCKED on safety |
| 4 | shiatsu-foot-massager-machine | $109.99 | $64.49 | $35.41 | $58.89 | -$9.89 | -$23.48 | -$36.38 | 34,300 | 52.1 | red | BLOCKED on safety |
| 5 | cordless-heated-hand-massager | $79.99 | $31.69 | $40.88 | $58.89 | -$4.42 | -$18.01 | -$24.35 | 14,700 | 51.7 | red | BLOCKED on safety |

## Rule review (ASSUMED: our reading of CLAUDE.md section 2; Dhruv can overrule)

- barkfare-extender-cheaper-listing: CAUTION. A lead, not a supplier: a $47.31 US-stock card with no sales count, seen Nov 22. Check size, board rigidity and weight rating before relying on it.
- japanese-style-knife-set: CAUTION. The $26.49 cost is a 15-piece block set with 12 sold, not the gift set the $99 price is based on. Meta's ad rules on bladed items do not clearly allow kitchen knives. Never call it Japanese-made unless it is.
- rechargeable-wall-sconce-pair: CAUTION. Amazon sells sets of 2 at $45 to $57 with Prime, about half our price. The cost is one listing with 12 sold.
- barkfare-extender-us-stock: CAUTION. Your approved Nov 18 fast lane. The listing has 9 sales and an unknown store; the price is our own proposed kit price.
- cordless-tire-inflator: CAUTION. Lithium battery with a motor; certification UNKNOWN; two giant brands.
- portable-carplay-screen-kit: CAUTION. CarPlay and Android Auto are trademarks: 'works with' wording only, no logos. Similar screens sell for $45 to $77 on Amazon.
- mattress-vacuum-uv: CAUTION. UV light: no germ-killing or health claims allowed without proof.
- music-boxing-machine: CAUTION. Design patents exist for this product type; which factory shapes they cover is UNKNOWN.
- jump-starter-air-compressor: BLOCKED. High-current lithium pack clamped to a car battery; certification UNKNOWN. The scout flagged it as a likely fail on safety.
- leg-air-compression-massager-heat: BLOCKED. Medical rule: an air-compression leg massager is an FDA Class II device when sold for circulation or pain. The scout flagged it as likely excluded.
- heated-gloves-7v: BLOCKED. Blocked until battery certification is in hand: lithium packs and a heating element worn on the body, paperwork (UL, ETL or UN38.3) UNKNOWN. Its low cost is a listing with 3 sold.
- cordless-neck-shoulder-kneading-massager: BLOCKED. Blocked until battery certification is in hand: lithium battery and a heating element next to the neck.
- dog-force-dryer: BLOCKED. Mains-powered heated appliance used on animals; electrical certification UNKNOWN; over 10 lb.
- heated-vest-powerbank-kit: BLOCKED. Blocked until battery certification is in hand: heating element worn on the body; two sellers and two parcels.
- shiatsu-foot-massager-machine: BLOCKED. Mains-powered heated appliance, certification UNKNOWN; listings lean on health claims we cannot use.
- cordless-heated-hand-massager: BLOCKED. Medical rule: air-compression massagers sold for pain or circulation are FDA Class II devices; lithium battery and heat.
- towel-warmer-bucket: BLOCKED. Mains-powered heating appliance; electrical certification UNKNOWN; over 9 lb.
- heated-socks-app: BLOCKED. Blocked until battery certification is in hand: lithium packs worn against the leg.
- cordless-heated-blanket: BLOCKED. Battery-heated textile; certification UNKNOWN; no US stock found.

## Re-check at the cost of a better-proven US listing

| Product | Cheapest listing | Profit (tough) | Better-proven listing | Profit (tough) |
|---|---|---|---|---|
| japanese-style-knife-set | $26.49 | $0.21 | $33.39 (next US block set) | -$6.69 |
| rechargeable-wall-sconce-pair | $36.69 | $0.02 | $47.15 (style closer to the Amazon best sellers ($45.91 to $52.89)) | -$10.44 |
| heated-gloves-7v | $25.89 | $4.19 | $48.69 (the US listing with 110 sold) | -$18.61 |

## Shortlist for the logged-in cost check (listed cost within 15% of the cost that passes the cushion rule)

| Product | Sell | Listed US cost | Go price: cost must be at or under | Profit at that cost (tough) |
|---|---|---|---|---|
| barkfare-extender-cheaper-listing | $149.00 | $54.01 | $83.13 | $1.31 |
| japanese-style-knife-set | $99.00 | $26.49 | $25.08 | $1.62 |
| rechargeable-wall-sconce-pair | $109.99 | $36.69 | $35.09 | $1.62 |
| barkfare-extender-us-stock | $149.00 | $83.69 | $83.13 | $1.31 |

## First week on a small budget (top 10 overall, tough ad cost, no payout yet)

| Product | Budget | Orders the cash covers | Sales | Profit after setup and sample | Orders for $2,000 | Cash needed for $2,000 |
|---|---|---|---|---|---|---|
| barkfare-extender-cheaper-listing | $500.00 | 4 | $596.00 | $51.71 | 14 | $1,540.14 |
| barkfare-extender-cheaper-listing | $1,000.00 | 8 | $1,192.00 | $173.43 | 14 | $1,540.14 |
| japanese-style-knife-set | $500.00 | 5 | $495.00 | -$41.46 | 21 | $1,925.83 |
| japanese-style-knife-set | $1,000.00 | 10 | $990.00 | -$40.43 | 21 | $1,925.83 |
| rechargeable-wall-sconce-pair | $500.00 | 4 | $439.96 | -$52.62 | 19 | $1,950.47 |
| rechargeable-wall-sconce-pair | $1,000.00 | 9 | $989.91 | -$52.53 | 19 | $1,950.47 |
| barkfare-extender-us-stock | $500.00 | 2 | $298.00 | -$98.19 | 14 | $1,985.34 |
| barkfare-extender-us-stock | $1,000.00 | 6 | $894.00 | -$95.19 | 14 | $1,985.34 |
| cordless-tire-inflator | $500.00 | 7 | $419.93 | -$79.94 | 34 | $2,116.55 |
| cordless-tire-inflator | $1,000.00 | 15 | $899.85 | -$135.84 | 34 | $2,116.55 |
| filtered-shower-head-kit | $500.00 | 6 | $474.00 | -$55.79 | 26 | $2,008.67 |
| filtered-shower-head-kit | $1,000.00 | 12 | $948.00 | -$82.64 | 26 | $2,008.67 |
| mini-smart-projector | $500.00 | 4 | $399.96 | -$100.30 | 21 | $2,210.52 |
| mini-smart-projector | $1,000.00 | 9 | $899.91 | -$160.18 | 21 | $2,210.52 |
| small-dog-booster-car-seat | $500.00 | 6 | $419.94 | -$94.39 | 29 | $2,151.37 |
| small-dog-booster-car-seat | $1,000.00 | 13 | $909.87 | -$160.32 | 29 | $2,151.37 |
| portable-carplay-screen-kit | $500.00 | 3 | $359.97 | -$108.06 | 17 | $2,134.25 |
| portable-carplay-screen-kit | $1,000.00 | 7 | $839.93 | -$157.49 | 17 | $2,134.25 |
| lightweight-pet-stroller | $500.00 | 5 | $424.95 | -$112.71 | 24 | $2,187.23 |
| lightweight-pet-stroller | $1,000.00 | 10 | $849.90 | -$171.52 | 24 | $2,187.23 |

## Capped test plan: up to $350.00 of ads on one product, cut where needed to keep total cash out under $1,000.00 (top 8 with US stock)

| Product | Ad cap | Orders (benchmark to tough) | Sales | Net after setup and sample | Cash out before any payout | Stop an ad with no sale at |
|---|---|---|---|---|---|---|
| barkfare-extender-cheaper-listing | $350.00 | 8.9 to 6.9 | $1,329.34 to $1,022.57 | $306.48 to $138.83 | $901.87 to $790.67 | $81.43 |
| japanese-style-knife-set | $350.00 | 7.2 to 5.5 | $712.82 to $548.32 | $63.99 to -$41.35 | $583.22 to $539.21 | $63.40 |
| rechargeable-wall-sconce-pair | $350.00 | 7.2 to 5.5 | $791.95 to $609.19 | $52.44 to -$52.59 | $666.86 to $605.90 | $63.21 |
| barkfare-extender-us-stock | $280.00 | 7.1 to 5.5 | $1,063.47 to $818.06 | -$10.34 to -$95.57 | $977.02 to $839.17 | $51.75 |
| cordless-tire-inflator | $350.00 | 9.8 to 7.6 | $589.29 to $453.30 | $5.33 to -$83.82 | $528.56 to $494.52 | $39.33 |
| filtered-shower-head-kit | $350.00 | 7.2 to 5.5 | $568.81 to $437.55 | $43.84 to -$53.73 | $472.19 to $450.67 | $58.72 |
| mini-smart-projector | $350.00 | 6.9 to 5.3 | $685.40 to $527.23 | -$29.49 to -$115.54 | $651.83 to $594.27 | $54.40 |
| small-dog-booster-car-seat | $350.00 | 8.9 to 6.9 | $624.43 to $480.33 | -$16.91 to -$102.52 | $583.09 to $538.04 | $41.58 |

## The $100,000 by year end claim on benchmark numbers

- Orders needed at a $74.62 average order: 1,341 in 40 days (34 a day).
- Ad spend at the all-industry benchmark: $53,277.93 ($1,331.95 a day); at new-store cost: $69,261.31.
- That is 53 times a $1,000 budget for ads alone.
- Supplier payments at the median cost share in our candidates (43% of price): $42,930.37.
- The creator's own reported month: ads were 55% of revenue and profit 10%. At that margin $100,000 of sales leaves $10,039.94.

## China-shipped comparison (where a China cost was found; 10% refund allowance ASSUMED)

| Product | US cost | China cost | Profit tough, US | Profit tough, China |
|---|---|---|---|---|
| japanese-style-knife-set | $26.49 | $20.89 | $0.21 | $1.85 |
| mini-smart-projector | $36.39 | $58.79 | -$11.98 | -$38.38 |
| portable-carplay-screen-kit | $54.99 | $58.39 | -$12.36 | -$20.56 |
| mattress-vacuum-uv | $34.83 | $31.89 | -$7.23 | -$8.29 |
| hd-galaxy-projector | $28.06 | $15.45 | -$36.90 | -$26.69 |
| ai-translation-earbuds | $37.79 | $11.69 | -$40.74 | -$17.44 |
| wireless-carplay-adapter | $26.29 | $13.33 | -$38.32 | -$27.76 |
| compact-digital-camera-kit | $33.69 | $19.59 | -$27.50 | -$16.60 |
| jump-starter-air-compressor | $33.49 | $41.39 | $10.98 | -$0.92 |
| heated-gloves-7v | $25.89 | $54.99 | $4.19 | -$28.83 |
| cordless-heated-hand-massager | $31.69 | $47.49 | -$18.01 | -$37.01 |
| heated-socks-app | $24.59 | $37.89 | -$26.40 | -$42.22 |

## Ad spend needed to leave Meta's learning phase (50 purchases in a week)

- pets: $1,961.50
- home: $2,430.50
- tech: $2,553.00
- outdoor: $2,265.00
- beauty: $2,022.00
- auto: $1,781.50
- all: $1,986.50
