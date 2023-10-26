from result import Result
from potential_calculation import calculate_potential_at
from growth_cone import initialize_growth_cones
from substrate import Substrate
import config as cfg
import random


def clamp_to_boundaries(position, substrate, xt_direction, yt_direction):
    new_x = position[0] + xt_direction
    new_y = position[1] + yt_direction

    # Clamp the new positions to stay within the substrate boundaries
    new_x = max(0, min(new_x, substrate.cols - 1))
    new_y = max(0, min(new_y, substrate.rows - 1))

    return new_x, new_y


def calculate_probability(old_potential, new_potential):
    if old_potential + new_potential == 0:
        probability = 0.5
    else:
        probability = old_potential / (old_potential + new_potential)
    return probability


class Simulation:
    def __init__(self, config):
        self.substrate = Substrate(config)
        self.growth_cones = initialize_growth_cones(config)
        self.adaptation = config.get(cfg.ADAPTATION)
        self.step_size = config.get(cfg.STEP_SIZE)
        self.num_steps = config.get(cfg.STEP_AMOUNT)
        self.x_step_probability = config.get(cfg.X_STEP_POSSIBILITY)
        self.y_step_probability = config.get(cfg.Y_STEP_POSSIBILITY)
        self.sigma = config.get(cfg.SIGMA)

    def run(self):
        final_positions = []
        for gc in self.growth_cones:
            # potential initialization
            gc.potential = calculate_potential_at(gc, self.growth_cones, self.substrate, 0)

        for step in range(self.num_steps):
            # Update growth cones
            for gc in self.growth_cones:
                self.step_decision(gc, step)
                # print(gc.__str__(), step)

        for gc in self.growth_cones:
            # Fetch final positions
            final_positions.append(gc.position)

        return Result(final_positions, self.substrate)

    def reset_run(self):
        self.growth_cones = initialize_growth_cones(cfg.config)

    def step_decision(self, gc, step):
        # TODO: check if matlab does it this way too, maybe split

        # Randomly step in xt and yt directions -1, 0, +1
        xt_direction = random.choices([-1, 0, 1],
                                      weights=[(1 - self.x_step_probability) / 3, 1 / 3, self.x_step_probability / 3])[
            0]
        yt_direction = random.choices([-1, 0, 1],
                                      weights=[(1 - self.y_step_probability) / 3, 1 / 3, self.y_step_probability / 3])[
            0]

        xt_direction, yt_direction = xt_direction * self.step_size, yt_direction * self.step_size

        old_position = gc.position
        old_potential = gc.potential

        # Calculate new potential
        new_position = clamp_to_boundaries(gc.position, self.substrate, xt_direction, yt_direction)
        gc.position = new_position
        new_potential = calculate_potential_at(gc, self.growth_cones, self.substrate, step)

        # Step realization probability
        random_number = random.random()
        # TODO: sigma?
        probability = calculate_probability(gc.potential, new_potential)

        if random_number > probability:
            # TODO: seperate decision logic from moving and implement calculation at given position
            gc.potential = new_potential
        else:
            gc.position = old_position
