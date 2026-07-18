def cup_shop():
    yield "cup 1 : this is cup1"
    yield "cup 2 : this is cup2"
    yield "cup 3 : this is cup3"

stall = cup_shop()

# for cup in stall :
#     print(cup)

def chai_shop():
    yield "chai 1"
    yield "chai 2"
    yield "chai 3"
    yield "chai 4"

chai = chai_shop()

print(next(chai))
print(next(chai))
print(next(chai))
print(next(chai))
# print(next(chai))  #stops the iterations and gives error   #no of yields = no of  print next(var)


