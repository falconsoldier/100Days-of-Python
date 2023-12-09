def playround(rdeck):
    return 1


def main():
    sdeck = {"One": 1, "Two": 2, "Three":3, "Four": 4, "Five":5, "Six":6, "Seven":7,"Eight":8,"Nine":9,"Ten":10, "Jack": 10, "Queen":10,"King":10,"Ace":11}
    rdeck = []
    d = setup()
    print("The number of decks will be ",d)
    for x in range(d):
        rdeck += list(sdeck.keys())
    print(rdeck)
    while True:
        playround(rdeck)
        #ans = input("blblbl")
        while True:
            print("Do you wnat to keep playing?")
            ans = input("Y/N: ")
            if ans.lower() == 'y' or ans.lower() == 'n':
                break
            else:
                print("Please answer the questions")
        if ans.lower() == 'n':
            break


def setup():
    print("Hello, Welcome to Blackjack")
    print("How many decks would you like to play with?")
    while True:
        try:
            decks = int(input("Enter a number 1-9: "))
            if decks > 9 or decks < 1:
                print("Please pick a number 1-9")
            else:
                break
        except ValueError:
            print("Please enter a number")
    return decks

main()