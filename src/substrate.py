import numpy as np


class Substrate:
    def __init__(self, rows, cols, config_dict=None):
        self.rows = rows
        self.cols = cols
        # Initialize the grid with numeric values of ligands and receptors
        self.grid = np.zeros((rows, cols), dtype=float)
        self.config_dict = config_dict or {}  # Use the provided configuration dictionary or an empty dictionary
        self.initialize_substrate()  # Initialize substrate based on the initial configuration

    def initialize_substrate(self):
        substrate_type = self.config_dict.get("substrate_type")

        if substrate_type == "continuous_gradients":
            self.initialize_continuous_gradients()
        elif substrate_type == "wedges":
            self.initialize_wedges()
        else:
            raise ValueError("Invalid substrate type specified in the configuration dictionary.")

    def initialize_continuous_gradients(self, config_dict):

        # TODO: fix this

        # Extract configuration parameters
        min_value = config_dict.get("min_value")
        max_value = config_dict.get("max_value")

        # Generate continuous gradients in the substrate using NumPy
        gradient_range = max_value - min_value
        self.grid = np.random.uniform(min_value, max_value, size=(self.rows, self.cols))

        # test
        # Generate continuous gradients in the substrate using NumPy
        min_value = 1
        max_value = 20.3
        gradient_range = max_value - min_value
        grid = np.random.uniform(min_value, max_value, size=(10, 10))

    def initialize_wedges(self, config_dict):

        # TODO: fix this

        # Extract configuration parameters
        min_edge_length = config_dict.get("min_edge_length")
        max_edge_length = config_dict.get("max_edge_length")

        # Calculate the number of wedges that fit in the substrate
        num_wedges_x = self.cols // max_edge_length
        num_wedges_y = self.rows // max_edge_length

        # Initialize the substrate with wedges
        for i in range(num_wedges_x):
            for j in range(num_wedges_y):
                x_start = i * max_edge_length
                x_end = (i + 1) * max_edge_length
                y_start = j * max_edge_length
                y_end = (j + 1) * max_edge_length

                # Set wedges to 1.0 directly in the grid (no need for Cell objects)
                self.grid[y_start:y_end, x_start:x_end] = 1.0
