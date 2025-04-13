import random
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll

while True:
    player = input("enter the no of players (2-4): ")
    if player.isdigit():
        player = int(player)
        if 2 <= player <= 4:
            break
        else:
            print("must be between 2-4")
    else:
        print("invalid try again")

max_score = 50
player_scores = [0 for _ in range(player)]

while max(player_scores ) < max_score:
    for player_idx in range(player):
        print("\nplayer number ", player_idx + 1,"turn has been started\n")
        print("your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_role = input("do you want to roll (y) ?")
            if should_role.lower() != "y":
                break

            value = roll()
            if value == 1 :
                print("you rolled 1! Turn done!!")
                current_score = 0
                break
            else:
                current_score += value
                print("you rolled a ", value)

            print("your score is :", current_score)

        player_scores[player_idx] += current_score
        print("your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("player number",winning_idx + 1,"is the winner with score", max_score)

