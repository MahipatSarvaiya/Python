def make_chai():
    add_tea()
    add_milk()
    
def add_tea():
    if not tea_leaves():
        print("please tea leaves")
def add_milk():
    print("Adding milk")

make_chai()
add_tea()
add_milk()