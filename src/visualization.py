"""
Module for visualizing substrate and simulation results.
"""

import matplotlib.pyplot as plt


def visualize_substrate(substrate):
    """
    Visualize the ligands and receptors in the substrate as separate plots.

    :param substrate: The Substrate object containing ligand and receptor values.
    """

    # TODO: visualize both substrate onto each other
    plt.imshow(substrate.ligands, cmap='Reds')
    plt.title("Ligands")
    plt.show()

    plt.imshow(substrate.receptors, cmap='Blues')
    plt.title("Receptors")
    plt.show()


def visualize_result(result):
    """
    Generate plots for the projection mapping and tectum end-positions.

    :param result: Result object containing growth cone positions and details.
    """

    x_values, y_values = result.get_projection_repr()

    # fig = plt.figure()
    plt.plot(x_values, y_values, '*')
    plt.title("Projection Mapping")
    plt.show()

    x_values, y_values = result.get_final_positioning()

    # fig = plt.figure()
    plt.plot(x_values, y_values, '*')
    plt.title("Tectum End-positions")
    plt.show()
