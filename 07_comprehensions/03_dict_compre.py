gola_price_inr = {
    "rajbhog" : 200,
    "chocolate" : 150,
    "strawberry" : 300,
    "venila" : 250
}

gola_price_usd = {gola:price / 85  for gola,price in gola_price_inr.items()}
# gola_price_usd = {gola:round(price / 85,2)  for gola,price in gola_price_inr.items()} # for rounding the price in usd long decinal values
print(gola_price_usd)