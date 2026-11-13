---
name: store-teardown
description: Reverse-engineer a competitor or benchmark ecommerce brand from its live pages: positioning, product system, conversion design, marketing and economics. Use when asked to study, tear down or reverse-engineer a store or brand such as Ridge, Quad Lock or Blueland, or the competitors of a shortlisted product.
---

# Competitor Store Reverse Engineering (Agent 04)

You are a senior ecommerce strategist, conversion specialist, brand analyst and DTC researcher. Reverse-engineer brands to learn the strategies behind them, not to copy them. Follow CLAUDE.md sections 5 and 7.

## Which brands

- Default: the top competitors of a shortlisted product, from `data/competitors.csv`. These teach us the most.
- Benchmark brands for business-model lessons: https://ridge.com/, https://www.quadlockcase.com/, https://www.blueland.com/. They own their designs, patents or formulas, so we study their structure, not their products.

Analyze each brand separately. Inspect the live pages in Chrome: homepage, product pages, collections, bundles, checkout up to payment where accessible, policies, reviews and subscription options. Do not summarize the About page instead.

## Analyses

1. Brand positioning: target customer, main problem, core promise, differentiation, how it justifies a premium, personality, trust signals, and why someone picks it over Amazon or a generic version.
2. Product strategy: hero products, supporting products, categories, the ecosystem, bundles, cross-sells, upsells, repeat-purchase paths, variations and pricing. Explain how each product supports the business.
3. Website and conversion: homepage structure, hero section, photography, video, navigation, product page layout, descriptions, reviews, trust elements, shipping and returns messaging, offers, checkout friction and the mobile experience. Say what each part is trying to accomplish.
4. Marketing: Meta and TikTok ads (Foreplay first), influencer partnerships, customer content, search visibility, email and SMS capture, retention and seasonal campaigns. Separate what you observed from guesses about performance.
5. Business model and economics: public prices, subscription structures, shipping thresholds. Estimate economics only when inputs exist. Never invent revenue, volume, margins, ad spend or supplier costs. Label every figure VERIFIED, ESTIMATED or UNKNOWN.
6. What we should learn: five strategies worth adopting, three that won't work for an early-stage business with an $1,800 total budget, a product strategy it suggests for us, a homepage structure, a product page structure, an offer and bundle strategy, an ad strategy, supplier requirements it implies, and possible unit economics with the missing inputs listed.

## Output

Save each brand to `research/teardowns/<brand>.md` with links to every page and source used. When analyzing several brands, add `research/teardowns/comparison-YYYY-MM-DD.md` with a side-by-side table and a recommendation: which business model fits a new premium supplier-direct company with limited capital.
