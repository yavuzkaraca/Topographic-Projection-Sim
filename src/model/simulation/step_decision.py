import math

import numpy as np


def clamp_to_boundaries(position, substrate, size, xt_direction, yt_direction):
    """
    Clamp the growth cone's new positions within the substrate boundaries.

    :param position: Current position of the growth cone.
    :param substrate: Substrate object defining the model area.
    :param size: Size of the growth cone.
    :param xt_direction: The change in x-direction.
    :param yt_direction: The change in y-direction.
    :return: The clamped new position of the growth cone within the substrate boundaries.
    """
    new_x = position[0] + xt_direction
    new_y = position[1] + yt_direction

    # Clamp the new positions to stay within the substrate boundaries
    new_x_clamped = max(size, min(new_x, substrate.cols - 1 - size))
    new_y_clamped = max(size, min(new_y, substrate.rows - 1 - size))

    return new_x_clamped, new_y_clamped


def probabilistic_density(potential, sigma):
    """
    Calculate the probability density function for a gaussian distribution.

    :param potential: The potential of a growth cone.
    :param sigma: The standard deviation of the distribution.
    :return: The probability density at the given potential value.
    """

    y = math.exp(-potential ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma)
    return y


def calculate_probability(old_prob, new_prob):
    """
    Calculate the probability of a growth cone taking a step based on potential differences.

    :param old_prob: Old probability based on the previous potential.
    :param new_prob: New probability based on the current potential.
    :return: Probability of the growth cone taking a step.
    """

    if old_prob + new_prob == 0:
        probability = 0.5
    else:
        probability = old_prob / (old_prob + new_prob)
    return probability


def calculate_ff_coef(step, num_steps, sigmoid_steepness, sigmoid_shift, sigmoid_height=1):
    """
    Calculate the ratio of steps taken using a sigmoid function, scaled by sigmoid_gain.

    :param sigmoid_height:
    :param step: The current step number of the growth cone.
    :param num_steps: The total steps possible for the growth cone.
    :param sigmoid_steepness: The factor that controls the steepness of the sigmoid curve.
    :param sigmoid_shift: The factor to adjust the midpoint of the sigmoid; defaults to 0.05.
    :return: The scaled output of the sigmoid function, representing the step ratio.
    """

    step += (num_steps * 0.01)  # such that with shift = 100 immediate activation
    step_ratio = step / num_steps
    sigmoid_adjustment = (step_ratio * sigmoid_shift) ** sigmoid_steepness
    safe_sigmoid = np.clip(sigmoid_adjustment, a_min=1e-10, a_max=None)  # Prevent log(0) which results in -inf

    return (-np.exp(-safe_sigmoid) + 1) * sigmoid_height