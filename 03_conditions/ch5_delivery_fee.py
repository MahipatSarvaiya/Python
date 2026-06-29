order = int(input("enter delivery fee : "))

print(f"order amount {type(order)}")

del_fee = 0 if order > 300 else 50

print(f"delivery fee is : {del_fee}")

