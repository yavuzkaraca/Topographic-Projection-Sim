import numpy as np


class Substrate:
    def __init__(self, rows, cols, config_dict=None):
        self.rows = rows
        self.cols = cols
        self.config_dict = config_dict or {}  # Use the provided configuration dictionary or an empty dictionary

        # Initialize the grid with 3D array to store ligand and receptor values
        self.grid = np.zeros((rows, cols, 2), dtype=float)
        self.initialize_substrate()  # Initialize substrate based on the initial configuration

    def set_ligand(self, x, y, value):
        self.grid[y][x][0] = value

    def set_receptor(self, x, y, value):
        self.grid[y][x][1] = value

    def get_ligand(self, x, y):
        return self.grid[y][x][0]

    def get_receptor(self, x, y):
        return self.grid[y][x][1]

    def initialize_substrate(self):
        substrate_type = self.config_dict.get("substrate_type")

        if substrate_type == "continuous_gradients":
            self.initialize_continuous_gradients()
        elif substrate_type == "wedges":
            self.initialize_wedges()
        else:
            raise ValueError("Invalid substrate type specified in the configuration dictionary.")

    def initialize_continuous_gradients(self):
        rows, cols, _ = self.grid.shape
        min_value = 0.0
        max_value = 1.0  # Adjust these values according to your requirements

        # Calculate the ligand and receptor gradients
        ligand_gradient = np.linspace(1.0, 0.0, cols)
        receptor_gradient = np.linspace(0.0, 1.0, cols)

        for row in range(rows):
            # Set the ligand and receptor values in each cell based on the gradients
            self.grid[row, :, 0] = min_value + ligand_gradient * (max_value - min_value)
            self.grid[row, :, 1] = min_value + receptor_gradient * (max_value - min_value)

    def initialize_wedges(self):

        # TODO: fix this

        # Extract configuration parameters
        min_edge_length = self.config_dict.get("min_edge_length")
        max_edge_length = self.config_dict.get("max_edge_length")

        # Calculate the number of wedges that fit in the substrate along the x-axis
        num_wedges_x = self.cols // max_edge_length

        # Initialize the substrate with wedges
        for i in range(num_wedges_x):
            x_start = i * max_edge_length
            x_end = (i + 1) * max_edge_length

            # Create Cell objects with ligand and receptor values and set them in the grid
            ligament = 1.0
            receptor = 1.0
            for y in range(self.rows):
                for x in range(x_start, x_end):
                    self.set_ligand(x, y, 1.0 - ligament)
                    self.set_receptor(x, y, receptor)

            # Adjust ligand and receptor values for the next wedge
            ligament = 1.0 - ligament
            receptor = 1.0 - receptor

    def __str__(self):
        # Customize the string representation of the Substrate
        result = ""
        for y in range(self.rows):
            row_str = ""
            for x in range(self.cols):
                ligand = self.get_ligand(x, y)
                receptor = self.get_receptor(x, y)
                row_str += f"({ligand},{receptor}) "
            result += row_str + "\n"
        return result
