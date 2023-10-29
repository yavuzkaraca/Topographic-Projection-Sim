import numpy as np


class Result:
    def __init__(self, gcs, substrate):
        self.gcs = gcs
        self.frame = substrate.rows, substrate.cols

    def get_projection_repr(self):
        x_values = np.array([gc.position[0] for gc in self.gcs])
        y_values = np.array([gc.start_position[1] for gc in self.gcs])

        return x_values, y_values

    def get_final_positioning(self):
        x_values = np.array([gc.position[0] for gc in self.gcs])
        y_values = np.array([gc.position[1] for gc in self.gcs])

        return x_values, y_values

    def __str__(self):
        x_values, y_values = self.get_projection_repr()
        return x_values.__str__(), y_values.__str__()

