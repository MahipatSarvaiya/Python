essential_spice = {"cardamon", "cinnamon", "clove"}

optional_spice = {"nutmeg", "cinnamon", "pepper"}

all_spice = essential_spice | optional_spice     # | for union

print(all_spice)

common_spice = essential_spice & optional_spice    # & for intersection

print(common_spice)

only_essential = essential_spice - optional_spice   # - for difference
print(only_essential)

print("cardamon" in essential_spice) #membership test

# frozenset is an immutable set