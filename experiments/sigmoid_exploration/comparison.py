import numpy as np
import matplotlib.pyplot as plt

# Define the range for the input values
ratio_values = np.linspace(-1, 2, 1000)

# Sigmoid function using the ratio as input
sigmoid = 1 / (1 + np.exp(-ratio_values))

# Transformed exponential function using the ratio as input
transformed_exp = 1 - np.exp(-ratio_values)

# Plotting both functions
plt.figure(figsize=(10, 6))
plt.plot(ratio_values, sigmoid, label='Sigmoid Function $\\sigma(x) = \\frac{1}{1 + e^{-x}}$')
plt.plot(ratio_values, transformed_exp, label='Transformed Exponential $1 - e^{-x}$')
plt.title('Comparison of Sigmoid and Transformed Exponential Functions')
plt.xlabel('Ratio (0 to 1)')
plt.ylabel('Function Output')
plt.legend()
plt.grid(True)
plt.show()
