from Smoothie_machine import Machine
from Menu import Menu, MenuItem


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



def nmain():

    menu = Menu()
    mach = Machine()


    print("Powering up... ZIP ZAP ZOP")
    print("I am Smoothie Machine Beep Boop")
    print("You're Welcome")
    print("Enter 'OFF' to turn off the machine at any point")

    on = True
    while on:
        print("Here is the menu:")
        print(f"{menu.get_items()}")
        print("To Check resources click option: Check")
        choice = input("Which drink would you like?: ")
        if choice.lower() == 'off':
            break
        if choice.lower() == 'check':
            mach.report()
        else:
            item = menu.find_drink(choice)
            cando = mach.is_resource_sufficient(item)

        if cando == True:
            mach.make_drink(item)
            print("here you go!")
    
    
    
def nnmain():
    menu = Menu()
    mach = Machine()
    item = menu.find_drink("Ban Straw")
    print(item)
    attributes_dict = vars(item)
    print(attributes_dict)
    mach.make_drink(item)


nmain()







    #item = menu.find_drink("Ban Straw")

    #print(item)
    #for sin in items:
    #    mach.is_resource_sufficient(sin)
    





