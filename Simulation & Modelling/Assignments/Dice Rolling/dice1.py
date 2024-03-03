import random
import os
import math

# function to clear the terminal screen on linux os
def clear_screen():
    _ = os.system('clear')



# Number of rolls
total_dice_rolls = 1000

# initialize counters for each face of the dice
face_counts = [0] * 6

# simulating the rolling of the dice with for loop
"""
    for loop for updating the face counts, that have 6 elements, each
    set to 0.
    Each element corresponds to a face of the dice (from 1 to 6)
"""
for _ in range(total_dice_rolls):
    # Generate a random number between 0 and 1
    random_number = random.uniform(0, 1)

    # Determine the face based on the random number
    """
        the random number determines dice face to roll. 
        multiplying the random number by 6 (the number of faces on a dice)
        and adding 1 ensures the result is between 1 and 6 as it scales it to the possible 
        range of faces on a six-faced die (a valid face)
    """
    face = random_number * 6 + 1

    # Update the counter for the corresponding face
    """
        the counter for the corresponding face rolled is then updated by incrementing 
        the value at the index corresponding to that face in the face_counts list
    """
    face_index = (math.floor(face) - 1)
    face_counts[face_index] += 1

# Display the table of outcomes
"""
    After all rolls are simulated, the face_counts list will contain 
    the frequency of each face rolled during the simulation
"""
clear_screen()
print("Outcome \tFrequency \tPercentage")
print("-------------------------------------------")
for face, count in enumerate(face_counts, 1):
    percentage = (count / total_dice_rolls) * 100
    print(f"Face {face}\t\t{count}\t\t{percentage:.2f}%")
print("-------------------------------------------")
print(f"Total:\t\t{total_dice_rolls}\t\t{100}%")
