# Ruff Liners teardown (2026-11-15)

Product: dog back-seat extender (our kit at $149). Competitor role: price and volume leader of the premium band (Amazon B0DSK22N1J, 3,000+/mo, per `research/hero-deep-dive-2026-11-14/dog-car-travel-kit.json`).

All figures are ESTIMATED (third-party live page, read 2026-11-15) unless marked UNKNOWN. Screenshots: `stores/shots/ruffliners-*.jpg` in the session scratchpad (see `stores.json`); they are temporary and are not saved in the repo.

Pages read:
- Home: https://ruffliners.com/
- PDP: https://ruffliners.com/products/ruff-liners-medium-dog-back-seat-extender-for-dogs-and-door-protection-for-cars-mid-size-suv-and-mid-size-trucks-waterproof-hard-bottom-dog-car-seat-cover-for-back-seat
- Policies: https://ruffliners.com/policies/shipping-policy, https://ruffliners.com/policies/refund-policy
- Catalog and prices: https://ruffliners.com/products.json

## Store facts

| Field | Observed |
|---|---|
| Hero and price | Hard Bottom Backseat Extender with Door Protection. Standard $169.99 (compare-at $189.99); XL $189.99 (its compare-at is the same price) |
| Bundles and add-ons | Early Black Friday: extender plus Travel Dog Bed, 20% off both, "Both for $191.98" (Standard), countdown to Nov 24. Bed $69.99 (compare $79.99). Replacement window inserts, 6 for $15 (a replacement-part path). Soft hammock $109.99; XL truck floor cover $159.99 to $199.99 |
| Shipping | Free standard shipping on every US order. Ships in 1 to 2 business days and arrives 2 to 5 business days later. A Buy with Prime option appears at checkout |
| Returns and warranty | 30 days, no questions asked; refund within 10 business days. Warranty is 90 days, or 1 year if registered within 30 days |
| Reviews | 4.5 from 2,109 reviews on the PDP. The page code loads Appio's Amazon reviews importer, and on-page reviews mention buying on Amazon. The Amazon listing shows about 2,200 at 4.5 (DataForSEO, 2026-11-14) |
| Trust signals | US patent 12,221,024 printed on the PDP (door panels hung from window inserts). Car and Driver "#1 pick, best overall" quote. "More than 100,000 pup owners". Support 7 days a week. "As Seen on Shark Tank" appears in the Amazon title but nowhere in the site HTML we read |
| Payments | Shop Pay, PayPal, Apple Pay, Google Pay. No BNPL widget found. Checkout not tested |
| Fit guidance | Standard or XL by vehicle class. Homepage has a 5-type "What do you drive?" picker; the description lists compatible models. No measurement check. Captain's chairs are not addressed on the PDP (one reviewer used a third-party gap filler) |
| Popups and offers | Klaviyo "Ready to Save 10%?" email popup for 10% off. The footer signup asks for your vehicle. Intelligems price-testing script present |
| Photography and video | Real dogs in real trucks with seasonal styling (Santa hat). Install and use videos on the PDP. Meta: 1,133 active ads on 2026-11-14, 1,124 of them video (Foreplay brand uI70669iveAITZm3JY6o) |

## Page structure

- **Home:** countdown bar, then a Black Friday bundle hero with a countdown, the vehicle picker, best sellers with review counts, a 3-step explainer of the patented door protection, a guarantee row (30-day refund, 1-year warranty enrolment, 7-day support), detail features (clips, console zippers, seat-belt slots), testimonials plus the Car and Driver quote, a "layer by layer" materials section, a table against "Standard" covers, FAQ, an email form with a vehicle field, and the footer.
- **PDP:** a 7-slide gallery with video, then rating, title and one-line promise ("Bridges the footwell for a flat, sag-free surface"). Next come a pull-quote review (a 145 lb Great Dane), color, and a size selector with "Will it fit my vehicle?", then the bundle selector with countdown, add to cart and "Free shipping". Tabs cover description, install, cleaning, fit guide and policies. Below sit the guarantee row, a "what makes us different" video, reviews, cross-sells (bed, inserts) and FAQ.

## Positioning and product strategy

- **Customer:** owners of large dogs in trucks and SUVs, mostly men in the photos and reviews (F-150, Tacoma, 4Runner).
- **Promise:** seats, footwell and doors all covered. Door-panel protection is the differentiator, protected by a patent.
- **Premium case:** patent, press quote, heavy-duty build, review volume. It beats Amazon generics by covering the door panel and by brand trust.
- **Ecosystem:** extender, then the bed (20% bundle), then replacement window inserts at $15. The same customer is cross-sold to the truck floor cover. Amazon is clearly the main sales channel; the DTC site recycles Amazon reviews.

## Conversion design

- The vehicle picker is the homepage's first real decision, which lowers fit anxiety without a measuring step.
- The bundle selector sits above add to cart and its math is honest ($191.98 = 20% off both items).
- The guarantee row repeats on home and PDP.
- Weak spots: the 90-day base warranty is shown as a positive ("enroll for 1-year"), and the XL "regular price" equals its price.

## Visible weaknesses

1. The 90-day base warranty is far below RuffRover's and 4Knines' lifetime promises.
2. The door guards rely on window inserts, which 4Knines' published review analysis calls the top complaint (inserts and Velcro in 57.6% of 425 negative or mixed door-guard reviews; competitor marketing, ESTIMATED).
3. Fit is by vehicle class only, with no measurements and no captain's-chair answer.
4. On-site reviews appear imported from Amazon.
5. Countdown-driven urgency. One reviewer dislikes the large logos on the door covers.

## Economics (public)

Price $169.99, free shipping, 30-day returns. Revenue, ad spend, margins and supplier cost are UNKNOWN. The 1,133 active Meta ads are a signal of sustained spend, not proof of profit (CLAUDE.md section 3).

## What we should learn

- **Adopt:**
  1. A vehicle picker as the first step.
  2. An honest bundle selector on the PDP.
  3. A replacement-part SKU (inserts) as a reorder path.
  4. A guarantee row repeated near add to cart.
  5. Video-first creative.
- **Not for a $1,800 budget:**
  1. Over 1,000 live ad variants.
  2. A patent program.
  3. Amazon-first volume.
- **For us:** strap-hung door guards (no window inserts, which also avoids patent 12,221,024 claim elements per the hero deep dive), a 1-year warranty with no registration, and a measured fit check.
