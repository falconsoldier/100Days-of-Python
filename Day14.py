def profile(jc):
        import random

        num = random.randint(0,49)
        prof = jc[num]


        return prof







#from day14data.js import data as d
def main():
        import json
        js_file_path = 'C:/Users/andre/Desktop/Python/100 Days/100Days-of-Python/data1.js'

        with open(js_file_path, "r") as js_file:
                jcd = js_file.read()
        jcd = jcd.split('=')[1].strip() ### Have to rename variables
        jc = json.loads(jcd)
        print("Welcome to another guessing game")
        print("This time you will be guessing out of a fake JS file")
        profa = profile(jc)
        profb = profile(jc)
        while True:
                if profa == profb:
                        profb = profile(jc)
                else:
                        break
        print("The first options is ", profa["name"], " from ", profa["country"])
        print("The first options is ", profb["name"], " from ", profb["country"])
        print("Which one has more followers?")
        guess = input("A or B: ")
        ans = 'a'
        if profa['follower_count'] < profb['follower_count']:
                ans = 'b'
        if guess == ans:
                print("You win")
        else:
                print("Loser")











main()