#bool

is_hot = True

count = 10  

total = count + is_hot #upcasting of bool to int
print(f"the total is : {total}")

milk_avail = 0 #no milk available
print(f"Present milk? :{bool(milk_avail)}")

# and or not

hot_water = True
hot_milk = False

can_serve = hot_water and hot_milk
print(f"can we serve tea? : {can_serve}")