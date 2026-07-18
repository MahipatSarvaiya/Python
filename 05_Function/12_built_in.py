# https://docs.python.org/3/library/functions.html   doc for this  

# def fav_flavour(flavour = "strawberry"):

#     """ return the flavour of the chai""" #this should be first line to access or work 

#     return flavour

# print(fav_flavour.__doc__)
# print(fav_flavour.__name__)

# help( list )
# help( len )   

def chai_bill(chai = 0,samosa = 0):
    """  hey this your chai bill :
        chai is = 10
        and samosa =  15
    """

    total = chai*10 + samosa*15
    return  total, "thank you for visiting my shop"


print(chai_bill(2,3))
print(chai_bill.__doc__)