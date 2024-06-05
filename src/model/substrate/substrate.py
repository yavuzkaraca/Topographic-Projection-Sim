"""
Module providing the Substrate class for substrate representation and initialization.
"""

import numpy as np


class BaseSubstrate:
    def __init__(self, rows, cols, offset, custom_first, custom_second):
        """
        Initialize the base Substrate object with common parameters.

        :param rows: Number of rows in the substrate grid.
        :param cols: Number of columns in the substrate grid.
        :param offset: Offset value used to calculate the substrate boundaries.

        :param custom_first: Has different roles based on the substrate type
        WEDGE: small edge length ; STRIPE: - ; GAP: last column of first part

        :param custom_second: Has different roles based on the substrate type
        WEDGE: big edge length ; STRIPE: stripe width ; GAP: first column of last part
        """
        self.rows = rows + offset * 2
        self.cols = cols + offset * 2
        self.offset = offset  # is equal to gc_size
        self.custom_first = custom_first  # min_value
        self.custom_second = custom_second  # max_value

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

    def set_col_ligand_only(self, col):
        self.ligands[:, col] = np.ones(self.rows)
        self.receptors[:, col] = np.zeros(self.rows)

    def set_col_receptor_only(self, col):
        self.ligands[:, col] = np.zeros(self.rows)
        self.receptors[:, col] = np.ones(self.rows)

    def set_col_empty(self, col):
        self.ligands[:, col] = np.zeros(self.rows)
        self.receptors[:, col] = np.zeros(self.rows)

    def set_row_ligand_only(self, row):
        self.ligands[row, :] = np.ones(self.cols)
        self.receptors[row, :] = np.zeros(self.cols)

    def set_row_receptor_only(self, row):
        self.ligands[row, :] = np.zeros(self.cols)
        self.receptors[row, :] = np.ones(self.cols)

    def set_row_empty(self, row):
        self.ligands[row, :] = np.zeros(self.cols)
        self.receptors[row, :] = np.zeros(self.cols)


class ContinuousGradientSubstrate(BaseSubstrate):
    def initialize_substrate(self):
        """
        Initialize the substrate using continuous gradients of ligand and receptor values.
        """
        ligand_gradient = np.linspace(0.01, 0.99, self.cols - (2 * self.offset))
        receptor_gradient = np.linspace(0.99, 0.01, self.cols - (2 * self.offset))

        # Append 0.01 and 0.99 on both ends
        low_end = np.full(self.offset, 0.01)  # Creates an array of 0.01 with length self.offset
        high_end = np.full(self.offset, 0.99)  # Creates an array of 0.99 with length self.offset
        ligand_gradient = np.concatenate([low_end, ligand_gradient, high_end])
        receptor_gradient = np.concatenate([high_end, receptor_gradient, low_end])

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
        min_edge_length = self.custom_first
        max_edge_length = self.custom_second
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


class BaseStripeSubstrate(BaseSubstrate):
    def initialize_substrate(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def initialize_stripe(self, forward, reverse):
        for row in range(self.rows):
            if (row // self.custom_second) % 2 == 0:
                # Even stripe: Set ligands and clear receptors
                if forward:
                    self.set_col_ligand_only(row)
            else:
                # Odd stripe: Clear ligands and set receptors
                if reverse:
                    self.set_row_receptor_only(row)


class StripeFwdSubstrate(BaseStripeSubstrate):
    def initialize_substrate(self):
        self.initialize_stripe(True, True)


class StripeRewSubstrate(BaseStripeSubstrate):
    def initialize_substrate(self):
        self.initialize_stripe(False, True)


class StripeDuoSubstrate(BaseStripeSubstrate):
    def initialize_substrate(self):
        self.initialize_stripe(True, True)


class BaseGapSubstrate(BaseSubstrate):
    @property
    def parts(self):
        first_part = int(self.cols * self.custom_first)  # last column of the first part
        second_part = first_part + int(self.cols * self.custom_second)  # last column of the second part
        return first_part, second_part

    def initialize_substrate(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def initialize_gap(self, start_red, end_red):
        first_part, second_part = self.parts

        # First third: Filled with Signals
        for col in range(first_part):
            if start_red:
                self.set_col_ligand_only(col)
            else:
                self.set_col_receptor_only(col)

        # Second third: Empty
        for col in range(first_part, second_part):
            self.set_col_empty(col)

        # Final third: Filled with Signals
        for col in range(second_part, self.cols):
            if end_red:
                self.set_col_ligand_only(col)
            else:
                self.set_col_receptor_only(col)


class GapSubstrateRR(BaseGapSubstrate):
    def initialize_substrate(self):
        self.initialize_gap(True, True)


class GapSubstrateRB(BaseGapSubstrate):
    def initialize_substrate(self):
        self.initialize_gap(True, False)


class GapSubstrateBR(BaseGapSubstrate):
    def initialize_substrate(self):
        self.initialize_gap(False, True)


class GapSubstrateBB(BaseGapSubstrate):
    def initialize_substrate(self):
        self.initialize_gap(False, False)


class GapSubstrateInverted(BaseGapSubstrate):
    def initialize_substrate(self):
        first_part, second_part = self.parts
        for col in range(first_part, second_part):
            self.set_col_receptor_only(col)

