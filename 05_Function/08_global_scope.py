raw_chai = "raw"

def front_desk():
     def kitchen():
          global raw_chai
          raw_chai = "pure tea"
     kitchen()

front_desk()

print("global chai is ", raw_chai )