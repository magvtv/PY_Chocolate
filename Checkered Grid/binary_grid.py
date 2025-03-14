import numpy as np
import matplotlib.pyplot as plt

# Define the 2x2 grid training dataset
# 0 is black, 1 is white
X = np.array([
    [0, 0, 0, 0],  # 0 white (all black) - Dark
    [0, 0, 0, 1],  # 1 white - Dark
    [0, 0, 1, 0],  # 1 white - Dark
    [0, 0, 1, 1],  # 2 white - Bright
    [0, 1, 0, 0],  # 1 white - Dark
    [0, 1, 0, 1],  # 2 white - Bright
    [0, 1, 1, 0],  # 2 white - Bright
    [0, 1, 1, 1],  # 3 white - Bright
    [1, 0, 0, 0],  # 1 white - Dark
    [1, 0, 0, 1],  # 2 white - Bright
    [1, 0, 1, 0],  # 2 white - Bright
    [1, 0, 1, 1],  # 3 white - Bright
    [1, 1, 0, 0],  # 2 white - Bright
    [1, 1, 0, 1],  # 3 white - Bright
    [1, 1, 1, 0],  # 3 white - Bright
    [1, 1, 1, 1],  # 4 white (all white) - Bright
])

# Expected output (1 = Bright, 0 = Dark)
y = np.array([0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1])

# Initialize perceptron parameters
weights = np.random.rand(4)  # 4 input weights
bias = np.random.rand(1)
learning_rate = 0.1
epochs = 10  # Training iterations

# Activation function (Step Function)


def step_function(x):
    return 1 if x >= 0 else 0


# Training Perceptron
for epoch in range(epochs):
    total_error = 0
    for i in range(len(X)):
        # Compute weighted sum
        z = np.dot(weights, X[i]) + bias
        y_pred = step_function(z)

        # Compute error
        error = y[i] - y_pred
        total_error += abs(error)

        # Update weights and bias
        weights += learning_rate * error * X[i]
        bias += learning_rate * error

    # Print error for debugging
    print(f"Epoch {epoch+1}, Error: {total_error}")

# Testing on new unseen inputs
test_grid = np.array([1, 0, 1, 1])
print(f"\nTest Grid: {test_grid}")
print("Final Weights:", weights)
print("Final Bias:", bias)

output = step_function(np.dot(weights, test_grid) + bias)
print("Test Grid Output:", "Bright" if output == 1 else "Dark")
