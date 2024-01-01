class Machine:

    def __init__(self):
        self.resources = {
        "ban" : 500,
        "straw" : 500,
        "mang" : 500,
        "kiwi" : 500,
        "yog" : 500,
        "milk" : 500,
    }
        
    def report(self):
        print(f'Ban: {self.resources["ban"]} grams')
        print(f'Straw: {self.resources["straw"]} grams')
        print(f'Mang: {self.resources["mang"]} grams')
        print(f'Kiwi: {self.resources["kiwi"]} grams')
        print(f'Yog: {self.resources["yog"]} grams')
        print(f'Milk: {self.resources["milk"]} militers')
    
    def is_resource_sufficient(self, item):
        for ity in item.ingrediants:
            if item.ingrediants[ity] > self.resources[ity]:
                print("Please refill")
                return False
        return True
        
    

    def make_drink(self, item):
        self.resources["ban"] -= item.ingrediants["ban"]
        self.resources["straw"] -= item.ingrediants["straw"]
        self.resources["kiwi"] -= item.ingrediants["kiwi"]
        self.resources["mang"] -= item.ingrediants["mang"]
        self.resources["yog"] -= item.ingrediants["yog"]
        self.resources["milk"] -= item.ingrediants["milk"]