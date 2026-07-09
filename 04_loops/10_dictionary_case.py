
users = [
    {"id": 10, "total" : 150, "coupon" :"F10"},
    {"id": 20, "total" : 200, "coupon" :"F20"},
    {"id": 30, "total" : 250, "coupon" :"P10"}
]
 
discounts = {
     "F10" : (.3,0),
     "F20" : (.5,0),
     "P10" : (0,10),
     
} 

for user in users :
    percent, fixed = discounts.get(user["coupon"], (0,0))
    discount = round(user["total"] * percent + fixed , 2)

   #print(f"{user["id"]} paid {user["total"]} and get {discount} for next purchasse ")
    print(f"{user['id']} paid {user['total']} and get {discount} for next purchase")

 #extra
 
    # print("for now discount for this purchase")
    # final_amount = user["total"] - discount   

    
    # print (f"final amount for {user['id']} is {final_amount}") 
    # print()
