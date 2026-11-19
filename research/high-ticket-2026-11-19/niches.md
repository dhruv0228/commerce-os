# High-ticket authorized-dealer niches (2026-11-19)

Question: which high-ticket niches can a solo founder with $2,000 or less enter as an authorized online dealer, with US brands or distributors shipping direct to the buyer?

Files in this folder:
- `niches.json`: one object per niche, machine-readable (17 niches).
- `google_ads_keywords.json`: new DataForSEO Google Ads pull, US, 2026-11-19, with 12 months of volumes.
- `google_trends_monthly.json`: DataForSEO Google Trends, US, for the keywords already pulled on 2026-11-16, to read their seasonality.
- Earlier keyword pull reused, not re-queried: `research/high-ticket-2026-11-16/google_ads_keywords.json`.

Reminder: CLAUDE.md section 1 allows reselling other brands for add-ons only, never the hero. A dealer store would need Dhruv to change that rule. This file is research only. No margin, CAC or profit math is done here; that belongs in `scripts/economics.py`.

## Executive summary

- **Most niches have no public dealer terms.** Margins, MAP rules and whether online-only stores are accepted are mostly UNKNOWN. Brands share them only after you apply. Dealer margin is UNKNOWN in 4 niches. The other 13 rest on proxies: dated trade press, other categories or countries, course-seller claims or anecdotes. Only Dundalk's figure is a brand's own dealer discount.
- **Some brands say no in writing:**
  - REP Fitness has no authorized US resellers.
  - SkyTrak does not accept dropship accounts.
  - Radio Flyer (Flyer e-bikes) is not opening new dropship accounts.
  - The Luxury Pergola requires your own install crew.
  - Hot tub brands sell through local dealers with territories.
- **Some programs say yes, or likely yes:**
  - Rain or Shine Golf names e-commerce resellers.
  - Shop Indoor Golf offers wholesale and drop ship of its SIGPRO products.
  - Osaki/Titan massage chairs have a long-standing dropship-wholesaler model (2012 source; confirm it still applies).
  - Golden Designs/Dynamic saunas are sold by many online-only "authorized dealers".
  - Dundalk LeisureCraft has a non-showroom dealer tier at 25% off MSRP (Canadian terms).
  - Ooni's dealer form asks about "your store or website".
- **Best fit on demand, timing and shipping:**
  - Golf simulator components: parcel freight, strong Dec to Jan, specialist suppliers with reseller programs.
  - Infrared and barrel saunas: strongest Dec to Jan of the high-ticket items.
  - Massage chairs: dropship model, December gift peak.
  - Electric fireplaces: the most seasonal item (Nov to Jan), parcel freight, about 38-40% hearth-retailer margin (2014 data).
- **Worst fit for this model:**
  - Hot tubs and swim spas: territories, hardwiring, no returns.
  - E-bikes: battery-fire risk, a CPSC rule in progress, and brands that want showrooms.
  - Pool tables: install network needed.
  - Pergolas and outdoor kitchens: Dec to Jan is their low season.
- **Cash:** with $2,000, one order means paying the supplier $1,500 to $7,000+ before Shopify pays out (the dealer cost is retail minus a 20-35% margin; ESTIMATED). Shopify Payments can also hold reserves on high-ticket or new stores (forum reports; official help page not retrieved). This alone may rule out sauna, hot tub and simulator packages until a supplier gives net-30 terms. Net-30 is described as coming "once you build dealer trust" (course-seller source).

## Summary table

Search volume and CPC: DataForSEO Google Ads, US. Dec/Jan index = average of Dec and Jan divided by the 12-month average (1.00 = average). Prices and margins are ESTIMATED unless marked; see `niches.json` for sources.

