chai_order = dict(type = "chai", size = "large", price = 3.50, quantity = 2)

print(f"your chai order is :{chai_order}")

chai_recipe= {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"
print(f"chai recipe is : {chai_recipe}")

del chai_recipe["liquid"] # delete a key-value pair

print(f"chai base is {chai_recipe['base']} ")

print(f"suger in chai ?:  {'suger' in chai_recipe}")  #membership test for key in dictionary



chai_order = {"type": "ginger chai", "size": "medium", "price": 5.0, "quantity": 3}

# print(f"your chai order (keys) :{chai_order.keys()}")  # get all keys in the dictionary
# print(f"your chai order (valus) :{chai_order.values()}")  # get all values in the dictionary
# print(f"your chai order (item) :{chai_order.items()}")  # get all key-value pairs in the dictionary

last_item = chai_order.popitem()  # remove and return the last key-value pair
print(f"last item removed from chai order : {last_item}")

extra_spice = {"ginger": "sliced", "cardamom": "ground"}

chai_recipe.update(extra_spice)  # add key-value pairs from extra_spice to chai_recipe
print(f"updated chai recipe : {chai_recipe}")

chai_size = chai_order["size"]  # access value by key
print(f"chai size is : {chai_size}")

#customer_note = chai_order.get("customer_note", "no note")  # return note if key is not found, otherwise return value
customer_note = chai_order.get("size", "no note")  # return size key value

print(f"customer note is : {customer_note}")