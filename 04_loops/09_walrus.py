# value = 14 
# rem = value % 5

# if rem :
#     print(f" not divisible, rem is {rem}")

val = 14 

if (rem := val % 5):   #   := walrus operator
    print(f" not divisible, rem is {rem}")



# chai_size = ["small", "med","large"]

# if(user_size := input("enter size : "))in chai_size:
#     print(f"size is {user_size}")
# else:
#     print(f"not avaiable {user_size}")


flavorss = ["mint", "ginger", "hajma"]

print("Available Flavour" , flavorss)

while( flavor := input ("choose flavor : ")) not in flavorss:
    print(f"not available {flavor}")

print(f" you choose : {flavor}")
