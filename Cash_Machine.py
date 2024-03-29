class Cash_Machine:
    
    currency = "$"
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    def __init__(self):
        self.profit = 0


    def report(self):
        print(self.profit)

    def process(self, cost):
        print("Please enter payment")
        while True:
           q = input("Quarters?")
           d = input("Dimes?")
           n = input("nickles?")
           p = input("pennies?")
           if q.lower == 'off' or d.lower == 'off' or n.lower == 'off' or p.lower == 'off':
               return False
           total = (.25*q)+(.1*d)+(.05*n)+(.01*p)
           if total > cost:
              break
        if total > cost:
            print(f"Your change is {total-cost}")
        self.profit += cost
        return True