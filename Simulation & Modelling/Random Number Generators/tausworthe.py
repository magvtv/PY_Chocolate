from random import seed


class TauswortheGenerator:
    def __init__(self, r, q, seed_sequence, initial_i):
        self.seed_sequence = seed_sequence
        self.r = r
        self.q = q
        self.i = initial_i - 1
        self.seed_length = len(seed_sequence)
        
    def generate_random_number(self):
        next_i = (self.i + 1) % self.seed_length
        next_j = (self.i + self.q) % self.seed_length
        next_k = (self.i + self.r) % self.seed_length
        
        bi = int(self.seed_sequence[next_i])
        bj = int(self.seed_sequence[next_j])  
        bk = int(self.seed_sequence[next_k])  
        
        new_bit = (bi ^ bj) ^ bk
        self.seed_sequence = self.seed_sequence[:next_i] + str(new_bit) + self.seed_sequence[next_i + 1:]
        self.i = next_i
        return new_bit
    

r = 4
q = 17
seed_sequence = "10101110010001101"
initial_i = 17

generator = TauswortheGenerator(r, q, seed_sequence, initial_i)

# generate 20 random numbers
random_numbers = []
for _ in range(20):
    random_numbers.append(generator.generate_random_number())

print("Generate random numbers:\n", random_numbers)        
        