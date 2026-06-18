class chai :
    def __init__(self,sweetness,tea_leaves):
        self.sweetness = sweetness
        self.tea_leaves = tea_leaves
    def make_chai(self, amount):
        self.add_tea()
        self.add_milk()
        self.add_sugar(amount)
mychai = chai(amount=5, tea_leaves=True)
    
