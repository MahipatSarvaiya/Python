# def serve_chai():
#     chai_type = "masala"
#     print(f"your chai is : {chai_type}")



# serve_chai()

# chai_type = "ginger"
# print(f"outside function : {chai_type}")

def chai_counter():
    chai_order = "lemon"

    def print_order():
        chai_order = "cardamom"
        print(f"your chai order is : {chai_order}")
       
    print_order()
    print("outer", chai_order)
chai_counter()

chai_order = "pink"
print("global", chai_order)