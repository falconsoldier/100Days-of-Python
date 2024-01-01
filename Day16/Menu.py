class MenuItem:
    def __init__(self, name, ban, mang, kiwi, straw, yog, milk, cost):
        self.name = name
        self.cost = cost
        self.ingrediants = {
            "ban" : ban,
            "mang" : mang,
            "kiwi": kiwi,
            "straw": straw,
            "yog" : yog,
            "milk" : milk

        }


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name = "Ban Straw", ban =  100, mang = 0, kiwi = 0, straw = 100, yog = 50, milk = 50, cost = 1.5),
            MenuItem(name = "Mang Ban", ban =  150, mang = 100, kiwi = 0, straw = 0, yog = 150, milk = 50, cost = 2),
            MenuItem(name = "Straw Kiw", ban =  0, mang = 0, kiwi = 75, straw = 100, yog = 50, milk = 75, cost = 1.75)                        
        ]

    def get_items(self):
        options = "|"
        for item in self.menu:
            options += f"{item.name}|"
        return options
    
    def find_drink(self, str):
        for item in self.menu:
            if item.name == str:
                return item
        print("Error")
        return None