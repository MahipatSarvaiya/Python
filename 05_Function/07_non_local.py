
def chai_type():
    chai_item = "pinch"

    def kitchen():
        nonlocal chai_item 
        # global chai_item 
        chai_item = "badam"
    kitchen() 
    
    print("after kitchen",chai_item)

chai_type()
#print("outter of all this",chai_item) 