| Niche | Retail range | Typical AOV (label) | Dealer margin % | Freight | Main keyword: vol / CPC | Dec/Jan index | Online-only dealer access |
|---|---|---|---|---|---|---|---|
| Infrared saunas | $1,500-9,000 | $4,000 (ASSUMED) | 20-35 (weak proxy) | LTL | infrared sauna: 110,000 / $5.92 | 1.45 (Trends) | Golden Designs likely; others UNKNOWN |
| Outdoor/barrel saunas | $2,700-8,500 | $5,500 (ASSUMED) | 25-35 (Dundalk, Canada) | LTL | outdoor sauna: 33,100 / $4.28 | 1.30 | Dundalk non-showroom tier possible |
| Cold plunges | $400-14,500 | $4,500 (ASSUMED) | UNKNOWN | LTL (parcel for inflatables) | cold plunge: 60,500 / $9.71 | 1.15 | No dealer programs found for major brands |
| Golf simulators | $800-48,499 | $6,000 (ASSUMED) | UNKNOWN | Parcel | golf simulator: 165,000 / $4.50 | 1.22 | Rain or Shine yes; SIG dropship; SkyTrak no dropship |
| Home gym | $240-4,300 | $1,500 (ASSUMED) | 25-50 (dated) | LTL | treadmill: 301,000 / $3.60 | 1.33 | REP no; GoFit yes (low ticket); others UNKNOWN |
| Massage chairs | $800-12,000 | $3,000 (ASSUMED) | 20-40 | LTL | massage chair: 110,000 / $2.63 | 1.18 | Osaki dropship likely |
| Hot tubs/swim spas | $4,000-70,000 | $9,000 (ASSUMED) | 40-50 (2017 showroom target) | LTL/flatbed | hot tub: 201,000 / $3.30 | 1.02 (swim spa 0.69) | Unlikely |
| Standing desks/ergo chairs | $249-2,350 | $750 (ESTIMATED median) | UNKNOWN | Parcel | standing desk: 135,000 / $5.18 | 0.96 (chair 1.54) | UNKNOWN; Herman Miller/Steelcase unlikely |
| Pizza ovens | $349-2,000 | $600 (ASSUMED) | 30-50 (category proxy) | Parcel | pizza oven: 110,000 / $1.15 | 1.21 | Ooni possible |
| Outdoor kitchens/grills | $5,399-17,423 | $9,000 (ASSUMED) | 30-50 (category proxy) | LTL | outdoor kitchen: 60,500 / $4.58 | 0.79 | UNKNOWN |
| Pergolas/outdoor furniture | $1,299-55,000 | $4,000 (ASSUMED) | 30-50 (category proxy) | LTL | pergola: 301,000 / $3.18 | 0.59 | Luxury Pergola no; others UNKNOWN |
| E-bikes | $999-2,499 | $2,000 (ESTIMATED) | 20-45 | Parcel (lithium) | electric bike: 1,500,000 / $1.10 | 0.68 | Flyer no; Aventon/Velotric unlikely |
| Espresso (prosumer) | $1,747-8,820 | $2,500 (ASSUMED) | 20-35 (weak) | Parcel | espresso machine: 368,000 / $1.12 | 1.23 | UNKNOWN |
| Electric fireplaces (added) | $670-8,999 | $1,500 (ASSUMED) | 38-40 (2014 hearth avg) | Parcel | electric fireplace: 135,000 / $1.40 | 1.67 (Trends) | UNKNOWN |
| Home backup power stations (added) | $299-6,199 | $2,000 (ASSUMED) | UNKNOWN | Parcel (lithium) | portable power station: 246,000 / $0.89 | 1.27 | UNKNOWN |
| Gas fire pit tables (added) | $399-4,499 | $2,000 (ASSUMED) | 30-50 (category proxy) | Mixed | fire pit table: 18,100 / $1.62 | 0.70 | Solo Stove via Faire possible |
| Slate pool tables (added) | $2,000-12,000 | $5,000 (ESTIMATED, weak) | 35-40 (forum anecdote) | LTL + install | pool table: 201,000 / $1.50 | 1.37 | Unlikely (install) |

Every keyword in both pulls shows Google Ads competition HIGH (index 100).

Head-term search volume overstates demand at dealer price points:
- "espresso machine", "electric bike", "portable power station" and "standing desk" are dominated by sub-$1,000 products.
- "infrared sauna" includes blankets and near-me searches.

