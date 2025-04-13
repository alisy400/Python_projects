import random

user_wins = 0
comp_wins = 0

options = ["rock", "paper", "scissor"]
options[0]

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Enter a valid input")

        continue

    random_number = random.randint(0, 2)

    comp_pick = options[random_number]
    print("computer picks", comp_pick, ".")

    if user_input == "rock" and comp_pick == "scissor":
        print("you win!!")
        user_wins += 1

    elif user_input == "paper" and comp_pick == "rock":
        print("you win!!")
        user_wins += 1

    elif user_input == "scissor" and comp_pick == "paper":
        print("you win!!")
        user_wins += 1

    elif user_input == comp_pick:
        print("Try again")


    else:
        print("you lost")
        comp_wins += 1

print("you won", user_wins, "games out of", str(comp_wins + user_wins), "games")
print("goodbye!!")

