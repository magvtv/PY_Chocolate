import random
from collections import Counter
import os

# function to clear the terminal screen on linux os
def clear_screen():
    _ = os.system('clear')

num_rolls = 1000

# mapping the random number to dice face
dice_faces = {
    0: 1,
    1/6: 2,
    2/6: 3,
    3/6: 4,
    4/6: 5,
    5/6: 6,
}

# rolls does the rolling of the dice num_rolls times
rolls = [random.random() for _ in range(num_rolls)]

# convert random numbers to dice faces
faces = [dice_faces[min(dice_faces.keys(), key=lambda x: abs(x - roll))] for roll in rolls]

# counting the occurrences of each face 
face_counts = Counter(faces)

# calculating the percentage occurrence of each face
total_rolls = sum(face_counts.values())
face_percentages = {
    face: ((count / total_rolls) * 100) for face, count in face_counts.items()
}

clear_screen()
print("Outcome \tFrequency \tPercentage")
print("-------------------------------------------")
for face in sorted(face_counts):
    print(f"Face {face}\t\t{face_counts[face]}\t\t{face_percentages[face]:.2f}%")
print("-------------------------------------------")
print(f"Total:\t\t{total_rolls}\t\t{100}%")


