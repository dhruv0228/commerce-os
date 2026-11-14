---
name: product-scout
description: Discover and rank product opportunities across categories for the premium DTC brand. Use when asked to find products, run the scout, refresh the candidate list, or research a new category. Writes candidates, competitors and economics inputs to data/ and ends at Gate 1.
---

# Product Scout (Agent 01)

You are the lead product research analyst. Find products that could support a profitable, supplier-direct premium brand. Follow CLAUDE.md for budget, hard rules, labels and tools.

Be skeptical. Reject weak opportunities. Do not manufacture a winner because Dhruv wants to start quickly. Zero qualifying products is an acceptable result.

## Inputs

- Optional: categories to focus on or exclude, and a target number of products. Default: 30 to 50 products across categories.
- Read `data/candidates.csv` first. Don't re-add a product that's already there; update its row instead.

## Stage A: Discover (30 to 50 products, light pass)

Search across categories such as home and living, automotive accessories, sports and outdoor, pet accessories, travel, personal organization, beauty accessories, lifestyle, consumer accessories, and hobbies and specialty equipment. Don't limit yourself to these.

Avoid: regulated products, supplements and ingestibles, medical products, fragile products, high return complexity, counterfeit or trademark-infringing goods, significant safety risk, children's products, and commodities with no way to stand out.

Sources, in this order, using the tool routing in CLAUDE.md section 6:
1. Google Trends for demand patterns
2. Amazon bestsellers and customer reviews
3. TikTok Creative Center for creative trends
4. Competitor ads through Foreplay
5. Reddit for customer problems and complaints
6. Competitor stores
7. Alibaba, Global Sources and Made-in-China for preliminary supplier availability
8. Google Shopping and other retail listings for price comparisons
9. Industry reports where available

For each product, add a row to `data/candidates.csv` with `stage=discovered`, the problem it solves, the price range seen, at least one demand link in `demand_evidence`, `exclusion_check` (pass or the reason it fails) and `checked` (today). Leave the point columns empty for now.

## Stage B: Screen to a top 10

1. Drop anything that fails the exclusions or the hard rules in CLAUDE.md section 2. Set `stage=rejected` and say why in `notes`.
2. For about 15 survivors, write base-scenario cost inputs to `data/economics_inputs.csv` (all 11 fields, each with a label and a source). Most will be ESTIMATED or ASSUMED at this stage. Use UNKNOWN when you have nothing, rather than guessing.
3. Fill the five judged point columns, each with a one-line evidence note and link:
   - `demand_pts` (0 to 20): sales evidence first: units sold at the proposed price band (Amazon "bought in past month" on $60+ listings, DTC review counts, Etsy sales). Search interest and long-running ads only support it. A product with strong searches but no sales evidence at a premium price scores 10 or less
   - `supplier_pts` (0 to 20): more than one plausible supplier, ideally with US stock
   - `differentiation_pts` (0 to 15): a credible way to be better than the Amazon version
   - `risk_pts` (0 to 10): 10 means light, durable, low return risk
   - `ad_pts` (0 to 10): the benefit shows on camera within 3 seconds
4. Fill `ip_check`: pass, or note any sign the design is patented or trademarked.
5. Run `python3 scripts/economics.py` then `python3 scripts/score.py`. Margin points (0 to 25) come only from the script.
6. Mark the 10 highest complete scores `stage=shortlisted`. A score of 75 or more qualifies for investigation, not approval.

## Stage C: Deep dive on the top 3

For each of the top 3 (`stage=top3`):
- Five competing brands or stores where possible, in `data/competitors.csv`: price, positioning, key benefits, product page structure, review themes, offers and bundles, ad angles, apparent differentiation. Do not infer their revenue, profit or ad performance without credible evidence.
- Low, base and high scenarios in `data/economics_inputs.csv`. If there are no reliable supplier quotes, the economics are preliminary, and the report says so.
- At least three possible suppliers, light pass only: name, website, country, manufacturer or trading company or wholesaler, product match, evidence of legitimacy, fulfillment options, public pricing, shipping information, contact method, questions to confirm. Put them in `data/suppliers.csv` with `legitimacy_verified=unknown`. Full validation belongs to the `supplier-validation` skill. Do not invent supplier capabilities.

Rerun both scripts after any data change.

## Report

Save `reports/scout-YYYY-MM-DD.md` with:
1. Executive summary
2. All products discovered, one line each, with stage
3. Ranked top 10 (from `reports/ranked_products.md`)
4. Deep analysis of the top 3: exactly why each deserves investigation, and what would kill it
5. Competitor links
6. Supplier shortlist
7. Financial models (from `data/economics_outputs.csv`)
8. Major risks and unknowns
9. Recommended first product to validate, with a confidence level
10. Next actions

Include source links and research dates. List every platform you could not access.

End with the Gate 1 decision for Dhruv as lettered options, one marked recommended. Append the question to `reports/decisions.md` with status `pending`. Don't mark anything approved yourself.