## Seasonality (is Dec/Jan good?)

| Good in Dec/Jan (index 1.15 or higher) | Neutral (0.95 to 1.15) | Weak (below 0.95) |
|---|---|---|
| electric fireplace 1.67, ergonomic office chair 1.54, infrared sauna 1.45, barrel sauna 1.38, pool table 1.37, golf simulator enclosure 1.34, treadmill 1.33, outdoor sauna 1.30, home gym 1.27, portable power station 1.27, espresso machine 1.23, golf simulator 1.22, pizza oven 1.21, massage chair 1.18, rowing machine 1.16, cold plunge 1.15 | hot tub 1.02, power rack 1.00, launch monitor 0.98, pellet grill 0.98, standing desk 0.96 | outdoor kitchen 0.79, fire pit table 0.70, swim spa 0.69, electric bike 0.68, pergola 0.59, outdoor furniture 0.47 |

Data caveat:
- In the Google Trends pull, every series jumps in Mar to Jun 2026, including electric fireplace, a winter product. This is treated as a data artifact, so seasonality for those keywords is read from Nov 2024 to Oct 2025.
- The Google Ads monthly volumes (Nov 2025 to Oct 2026) do not show that jump.

## Per-niche notes

### Infrared saunas
- **Price:**
  - 1-2 person far-infrared units: $1,500 to $4,000 (vendor guide, peaksaunas.com).
  - Quality 2-person units: $4,800 to $9,000.
  - Sun Home Equinox 2: $6,099, 120V plug-in.
- **Suppliers:**
  - Golden Designs/Dynamic/Maxxus is sold by Costco, Wayfair and many online-only "authorized dealers". No public terms found.
  - Clearlight has a dealer page aimed at bath and spa retailers.
  - Sun Home has a dealer/wholesale inquiry form.
  - Sunlighten and Health Mate: only referral or affiliate programs found.
- **Margin:** ESTIMATED 20-35%, from the Dundalk proxy and course-seller ranges. The Dundalk terms PDF host could not be reached from this session; the figure comes from the search snippet.
- **Shipping:** LTL curbside. Larger units need 240V wiring.
- **Risks:** freight damage, and the temptation to make health claims (not allowed).

### Outdoor and barrel saunas
- **Price:** $3,799 to $8,499+; most 4-6 person models $4,500 to $7,500 (topture.com, retailer).
- **Dundalk LeisureCraft dealer terms (Canadian):**
  - Trade only.
  - 25% off MSRP without a showroom, 35% with one.
  - New dealers pay at order.
  - US terms may differ.
- **Almost Heaven:** no public dealer application.
- **Shipping and install:** LTL kit, customer assembly, 240V heater wiring or wood-fired. Outdoor structures may need local permits.

### Cold plunges
- **Price pressure:** Costco sold the LifeTrend chiller tub at $399.97 to $899.99 during 2026, and that pulls buyer expectations down.
- **Suppliers:**
  - Plunge has an affiliate program only ($250 per order).
  - No dealer program found for Ice Barrel, BlueCube, Renu or Dragon Plunge.
  - Sun Home and Dundalk sell plunges through dealers.
- **CPC:** $9.71, the highest in the set.
- **Margin:** UNKNOWN.

### Golf simulators, launch monitors, enclosures
- **Most open supplier side found:**
  - Rain or Shine Golf (names e-commerce resellers).
  - Shop Indoor Golf partner portal (wholesale and drop ship).
  - Carl's Place wholesale.
  - The SportScreen verified resellers (Feb 2026; checks territory overlap).
- **Launch monitors are harder:** SkyTrak refuses dropship accounts and requires minimum orders and a credit check. Foresight, Uneekor and TrackMan sell through established dealers; terms not found.
- **Shipping:** parcel, multi-box.
- **Margin:** UNKNOWN.
- **Competition:** large specialist dealers who also sell their own private-label enclosures.

### Home gym
- **Suppliers:**
  - REP Fitness: "no authorized resellers in the US"; affiliate up to 8%.
  - Body-Solid: MAP on 375+ items (2021).
  - Life Fitness: dealer form includes a dropship option.
  - GoFit: accepts e-commerce dealers (not Amazon/eBay), but it is a low-ticket brand.
