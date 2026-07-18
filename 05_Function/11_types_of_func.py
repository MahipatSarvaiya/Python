# def pure_chai(cups):
#     return cups * 10


# print(pure_chai(5))

# #impure func
# total_chai = 0

# def impure_chai(cups):
#     global total_chai
#     total_chai += cups

# print(impure_chai(20))


# #recursion func
# def pore_chai(cup):
#     # print(cup)
#     if cup == 0 :
#         return "all done"
#     return pore_chai(cup-1)
    

# print(pore_chai(5))


# lambda


chai_types = ["kadak","heavy", "light", "fresh", "kadak"]

# strong_chai = list(filter(lambda chai : chai=="kadak", chai_types))
strong_chai = list(filter(lambda chai : chai!="kadak", chai_types))

print(strong_chai)