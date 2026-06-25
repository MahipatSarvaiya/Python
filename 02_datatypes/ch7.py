spices = ("tea leaves", "cinnamon", "cloves", "nutmeg")

(spice1, spice2, spice3, spice4) = spices

print(f"masal spices are {spice1}, {spice2}, {spice3} and {spice4}")

ginger_ratio, cardamom_ratio = 2, 1

print(f"ginger G:{ginger_ratio} and cardamom C:{cardamom_ratio} ")

ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"ginger G:{ginger_ratio} and cardamom C:{cardamom_ratio} ")

#membership
print(f"ginger available ? {'ginger' in spices}")
print("cinnamon" in spices)