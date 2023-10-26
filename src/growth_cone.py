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
    receptors = np.linspace(1.0, 0.0, gc_count)
    ligands = np.linspace(0.0, 1.0, gc_count)

    # Create an array of evenly distributed x-positions for the growth cones
    y_positions = np.linspace(0, rows - 1, gc_count, dtype=int)

    for i in range(gc_count):
        # Create a GrowthCone instance and initialize it
        pos_y = y_positions[i]
        gc = GrowthCone((0, pos_y), size, receptors[i], ligands[i])
        growth_cones.append(gc)

    return growth_cones


class GrowthCone:
    def __init__(self, position, size=10, ligand=1.0, receptor=1.0):
        self.position = position  # Center point of the circular modeled GC, as x,y
        self.size = size  # Radius of the circle
        self.ligand = ligand
        self.receptor = receptor
        self.potential = 0

    def __str__(self):
        return f"Receptor: {self.receptor}, Ligand: {self.ligand}, Position: {self.position}, Potential: {self.potential}"
