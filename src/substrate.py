"""
Module providing the Substrate class for substrate representation and initialization.
"""

import numpy as np


class BaseSubstrate:
    def __init__(self, rows, cols, offset, min_value, max_value):
        """
        Initialize the base Substrate object with common parameters.

        :param rows: Number of rows in the substrate grid.
        :param cols: Number of columns in the substrate grid.
        :param offset: Offset value used to calculate the substrate boundaries.
        :param min_value: Minimum value for substrate initialization.
        :param max_value: Maximum value for substrate initialization.
        """

        self.rows = rows + offset * 2
        self.cols = cols + offset * 2
        self.offset = offset
        self.min_value = min_value
        self.max_value = max_value

        self.ligands = np.zeros((self.rows, self.cols), dtype=float)
        self.receptors = np.zeros((self.rows, self.cols), dtype=float)

    def initialize_substrate(self):
        """
        Abstract method to initialize the substrate.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses should implement this method.")

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


class ContinuousGradientSubstrate(BaseSubstrate):
    def initialize_substrate(self):
        """
        Initialize the substrate using continuous gradients of ligand and receptor values.
        """
        ligand_gradient = np.linspace(0.01, 0.99, self.cols)
        receptor_gradient = np.linspace(0.99, 0.01, self.cols)

        for row in range(self.rows):
            self.ligands[row, :] = ligand_gradient
            self.receptors[row, :] = receptor_gradient


class WedgeSubstrate(BaseSubstrate):
    def initialize_substrate(self):
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


class StripeFwdSubstrate(BaseSubstrate):
    # TODO: refactor all stripe substrates
    def initialize_substrate(self):
        """
        Initialize the substrate with alternating stripes of ligands and receptors.
        Each stripe is 'self.max_value' rows thick.
        """
        for row in range(self.rows):
            self.receptors[row, :] = np.zeros(self.cols)
            if (row // self.max_value) % 2 == 0:
                # Even stripe: Set ligands and clear receptors
                self.ligands[row, :] = np.ones(self.cols)

            else:
                # Odd stripe: Clear ligands and set receptors
                self.ligands[row, :] = np.zeros(self.cols)


class StripeRewSubstrate(BaseSubstrate):
    def initialize_substrate(self):
        """
        Initialize the substrate with alternating stripes of ligands and receptors.
        Each stripe is 'self.max_value' rows thick.
        """
        for row in range(self.rows):
            self.ligands[row, :] = np.zeros(self.cols)
            if (row // self.max_value) % 2 == 0:
                # Even stripe: Set ligands and clear receptors
                self.receptors[row, :] = np.zeros(self.cols)
            else:
                # Odd stripe: Clear ligands and set receptors
                self.receptors[row, :] = np.ones(self.cols)


class StripeDuoSubstrate(BaseSubstrate):
    def initialize_substrate(self):
        """
        Initialize the substrate with alternating stripes of ligands and receptors.
        Each stripe is 'self.max_value' rows thick.
        """
        for row in range(self.rows):
            if (row // self.max_value) % 2 == 0:
                # Even stripe: Set ligands and clear receptors
                self.ligands[row, :] = np.ones(self.cols)
                self.receptors[row, :] = np.zeros(self.cols)
            else:
                # Odd stripe: Clear ligands and set receptors
                self.ligands[row, :] = np.zeros(self.cols)
                self.receptors[row, :] = np.ones(self.cols)


class GapSubstrate(BaseSubstrate):
    def initialize_substrate(self):
        """
        Initialize the substrate with three different sections, each taking up a third of the total rows.
        The first third is filled with ligands, the second third is empty, and the third is filled with receptors.
        """
        first_part = int(self.cols * self.min_value)  # last column of the first part
        second_part = first_part + int(self.cols * self.max_value)  # last column of the second part

        # TODO: make configurable from outside
        start_red = False
        end_red = False

        # First third: Filled with sensors
        for col in range(first_part):
            if start_red:
                self.set_ligand(col)
            else:
                self.set_receptor(col)

        # Second third: Empty
        for col in range(first_part, second_part):
            self.ligands[:, col] = np.zeros(self.rows)
            self.receptors[:, col] = np.zeros(self.rows)

        # Final third: Filled with sensors
        for col in range(second_part, self.cols):
            if end_red:
                self.set_ligand(col)
            else:
                self.set_receptor(col)

    def set_ligand(self, col):
        self.ligands[:, col] = np.ones(self.rows)
        self.receptors[:, col] = np.zeros(self.rows)

    def set_receptor(self, col):
        self.ligands[:, col] = np.zeros(self.rows)
        self.receptors[:, col] = np.ones(self.rows)
