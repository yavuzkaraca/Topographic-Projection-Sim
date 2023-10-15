import random

from src import growth_cone


def clamp_to_boundaries(growth_cone, substrate, xt_direction, yt_direction):
    new_x = growth_cone.position[0] + xt_direction
    new_y = growth_cone.position[1] + yt_direction

    # Clamp the new positions to stay within the substrate boundaries
    new_x = max(0, min(new_x, substrate.cols - 1))
    new_y = max(0, min(new_y, substrate.rows - 1))

    return new_x, new_y


def step_decision(growth_cone, substrate):
    # Step probabilities
    x_step_probability = 0.2
    y_step_probability = 0.3

    # TODO: check if matlab does it this way too.
    # Randomly step in xt and yt directions -1, 0, +1
    xt_direction = \
    random.choices([-1, 0, 1], weights=[(1 - x_step_probability) / 3, 1 / 3, x_step_probability / 3])[0]
    yt_direction = \
    random.choices([-1, 0, 1], weights=[(1 - y_step_probability) / 3, 1 / 3, y_step_probability / 3])[0]

    # TODO: step size
    # Calculate new potential
    new_position = clamp_to_boundaries(growth_cone, substrate, xt_direction, yt_direction)
    new_potential = calculate_potential_at(growth_cone, substrate, new_position)

    # Step realization probability
    random_number = random.random()
    probability = calculate_probability(growth_cone.potential, new_potential)

    if random_number > probability:
        growth_cone.potential = new_potential
        growth_cone.position = new_position


def calculate_probability(old_potential, new_potential):
    if old_potential + new_potential == 0:
        probability = 0.5
    else:
        probability = old_potential / (old_potential + new_potential)
    return probability


def calculate_potential_at(growth_cone, substrate, position, options):
    pass

def calculate_forward_potential(growth_cone, substrate):
    pass

def calculate_reverse_potential(growth_cone, substrate):
    pass

def calculate_ff_interaction(growth_cone, substrate):
    pass


class Simulation:
    def __init__(self, substrate, growth_cones, num_steps, config_dict):
        self.substrate = substrate
        self.growth_cones = self.initialize_growth_cones()
        self.num_steps = num_steps
        self.step_size = config_dict.get("step_size")
        self.config_dict = config_dict  # Pass the configuration dictionary to the simulation

    def run(self):
        for step in range(self.num_steps):
            # Update growth cones
            for cone in self.growth_cones:
                step_decision(cone,self.substrate)

    def initialize_growth_cones(self):
        # TODO: position and signal protein configuration
        growth_cones = []
        gc_count = self.config_dict.get("gc_count")
        for gc_id in range(gc_count):
            # Create a GrowthCone instance and initialize it
            gc = growth_cone.GrowthCone((gc_id, 0), self.config_dict)
            growth_cones.append(gc)
        return growth_cones
