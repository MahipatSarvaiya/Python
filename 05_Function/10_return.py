# def make_chai():
#     # return "chai is in the process"
#     print("here is your masala chai")

# value = make_chai()

# print(value)
# # print(make_chai())



# def simple_chaiwala():
#     pass

# print(simple_chaiwala())




# def total_cup():
#     return 100

# total = total_cup()
# print(total)





# def chai_order(cup):
#     if cup == 0:
#         return " sorry no cups available"
#     return "chai is ready"
#     print("chai")

# print(chai_order(0))
# print(chai_order(10))



def chai_report():
    return 100,20  #sold , remaining
    return 100,20, 10  #sold , remaining ,  not paid

sold , remaining = chai_report()
#sold , remaining, _ = chai_report() #you can use the _ for third value 

print(chai_report())
print("Solded =", sold)
print("Remaining =", remaining)

