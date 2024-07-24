# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Function for the model (using a second-degree polynomial for fitting)
def model(x, a, b, c):
    return a * x ** 2 + b * x + c


def main():
    # Data: Number of growth cones and corresponding runtimes
    growth_cone_counts = np.array([10, 50, 100, 200, 300, 500, 750, 1000])
    runtimes = np.array([0.05, 0.26, 0.8, 2.5, 5, 12, 26, 45])

    # Scatter plot of the data
    plt.figure(figsize=(10, 7))
    plt.scatter(growth_cone_counts, runtimes, color='blue', label='Data Points')
    plt.xlabel('Number of Growth Cones')
    plt.ylabel('Runtime (minutes)')
    plt.title('Simulation Runtime in terms of Number of Growth Cones')
    plt.grid(True)

    # Curve fitting
    popt, _ = curve_fit(model, growth_cone_counts, runtimes)

    # Generate values for the fitted curve
    x_line = np.arange(min(growth_cone_counts), max(growth_cone_counts), 1)
    y_line = model(x_line, *popt)

    # Plot the fitted curve
    plt.plot(x_line, y_line, '--', color='red', label='Fit: ax² + bx + c')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
