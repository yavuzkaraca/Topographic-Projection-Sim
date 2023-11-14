import matplotlib.pyplot as plt
import numpy as np


def visualize_substrate(substrate):
    """
    Visualize the ligands and receptors in the substrate by blending their colors.

    :param substrate: The Substrate object containing ligand and receptor values.
    """
    fig, ax = plt.subplots(figsize=(8, 8))  # Create a single plot

    # Blend the colors of ligands and receptors
    blended_colors = np.zeros(substrate.ligands.shape + (3,))
    blended_colors[..., 0] = substrate.ligands  # Red channel for ligands
    blended_colors[..., 2] = substrate.receptors  # Blue channel for receptors

    ax.imshow(blended_colors, cmap='RdBu')  # Use RdBu colormap for blending

    ax.set_title("Combined Ligands and Receptors")

    plt.show()


def visualize_substrate_separately(substrate):
    """
    Visualize the ligands and receptors in the substrate in separate subplots.

    :param substrate: The Substrate object containing ligand and receptor values.
    """

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))  # Create a single figure with two subplots

    axes[0].imshow(substrate.ligands, cmap='Reds')  # Plot ligands in the first subplot
    axes[0].set_title("Ligands")

    axes[1].imshow(substrate.receptors, cmap='Blues')  # Plot receptors in the second subplot
    axes[1].set_title("Receptors")

    plt.show()


def visualize_result(result):
    """
    Generate plots for the projection mapping and tectum end-positions.

    :param result: Result object containing growth cone positions and details.
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))  # Create a single figure with two subplots

    x_values, y_values = result.get_projection_repr()
    axes[0].plot(x_values, y_values, '*')  # Plot projection mapping in the first subplot
    axes[0].set_title("Projection Mapping")

    x_values, y_values = result.get_final_positioning()
    axes[1].plot(x_values, y_values, '*')  # Plot tectum end-positions in the second subplot
    axes[1].set_title("Tectum End-positions")

    plt.show()


def visualize_results_on_substrate(result, substrate):
    """
    Visualize tectum end-positions on top of the color-mixed substrate.

    :param result: Result object containing tectum end-positions.
    :param substrate: The Substrate object containing ligand and receptor values.
    """
    fig, ax = plt.subplots(figsize=(8, 8))  # Create a single plot

    # Blend the colors of ligands and receptors
    blended_colors = np.zeros(substrate.ligands.shape + (3,))
    blended_colors[..., 0] = substrate.ligands  # Red channel for ligands
    blended_colors[..., 2] = substrate.receptors  # Blue channel for receptors

    ax.imshow(blended_colors)  # Display the color-mixed substrate

    x_values, y_values = result.get_final_positioning()
    ax.plot(x_values, y_values, '*', color='yellow', label='Tectum End-positions')  # Plot tectum end-positions

    ax.set_title("Tectum End-positions on Color-Mixed Substrate")
    ax.legend()  # Show legend

    plt.show()
