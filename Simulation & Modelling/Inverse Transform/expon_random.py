import math
import random

def expon_inverse_transform(U, b):
    return -b * math.log(1- U)

mean = 1.0
observations = []
for _ in range(20):
    U = random.random()
    x = expon_inverse_transform(U, mean)
    observations.append(x)
    
print("Generated Observations\n")

for i, obs in enumerate(observations, 1):
    print(f"Observation {i}: {obs:.3f}")