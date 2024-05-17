"""
Module providing Result class for result representation of a simulation.
"""

import numpy as np


class Result:
    """
    Represents the results of a growth cone simulation.

    Attributes:
        gcs (list): List of Growth Cone objects involved in the simulation.
        frame (tuple): Tuple representing the dimensions of the substrate grid (rows, columns).

    Methods:
        get_projection_repr(): Generates a projection representation based on the initial positions of growth cones.
        get_final_positioning(): Retrieves the final positions of the growth cones.
    """

    def __init__(self, gcs, substrate):
        """
        Initializes a Result object with growth cones and substrate information.

        :param gcs: List of Growth Cone objects participating in the simulation.
        :param substrate: Substrate object providing the simulation environment.
        """
        self.gcs = gcs
        self.frame = substrate.rows, substrate.cols

    def get_projection_repr(self):
        """
        Generates a projection mapping representation based on the initial positions of growth cones.
        """
        x_values = np.array([gc.pos_current[0] for gc in self.gcs])
        y_values = np.array([gc.pos_start[1] for gc in self.gcs])

        return x_values, y_values

    def get_projection_id(self):
        """
        Generates a projection mapping representation based on the ids of growth cones.
        """
        x_values = np.array([gc.pos_current[0] for gc in self.gcs])
        y_values = np.array([gc.id for gc in self.gcs])

        return x_values, y_values

    def get_projection_halved(self):
        """
        Generates a projection mapping representation based on the ids of growth cones.
        """
        x_values = np.array([gc.pos_current[0] for gc in self.gcs])
        y_values = np.array([gc.id/2 for gc in self.gcs])

        return x_values, y_values


    def get_final_positioning(self):
        """
        Retrieves the final positions of the growth cones after the simulation.
        """
        x_values = np.array([gc.pos_current[0] for gc in self.gcs])
        y_values = np.array([gc.pos_current[1] for gc in self.gcs])

        return x_values, y_values

    def __str__(self):
        """
        Returns a string representation of the projection representation.
        """
        x_values, y_values = self.get_projection_repr()
        return x_values.__str__(), y_values.__str__()
