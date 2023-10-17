import random

def victory(player, opponent):
    if (((player == 'Rock') and (opponent == 'Scissors')) or 
        ((player == 'Scissors') and (opponent == 'Paper'))  or 
        ((player == 'Paper') and (opponent == 'Rock'))):
        return True

def playGame():
    user_choice = input("1.Rock 2.Paper 3.Scissors \nEnter choice number: ")    
    game_options = {
        '1': 'Rock',
        '2': 'Paper',
        '3': 'Scissors',
    }

    if user_choice in game_options:
        user_choice = game_options[user_choice]
    else:
        while user_choice not in game_options:
            print("Invalid choice! Please enter 1, 2 or 3.")
            user_choice =  input("1.Rock 2.Paper 3.Scissors \nEnter choice number: ")
    
    CPU_choice = random.choice(list(game_options.values()))
    
    if user_choice == CPU_choice:
        return f"A draw! I chose {CPU_choice} too!"
    elif victory(user_choice, CPU_choice):
        return f"You win! I chose {CPU_choice}"
    else:
        return f"You lost! I chose {CPU_choice}"


print(playGame())
