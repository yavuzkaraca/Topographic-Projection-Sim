import numpy as np
import config as cfg


class Substrate:
    def __init__(self, config):
        self.rows = config.get(cfg.ROWS)
        self.cols = config.get(cfg.COLS)
        self.type = config.get(cfg.SUBSTRATE_TYPE)
        self.min_value = config.get(cfg.MIN_VALUE)
        self.max_value = config.get(cfg.MAX_VALUE)

        # Initialize the grid with 3D array to store ligand and receptor values
        self.ligands = np.zeros((self.rows, self.cols), dtype=float)
        self.receptors = np.zeros((self.rows, self.cols), dtype=float)

        self.initialize_substrate()  # Initialize substrate based on the initial configuration

    def initialize_substrate(self):
        substrate_type = self.type

        if substrate_type == "continuous_gradients":
            self.initialize_continuous_gradients()
        elif substrate_type == "wedges":
            self.initialize_wedges()
        else:
            raise ValueError("Invalid substrate type specified in the configuration dictionary.")

    def initialize_continuous_gradients(self):
        # Calculate the ligand and receptor gradients
        ligand_gradient = np.linspace(0.0, 1.0, self.cols)
        receptor_gradient = np.linspace(1.0, 0.0, self.cols)

        for row in range(self.rows):
            # Set the ligand and receptor values in each cell based on the gradients
            self.ligands[row, :] = ligand_gradient
            self.receptors[row, :] = receptor_gradient

    def initialize_wedges(self):

        # Set for readability
        rows, cols, = self.ligands.shape
        min_edge_length = self.min_value
        max_edge_length = self.max_value
        receptors = np.zeros((rows, cols), dtype=float)
        ligands = np.ones((rows, cols), dtype=float)

        # Calculate the number of wedges that fit in the substrate along the x-axis
        num_wedges_x = cols // (max_edge_length + min_edge_length + 2)

        # Slope of upper and lower triangle hypotenuse
        ratio = (cols / max_edge_length) * 2

        # TODO: Fit extra cones to bottom, test ligands and receptors separately!
        for n in range(num_wedges_x):

            # Make upper triangle
            start_row_upperhalf = n * (max_edge_length + min_edge_length) + 1  # Adjust the start_row calculation
            end_row_upperhalf = start_row_upperhalf + (max_edge_length // 2)  # Adjust the end_row calculation
            for i in range(start_row_upperhalf, end_row_upperhalf):
                fill_until = int((i - start_row_upperhalf + 1) * ratio)
                receptors[i, :fill_until] = 1.0  # Adjust the slicing to fill only up to 'fill_until'
                ligands[i, :fill_until] = 0.0

            # Make the rectangle in the middle
            if min_edge_length > 1:
                for i in range(end_row_upperhalf, end_row_upperhalf + min_edge_length - 1):
                    receptors[i, :] = 1.0
                    ligands[i, :] = 0.0
                end_row_upperhalf += min_edge_length - 1

            # Make lower triangle
            start_row_lowerhalf = end_row_upperhalf - 1
            end_row_lowerhalf = start_row_lowerhalf + (max_edge_length // 2)
            for i in range(start_row_lowerhalf, end_row_lowerhalf + 1):
                fill_until = int((end_row_lowerhalf - i + 1) * ratio)
                receptors[i, :fill_until] = 1.0  # Adjust the slicing to fill only up to 'fill_until'
                ligands[i, :fill_until] = 0.0

        self.receptors, self.ligands = receptors, ligands

    def __str__(self):
        # Create a string representation of the substrate
        result = "Ligands:\n"
        result += str(self.ligands) + "\n\n"
        result += "Receptors:\n"
        result += str(self.receptors)
        return result