- **Margin:** 38.2% for specialty fitness retailers (NSGA, 2003, OLD). One dealer reported 45-50% (anecdote). Treadmills are lower-margin.
- **Seasonality:** strong January.

### Massage chairs
- **Osaki/Titan (Carrollton, TX):**
  - Dropship wholesaler: the dealer holds no stock, and Osaki ships and covers warranty (2012 press release, OLD).
  - Its Faire listing invites dealer applications, with 60-day terms (search snippet; Faire returned 403 to fetch).
  - Titan Chair Trustpilot score: 2.5.
- **Margin:** 20-40%. Sources are a franchise pitch (20-50%) and a 2008 dealer blog (25-40%).
- **Returns:** one dealer charges a 25% restocking fee plus freight and white glove both ways. Human Touch and Cozzia charge 15%; Synca 20%.

### Hot tubs and swim spas
- **Sales model:** local dealer networks with territories; Hydropool says it doesn't sell online.
- **Margin:** 40-50% dealer target (2017, showroom model).
- **Install:** electrical hardwiring and site prep.
- **Verdict:** poor fit for a solo online dealer.

### Standing desks and ergonomic chairs
- **Prices:** median standing desk $744 (20 desks, July 2026), so this is mid-ticket rather than high-ticket.
- **Suppliers:**
  - UPLIFT lists reseller accounts and a trade program.
  - iMovR targets contract furniture dealers.
  - Vivo takes wholesale inquiries by email.
  - Herman Miller and Steelcase choose their own resellers, and Steelcase publishes a gray-market list.
- **Margin:** UNKNOWN.
- **Shipping:** parcel; the lowest freight risk in the set.
- **Fit:** Dhruv knows this buyer first-hand, but dealer access and ticket size are weak.

### Pizza ovens
- **Prices:** Ooni Karu 2 is $449 (often $349 on sale); Gozney Dome about $1,800 to $2,000.
- **Suppliers:** Ooni has a dealer sign-up form that asks about "your store or website". Gozney's dealer path was not found.
- **Fit:** mid-ticket, parcel shipping, strong December, heavy Amazon and brand-DTC competition.

### Outdoor kitchens and premium grills
- **Prices:** BBQGuys complete islands $5,399 to $17,423.
- **Blaze:** authorized dealers only, and warranty is void if bought from unauthorized sellers.
- **Napoleon:** its MAP policy restricts free shipping and assembly add-ons.
- **Install and season:** gas install by a licensed trade; Dec to Jan is below average.

### Pergolas and outdoor furniture
- **Prices:**
  - Costco and Sam's aluminum grill pergolas: $1,299 to $1,899.
  - Louvered kits: $10,000 to $15,000.
- **Suppliers:**
  - The Luxury Pergola requires your own install crew.
  - Mirador's dealer program targets store owners and contractors.
- **Seasonality:** worst Dec to Jan in the set (outdoor furniture 0.47).

### E-bikes
- **Prices:** $999 to $2,499 typical.
- **Rad Power Bikes:**
  - Filed Chapter 11 on Dec 15, 2025, with $73M in liabilities.
  - Before filing, it said it could not afford a battery recall.
  - Sold to Life EV for $13.2M (closed March 2026).
- **CPSC battery rule:** proposed (NPRM June 24, 2026; comments closed Aug 24, 2026). No final rule found.
- **Dealer access:**
  - Aventon and Velotric dealers appear to be physical shops (inferred).
  - Radio Flyer says no new dropship accounts.
- **Verdict:** highest safety risk in the set.

### Espresso machines (prosumer and commercial)
- **Prices:** dual-boiler machines $1,747 to $8,820.
- **Market:** dominated by established specialists (Whole Latte Love, Seattle Coffee Gear, Clive, Cliff & Pebble). Warranty is tied to authorized dealers.
- **Margin:** weak evidence (20-35% for commercial, from a low-reliability report).
- **Service:** service-heavy category.

