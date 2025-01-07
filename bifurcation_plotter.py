import numpy as np
import matplotlib.pyplot as plt

# Logistic map function
def logistic_map(x, r):
    return r*x*(1 - x)

# Function to compute and plot bifurcation diagram
def bifurcation_diagram(r_min, r_max, num_r_values, num_iterations, num_skip):
    # Create a figure
    plt.figure(figsize=(10, 6))
    
    # Values of r (control parameter)
    r_values = np.linspace(r_min, r_max, num_r_values)
    
    # Iterate over values of r
    for r in r_values:
        # Initial condition (start the iteration with x = 0.5)
        x = 0.5
        
        # Skip initial transients
        for i in range(num_iterations - num_skip):
            x = logistic_map(x, r)
        
        # Now plot the last few values of x (the attractors)
        for i in range(num_skip):
            x = logistic_map(x, r)
            plt.plot(r, x, ',k', alpha=0.5)  # ',' for thin dots
    
    # Customize plot
    plt.title("Bifurcation Diagram of Logistic Map")
    plt.xlabel("r (Control Parameter)")
    plt.ylabel("x (State of the System)")
    plt.show()

# Parameters for the bifurcation diagram
r_min = 2.4      # Minimum value of r
r_max = 4.0      # Maximum value of r
num_r_values = 10000  # Number of r values to evaluate
num_iterations = 100  # Total number of iterations to compute
num_skip = 100  # Number of iterations to skip for transients

# Generate the bifurcation diagram
bifurcation_diagram(r_min, r_max, num_r_values, num_iterations, num_skip)
