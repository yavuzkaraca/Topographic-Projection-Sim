"""
Main module which executes simulation logic
"""
import math
import time
from model.result import Result
from model.potential_calculation import calculate_potential
import random

progress = 0  # Global progress variable


def get_updated_progress():
    # print(progress)
    return progress


class Simulation:
    """
    Manages the simulation of growth cone dynamics within a defined substrate.

    Attributes:
        substrate (object): The environmental context in which growth cones grow.
        growth_cones (list): A collection of all active growth cone instances participating in the simulation.
        adaptation (bool): Flag to determine whether growth cones adapt.
        step_size (int): The magnitude of each movement step taken by the growth cones.
        num_steps (int): The number of steps each growth cone will attempt to complete in the simulation.
        x_step_p (float): The probability of a step generated in the positive x-direction.
        y_step_p (float): The probability of a step generated in the positive y-direction.
        sigma (float): The standard deviation parameter used in potential calculations.
        sigmoid_steepness (float): Controls the sharpness of the sigmoid function in ff_coef calculation.
        sigmoid_shift (float): Modifies the midpoint of the sigmoid function in ff_coef calculation.
        force (bool): Flag to toggle forcing growth cones to move regardless of step probabilities.
        forward_sig (bool): Flag to toggle forward signals in potential calculation.
        reverse_sig (bool): Flag to toggle reverse signals in potential aging calculation.
        ff_inter (bool): Flag to toggle fiber-fiber interactions in potential calculation.
        ft_inter (bool): Flag to toggle fiber-target interactions in potential calculation.
        mu (float): Adjusting parameter for the adaptation coefficient.
        lambda_ (float): Adjusting parameter for the resetting force.
        history_length (int): The number of historical steps to consider for adaptation.
    """

    def __init__(self, config, substrate, growth_cones, adaptation, step_size, num_steps, x_step_p, y_step_p, sigmoid_steepness,
                 sigmoid_shift, sigmoid_height, sigma, force, forward_sig, reverse_sig, ff_inter, ft_inter,cis_inter, mu, lambda_,
                 history_length):
        self.config = config
        self.forward_sig = forward_sig
        self.reverse_sig = reverse_sig
        self.ff_inter = ff_inter
        self.ft_inter = ft_inter
        self.cis_inter = cis_inter
        self.substrate = substrate
        self.growth_cones = growth_cones
        self.adaptation = adaptation
        self.step_size = step_size
        self.num_steps = num_steps
        self.x_step_p = x_step_p
        self.y_step_p = y_step_p
        self.sigmoid_steepness = sigmoid_steepness
        self.sigmoid_shift = sigmoid_shift
        self.sigmoid_height = sigmoid_height
        self.sigma = sigma
        self.force = force
        self.mu = mu
        self.lambda_ = lambda_
        self.history_length = history_length

    def run(self):
        """
        Manages the full execution of the simulation, timing the process and orchestrating the setup,
        iteration, and completion steps.
        """
        start_time = time.time()  # Start timing the model

        self.prepare_gcs()
        self.iterate_simulation()

        end_time = time.time()
        total_time = end_time - start_time

        return Result(self, total_time, self.config)

    def prepare_gcs(self):
        """
        Initializes the potential values for each growth cone.
        """
        for gc in self.growth_cones:
            # Potential initialization
            gc.potential = calculate_potential(gc, gc.pos, self.growth_cones, self.substrate, self.forward_sig,
                                               self.reverse_sig, self.ff_inter, self.ft_inter, self.cis_inter, 0,
                                               self.num_steps, self.sigmoid_steepness, self.sigmoid_shift, self.sigmoid_height)

    def iterate_simulation(self):
        """
        Iteratively processes each simulation step, generating random steps, and making stepping decisions.
        """
        global progress

        for step_current in range(self.num_steps):
            if step_current % 250 == 0:
                progress = int((step_current / self.num_steps) * 100)

            for gc in self.growth_cones:
                if not gc.freeze:  # Check if the growth cone is not frozen
                    if self.adaptation:
                        self.adapt_growth_cone(gc)
                    pos_new = self.gen_random_step(gc)

                    # do NOT recalculate the current potential for reduced time-complexity

                    potential_new = calculate_potential(gc, pos_new, self.growth_cones, self.substrate,
                                                        self.forward_sig, self.reverse_sig, self.ff_inter,
                                                        self.ft_inter, self.cis_inter, step_current, self.num_steps,
                                                        self.sigmoid_steepness, self.sigmoid_shift, self.sigmoid_height)
                    self.step_decision(gc, pos_new, potential_new)

        progress = 100
        # TODO: @Performance Early stopping mechanism based on total potential

    def adapt_growth_cone(self, gc):
        """
        Adapt the growth cones. Check parameter_exploration experiment for more details on the parameters.
        """
        gc.calculate_adaptation(self.mu, self.lambda_, self.history_length)
        gc.apply_adaptation()

    def step_decision(self, gc, pos_new, potential_new):
        """
        Decides whether the growth cone should step in the new position proposal based on its guidance potential
        """
        if self.force:
            # Force gc to take the random generated step, neglecting ques from guidance potential
            gc.take_step(pos_new, potential_new)
            return

        # Calculate Step realization probabilities
        old_density = probabilistic_density(gc.potential, self.sigma)
        new_density = probabilistic_density(potential_new, self.sigma)
        probability = calculate_step_probability(old_density, new_density)

        # Step Decision
        random_number = random.random()
        if random_number > probability:
            gc.take_step(pos_new, potential_new)

    def gen_random_step(self, gc):
        """
        Generates a random step for the growth cone based on predefined probabilities.
        """

        # Initialization
        x_prob = self.x_step_p
        y_prob = self.y_step_p

        # Randomly step in xt and yt directions -1, 0, +1
        xt_direction = random.choices([-1, 0, 1], weights=[(1 - x_prob), (1 - x_prob), x_prob])[0]
        yt_direction = random.choices([-1, 0, 1], weights=[y_prob, (1 - y_prob), y_prob])[0]

        xt_direction *= self.step_size
        yt_direction *= self.step_size

        return clamp_to_boundaries(gc.pos, self.substrate, gc.radius, xt_direction, yt_direction)


"""
Utility functions needed for step decision
"""


def clamp_to_boundaries(position, substrate, size, xt_direction, yt_direction):
    """
    Ensures that the position of the growth cone remains within the boundaries defined by the substrate after moving.
    """
    new_x = position[0] + xt_direction
    new_y = position[1] + yt_direction

    # Adjust the new position to prevent the growth cone from crossing the substrate boundaries
    new_x_clamped = max(size, min(new_x, substrate.cols - 1 - size))
    new_y_clamped = max(size, min(new_y, substrate.rows - 1 - size))

    return new_x_clamped, new_y_clamped


def probabilistic_density(potential, sigma):
    return math.exp(-potential**2 / (sigma**2))  # simplified version
    # return math.exp(-potential ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma)


def calculate_step_probability(old_prob, new_prob):
    if old_prob + new_prob == 0:
        probability = 0.5  # Both possibilities are zero = GC is far off from optimal location
    else:
        probability = old_prob / (old_prob + new_prob)
    return probability
