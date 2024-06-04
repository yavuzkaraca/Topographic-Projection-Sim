"""
Module for conducting a simulation.
"""
import concurrent.futures
import math
import time

import numpy as np

from simulation.result import Result
from simulation.potential_calculation import calculate_potential
import random


def clamp_to_boundaries(position, substrate, size, xt_direction, yt_direction):
    """
    Clamp the growth cone's new positions within the substrate boundaries.

    :param position: Current position of the growth cone.
    :param substrate: Substrate object defining the simulation area.
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

    step += (num_steps * 0.01)
    step_ratio = step / num_steps
    sigmoid_adjustment = (step_ratio * sigmoid_shift) ** sigmoid_steepness
    safe_sigmoid = np.clip(sigmoid_adjustment, a_min=1e-10, a_max=None)  # Prevent log(0) which results in -inf

    return (-np.exp(-safe_sigmoid) + 1) * sigmoid_height


class Simulation:
    """
    Class managing the simulation process for growth cones.

    Attributes:
        substrate: Substrate object representing the simulation area.
        growth_cones: List of Growth Cone instances.
        adaptation: Boolean indicating adaptation feature.
        step_size: Size of step movement for growth cones.
        steps_total: Total number of steps for the simulation.
        x_step_p: Probability of a growth cone stepping in the x-direction.
        y_step_p: Probability of a growth cone stepping in the y-direction.
        sigma: Standard deviation for the potential calculation.

    Methods:
        run(): Runs the simulation and gathers final growth cone positions.
        step_decision(gc, step): Makes a decision for a growth cone to step or not.
        gen_random_step(): Generates a random step in the x and y directions.
    """

    def __init__(self, substrate, growth_cones, adaptation, step_size, num_steps, x_step_p, y_step_p, sigmoid_gain,
                 sigmoid_shift, sigma, force, forward_sig, reverse_sig, ff_inter, ft_inter, mu, lambda_,
                 history_length):
        """
        Initialize the Simulation class with necessary parameters.

        :param substrate: Substrate object defining the simulation area.
        :param growth_cones: List of Growth Cone instances participating in the simulation.
        :param adaptation: Boolean value indicating whether adaptation is enabled or not.
        :param step_size: Size of the step movement for the growth cones.
        :param num_steps: Total number of steps for the simulation.
        :param x_step_p: Probability of a growth cone stepping in the x-direction.
        :param y_step_p: Probability of a growth cone stepping in the y-direction.
        :param sigmoid_shift:
        :param sigma: Standard deviation for potential calculations.
        :param mu: Parameter for adaptation coefficient calculation.
        :param lambda_: Parameter for resetting force calculation.
        :param history_length: Number of historical steps to consider for adaptation.
        """
        self.forward_sig = forward_sig
        self.reverse_sig = reverse_sig
        self.ff_inter = ff_inter
        self.ft_inter = ft_inter
        self.substrate = substrate
        self.growth_cones = growth_cones
        self.adaptation = adaptation
        self.step_size = step_size
        self.steps_total = num_steps
        self.x_step_p = x_step_p
        self.y_step_p = y_step_p
        self.sigmoid_gain = sigmoid_gain
        self.sigmoid_shift = sigmoid_shift
        self.sigma = sigma
        self.mu = mu
        self.lambda_ = lambda_
        self.history_length = history_length
        self.force = force

        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)

    def run(self):
        """
        Execute the simulation for the defined number of steps using multi-threading.
        """
        for gc in self.growth_cones:
            # Potential initialization
            gc.potential = calculate_potential(gc, self.growth_cones, self.substrate, 0)

        print(f"\nInitialization completed.\nIteration starts, {self.steps_total} many steps will be taken\n")

        for step_current in range(self.steps_total):
            if step_current % 250 == 0:
                print(f"Current Step: {step_current}")

            # Create a list of futures for the thread pool
            futures = []
            for gc in self.growth_cones:
                if self.adaptation:
                    self.adapt_growth_cone(gc)
                if not gc.marked:
                    # Submit update tasks to the executor
                    futures.append(
                        self.executor.submit(self.step_decision, gc, calculate_ff_coef(step_current, self.steps_total,
                                                                                       self.sigmoid_gain,
                                                                                       self.sigmoid_shift)))

            # Wait for all threads to complete before moving to the next step
            concurrent.futures.wait(futures)

        print("\nIteration completed\n")

        for gc in self.growth_cones:
            print(gc)

        return Result(self.growth_cones, self.substrate)

    def step_decision(self, gc, step_ratio):
        """
        Make a decision for a growth cone to step or not based on potential and probabilities of its new position.

        :param step_ratio:
        :param gc: A Growth Cone instance.
        """

        # Choose a new position
        xt_direction, yt_direction = self.gen_random_step()
        gc.pos_new = clamp_to_boundaries(gc.pos_current, self.substrate, gc.size, xt_direction, yt_direction)

        # Calculate new potential
        new_potential = calculate_potential(gc, self.growth_cones, self.substrate, step_ratio,
                                            self.forward_sig, self.reverse_sig, self.ff_inter, self.ft_inter)

        if self.force:
            # Force gc to take the random generated step, neglecting ques from guidance potential
            gc.take_step(new_potential)
            return

        # Calculate Step realization probabilities
        old_density = probabilistic_density(gc.potential, self.sigma)
        new_density = probabilistic_density(new_potential, self.sigma)
        probability = calculate_probability(old_density, new_density)

        # Step Decision
        random_number = random.random()

        if random_number > probability:
            gc.take_step(new_potential)

    def gen_random_step(self):
        """
        Generate a random step in the x and y directions.

        :return: Tuple of x and y directional steps.
        """

        # Initialization
        x_prob = self.x_step_p
        y_prob = self.y_step_p

        # Randomly step in xt and yt directions -1, 0, +1
        xt_direction = random.choices([-1, 0, 1], weights=[(1 - x_prob), (1 - x_prob), x_prob])[0]
        yt_direction = random.choices([-1, 0, 1], weights=[y_prob, (1 - y_prob), y_prob])[0]

        return xt_direction * self.step_size, yt_direction * self.step_size

    def adapt_growth_cone(self, gc):
        """
        Adapt the growth cone properties based on the simulation's adaptation configuration.

        :param gc: A Growth Cone instance.
        """
        gc.calculate_adaptation(self.mu, self.lambda_, self.history_length)
        gc.apply_adaptation()
