import numpy as np
import matplotlib.pyplot as plt

def henon_map(x0, a, num_iterations):
    x_values = np.zeros(num_iterations)
    x_values[0] = x0

    for n in range(1, num_iterations):
        x_values[n] = 1 - a*x_values[n-1]**2

    return x_values

# Parameters
x0 = 0  # Initial condition
num_iterations = 1000
a_values = np.linspace(1.0, 2.0, 200)  # Range of a values

# Prepare the plot
plt.figure(figsize=(10, 6))

for a in a_values:
    # Generate the Henon map for each value of a
    x_values = henon_map(x0, a, num_iterations)
    
    # Plot the final few iterations for each a value to see the long-term behavior
    plt.plot([a] * num_iterations, x_values, ',k', alpha=0.25)  # Using a scatter plot for density

plt.title("1D Henon Map: x vs a")
plt.xlabel("Parameter a")
plt.ylabel("x_n (state after many iterations)")
plt.show()
