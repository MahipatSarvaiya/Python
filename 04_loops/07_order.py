#break, continue, pass

flavours = [ "ginger", "out of stock", "mint", "discontinued", "chocolate" ]

for flavour in flavours:
    if  flavour == "out of stock":
        continue
    if flavour == "discontinued":
        break
    print(f"{flavour} found")

print(f"out of loop")
