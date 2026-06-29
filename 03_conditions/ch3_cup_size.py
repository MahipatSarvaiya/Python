cup = input("please enter cup size: small/medium/large : ").lower()

if cup == "small":
    print("Price of small cup is 10")
elif cup == "medium":
    print("Price of medium cup is 20")
elif cup == "large":
    print("Price of large cup is 30")
else:
    print("Invalid cup size. Please choose small, medium, or large.")