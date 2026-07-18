# chai = "ginger chai"

# def prepare_chai(order):
#     print("preparing ", order)

# prepare_chai(chai)
# # print(chai)




# chai_order = [ 1,2,3]


# def chai_menu(cup):
#     cup[0] = 40

# chai_menu(chai_order)
# print(chai_order)






# order = [30,40,50]

# def chai(cup):
#     cup[0] = 90
#     return cup

# print(order)
# changed = chai(order.copy())
# print(changed)



# def make_chai(tea, leaves, flavour):
#     print(tea, leaves, flavour)

# make_chai("home", "yes", "low")

# make_chai(leaves = "no", flavour = "strawberry", tea = "raw" )


# def new_chai(*items, **addition):  # first 1.args and 2.kwargs
#     print("Items are ",items)
#     print("added are ",addition)


# new_chai("clove", "leaves", "ginger", hot = "true", cup = "available", serving = "in process")


# def chai(order=[]):
#     order.append("ginger")
#     print(order)

def chai(order=None):
    if order is None:
        order = []
        print(order)
   

chai()
chai()
chai()
