things = ["milk", "water", "black tea"]

things.append("sugar")
print(f"thinhs are :{things}")

things.remove("water")
print(f"thinhs are :{things}")

options = ["ginger","cardmom" ]
chai_things = ["milk","water"]

chai_things.extend(options)

chai_things.insert(0,"black tea")
print(f"thinhs are :{chai_things}")

chai_things.reverse()

print(f"things reversed : {chai_things}")

sugar_level = [1,2,3,4,5]

print(f"max sugar level : {max(sugar_level)}")
print(f"min sugar level : {min(sugar_level)}")



#ch9 operator overloading 

base_flavour = ["water","milk"]
extra_flavour = ["ginger"]

full_flavour = base_flavour + extra_flavour
print(f"full flavour : {full_flavour}")

strong_flavour = base_flavour * 2
print(f"strong flavour : {strong_flavour}")

# from operator import itemgetter

raw_item = bytearray(b"CINAMON")

raw_item= raw_item.replace(b"CINA",b"CARDAa")
print(f"raw item : {raw_item}")