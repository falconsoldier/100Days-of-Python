MENU = {
    #Ban Straw
    "A": {
        "ingredients": {
            "ban": 100,
            "straw": 100,
            "yog": 50,
            "milk": 50,
        },
        "cost": 1.5,
    },
    #Mang Ban
    "B": {
        "ingredients": {
            "mang": 100,
            "ban": 150,
            "yog": 75,
            "milk": 25
        },
        "cost": 2.5,
    },
    #Kiwi Straw
    "C": {
        "ingredients": {
            "straw": 150,
            "kiwi": 75,
            "yog": 80,
            "milk": 20
        },
        "cost": 3.0,
    }
}

resources = {
    "ban" : 500,
    "straw" : 500,
    "mang" : 500,
    "kiwi" : 500,
    "yog" : 500,
    "milk" : 500,
    "money": 0
}

def cs(ch):
    print("That costs: ", MENU[ch]["cost"])
    print("Trust system though, put money in the box on the counter")

    for ing in MENU[ch]['ingredients']:
        if MENU[ch]['ingredients'][ing] > resources[ing]:
            print("Cannot make drink, please Refill Resources")
            return 1
        else:
            return 0

def ded(ch):
    for ing in MENU[ch]['ingredients']:
        resources[ing] -= MENU[ch]['ingredients'][ing]
    
def cr():
    print(f'Ban: {resources["ban"]} grams')
    print(f'Straw: {resources["straw"]} grams')
    print(f'Mang: {resources["mang"]} grams')
    print(f'Kiwi: {resources["kiwi"]} grams')
    print(f'Yog: {resources["yog"]} grams')
    print(f'Milk: {resources["milk"]} militers')
    print(f'Money: {resources["money"]} dollars')

def payment(c):
    print(f"Payment due is {c}")
    print("Please insert coins: ")
    while True:
        while True:
            try:
                qtr = int(input("Quarters: "))
                break
            except:
                print("You must enter an int")
        while True:
            try:
                dme = int(input("Dimes: "))
                break
            except:
                print("You must enter an int")            
        while True:
            try:
                nck = int(input("Nickles: "))
                break
            except:
                print("You must enter an int")
        while True:
            try:
                pnn = int(input("Pennies: "))
                break
            except:
                print("You must enter an int")
        total = round((qtr*.25)+(dme*.1)+(nck*.05)+(pnn*.01), 2)
        if total < c:
            print("You need more coins")
        else:
            break
    if total > c:
        floating_point_BS = round(total-c, 2)
        print(f"Your change is {floating_point_BS}")
    resources["money"] += total
    return
    
    
    
    
    
def makedrink():   
    print("Bananaa Strawbery smoothie click option: A")
    print("Mango Banana smoothie click option: B")
    print("Kiwi Strawberry smoothie click option: C")
    print("To Chek resources click option: D")
    choice = input("Which drink would you like?: ")

    b = False
    while b == False:
        if choice.lower() != 'a' and choice.lower() != 'b' and choice.lower() != 'c' and choice.lower() != 'd':
            choice = input("Maybe you mistyped, the chioces are A, B, C, D")
        elif choice.lower() == 'd':
            cr()
            choice = input("Which drink would you like?: ")
            if choice.lower() != 'a' and choice.lower() != 'b' and choice.lower() != 'c':
                choice = input("Maybe you mistyped, the chioces are A, B, C, D")
        else:
            b = True
    
    cando = cs(choice)
    if cando == 1:
        return
    else:
        ded(choice)



def main():
    print("Powering up... ZIP ZAP ZOP")
    print("I am Smoothie Machine Beep Boop")
    print("I can make nana straw, mango ban, kiwi kiwi straw")
    print("You're Welcome")
    
    maker = True

    while maker == True:
        if resources["ban"] < 100 or resources["straw"] < 100 or resources["mang"] < 100 or resources["yog"] < 100 or resources["kiwi"] < 100 or resources["milk"] < 100:
            print("-- Warning, low ingrediants --")
        print("Would you like a drink?")
        ans = input("Y/N: ")
        if ans.lower() == 'y':
            makedrink()
        else:
            print("cool, comeback anytime")
            maker = False









main()