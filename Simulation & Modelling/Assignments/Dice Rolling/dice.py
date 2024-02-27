import random

# Number of rolls
num_rolls = 1000

# Initialize counters for each face
face_counts = [0] * 6

# Simulate rolling the die
for _ in range(num_rolls):
    # Generate a random number between 0 and 1
    random_number = random.uniform(0, 1)

    # Determine the face based on the random number
    face = int(random_number * 6) + 1

    # Update the counter for the corresponding face
    face_counts[face - 1] += 1

# Display the table of outcomes
print("Outcome \tFrequency \tPercentage")
print("-------------------------------------------")
for face, count in enumerate(face_counts, 1):
    percentage = (count / num_rolls) * 100
    print(f"Face {face} \t\t{count} \t\t{percentage:.2f}%")
print("-------------------------------------------")
print(f"Total:\t\t{num_rolls}\t\t{int(num_rolls * 0.1)}%")
