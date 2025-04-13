import random

top_of_range = input("enter your number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("enter a value greater than 0")
        quit()
else:
    print("enter a real value")
    quit()

random_number = (random.randint(0, top_of_range))
guesses = 0


while True:
    guesses += 1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type a number")
        continue

    if user_guess == random_number:
        print("you got it baby")
        break
    else:
        if user_guess > random_number:
            print("your guess is greater")
        else:
            print("you guess is smaller")
print("you got it in " + str(guesses) + " guesses")

