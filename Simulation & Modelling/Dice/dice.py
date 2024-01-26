import random

num_rolls = 1000
face_counts = [0] * 6


for _ in range (num_rolls):
    random_num = random.uniform(0, 1)
    face = int(random_num * 6) + 1
    face_counts[face - 1] += 1
    
print("Outcome \tFrequency \tPercentage ")
print("-----------------------------------------")
for face, count in enumerate(face_counts, 1):
    percentage = (count / num_rolls) * 100
    print(f"{face} \t\t{count} \t\t{percentage:.2f}%")