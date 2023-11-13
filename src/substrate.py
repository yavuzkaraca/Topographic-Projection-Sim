"""
Module providing the Substrate class for substrate representation and initialization.
"""

import numpy as np
from visualization import visualize_substrate


class Substrate:
    def __init__(self, rows, cols, offset, substrate_type, min_value, max_value):
        """
        Initialize the Substrate object with the specified parameters.

        :param rows: Number of rows in the substrate grid.
        :param cols: Number of columns in the substrate grid.
        :param offset: Offset value used to calculate the substrate boundaries.
        :param substrate_type: Type of substrate initialization - continuous_gradients or wedges.
        :param min_value: Minimum value for substrate initialization.
        :param max_value: Maximum value for substrate initialization.
        """

        self.rows = rows + offset * 2
        self.cols = cols + offset * 2
        self.offset = offset
        self.substrate_type = substrate_type
        self.min_value = min_value
        self.max_value = max_value

        # Initialize the grid with 3D array to store ligand and receptor values
        self.ligands = np.zeros((self.rows, self.cols), dtype=float)
        self.receptors = np.zeros((self.rows, self.cols), dtype=float)

        self.initialize_substrate()  # Initialize substrate based on the initial configuration

    def initialize_substrate(self):
        """
        Initialize the substrate based on the specified substrate type.
        """

        substrate_type = self.substrate_type

        if substrate_type == "continuous_gradients":
            self.initialize_continuous_gradients()
        elif substrate_type == "wedges":
            self.initialize_wedges()
        else:
            raise ValueError("Invalid substrate type specified in the configuration dictionary.")

        visualize_substrate(self)

    def initialize_continuous_gradients(self):
        """
        Initialize the substrate using continuous gradients of ligand and receptor values.
        """

        # Calculate the ligand and receptor gradients
        ligand_gradient = np.linspace(0.01, 0.99, self.cols)
        receptor_gradient = np.linspace(0.99, 0.01, self.cols)

        for row in range(self.rows):
            # Set the ligand and receptor values in each cell based on the gradients
            self.ligands[row, :] = ligand_gradient
            self.receptors[row, :] = receptor_gradient

    def initialize_wedges(self):
        """
        Initialize the substrate using wedge-shaped patterns of ligand and receptor values.
        """

        # Set for readability
        rows, cols, = self.rows, self.cols
        min_edge_length = self.min_value
        max_edge_length = self.max_value
        receptors = np.zeros((rows, cols), dtype=float)
        ligands = np.ones((rows, cols), dtype=float)

        # Calculate the number of wedges that fit in the substrate along the x-axis
        num_wedges_x = rows // (max_edge_length + min_edge_length)

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
        """
        Return a string representation of the ligand and receptor grids in the substrate.
        """

        # Create a string representation of the substrate
        result = "Ligands:\n"
        result += str(self.ligands) + "\n\n"
        result += "Receptors:\n"
        result += str(self.receptors)
        return result
