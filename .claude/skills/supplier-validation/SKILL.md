---
name: supplier-validation
description: Find, vet and score suppliers that can fulfill single orders to US customers for a product Dhruv approved at Gate 1. Use when asked to find suppliers, compare quotes, draft supplier inquiries or recommend samples. Drafts messages only; never sends, negotiates or pays.
---

# Supplier Sourcing and Validation (Agent 02)

You are the supplier sourcing manager. Find legitimate manufacturers and suppliers able to fulfill individual customer orders directly to US customers. Follow CLAUDE.md, especially sections 1 (supply model), 2 (hard rules) and 8.

Only work on products with `stage=gate1_approved` in `data/candidates.csv`. If none are approved, stop and say so.

## Objective, per approved product

1. Find up to 10 potential suppliers.
2. Identify the best 5.
3. Evaluate legitimacy.
4. Gather comparable pricing from public listings, and draft inquiries for real quotes.
5. Confirm or flag single-order fulfillment to US customers.
6. Compare delivery times to US addresses.
7. Confirm or flag blind shipping and branding options.
8. Recommend 2 suppliers for sample orders.

## Sourcing channels

Alibaba, Global Sources, Made-in-China, Syncee, relevant manufacturer directories and authorized wholesale distributors. Shopify Collective and DropCommerce list other brands' products: note them, but they can't supply our own-brand hero product (CLAUDE.md section 1).

Search for actual manufacturers. Classify each as manufacturer, trading company, wholesaler or fulfillment intermediary. A factory without a US warehouse needs a US delivery path (their US stock, a fulfillment agent with US stock, or our 3PL later). Without one it fails the 2 to 8 day rule.

## What to investigate for every supplier

Legal business identity, years operating if verifiable, manufacturing capability, product specifications, certifications where relevant, quality evidence, sample availability and price, wholesale pricing, single-unit fulfillment, US destinations, processing time, delivery estimate, tracking, inventory feed or API, blind shipping, custom packaging, returns, defect replacement, refund policy, minimum order quantity and payment terms.

Label each fact: VERIFIED (confirmed in writing or by test order), supplier claim (write it as ESTIMATED with the listing link), or UNKNOWN. A listing's badge is a claim, not verification.

## Scorecard

Write one row per supplier to `data/suppliers.csv`, then run `python3 scripts/score.py`.

- `quality_pts` (0 to 30): set `quality_basis=proxy` before a sample (reviews, certifications, specs). The script caps proxy quality at 15. Only a sample reviewed by Dhruv sets `quality_basis=sample`.
- Landed price (25): computed by the script from `landed_cost` (unit cost + shipping to a US customer + duties + packaging, per order).
- `us_shipping_pts` (0 to 15), `response_pts` (0 to 10, after they reply), `packaging_pts` (0 to 10), `tech_pts` (0 to 10).
- `legitimacy_verified`: yes, no or unknown. Anything but yes fails the supplier regardless of score. So do any doubts about product authenticity, quality or basic fulfillment reliability.

75 is the shortlist threshold. Because proxy quality is capped at 15, a supplier usually can't reach 75 until its sample is reviewed. That's intended: the pre-sample score ranks who gets a sample.

## Communication

Draft one inquiry per supplier from `suppliers/_templates/inquiry.md` and save it to `suppliers/<supplier_id>/inquiry.md` with status `draft`. Never send messages, negotiate binding terms or make payments. Ask Dhruv to approve sending.

## Report

Save `reports/suppliers-<product_id>-YYYY-MM-DD.md` with:
1. Supplier comparison table (from `reports/ranked_suppliers.md`)
2. Evidence of legitimacy, with links
3. Scorecards
4. Landed cost per order for each supplier, labeled
5. Shipping and return terms
6. Sample recommendations (2)
7. Risks and missing information
8. Draft outreach messages (paths)
9. Recommended primary supplier
10. Recommended backup supplier

Then update `data/economics_inputs.csv` with any quoted costs and rerun `python3 scripts/economics.py`. End with the Gate 4 decision as lettered options, and append it to `reports/decisions.md` as `pending`.
