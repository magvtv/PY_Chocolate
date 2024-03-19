import random
from tabulate import tabulate


# Define function to roll a dice using floating-point numbers
def roll_dice():
  return random.random()


# Define function to get face based on random number
def get_face(random_number):
  if random_number < 1 / 6:
    return 1
  elif 1 / 6 < random_number < 2 / 6:
    return 2
  elif 2 / 6 < random_number < 3 / 6:
    return 3
  elif 3 / 6 < random_number < 4 / 6:
    return 4
  elif 4 / 6 < random_number < 5 / 6:
    return 5
  else:
    return 6


# Simulate rolling a dice 1000 times using floating-point numbers
dice_rolls = [get_face(roll_dice()) for _ in range(1000)]

# Count the occurrences of each face
face_counts = [dice_rolls.count(i) for i in range(1, 7)]

# Calculate the percentage occurrence of each face
percentage_occurrences = [count / 1000 * 100 for count in face_counts]

# Create a table
table_headers = ['Face', 'Frequency', 'Percentage']
table_data = list(
    zip(range(1, 7), face_counts, percentage_occurrences, strict=True))

table = tabulate(table_data, headers=table_headers, tablefmt='grid')

# Print the table
print(table)