from Smoothie_machine import Machine
from Menu import Menu, MenuItem
from Cash_Machine import Cash_Machine 

def nmain():

    menu = Menu()
    mach = Machine()
    cashy = Cash_Machine()


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
            cashy.report()
        else:
            item = menu.find_drink(choice)
            cando = mach.is_resource_sufficient(item)

        if cando == True:
            cashy.process(item.cost)
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
    





