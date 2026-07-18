menu = [
    "veg Burger",
    "veg biriyani",
    "milk shake",
    "veg pulao",
    "chocolate"
]

# veg_item = [vitem for vitem in menu if "veg" in vitem]
# print(veg_item)


bigger_item = [ Big for Big in menu if len(Big)> 10 ]
print(bigger_item)