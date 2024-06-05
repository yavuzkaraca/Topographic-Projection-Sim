"""
Module for conducting a model.
"""
import time
from model.result import Result
from model.simulation.potential_calculation import calculate_potential, calculate_ff_coef
import random
from model.simulation.step_decision import clamp_to_boundaries, probabilistic_density, calculate_probability


class Simulation:
    """
    Class managing the model process for growth cones.

    Attributes:
        substrate: Substrate object representing the model area.
        growth_cones: List of Growth Cone instances.
        adaptation: Boolean indicating adaptation feature.
        step_size: Size of step movement for growth cones.
        steps_total: Total number of steps for the model.
        x_step_p: Probability of a growth cone stepping in the x-direction.
        y_step_p: Probability of a growth cone stepping in the y-direction.
        sigma: Standard deviation for the potential calculation.

    Methods:
        run(): Runs the model and gathers final growth cone positions.
        step_decision(gc, step): Makes a decision for a growth cone to step or not.
        gen_random_step(): Generates a random step in the x and y directions.
    """

    def __init__(self, substrate, growth_cones, adaptation, step_size, num_steps, x_step_p, y_step_p, sigmoid_gain,
                 sigmoid_shift, sigma, force, forward_sig, reverse_sig, ff_inter, ft_inter, mu, lambda_,
                 history_length):
        """
        Initialize the Simulation class with necessary parameters.

        :param substrate: Substrate object defining the model area.
        :param growth_cones: List of Growth Cone instances participating in the model.
        :param adaptation: Boolean value indicating whether adaptation is enabled or not.
        :param step_size: Size of the step movement for the growth cones.
        :param num_steps: Total number of steps for the model.
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

    def run(self):
        """
        Execute the model for the defined number of steps using multi-threading.
        """
        start_time = time.time()  # Start timing the model

        self.prepare_gcs()
        print(f"\nInitialization completed.")

        print(f"\nIteration starts, {self.steps_total} many steps will be taken\n")
        self.iterate_simulation()

        end_time = time.time()  # End timing the model
        total_time = end_time - start_time
        print(f"\nIteration completed in {total_time:.2f} seconds\n")

        for gc in self.growth_cones:
            print(gc)

        return Result(self.growth_cones, self.substrate)

    def prepare_gcs(self):
        for gc in self.growth_cones:
            # Potential initialization
            gc.potential = calculate_potential(gc, self.growth_cones, self.substrate, 0)

    def iterate_simulation(self):
        for step_current in range(self.steps_total):
            if step_current % 250 == 0:
                print(f"Current Step: {step_current}")

            for gc in self.growth_cones:
                if self.adaptation:
                    self.adapt_growth_cone(gc)
                if not gc.marked:
                    self.step_decision(gc, calculate_ff_coef(step_current, self.steps_total, self.sigmoid_gain,
                                                             self.sigmoid_shift))

    def adapt_growth_cone(self, gc):
        """
        Adapt the growth cone properties based on the model's adaptation configuration.

        :param gc: A Growth Cone instance.
        """
        gc.calculate_adaptation(self.mu, self.lambda_, self.history_length)
        gc.apply_adaptation()

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
