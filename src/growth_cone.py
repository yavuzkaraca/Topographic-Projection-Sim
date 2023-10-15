import numpy as np


class GrowthCone:
    def __init__(self, position, config_dict):
        self.position = position  # Center point of the circular modeled GC, as x,y
        self.size = config_dict.get("gc_size")  # Radius of the circle

        # Protein Grid Initialization
        self.ligand = 0
        self.receptor = 0
        self.sigma_ligand = 3.0  # Adjust this value as needed for the x direction
        self.sigma_receptor = 2.0  # Adjust this value as needed for the y direction
        self.ligand_signals, self.receptor_signals = self.initialize_protein_grid()

        self.potential = 0

    # TODO: save this implementation to git

    '''
    def bounding_box(self):
        # Calculate the bounds of the bounding box
        x_min = max(0, int(self.position[0] - self.size))
        x_max = min(self.substrate.cols - 1, int(self.position[0] + self.size))
        y_min = max(0, int(self.position[1] - self.size))
        y_max = min(self.substrate.rows - 1, int(self.position[1] + self.size))

        return x_min, x_max, y_min, y_max

    def gaussian_weight(self, x, y, sigma_factor):
        # Calculate the Gaussian weight based on distance from the growth cone center.
        distance = np.sqrt(np.sum((self.position - np.array([x, y])) ** 2))
        sigma = self.size / sigma_factor  # Adjust sigma for desired influence range
        return np.exp(-(distance ** 2) / (2 * sigma ** 2))


    def initialize_protein_grid(self):
        x_min, x_max, y_min, y_max = self.bounding_box()
        x_range = np.arange(x_min, x_max + 1)
        y_range = np.arange(y_min, y_max + 1)

        xx, yy = np.meshgrid(x_range, y_range)
        weights_ligand = self.gaussian_weight(xx, yy, self.sigma_ligand)
        weights_receptor = self.gaussian_weight(xx, yy, self.sigma_receptor)

        ligand_signals = self.ligand * weights_ligand
        receptor_signals = self.receptor * weights_receptor

        return ligand_signals, receptor_signals
    
    '''
