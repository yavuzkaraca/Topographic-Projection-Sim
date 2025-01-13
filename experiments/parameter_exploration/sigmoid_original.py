import numpy as np
import matplotlib.pyplot as plt

shift = 3
steepness = 2
steps = 1000


def original_formula(ii, steps, ffConstant=1):
    # Adjust to avoid negative values in the logarithm
    ratio = (ii / (steps / shift)) ** steepness
    ratio = np.clip(ratio, a_min=1e-10, a_max=None)  # Prevent log(0) which results in -inf
    return ffConstant * (-np.exp(-np.log(2 ** ratio)) + 1)


def simplified_formula(ii, steps, ffConstant=1):
    # Adjust to avoid negative values in the logarithm
    ratio = (ii / (steps / shift)) ** steepness
    ratio = np.clip(ratio, a_min=1e-10, a_max=None)  # Prevent log(0) which results in -inf
    return ffConstant * (-np.exp(-ratio) + 1)


ii_values = np.arange(0, steps)  # Evenly spaced values including the last point
results = [original_formula(ii, steps) for ii in ii_values]

plt.figure(figsize=(10, 6))
plt.plot(ii_values / steps, results, label='GC_GCfactor')
plt.title('ff_factor gain')
plt.xlabel('step / total steps')
plt.ylabel('ff_factor')
plt.grid(True)
plt.legend()
plt.show()


# Define the range for the input values
ratio_values = np.linspace(-1, 2, 50)

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
