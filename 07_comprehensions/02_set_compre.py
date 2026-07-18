# menu = [
#     "veg Burger",
#     "veg biriyani",
#     "milk shake",
#     "veg pulao",
#     "chocolate",
#     "veg biriyani",
#     "veg pulao"
# ]

# unique_item = { M_item  for M_item in menu} #if len(M_item) < 10}  #if does note require that much
# print(unique_item)



# complex 

Flavour_gola = {
    "chocolate" : ["choco", "red", "pink", "blue"],
    "rajbhog" : ["cream", "butter", "pink", "cheeze"],
    "special" : ["choco", "red", "pink", "mango"]

}

unique_flav = {flav for gola in Flavour_gola.values() for flav in gola } 
print(unique_flav)  

 # here in expressions the flav ---> it always be what is the final stmt we want to print while gola
#  is worked as middle man so it does comes at the place of the expressions
