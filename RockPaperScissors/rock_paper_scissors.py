import random

def victory(player, opponent):
    if ((player == 'Rock' and opponent == 'Scissors') or
        (player == 'Scissors' and opponent == 'Paper') or
        (player == 'Paper' and opponent == 'Rock')):
        return True

def playGame():
    user_choice = input("1.Rock 2.Paper 3.Scissors \nEnter choice number: ")
    game_options = {
        '1': 'Rock',
        '2': 'Paper',
        '3': 'Scissors'
    }
    
    if user_choice in game_options:
        user_choice = game_options[user_choice]
    else:
        print("Invalid choice. Please enter 1, 2, or 3!")
        user_choice = input("1.Rock 2.Paper 3.Scissors \nEnter choice number: ")

    CPU_choice = random.choice(list(game_options.values()))

    if CPU_choice == user_choice:
        return f"A draw! \nI chose {CPU_choice.lower()} too!"
    elif victory(user_choice, CPU_choice):
        return f"You Won! \nI chose {CPU_choice.lower()}."
    else:
        return f"You Lost! \nI chose {CPU_choice.lower()}."

print(playGame())
