#strings

chai_item = "chai ginger"
customer = "ms"

print(f"hey {customer}, would you like some {chai_item}?")

chai_desc = "aromatic and spicy and crisp"
print(f" first word {chai_desc[0:8:2]}") # first is index no , second is string length, thrid is word to skip

print(f"last word {chai_desc[::-1]}") # for reverseg

label_txt = " chai spécial "
encoded = label_txt.encode("utf-8")
print("non encoded", label_txt)
print("encoded", encoded)

decode = encoded.decode("utf-8")
print("decoded", decode)
