print("welcome to my quiz game!!")

playing = input("Do you want to play ?")
if playing.lower() != "yes":
    quit()

print("Okay! Lets play :) ")
score = 0

answer = input("What is the full form of CPU?")
if answer == "central processing unit":
    print("correct!")
    score = score + 1
else:
    print("incorrect answer")

answer = input("What is the full form of GPU?")
if answer == "graphical processing unit":
    print("correct!")
    score = score + 1
else:
    print("incorrect answer")

answer = input("What is the full form of TV?")
if answer == "Television":
    print("correct!")
    score = score + 1

else:
    print("incorrect answer")

answer = input("What is the full form of UPS?")
if answer == "uninterruptible power suppy":
    print("correct!")
    score = score + 1

else:
    print("incorrect answer")

print("your total score is", str(score))
print("you score ", str((score / 4) * 100), "%")



