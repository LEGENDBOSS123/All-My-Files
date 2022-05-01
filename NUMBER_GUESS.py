import random
print("------WELCOME TO NUMBER GAME------")
range_min = 0
range_max = 100
def com_reply(num, com):
    if num < com:
        print("GUESS HIGH")
    if num > com:
        print("GUESS LESS")
while True:
    com = random.randint(range_min, range_max)
    while True:
        while True:
            try:
                yours = int(input("GUESS A NUMBER 1-100: "))
                if yours>range_max or yours<range_min:
                    raise ValueError
                break
            except:
                print("PLEASE TRY AGAIN...")
        if yours == com:
            print("YOU GUESSED THE NUMBER")
            break
        com_reply(yours, com)
    yours = input("DO YOU WANT TO PLAY AGAIN: ")
    answer = yours.lower()
    if "y" in answer:
        print("\nPLAYING AGAIN...")
    else:
        print("SEE YOU LATER")
        break
