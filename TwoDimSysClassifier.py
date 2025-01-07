import numpy as np
import matplotlib.pyplot as plt

def classify_and_plot_with_nullclines_and_manifolds(matrix):
    # Compute trace and determinant
    trace = np.trace(matrix)
    determinant = np.linalg.det(matrix)
    
    # Eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    
    # Classify the system
    if determinant < 0:
        classification = "Saddle Point"
    elif determinant == 0:
        classification = "Non-Isolated Fixed Point"
    else:
        if trace**2 < 4 * determinant:
            if trace < 0:
                classification = "Stable Spiral"
            elif trace > 0:
                classification = "Unstable Spiral"
            else:
                classification = "Center"
        elif trace**2 == 4 * determinant:
            if trace < 0:
                classification = "Stable Degenerate Node (Star)"
            else:
                classification = "Unstable Degenerate Node (Star)"
        else:
            if trace < 0:
                classification = "Stable Node"
            else:
                classification = "Unstable Node"
    
    # Print classification
    print(f"Matrix: \n{matrix}")
    print(f"Trace: {trace:.2f}, Determinant: {determinant:.2f}")
    print(f"Eigenvalues: {eigenvalues}")
    print(f"Eigenvectors:\n{eigenvectors}")
    print(f"System Classification: {classification}")
    
    # Plot trace-determinant diagram
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))
    
    # Trace-Determinant Diagram
    t = np.linspace(-10, 10, 500)
    det_curve = t**2 / 4
    ax[0].plot(t, det_curve, 'k--', label=r'Det = Tr$^2$/4')
    ax[0].fill_between(t, det_curve, 10, where=(t >= 0), color='lightcoral', alpha=0.3, label="Unstable Region")
    ax[0].fill_between(t, det_curve, 10, where=(t < 0), color='lightblue', alpha=0.3, label="Stable Region")
    ax[0].fill_between(t, -10, det_curve, color='lightgray', alpha=0.3, label="Saddle Region")
    ax[0].plot(trace, determinant, 'ko', label=f'({trace:.2f}, {determinant:.2f})')
    ax[0].set_title("Trace-Determinant Diagram", fontsize=14)
    ax[0].set_xlabel("Trace", fontsize=12)
    ax[0].set_ylabel("Determinant", fontsize=12)
    ax[0].axhline(0, color='black', linewidth=0.8)
    ax[0].axvline(0, color='black', linewidth=0.8)
    ax[0].set_xlim(-10, 10)
    ax[0].set_ylim(-10, 10)
    ax[0].legend()
    ax[0].grid()

    # Phase Portrait (x_dot vs y_dot)
    x = np.linspace(-10, 10, 20)
    y = np.linspace(-10, 10, 20)
    X, Y = np.meshgrid(x, y)
    U = matrix[0, 0] * X + matrix[0, 1] * Y  # x_dot
    V = matrix[1, 0] * X + matrix[1, 1] * Y  # y_dot

    ax[1].streamplot(X, Y, U, V, color='black', density=2)

    # Nullclines
    x_nullcline = np.linspace(-10, 10, 200)
    
    # Handle x_dot = 0 nullcline (vertical line at x = 0 if a12 == 0)
    if matrix[0, 1] != 0:  # Check if a12 is non-zero
        y_nullcline1 = -matrix[0, 0] / matrix[0, 1] * x_nullcline
        ax[1].plot(x_nullcline, y_nullcline1, 'r-.', label=r'$\dot{x} = 0$ (Nullcline)',linewidth=2)
    else:  # If a12 == 0, the nullcline for x_dot = 0 is a vertical line at x = 0
        ax[1].plot([0, 0], [-10, 10], 'r-.', label=r'$\dot{x} = 0$ (Nullcline)',linewidth=2)

    if matrix[1, 1] != 0:  # Check if a22 is non-zero
        y_nullcline2 = -matrix[1, 0] / matrix[1, 1] * x_nullcline
        ax[1].plot(x_nullcline, y_nullcline2, 'b--', label=r'$\dot{y} = 0$ (Nullcline)',linewidth=2)

    # Stable and Unstable Manifolds (if applicable)
    if "Saddle Point" in classification:
        # Eigenvectors for stable and unstable manifolds
        stable_index = np.argmin(eigenvalues.real)  # Index of stable eigenvalue (most negative)
        unstable_index = np.argmax(eigenvalues.real)  # Index of unstable eigenvalue (most positive)

        stable_vec = eigenvectors[:, stable_index]
        unstable_vec = eigenvectors[:, unstable_index]

        # Scale manifolds for visualization
        unstable_line_x = np.linspace(-10, 10, 100) * stable_vec[0]
        unstable_line_y = np.linspace(-10, 10, 100) * stable_vec[1]
        stable_line_x = np.linspace(-10, 10, 100) * unstable_vec[0]
        stable_line_y = np.linspace(-10, 10, 100) * unstable_vec[1]

        ax[1].plot(stable_line_x, stable_line_y, 'b-', label="Stable Manifold")
        ax[1].plot(unstable_line_x, unstable_line_y, 'r-', label="Unstable Manifold")


    ax[1].set_title("Phase Portrait", fontsize=14)
    ax[1].set_xlabel("x", fontsize=12)
    ax[1].set_ylabel("y", fontsize=12)
    ax[1].axhline(0, color='black', linewidth=0.8)
    ax[1].axvline(0, color='black', linewidth=0.8)
    ax[1].set_xlim(-10, 10)
    ax[1].set_ylim(-10, 10)
    ax[1].legend()
    ax[1].grid()

    plt.tight_layout()
    plt.show()

# Input the 2x2 matrix for a stable node
a11 = 2
a12 = 1
a21 = 1
a22 = -2
A = np.array([[a11, a12], [a21, a22]])

# Call the function
classify_and_plot_with_nullclines_and_manifolds(A)
