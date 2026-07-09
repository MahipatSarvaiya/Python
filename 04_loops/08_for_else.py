staff = [("amit",17), ("raj", 16), ("shiv",15)]

for name,age in staff:
    if age <=18:
        print(f"{name} is eligible") # here the who ever comes first will executed, after that loop breaks 
        break

else:
    print("no one is eligible")  #  else block runs only if loop didn't break