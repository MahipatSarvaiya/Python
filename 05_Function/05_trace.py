def vat_amount(price, vat_rate):
    return price * (100 + vat_rate) / 100

orders = [ 200, 300, 400 ]

for price in orders:
    final_amoount = vat_amount(price,15)

    print(f"Original is : {price}, final amount is {final_amoount} ")


 