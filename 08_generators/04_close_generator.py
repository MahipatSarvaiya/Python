# def indian_chai():
#     yield "ginger chai"
#     yield "masala chai"

# def foreign_chai():
#     yield "capachino"
#     yield "starbucks"

# def mixed_chai():
#     yield from indian_chai()
#     yield from foreign_chai()

# for chai in mixed_chai:
#     print(chai)


def chai_cafe():
    try :
        while True:

           ord = yield "waiting for your order!!"
            
    except:
        print("Sorry no more orders, closed")

list = chai_cafe()
print(next(list))

list.close()   #cleanup memory releasse