"""
Module providing Result class for result representation.
"""

import numpy as np
import base64
import io

from matplotlib.figure import Figure

from visualization import visualize_projection, visualize_trajectories, visualize_adaptation, \
    visualize_trajectory_on_substrate, visualize_results_on_substrate, visualize_substrate_separately, \
    visualize_substrate, visualize_growth_cones


class Result:
    def __init__(self, simulation, runtime, config):
        """
        Initializes a Result object.
        """
        self.config = config
        self.simulation = simulation
        self.runtime = runtime

    def get_images(self):
        """
        Generates visualizations and encodes them as base64 strings for frontend display.
        """
        images = {}

        # Pre-simulation visualizations
        images["growth_cones"] = _generate_image(visualize_growth_cones, self.simulation.growth_cones)
        images["substrate"] = _generate_image(visualize_substrate, self.simulation.substrate)
        images["substrate_separate"] = _generate_image(visualize_substrate_separately, self.simulation.substrate)

        # Post-simulation visualizations
        images["projection_linear"] = _generate_image(visualize_projection, self, self.simulation.substrate)
        images["results_on_substrate"] = _generate_image(visualize_results_on_substrate, self,
                                                         self.simulation.substrate)
        images["trajectory_on_substrate"] = _generate_image(visualize_trajectory_on_substrate, self,
                                                            self.simulation.substrate, self.simulation.growth_cones)
        images["trajectories"] = _generate_image(visualize_trajectories, self.simulation.growth_cones)
        images["adaptation"] = _generate_image(visualize_adaptation, self.simulation.growth_cones)

        return images

    def get_gc_count(self):
        return len(self.simulation.growth_cones)

    def get_num_steps(self):
        return self.simulation.num_steps

    def get_summary(self):
        """
        Returns a summary dictionary with key simulation parameters and runtime.
        """
        return {
            "totalGrowthCones": self.get_gc_count(),
            "simulationSteps": self.get_num_steps(),
            "computationTime": f"{self.runtime:.3f}",
            "config": self.config
        }

    def get_mapping(self, attribute="id", halved=False):
        """
        Generates a projection mapping representation based on a specified attribute.
        Supports 'id', 'start_pos', or 'final_pos' for y-axis mapping.

        :param attribute: Attribute for y-axis values ('id', 'start_pos', 'final_pos').
        :param halved: Whether to halve the y-axis values.
        """
        x_values = np.array([gc.pos[0] for gc in self.simulation.growth_cones])
        if attribute == "id":
            y_values = np.array([gc.id / 2 if halved else gc.id for gc in self.simulation.growth_cones])
        elif attribute == "start_pos":
            y_values = np.array(
                [gc.get_start_pos()[1] / 2 if halved else gc.get_start_pos()[1] for gc in self.simulation.growth_cones])
        elif attribute == "final_pos":
            y_values = np.array([gc.pos[1] / 2 if halved else gc.pos[1] for gc in self.simulation.growth_cones])
        else:
            raise ValueError("Invalid attribute specified for mapping.")

        return x_values, y_values

    def get_projection_ypos(self):
        """
        Generates a projection mapping based on initial y-positions of growth cones.
        """
        return self.get_mapping(attribute="start_pos")

    def get_projection_id(self):
        """
        Generates a projection mapping based on the ids of growth cones.
        """
        return self.get_mapping(attribute="id")

    def get_projection_halved(self):
        """
        Generates a halved projection mapping based on the ids of growth cones.
        """
        return self.get_mapping(attribute="id", halved=True)

    def get_final_positioning(self):
        """
        Retrieves the final positions of the growth cones after the model.
        """
        return self.get_mapping(attribute="final_pos")

    def __str__(self):
        """
        Returns a string representation of the projection representation.
        """
        x_values, y_values = self.get_projection_id()
        return x_values.__str__(), y_values.__str__()


def _generate_base64_image(figure: Figure) -> str:
    """Convert a matplotlib figure to a base64-encoded PNG image."""
    output = io.BytesIO()
    figure.savefig(output, format='png', transparent=False)
    output.seek(0)
    return base64.b64encode(output.getvalue()).decode('utf8')


def _generate_image(visualization_func, *args):
    """
    Generates a visualization with the provided function and encodes it in base64.
    """
    fig = visualization_func(*args)
    return _generate_base64_image(fig)
