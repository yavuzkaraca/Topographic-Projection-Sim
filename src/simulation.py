"""
Module for conducting a simulation.
"""

import math
from result import Result
from potential_calculation import calculate_potential
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

    # Probability density function for normal distribution
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


class Simulation:
    """
    Class managing the simulation process for growth cones.

    Attributes:
        substrate: Substrate object representing the simulation area.
        growth_cones: List of Growth Cone instances.
        adaptation: Boolean indicating adaptation feature.
        step_size: Size of step movement for growth cones.
        num_steps: Total number of steps for the simulation.
        x_step_p: Probability of a growth cone stepping in the x-direction.
        y_step_p: Probability of a growth cone stepping in the y-direction.
        sigma: Standard deviation for the potential calculation.

    Methods:
        run(): Runs the simulation and gathers final growth cone positions.
        step_decision(gc, step): Makes a decision for a growth cone to step or not.
        gen_random_step(): Generates a random step in the x and y directions.
    """

    def __init__(self, substrate, growth_cones, adaptation, step_size, num_steps, x_step_p, y_step_p, sigma, mu,
                 lambda_, history_length):
        """
        Initialize the Simulation class with necessary parameters.

        :param substrate: Substrate object defining the simulation area.
        :param growth_cones: List of Growth Cone instances participating in the simulation.
        :param adaptation: Boolean value indicating whether adaptation is enabled or not.
        :param step_size: Size of the step movement for the growth cones.
        :param num_steps: Total number of steps for the simulation.
        :param x_step_p: Probability of a growth cone stepping in the x-direction.
        :param y_step_p: Probability of a growth cone stepping in the y-direction.
        :param sigma: Standard deviation for potential calculations.
        :param mu: Parameter for adaptation coefficient calculation.
        :param lambda_: Parameter for resetting force calculation.
        :param history_length: Number of historical steps to consider for adaptation.
        """
        self.substrate = substrate
        self.growth_cones = growth_cones
        self.adaptation = adaptation
        self.step_size = step_size
        self.num_steps = num_steps
        self.x_step_p = x_step_p
        self.y_step_p = y_step_p
        self.sigma = sigma
        self.mu = mu
        self.lambda_ = lambda_
        self.history_length = history_length

    def run(self):
        """
        Execute the simulation for the defined number of steps.

        :return: Result object containing final growth cone positions and details.
        """
        for gc in self.growth_cones:
            # potential initialization
            gc.potential = calculate_potential(gc, self.growth_cones, self.substrate, 0)
            print(gc)

        print(f"\nInitialization completed.\nIteration starts, {self.num_steps} many steps will be taken\n")

        for step in range(self.num_steps):
            if step % 1000 == 0:
                print(step)
            # Update growth cones
            for gc in self.growth_cones:
                if self.adaptation:
                    self.adapt_growth_cone(gc)
                    # print(gc)
                self.step_decision(gc, step)

        print("\nIteration completed\n")

        for gc in self.growth_cones:
            # Fetch final positions
            print(gc)

        return Result(self.growth_cones, self.substrate)

    def step_decision(self, gc, step):
        """
        Make a decision for a growth cone to step or not based on potential and probabilities of its new position.

        :param gc: A Growth Cone instance.
        :param step: Current step in the simulation.
        """

        # Choose a new position
        xt_direction, yt_direction = self.gen_random_step()
        gc.new_position = clamp_to_boundaries(gc.position, self.substrate, gc.size, xt_direction, yt_direction)

        # Calculate new potential
        step_ratio = (step / self.num_steps) * 4  # TODO: clarify this step ratio by talking to Franco
        new_potential = calculate_potential(gc, self.growth_cones, self.substrate, step_ratio)

        # Calculate Step realization probabilities
        old_density = probabilistic_density(gc.potential, self.sigma)
        new_density = probabilistic_density(new_potential, self.sigma)

        # Step Decision
        random_number = random.random()
        probability = calculate_probability(old_density, new_density)

        # Trajectory Saving
        # TODO: Make configurable, maybe rename to Trace?
        if step % 50 == 0:
            gc.update_trajectory()

        if random_number > probability:
            # Take the step
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

        # Maintain the history length
        while len(gc.history) > self.history_length:
            gc.history.pop(0)  # Remove the oldest entry in the history
