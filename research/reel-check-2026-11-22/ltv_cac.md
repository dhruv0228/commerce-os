# LTV to CAC check (scripts/ltv_cac.py)

LTV here is what is left per customer after product, shipping, fees and refunds, before ads. CAC is the benchmark ad cost per purchase.
The reel's rule asks for a ratio of 3. The house cushion rule equals a first-order ratio of 1.33.

| Option | Left per customer, first order | Left per customer, 12 months (base to strong) | Ad cost per customer | Ratio, first order | Ratio, 12 months (base to strong) | Ad cost needed for 3 to 1 | Extra money per customer needed for 3 to 1 |
|---|---|---|---|---|---|---|---|
| Barkfare extender on Amazon (FBA), bulk stock | $56.31 | no reorders modelled | $13.10 (Amazon pay-per-click, from channels.py) | 4.30 | same as first order | $18.77 | $0.00 |
| Barkfare $189 bundle, bulk stock in a US warehouse | $85.88 | no reorders modelled | $39.23 (Meta, pets benchmark) | 2.19 | same as first order | $28.63 | $31.81 |
| Barkfare extender, cheaper US listing seen Nov 22 (lead) | $81.43 | no reorders modelled | $39.23 (Meta, pets benchmark) | 2.08 | same as first order | $27.14 | $36.26 |
| Barkfare extender, bulk stock in a US warehouse | $72.76 | no reorders modelled | $39.23 (Meta, pets benchmark) | 1.85 | same as first order | $24.25 | $44.93 |
| Dog portrait blanket and canvas at $149, print-on-demand | $59.18 | no reorders modelled | $39.23 (Meta, pets benchmark) | 1.51 | same as first order | $19.73 | $58.51 |
| Own-brand skincare 3-step set, US maker ships | $25.56 | $38.34 to $56.23 | $40.44 (Meta, beauty benchmark) | 0.63 | 0.95 to 1.39 | $18.74 | $65.09 |
| Barkfare extender, US-stock fast lane | $51.75 | no reorders modelled | $39.23 (Meta, pets benchmark) | 1.32 | same as first order | $17.25 | $65.94 |
| japanese style knife set | $63.40 | no reorders modelled | $48.61 (Meta, home benchmark) | 1.30 | same as first order | $21.13 | $82.43 |
| rechargeable wall sconce pair | $63.21 | no reorders modelled | $48.61 (Meta, home benchmark) | 1.30 | same as first order | $21.07 | $82.62 |
| Barkfare extender, 5-kit trial shipped from home | $32.87 | no reorders modelled | $39.23 (Meta, pets benchmark) | 0.84 | same as first order | $10.96 | $84.82 |
| Own-brand supplement, US maker ships each order | $14.23 | $21.34 to $31.31 | $39.73 (Meta, all benchmark) | 0.36 | 0.54 to 0.79 | $10.44 | $87.88 |
| Own-brand skincare, US maker ships each order (print-on-demand style) | $13.59 | $20.37 to $29.89 | $40.44 (Meta, beauty benchmark) | 0.34 | 0.50 to 0.74 | $9.96 | $91.43 |
| Resell a known K-beauty brand (wholesale), ship from home | $4.47 | $6.70 to $9.83 | $40.44 (Meta, beauty benchmark) | 0.11 | 0.17 to 0.24 | $3.28 | $111.49 |
| Affiliate: promote another brand for a commission | $3.75 | $3.75 to $3.75 | $40.44 (Meta, beauty benchmark) | 0.09 | 0.09 to 0.09 | $1.25 | $117.57 |

Options that reach 3 to 1 in their best case: ext_fba.
Options that pass the house rule on the first order: ext_fba, bulk_sea_bundle, barkfare-extender-cheaper-listing, bulk_sea, pod_149.

Benchmarks ESTIMATED (Triple Whale medians, established brands). Costs behind each row are ESTIMATED or ASSUMED in their own files. Reorder counts are ASSUMED. Nothing here is measured from our own store.
