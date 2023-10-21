import numpy as np


class Substrate:
    def __init__(self, rows, cols, config_dict=None):
        self.rows = rows
        self.cols = cols
        self.type = "continuous_gradients"
        self.config_dict = config_dict or {}  # Use the provided configuration dictionary or an empty dictionary

        # Initialize the grid with 3D array to store ligand and receptor values
        self.ligands = np.zeros((rows, cols), dtype=float)
        self.receptors = np.zeros((rows, cols), dtype=float)

        self.initialize_substrate()  # Initialize substrate based on the initial configuration

    def initialize_substrate(self):
        # substrate_type = self.config_dict.get("substrate_type")
        substrate_type = self.type

        if substrate_type == "continuous_gradients":
            self.initialize_continuous_gradients()
        elif substrate_type == "wedges":
            self.initialize_wedges()
        else:
            raise ValueError("Invalid substrate type specified in the configuration dictionary.")

    def initialize_continuous_gradients(self):
        rows, cols = self.ligands.shape
        # Calculate the ligand and receptor gradients
        ligand_gradient = np.linspace(0.0, 1.0, self.cols)
        receptor_gradient = np.linspace(1.0, 0.0, self.cols)

        for row in range(self.rows):
            # Set the ligand and receptor values in each cell based on the gradients
            self.ligands[row, :] = ligand_gradient
            self.receptors[row, :] = receptor_gradient

    def initialize_wedges(self):
        rows, cols, = self.ligands.shape
        # Extract configuration parameters
        """
        min_edge_length = self.config_dict.get("min_edge_length")
        max_edge_length = self.config_dict.get("max_edge_length")
        """
        min_edge_length = 30
        max_edge_length = 80
        ratio = (cols / max_edge_length) * 2

        # Calculate the number of wedges that fit in the substrate along the x-axis
        num_wedges_x = self.cols // (max_edge_length + min_edge_length + 2)

        self.ligands = np.ones((rows, cols), dtype=float)
        self.receptors = np.zeros((rows, cols), dtype=float)

        # TODO: Fit extra cones to bottom, test ligands and receptors seperately!
        for n in range(num_wedges_x):

            # Make upper triangle
            start_row_upperhalf = n * (max_edge_length + min_edge_length) + 1  # Adjust the start_row calculation
            end_row_upperhalf = start_row_upperhalf + (max_edge_length // 2)  # Adjust the end_row calculation
            for i in range(start_row_upperhalf, end_row_upperhalf):
                fill_until = int((i - start_row_upperhalf + 1) * ratio)
                self.receptors[i, :fill_until] = 1.0  # Adjust the slicing to fill only up to 'fill_until'
                self.ligands[i, :fill_until] = 0.0

            # Make the rectangle in the middle
            if min_edge_length > 1:
                for i in range(end_row_upperhalf, end_row_upperhalf + min_edge_length - 1):
                    self.receptors[i, :] = 1.0
                    self.ligands[i, :] = 0.0
                end_row_upperhalf += min_edge_length - 1

            # Make lower triangle
            start_row_lowerhalf = end_row_upperhalf - 1
            end_row_lowerhalf = start_row_lowerhalf + (max_edge_length // 2)
            for i in range(start_row_lowerhalf, end_row_lowerhalf + 1):
                fill_until = int((end_row_lowerhalf - i + 1) * ratio)
                self.receptors[i, :fill_until] = 1.0  # Adjust the slicing to fill only up to 'fill_until'
                self.ligands[i, :fill_until] = 0.0

    def __str__(self):
        # Create a string representation of the substrate
        result = "Ligands:\n"
        result += str(self.ligands) + "\n\n"
        result += "Receptors:\n"
        result += str(self.receptors)
        return result
