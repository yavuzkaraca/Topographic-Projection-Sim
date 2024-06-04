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


def calculate_ff_coef(step, num_steps, sigmoid_steepness=3, sigmoid_shift=2, sigmoid_height=1):
    """
    Calculate the ratio of steps taken using a sigmoid function, scaled by sigmoid_gain.

    :param sigmoid_height:
    :param step: The current step number of the growth cone.
    :param num_steps: The total steps possible for the growth cone.
    :param sigmoid_steepness: The factor that controls the steepness of the sigmoid curve.
    :param sigmoid_shift: The factor to adjust the midpoint of the sigmoid; defaults to 0.05.
    :return: The scaled output of the sigmoid function, representing the step ratio.
    """

    step_ratio = step / num_steps
    sigmoid_adjustment = (step_ratio * sigmoid_shift) ** sigmoid_steepness
    safe_sigmoid = np.clip(sigmoid_adjustment, a_min=1e-10, a_max=None)  # Prevent log(0) which results in -inf

    return (-np.exp(-safe_sigmoid) + 1) * sigmoid_height


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
results = [calculate_ff_coef(ii, steps) for ii in ii_values]

plt.figure(figsize=(10, 6))
plt.plot(ii_values / steps, results, label='GC_GCfactor')
plt.title('Plot of GC_GCfactor from ii/steps = 0 to 1')
plt.xlabel('ii/steps')
plt.ylabel('GC_GCfactor Value')
plt.grid(True)
plt.legend()
plt.show()
