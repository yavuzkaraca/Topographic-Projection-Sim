import numpy as np
import matplotlib.pyplot as plt

shift = 4
steepness = 5


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


def ratio(ii, steps):
    # Adjust to avoid negative values in the logarithm
    ratio = (ii / (steps / shift)) ** steepness
    ratio = np.clip(ratio, a_min=1e-10, a_max=None)  # Prevent log(0) which results in -inf
    return ratio


def expression(ii, steps):
    # Adjust to avoid negative values in the logarithm
    ratio = (ii / steps)
    return -np.exp(-np.log(2 ** ratio)) + 1


steps = 1000
ii_values = np.linspace(0, steps, 1000)  # Evenly spaced values including the last point
results = [simplified_formula(ii, steps) for ii in ii_values]

plt.figure(figsize=(10, 6))
plt.plot(ii_values / steps, results, label='GC_GCfactor')
plt.title('Plot of GC_GCfactor from ii/steps = 0 to 1')
plt.xlabel('ii/steps')
plt.ylabel('GC_GCfactor Value')
plt.grid(True)
plt.legend()
plt.show()
