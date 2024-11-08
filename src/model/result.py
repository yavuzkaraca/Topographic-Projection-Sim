"""
Module providing Result class for result representation.
"""

import numpy as np
import visualization as vz
import base64
import io
from matplotlib.figure import Figure


class Result:
    def __init__(self, simulation, runtime):
        """
        Initializes a Result object
        """
        self.simulation = simulation
        self.gcs = simulation.growth_cones
        self.frame = simulation.substrate.rows, simulation.substrate.cols
        self.runtime = runtime

    def get_gc_count(self):
        return len(self.gcs)

    def get_num_steps(self):
        return self.simulation.num_steps

    def get_summary(self):
        """
        Returns a summary dictionary with key simulation parameters and runtime.
        """
        return {
            "totalGrowthCones": self.get_gc_count(),
            "simulationSteps": self.get_num_steps(),
            "computationTime": self.runtime
        }

    def get_images(self):
        images = {}

        # TODO: @Clean duplicated data and redundancy

        # Visualize growth cones
        fig = vz.visualize_growth_cones(self.simulation.growth_cones)
        images["growth_cones"] = generate_base64_image(fig)

        # Visualize substrate
        fig = vz.visualize_substrate(self.simulation.substrate)
        images["substrate"] = generate_base64_image(fig)

        # Visualize substrate separately
        fig = vz.visualize_substrate_separately(self.simulation.substrate)
        images["substrate_separate"] = generate_base64_image(fig)

        fig = vz.visualize_projection_linear(self, self.simulation.substrate)
        images["projection_linear"] = generate_base64_image(fig)

        fig = vz.visualize_results_on_substrate(self, self.simulation.substrate)
        images["results_on_substrate"] = generate_base64_image(fig)

        fig = vz.visualize_trajectory_on_substrate(self, self.simulation.substrate, self.simulation.growth_cones)
        images["trajectory_on_substrate"] = generate_base64_image(fig)

        fig = vz.visualize_trajectories(self.simulation.growth_cones)
        images["trajectories"] = generate_base64_image(fig)

        return images

    def get_mapping(self):
        # TODO: @Clean Make a unified projection mapping by automatically dividing between position or id number
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


def generate_base64_image(figure: Figure) -> str:
    """Convert a matplotlib figure to a base64-encoded PNG image."""
    output = io.BytesIO()
    figure.savefig(output, format='png')
    output.seek(0)
    return base64.b64encode(output.getvalue()).decode('utf8')
