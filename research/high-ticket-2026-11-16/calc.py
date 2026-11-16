"""High-ticket dropship illustration. All inputs ASSUMED or ESTIMATED; replace with dealer quotes."""
import json
CARD_PCT, CARD_FIXED, PLATFORM_PCT = 0.029, 0.30, 0.01   # same as data/channel_params.json (Amboras)
cases = [
    # name, price, gross margin (ESTIMATED 15-35% per high-ticket guides), refund/damage allowance (ASSUMED), Google CPC (DataForSEO 2026-11-16)
    ("Outdoor barrel sauna, $4,000", 4000, 0.25, 0.05, 4.28),
    ("Golf simulator package, $5,000", 5000, 0.20, 0.05, 7.02),
    ("Cold plunge tub, $3,000", 3000, 0.25, 0.05, 6.95),
]
out = []
for name, price, gm, ref, cpc in cases:
    cost = price * (1 - gm)
    fees = price * (CARD_PCT + PLATFORM_PCT) + CARD_FIXED
    pre_ad = price - cost - fees - price * ref
    be_cac = pre_ad
    target_cac = 0.75 * be_cac
    out.append({"case": name, "gross_margin_assumed": gm, "pre_ad_contribution": round(pre_ad, 2),
                "break_even_cac": round(be_cac, 2), "target_cac": round(target_cac, 2), "cpc": cpc,
                "clicks_affordable_per_sale_at_target": int(target_cac // cpc),
                "conversion_rate_needed_at_target": round(cpc / target_cac, 4)})
json.dump(out, open(__file__.replace("calc.py", "calc.json"), "w"), indent=1)
for o in out: print(o)
