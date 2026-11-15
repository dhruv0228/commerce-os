# Sourcing platforms and "winning products" check, Nov 15, 2026

**Why:** Dhruv saw a Reel (@gianni.ecom) using TeemDrop's "winning products" with an AI-built Shopify store, and asked whether platform winners match our numbers.

**Data:**
- `research/platform-winners-2026-11-15/platforms.json`: 40 platforms.
- `winners.json`: 60 platform "winners", enriched with Amazon sales, YouTube, Google seasonality and Foreplay.
- `winners_scored.csv`: scores from `scripts/opportunity.py`; economics from `scripts/channels.py`.

## 1. Executive summary
- **Platform "winners" are real product types, sold at prices buyers don't pay.**
  - The platforms' suggested retail is a median of 2.0× the price where most Amazon units sell; 88% are more than 1.3× higher.
  - Only about 19% of Amazon units sell at or above the platform price (researcher's figure).
- **Of 60 winners:**
  - 13 fail our exclusions (mostly uncertified mains heaters); 47 are eligible.
  - At real prices, only 4 of the 47 break even at scale. Only 1 passes both gates: a GPS dog tracker, which needs cellular certification and a subscription back end, so it isn't practical.
  - Even at the platforms' own suggested prices, only 8 of 42 clear $8 profit at scale. Several of those barely sell at that price on Amazon.
- **TeemDrop scores 2/10 for us:**
  - Its "winning products" are picked by TeemDrop itself, with no sales data, and need an account to view.
  - It ships from China in 7 to 15 days and connects only to Shopify, with no API.
  - The operating company was incorporated in the UK in Nov 2024, and the business runs from Hangzhou. Its Trustpilot rating is suspended for guideline breaches.
- **The Reel's store copies a real brand.** "mellow" and "CloudAlign Pillow" belong to Mellow LLC (mellowsleep.com). The store shows 46,040 reviews and "#1 Selling TikTok Pillow" on a new store: trademark risk, plus FTC fake-review exposure (16 CFR Part 465).
- **The Reel's pillow fails our math** (`channels.py --price 54.99 --cost 6.80 --ship 17.98`):
  - Own store with Meta ads: $24.47 kept before ads, so it loses about $23 per order at the $47.93 Home & Garden median ad cost.
  - On Amazon the same pillow type sells about 350 units a month at $13.99.
- **Our finalists still lead:** dog back-seat extender kit 72.3, dash cam 68.7. The best eligible platform winner without a subscription back end is the electric spin scrubber at 56.6, with $0.20 profit per scaled order.

## 2. What the platforms' "winning" signal really is
| Signal | Platforms |
|---|---|
| Real sales | Amazon "bought in past month" via DataForSEO, Amazon Best Sellers, TikTok Shop "sold" counts, AliExpress order counts |
| Modeled sales | Kalodata, FastMoss, EchoTik, Jungle Scout, Keepa |
| Ad engagement | Minea, PiPiAds, TrendTrack, Winning Hunter, TikTok Creative Center |
| Curated by the supplier, which earns when you list its items | TeemDrop, CJ trending, Zendrop, AutoDS, Ecomhunt |

## 3. Recommended stack
1. **Sourcing:** CJdropshipping filtered to US-warehouse stock. It's the only supplier found with a documented API that can force US shipping and choose the warehouse, so it can connect to Amboras through our code. Alternative: an own-brand micro-batch from Alibaba (Trade Assurance) or 1688, air-shipped to Dhruv.
2. **Research:** real sales first.
   - DataForSEO Amazon (connected).
   - Amazon Best Sellers and TikTok Shop "sold" counts.
   - EchoTik free, or about $14.90 a month on yearly billing for the API when the scanner needs it.
   - Foreplay for ad evidence.
3. **Use platform "winner" lists only as idea feeds** into our scanner, never as evidence.

## 4. Decision
No new gate. These pending items remain:
- **Gate 4 (extender outreach)** needs the brand name, send-from email, ZIP code and the door-guard choice.
- **Optional:** sign up for a free CJdropshipping account (for its API key) and EchoTik free, so the weekly scanner can pull US-warehouse stock and TikTok Shop sales.

Sources: see `platforms.json` and `winners.json`. Key ones:
- https://apps.shopify.com/teemdrop-1
- UK Companies House (EASYFLOW LOGISTICS LIMITED, 16065800)
- https://mellowsleep.com
- https://www.ftc.gov/legal-library/browse/rules/rule-use-consumer-reviews-testimonials
- https://developers.cjdropshipping.com/en/api/api2/api/shopping.html
- https://www.echotik.live
