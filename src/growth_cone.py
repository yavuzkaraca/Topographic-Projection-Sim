import random
import numpy as np
import config as cfg


def initialize_growth_cones(config):
    # Fetch parameters from config
    growth_cones = []
    gc_count = config.get(cfg.GC_COUNT)
    size = config.get(cfg.GC_SIZE)
    rows = config.get(cfg.ROWS)

    # Create an array of evenly distributed receptor and ligand values
    receptors = np.linspace(0.99, 0.01, gc_count)
    ligands = np.linspace(0.01, 0.99, gc_count)

    # Create an array of evenly distributed y-positions for the growth cones
    y_positions = np.linspace(0, rows - 1 - size, gc_count, dtype=int)

    for i in range(gc_count):
        # Create a GrowthCone instance and initialize it
        pos_y = y_positions[i]
        gc = GrowthCone((size, pos_y + size), size, receptors[i], ligands[i])
        growth_cones.append(gc)

    return growth_cones


class GrowthCone:
    def __init__(self, position, size, ligand, receptor):
        self.start_position = position
        self.position = position  # Center point of the circular modeled GC, as x,y
        # TODO: new position?
        self.size = size  # Radius of the circle
        self.ligand = ligand
        self.receptor = receptor
        self.potential = 0

    def __str__(self):
        return (f"Receptor: {self.receptor}, Ligand: {self.ligand}, Position: {self.position}, "
                f"Start Position: {self.start_position}, Potential: {self.potential}")
