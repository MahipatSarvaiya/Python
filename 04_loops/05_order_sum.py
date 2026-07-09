#zip

orders = [ "chai", "coffee", "milk", "tea", "juice" ]
prices = [ 10, 20, 30, 40, 50 ]

for order, price in zip(orders, prices):
    print(f"order is : {order} and price is : {price}")