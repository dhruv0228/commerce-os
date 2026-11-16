import json, sys
sys.path.insert(0, "/home/user/commerce-os/scripts")
import channels as ch, fee_breakdown as fb
P = ch.load_params()
DUTY = 0.30   # ASSUMED: tariff + import fees on AliExpress parcels since US de minimis ended (Aug 29, 2025)
prods = [
  # name, AliExpress price (her screenshot), her sell price, Kalodata revenue, units, commission, weight lb, category
  ("Automatic curling iron", 10.33, 60, 869_500, 20_220, "auto", 1.5),
  ("Tummy-control flare leggings", 5.54, 50, 1_020_000, 35_290, "auto", 0.6),
  ("Neck alignment pillow", 11.55, 80, 1_400_000, 44_730, "home", 2.5),
]
out = []
for name, ae, sell, rev, units, cat, w in prods:
    cost = ae * (1 + DUTY)
    market = round(rev / units, 2)          # average unit price actually paid (Kalodata, her screenshot)
    row = {"product": name, "aliexpress": ae, "her_price": sell, "her_claim_profit": round(sell - ae, 2),
           "market_avg_price": market, "landed_cost_assumed": round(cost, 2)}
    for label, price in (("her_price", sell), ("market_price", market)):
        r = fb.breakdown(P, price, cost, w, None, cat, "test", ship_cost=0.0)
        row[label + "_dtc_meta"] = r["dtc_meta"]["profit"]
        row[label + "_dtc_meta_tough"] = r["dtc_meta"]["profit_tough"]
        row[label + "_tiktok_aff"] = r["tiktok_aff"]["profit"]
        row[label + "_meta_cpa"] = round(next(l["usd"] for l in r["dtc_meta"]["lines"] if "Meta" in l["item"]), 2)
    out.append(row)
json.dump(out, open("calc.json", "w"), indent=1)
for r in out: print(json.dumps(r))
