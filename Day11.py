def playround(rdeck, sdeck):
    import random
    player_hand = []
    comp_hand = []
    score = 0
    cscore = 0
    #ndeck = rdeck
    #handdealt = random.sample(range(0,len(rdeck)),4) #Change of plan, I couldn't figure out how to take out the sample from the population lol
    #Or rather I found .shuffle first
    random.shuffle(rdeck)
    print("You were dealt a", rdeck[0], "and a", rdeck[1])
    print("The dealer was dealt a", rdeck[2])
    player_hand = rdeck[0:2]
    score = sdeck[rdeck[0]] + sdeck[rdeck[1]]
    comp_hand = rdeck[2:4]
    cscore = sdeck[rdeck[2]] + sdeck[rdeck[3]]
    print(score)
    ndeck = rdeck[4:]

    while True:
        while True:
            print("Do you wnat to hit?")
            ans = input("Y/N: ")
            if ans.lower() == 'y' or ans.lower() == 'n':
                break
            else:
                print("Please answer the questions")
        if ans.lower() == 'n':
            break   
        else:
            print("You drew a ", ndeck[0])
            score += sdeck[ndeck[0]]
            ndeck = ndeck[1:]
            if score > 21:
                if "Ace" in player_hand:
                    score = score -10
                    player_hand.remove("Ace")
                else:
                    print("You bust you lose")
                    return ndeck
            print("You have ", score)
    print("The Computer has ", cscore)
    while True:    
        if cscore > 21:
            if "Ace" in comp_hand:
                cscore = cscore-10
                comp_hand.remove("Ace")
            else:
                print("The Computer loses") 
                return ndeck
        if cscore < 16:
            print("Computer drew a ", ndeck[0])
            cscore += sdeck[ndeck[0]]
            print("It has ",cscore)
            ndeck = ndeck[1:]
        else: 
            break
    if score > cscore:
        print("You won this round with ", score)
    else:
        print("You lost this round")

            

    return ndeck


def main():
    sdeck = {"Two": 2, "Three":3, "Four": 4, "Five":5, "Six":6, "Seven":7,"Eight":8,"Nine":9,"Ten":10, "Jack": 10, "Queen":10,"King":10,"Ace":11}
    rdeck = []
    d = setup()*4
    print("The number of decks will be ",d)
    for x in range(d):
        rdeck += list(sdeck.keys())
    print(rdeck)
    while True:
        playround(rdeck, sdeck)
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



sdeck = {"Two": 2, "Three":3, "Four": 4, "Five":5, "Six":6, "Seven":7,"Eight":8,"Nine":9,"Ten":10, "Jack": 10, "Queen":10,"King":10,"Ace":11}
rdeck = []
for x in range(4):
    rdeck += list(sdeck.keys())
playround(rdeck, sdeck)