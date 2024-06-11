"""
Module providing Result class for result representation.
"""

import numpy as np


class Result:
    def __init__(self, gcs, substrate):
        """
        Initializes a Result object
        """
        self.gcs = gcs
        self.frame = substrate.rows, substrate.cols

    def get_mapping(self):
        # TODO: Make a unified projection mapping by automatically dividing between position or id number
        pass

    def get_projection_ypos(self):
        """
        Generates a projection mapping representation based on the initial positions of growth cones.
        """
        x_values = np.array([gc.pos[0] for gc in self.gcs])
        y_values = np.array([gc.get_start_pos()[1] for gc in self.gcs])

        return x_values, y_values

    def get_projection_id(self):
        """
        Generates a projection mapping representation based on the ids of growth cones.
        """
        x_values = np.array([gc.pos[0] for gc in self.gcs])
        y_values = np.array([gc.id for gc in self.gcs])

        return x_values, y_values

    def get_projection_halved(self):
        """
        Generates a projection mapping representation based on the ids of growth cones.
        """
        x_values = np.array([gc.pos[0] for gc in self.gcs])
        y_values = np.array([gc.id / 2 for gc in self.gcs])

        return x_values, y_values

    def get_final_positioning(self):
        """
        Retrieves the final positions of the growth cones after the model.
        """
        x_values = np.array([gc.pos[0] for gc in self.gcs])
        y_values = np.array([gc.pos[1] for gc in self.gcs])

        return x_values, y_values

    def __str__(self):
        """
        Returns a string representation of the projection representation.
        """
        x_values, y_values = self.get_projection_id()
        return x_values.__str__(), y_values.__str__()
