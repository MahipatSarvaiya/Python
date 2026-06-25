spice = set()

print(f" the id of the spice is : {id(spice)}")
print(spice)

spice.add("kala mari")
spice.add("haldar")

print(f" the id of the spice is After : {id(spice)}")
print(spice)

spice = set()
print(f" the id of the spice is : {id(spice)}")

spice.add("ajmo")
spice.add("laving")

print(f" the id of the spice is After : {id(spice)}")

print(spice)
