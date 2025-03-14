import numpy as np
import matplotlib.pyplot as plt

# Define the 2x2 grid training dataset (0 = Black, 1 = White)
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

# Create a mapping to understand how the flattened array maps to the 2x2 grid
grid_indices = [
    [0, 1],  # top row
    [2, 3]   # bottom row
]

# Expected output (1 = Bright, 0 = Dark)
y = np.array([0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1])

# Set seed for reproducibility
np.random.seed(42)

# Initialize perceptron parameters
weights = np.random.rand(4)  # 4 input weights
bias = np.random.rand(1)
learning_rate = 0.25
epochs = 6  # Training iterations

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

print("\nFinal Weights:", weights)
print("Final Bias:", bias)

# Function to convert flattened array to 2x2 grid


def flat_to_grid(flat_array):
    """
    Converts a flattened array of 4 elements to a 2x2 grid.
    The mapping is:
    [0, 1, 2, 3] -> [[0, 1], [2, 3]]
    which represents the top-left, top-right, bottom-left, bottom-right positions.
    """
    return flat_array.reshape(2, 2)

# Function to visualize a single 2x2 grid


def visualize_grid(grid, label):
    """
    displays a 2x2 grid using Matplotlib and labels it as Bright or Dark.
    :param grid: 2x2 binary array (0 = Black, 1 = White)
    :param label: Classification result (Bright or Dark)
    """
    plt.figure(figsize=(3, 3))
    plt.imshow(grid, cmap="gray", vmin=0, vmax=1)  # Inverts 0=Black, 1=White
    plt.xticks([])  # Remove x-axis labels
    plt.yticks([])  # Remove y-axis labels
    plt.title(f"Classified as: {label}", fontsize=14, fontweight="bold")
    plt.show()

# Function to visualize all possible 2x2 grids


def visualize_all_grids():
    """
    Displays all 16 possible 2x2 grids with their classification results.
    """
    fig, axes = plt.subplots(4, 4, figsize=(10, 10))

    # Helper to count white cells in a grid
    def count_white(grid_flat):
        return sum(grid_flat)

    for i, ax in enumerate(axes.flat):
        # Get flat grid
        grid_flat = X[i]

        # Convert to 2x2 grid
        grid = flat_to_grid(grid_flat)

        # Classify
        z = np.dot(weights, grid_flat) + bias
        classification = step_function(z)
        label = "Bright" if classification == 1 else "Dark"

        # Count white cells for verification
        white_count = count_white(grid_flat)

        # Display
        ax.imshow(grid, cmap="gray", vmin=0, vmax=1)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(f"{label} ({white_count} white)", fontsize=9)

    plt.tight_layout()
    plt.show()

# Function to classify and visualize a test grid


def test_and_visualize(test_flat):
    """
    Classifies a flat grid and visualizes the result.

    :param test_flat: Flattened array representing the 2x2 grid
    """
    # Classify
    z = np.dot(weights, test_flat) + bias
    classification = step_function(z)
    label = "Bright" if classification == 1 else "Dark"

    # Convert to 2x2 grid
    grid = flat_to_grid(test_flat)

    # Count white cells
    white_count = sum(test_flat)

    print(f"\nTest Grid: {test_flat} (has {white_count} white cells)")
    print(f"Classification: {label}")

    # Visualize
    visualize_grid(grid, label)

    return label


# Test on several examples
print("\n--- Testing the perceptron ---")

# Test grid - example with 3 white cells
test_grid = np.array([1, 0, 1, 1])
test_and_visualize(test_grid)

# Show all possible grids
print("\n--- All Possible Grids ---")
visualize_all_grids()
