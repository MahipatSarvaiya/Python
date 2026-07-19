def chai_customer():
    print(" hey welcome customer!")
    order = yield

    while True:
        print(f"your order is {order}")
        order = yield

        


chai_ord = chai_customer()
next(chai_ord)  # start the generators

chai_ord.send("pink chai")
chai_ord.send("red  chai")
chai_ord.send("purple chai")
chai_ord.send("purple chai")









# def give_take():
#     x = yield "first chai"
#     print("recieved" , x)
    
# take = give_take()

# print(next(take))
# take.send("hello chai")