### Electric fireplaces (added)
- **Prices:** $669 to $8,999. The Modern Flames price guide is dated May 2025.
- **Margin:** 2014 hearth retailers averaged 38% actual against a 40% target, across all products.
- **Fit:**
  - Most seasonal keyword (1.67).
  - Parcel shipping, mostly 120V plug-in.
  - Competition from Home Depot, Lowe's, Amazon and Wayfair.
- **Dealer access:** UNKNOWN for all brands.

### Home backup power stations (added)
- **Prices:** Anker F3800 $1,800 to $2,200; EcoFlow Delta Pro Ultra $4,099 to $4,849.
- **Discounting:** brands discount heavily and often.
- **Risks:** lithium shipping rules, and whole-home kits need an electrician.
- **Margin:** UNKNOWN.

### Gas fire pit tables (added)
- **Prices:** Outdoor GreatRoom $999 to $4,499.
- **Suppliers:** Breeo has a dealer link. Solo Stove wholesales via Faire.
- **Seasonality:** weak in Dec to Jan.

### Slate pool tables (added)
- **Prices:** $2,000 to $12,000; Olhausen from $5,195 including delivery.
- **Margin:** forum anecdote, 35-40%.
- **Fit:** needs professional installation, so a local network is required. Poor fit.

## Cross-cutting findings

- **Course-seller and affiliate claims** (marked in `niches.json`):
  - 20-35% margins (dropshippingchampions.com, salehoo.com).
  - "Aim for 50%+" (trueprofit.io).
  - A sauna example of $9,500 retail, $7,520 cost and $250 ad spend per sale (Marcus Lam, promotional).
  - "Net-30 after trust" and "LLC and resale certificate required" (indiehackers.com and similar).
  - None of these are verified.
- **Freight:**
  - Vendor figures for LTL residential add-ons: $50-150 residential surcharge, $50-100 liftgate, $75-300 inside delivery.
  - Vendor modeling puts LTL furniture damage at 15% (wearewarp.com, vendor claim).
  - The industry-wide LTL claims ratio is 0.35% of freight spend (Synchrogistics, via Warp), but that covers all freight, not bulky goods.
- **MAP:**
  - Written MAP policies were found for Body-Solid, GoFit, Napoleon/Wolf, Olhausen and Expion360. Breville is monitored by third-party MAP trackers.
  - Most other brands' MAP terms: UNKNOWN.
- **Warranty:** tied to authorized dealers (Blaze, Jackery, Steelcase, espresso brands). Unauthorized resale is not an option.

## Blocked or unavailable sources

- `dealers.leisurecraft.com` (Dundalk terms PDF): did not resolve from this session's network. The Dundalk margin comes from the search-result snippet.
- `faire.com` brand pages: HTTP 403.
- Claude in Chrome, Foreplay and Amazon "bought in past month" data were not used. Same-SKU seller counts on Amazon and Google Shopping were not measured (UNKNOWN).

## Risks and unknowns

- Dealer approval, actual discount off MSRP and MAP terms are UNKNOWN for almost every brand until applications are submitted. Applying means contacting suppliers, which needs Dhruv's approval (CLAUDE.md section 10).
- Typical AOVs are mostly ASSUMED midpoints, not sales data.
- Benchmark cost per purchase for each niche was not gathered, so the cushion rule cannot be run yet.
- Most margin sources are 2003 to 2017 trade press.

## Confidence

- Medium on demand (live DataForSEO data).
- Low to medium on prices (retailer listings and vendor guides).
- Low on dealer margins and on whether online-only dealers are accepted.

## Recommended next action

If Dhruv wants to pursue this model (it needs the section 1 rule change):
1. Shortlist 2 or 3 niches with parcel freight and strong Dec to Jan (golf simulator components, electric fireplaces, massage chairs), plus saunas if a supplier offers terms.
2. Draft dealer applications for approval, starting with Rain or Shine Golf, Shop Indoor Golf, Osaki and Dundalk.
3. Put the quoted margins into `scripts/economics.py` with sourced CPC-based CAC benchmarks before any spend.
