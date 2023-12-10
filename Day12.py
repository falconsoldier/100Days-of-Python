def set():
    print("Select a setting")
    while True:
        s = input("Type Easy, Medium, or Hard: ")
        if s.lower() == 'easy':
            return 20
        elif s.lower() == 'medium':
            return 10
        elif s.lower() == 'hard':
            return 5
        else:
            print("You need to pick Easy, Medium, or Hard")

def guessnum():
    import random
    lives = 0
    print("Hello, welcome to the number game")
    print("I'm thinking of a number between 1-100")
    lives = set()
    ans = random.randint(1,100)
    p = play(ans, lives)
    if p == 1:
        print("you win!")
    else:
        print("You lose, maybe try again")

def play(ans, lives):
    while lives > 0:
        while True:
            try:
                guess = int(input("Guess a number: "))
                break
            except:
                print("Gotta be an integer")
        if guess == ans:
            return 1
        elif guess > ans:
            print("Too high bro")
            lives = lives-1
        elif guess < ans:
            print("Too low homes")
            lives = lives -1
    return 0
guessnum()