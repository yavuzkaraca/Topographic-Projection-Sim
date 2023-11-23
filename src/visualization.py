import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


def create_blended_colors(ligands, receptors):
    """
    Create blended colors for ligands and receptors with custom adjustments.
    Initializes a white background and adjusts the color channels based on ligand and receptor values.

    :param ligands: Array of ligand values.
    :param receptors: Array of receptor values.
    :return: Array of blended colors.
    """
    # Initialize with a white background
    blended_colors = np.ones(ligands.shape + (3,))

    # Custom color adjustments for ligands and receptors
    blended_colors[..., 0] -= ligands * 0.1 + receptors * 0.9  # Adjust Red channel
    blended_colors[..., 1] -= ligands * 0.9 + receptors * 0.6  # Adjust Green channel
    blended_colors[..., 2] -= ligands * 0.6 + receptors * 0.1  # Adjust Blue channel

    return blended_colors


def visualize_substrate(substrate):
    """
    Visualize the substrate with ligands and receptors.
    Uses the create_blended_colors function to generate the color representation.

    :param substrate: The Substrate object containing ligand and receptor values.
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    blended_colors = create_blended_colors(substrate.ligands, substrate.receptors)

    # Display the color-mixed substrate
    ax.imshow(blended_colors)
    ax.set_title("Combined Ligands and Receptors")

    # Flip the y-axis to have zero at the bottom
    ax.set_ylim(ax.get_ylim()[::-1])

    plt.show()


def visualize_substrate_separately(substrate):
    """
    Visualize the ligands and receptors in separate subplots with custom colors.
    Applies color blending to ligands and receptors separately.

    :param substrate: The Substrate object containing ligand and receptor values.
    """
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Create colored images for ligands and receptors separately
    ligand_colors = create_blended_colors(substrate.ligands, np.zeros_like(substrate.ligands))
    receptor_colors = create_blended_colors(np.zeros_like(substrate.receptors), substrate.receptors)

    # Display ligands with custom colors
    axes[0].imshow(ligand_colors)
    axes[0].set_title("Ligands")
    axes[0].set_ylim(axes[0].get_ylim()[::-1])  # Flip the y-axis

    # Display receptors with custom colors
    axes[1].imshow(receptor_colors)
    axes[1].set_title("Receptors")
    axes[1].set_ylim(axes[1].get_ylim()[::-1])  # Flip the y-axis

    plt.show()


def visualize_results_on_substrate(result, substrate):
    """
    Visualize tectum end-positions on top of the substrate.
    Overlays the results of tectum end-positions onto the color-mixed substrate.

    :param result: Result object containing tectum end-positions.
    :param substrate: The Substrate object containing ligand and receptor values.
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    blended_colors = create_blended_colors(substrate.ligands, substrate.receptors)

    # Display the color-mixed substrate
    ax.imshow(blended_colors)

    # Plot tectum end-positions over the substrate
    x_values, y_values = result.get_final_positioning()
    ax.plot(x_values, y_values, '*', color='yellow', label='Tectum End-positions')
    ax.set_title("Tectum End-positions on Color-Mixed Substrate")
    ax.legend()

    # Flip the y-axis to have zero at the bottom
    ax.set_ylim(ax.get_ylim()[::-1])

    plt.show()


def visualize_trajectory_on_substrate(result, substrate, growth_cones):
    """
    Visualize tectum end-positions and growth cone trajectories on top of the substrate.

    :param result: Result object containing tectum end-positions.
    :param substrate: The Substrate object containing ligand and receptor values.
    :param growth_cones: List of GrowthCone objects with trajectory data.
    """
    fig, ax = plt.subplots(figsize=(8, 8))

    # Create blended colors for the substrate
    blended_colors = create_blended_colors(substrate.ligands, substrate.receptors)
    ax.imshow(blended_colors)

    # Plot tectum end-positions
    x_values, y_values = result.get_final_positioning()
    ax.plot(x_values, y_values, '*', color='yellow', label='Tectum End-positions')

    # Plot growth cone trajectories
    for growth_cone in growth_cones:
        trajectory_x, trajectory_y = zip(*growth_cone.trajectory)
        ax.plot(trajectory_x, trajectory_y, label=f'Growth Cone {growth_cones.index(growth_cone)}')

    ax.set_title("Tectum End-positions and Growth Cone Trajectories on Substrate")
    ax.legend()
    ax.set_ylim(ax.get_ylim()[::-1])  # Flip the y-axis
    plt.show()


def visualize_result(result, substrate):
    """
    Generate plots for the projection mapping and tectum end-positions, including linear regression for the
    projection mapping.

    :param substrate: The Substrate object containing dimensions. (for normalization)
    :param result: Result object containing growth cone positions and details.
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))  # Create a single figure with two subplots

    # Get projection mapping data and normalize
    x_values, y_values = result.get_projection_repr()

    x_values_normalized = normalize_values(x_values, substrate.offset, substrate.cols - substrate.offset)
    y_values_normalized = normalize_values(y_values, substrate.offset, substrate.rows - substrate.offset - 1)

    slope, intercept, r_value, _, _ = linregress(x_values_normalized, y_values_normalized)
    regression_line = slope * x_values_normalized + intercept
    correlation = np.corrcoef(x_values_normalized, y_values_normalized)[0, 1] ** 2  # Squaring for R^2
    null_point_x = -intercept / slope if slope != 0 else None
    null_point_y = intercept

    axes[0].plot(x_values_normalized, y_values_normalized, '*', label='Growth Cones')
    axes[0].plot(x_values_normalized, regression_line, 'r-',
                 label=f'Linear Regression\nSlope: {slope:.2f}\nR^2: {correlation:.2f}'
                       f'\nNull Point X: {null_point_x:.2f}\nNull Point Y: {null_point_y:.2f}')
    axes[0].set_title("Projection Mapping")
    axes[0].set_xlabel("% a-p Axis of Target")
    axes[0].set_ylabel("% n-t Axis of Retina")
    axes[0].set_xlim(0, 100)  # Set x-axis limit
    axes[0].set_ylim(0, 100)  # Set y-axis limit
    axes[0].legend()

    # Tectum End-positions
    x_values, y_values = result.get_final_positioning()
    axes[1].plot(x_values, y_values, '*')  # Plot tectum end-positions in the second subplot
    axes[1].set_title("Tectum End-positions")
    axes[1].set_xlabel("X Coordinate")
    axes[1].set_ylabel("Y Coordinate")

    plt.show()


def normalize_values(values, min_val, max_val):
    """
    Normalize the given values to a range between 0 and 100.
    """
    return (values - min_val) / (max_val - min_val) * 100


def visualize_trajectories(growth_cones):
    """
    Visualize the trajectories of growth cones.

    :param growth_cones: List of GrowthCone objects.
    """
    plt.figure()
    for growth_cone in growth_cones:
        x_values, y_values = zip(*growth_cone.trajectory)  # Unpack the trajectory points
        plt.plot(x_values, y_values, label=f'Growth Cone {growth_cones.index(growth_cone)}')

    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Growth Cone Trajectories')
    plt.legend()
    plt.show()
