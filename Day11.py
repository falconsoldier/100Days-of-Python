class Invaliddeck(Exception):
    "Raised when the input value not 0-9"
    pass


def main():
    sdeck = {"One": 1, "Two": 2, "Three":3, "Four": 4, "Five":5, "Six":6, "Seven":7,"Eight":8,"Nine":9,"Ten":10, "Jack": 10, "Queen":10,"King":10,"Ace":11}
    rdeck = []
    d = setup()
    print("Lets do one deck to start")
    for x in range(d):
        rdeck += list(sdeck.keys())
    print(rdeck)



def setup():
    print("Hello, Welcome to Blackjack")
    print("How many decks would you like to play with?")
    while True:
        try:
            decks = int(input("Enter a number 0-9: "))
            if decks > 9 or decks < 1:
                raise Invaliddeck
            break
        except ValueError:
            print("Please enter a number")
    return decks

main()