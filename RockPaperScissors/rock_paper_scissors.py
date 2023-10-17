import random


def victory(player, opponent):
    if (((player == 'rock') and (opponent == 'scissors')) or ((player == 'scissors') and (opponent == 'paper')) or ((player == 'paper') and (opponent == 'rock'))):
        return True


def playGame():
    user = input("Enter rock, paper, scissors: ").lower()
    CPU = random.choice(['rock', 'paper', 'scissors'])

    if CPU == user:
        return "Draw!"

    # R beats > S, S beats > P, P beats > R
    if victory(user, CPU):
        return "You Win!"

    return "You Lose! "


print(playGame())
