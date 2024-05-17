# visualization.py
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


def create_blended_colors(ligands, receptors):
    """
    Create blended colors for ligands and receptors with custom adjustments.
    """
    blended_colors = np.ones(ligands.shape + (3,))
    blended_colors[..., 0] -= ligands * 0.1 + receptors * 0.9
    blended_colors[..., 1] -= ligands * 0.9 + receptors * 0.6
    blended_colors[..., 2] -= ligands * 0.6 + receptors * 0.1
    return blended_colors


def visualize_substrate_combined(ax, substrate):
    """
    Core visualization for the substrate combined.
    """
    blended_colors = create_blended_colors(substrate.ligands, substrate.receptors)
    ax.imshow(blended_colors)
    ax.set_ylim(ax.get_ylim()[::-1])  # Flip the y-axis to have zero at the bottom
    return ax


def visualize_substrate_separately(axes, substrate):
    """
    Core visualization for ligands and receptors separately.
    """
    ligand_colors = create_blended_colors(substrate.ligands, np.zeros_like(substrate.ligands))
    receptor_colors = create_blended_colors(np.zeros_like(substrate.receptors), substrate.receptors)
    axes[0].imshow(ligand_colors)
    axes[0].set_ylim(axes[0].get_ylim()[::-1])  # Flip the y-axis
    axes[1].imshow(receptor_colors)
    axes[1].set_ylim(axes[1].get_ylim()[::-1])  # Flip the y-axis
    return axes


def plot_tectum_end_positions(ax, result):
    """
    Plot tectum end-positions on the provided axes.
    """
    x_values, y_values = result.get_final_positioning()
    ax.plot(x_values, y_values, '*', color='orange', label='Tectum End-positions')


def visualize_results_on_substrate(ax, result, substrate):
    """
    Core function to visualize tectum end-positions on a color-mixed substrate.

    :param ax: The matplotlib axis to plot on.
    :param result: Result object containing tectum end-positions.
    :param substrate: The Substrate object containing ligand and receptor values.
    """
    blended_colors = create_blended_colors(substrate.ligands, substrate.receptors)
    ax.imshow(blended_colors)

    # Plot tectum end-positions over the substrate
    plot_tectum_end_positions(ax,result)

    # Drawing the border to represent the offset
    offset = substrate.offset
    ax.add_patch(plt.Rectangle((offset - 0.5, offset - 0.5), substrate.cols - 2 * offset, substrate.rows - 2 * offset,
                               fill=False, edgecolor='black', lw=2))
    ax.set_ylim(ax.get_ylim()[::-1])  # Flip the y-axis to have zero at the bottom
    return ax


def percentualize_values(values, min_val, max_val):
    """
    Normalize the given values to a range between 0 and 100.
    """
    return (values - min_val) / (max_val - min_val) * 100


def linear_regression(ax, x_values, y_values):
    slope, intercept, r_value, _, _ = linregress(x_values, y_values)
    regression_line = slope * x_values + intercept
    ax.plot(x_values, regression_line, 'r-', label=f'Linear Regression R^2={r_value ** 2:.2f}')


def curve_fitting(ax, x_values, y_values, color='b-'):
    nm_coeffs = np.polyfit(x_values, y_values, 3)
    nm_poly = np.poly1d(nm_coeffs)
    nm_x_new = np.linspace(min(x_values), max(y_values), 300)
    nm_y_new = nm_poly(nm_x_new)
    ax.plot(nm_x_new, nm_y_new, color)


def plot_projection_mapping(ax, result, substrate):
    """
    Plot the projection mapping on the provided axes.
    """
    x_values, y_values = result.get_projection_signature()
    max_val = len(y_values) - 1
    x_values_normalized = percentualize_values(x_values, substrate.offset, substrate.cols - substrate.offset)
    y_values_normalized = percentualize_values(y_values, 0, max_val)
    ax.plot(x_values_normalized, y_values_normalized, '*', color='blue')
    curve_fitting(ax, x_values_normalized, y_values_normalized)


def plot_disjunct_projection_sets(ax, result, substrate, marked_indexes):
    """
    Plot projection mapping of two data sets differentiated by indexes.
    """
    x_values, y_values = result.get_projection_id()
    x_values_normalized = percentualize_values(x_values, substrate.offset, substrate.cols - substrate.offset)
    max_val = len(y_values) - 1
    y_values_normalized = percentualize_values(y_values, 0, max_val)

    # Segment data into mutated and non-mutated
    first_group_x = [x for i, x in enumerate(x_values_normalized) if i in marked_indexes]
    first_group_y = [y for i, y in enumerate(y_values_normalized) if i not in marked_indexes]
    second_group_x = [x for i, x in enumerate(x_values_normalized) if i not in marked_indexes]
    second_group_y = [y for i, y in enumerate(y_values_normalized) if i not in marked_indexes]

    # Cubic polynomial fitting for non-mutated data
    if first_group_x and first_group_y:
        curve_fitting(ax, first_group_x, first_group_y)
        ax.plot(first_group_x, first_group_y, 'b*', label='Wildtype Growth Cones')

    # Cubic polynomial fitting for mutated data
    if second_group_x and second_group_y:
        curve_fitting(ax, second_group_x, second_group_y, 'r-')
        ax.plot(second_group_x, second_group_y, 'r*', label='Mutated Growth Cones')


def visualize_growth_cones(gcs):
    receptors = np.array([gc.receptor_current for gc in gcs])
    ligands = np.array([gc.ligand_current for gc in gcs])

    plt.figure(figsize=(10, 6))
    plt.plot(receptors, 'o-', label='Receptors')
    plt.plot(ligands, 'o-', color='red', label='Ligands')
    plt.xlabel('Growth Cone ID (sorted along %n-t Axis of Retina)')
    plt.ylabel('Signal Value')
    plt.title('GCs')
    plt.legend()
    plt.show()


def visualize_trajectories(growth_cones, trajectory_freq=50):
    """
    Visualize the trajectories of growth cones.

    :param growth_cones: List of GrowthCone objects.
    """
    plt.figure()
    for growth_cone in growth_cones:
        trajectory_x, trajectory_y = zip(*growth_cone.history.position[::trajectory_freq])
        plt.plot(trajectory_x, trajectory_y, label=f'Growth Cone {growth_cones.index(growth_cone)}')

    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Growth Cone Trajectories')
    plt.legend()
    plt.show()


def visualize_trajectory_on_substrate(result, substrate, growth_cones, trajectory_freq=50):
    """
    Visualize tectum end-positions and growth cone trajectories on top of the substrate.

    :param trajectory_freq:
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
    ax.plot(x_values, y_values, '*', color='orange', label='Tectum End-positions')

    # Drawing the border to represent the offset
    offset = substrate.offset
    ax.add_patch(plt.Rectangle((offset - 0.5, offset - 0.5), substrate.cols - 2 * offset,
                               substrate.rows - 2 * offset, fill=False, edgecolor='black', lw=2))

    # Plot growth cone trajectories
    for growth_cone in growth_cones:
        trajectory_x, trajectory_y = zip(*growth_cone.history.position[::trajectory_freq])
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


def visualize_growth_cones(gcs):
    receptors = np.array([gc.receptor_current for gc in gcs])
    ligands = np.array([gc.ligand_current for gc in gcs])

    plt.figure(figsize=(10, 6))
    plt.plot(receptors, 'o-', label='Receptors')
    plt.plot(ligands, 'o-', color='red', label='Ligands')
    plt.xlabel('Growth Cone ID (sorted along %n-t Axis of Retina)')
    plt.ylabel('Signal Value')
    plt.title('GCs')
    plt.legend()
    plt.show()


def visualize_projection(result, substrate, label="Growth Cones", halved=False):
    """
    Generate a plot for the projection mapping of growth cones.

    :param halved:
    :param label: Label for the data plotted, defaulting to "Growth Cones".
    :param substrate: The Substrate object containing dimensions for normalization.
    :param result: Result object containing growth cone positions and details.
    """
    plt.figure(figsize=(10, 10))  # Direct creation of a figure with specified size

    # Projection mapping data and normalization
    x_values, y_values = result.get_projection_id()

    if halved:
        x_values, y_values = result.get_projection_halved()

    x_values_normalized = normalize_values(x_values, substrate.offset, substrate.cols - substrate.offset)

    max_val = len(y_values) - 1
    y_values_normalized = normalize_values(y_values, 0, max_val)

    # Cubic polynomial fitting for the data
    coeffs = np.polyfit(x_values_normalized, y_values_normalized, 3)
    poly = np.poly1d(coeffs)
    x_new = np.linspace(min(x_values_normalized), max(x_values_normalized), 300)
    y_new = poly(x_new)
    plt.plot(x_values_normalized, y_values_normalized, 'b*', label=label)
    plt.plot(x_new, y_new, 'b-')

    plt.title("Projection Mapping")
    plt.xlabel("% a-p Axis of Target")
    plt.ylabel("% n-t Axis of Retina")
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.legend()

    plt.show()


def visualize_projection_disjunctsets(result, substrate, mutated_indexes,
                                      label_first="Wildtype Growth Cones", label_second="Mutated Growth Cones"):
    """
    Generate a plot for the projection mapping of non-mutated and mutated growth cones.

    :param label_second:
    :param label_first:
    :param substrate: The Substrate object containing dimensions. (for normalization)
    :param result: Result object containing growth cone positions and details.
    :param mutated_indexes: List of indexes of mutated growth cones to be colored differently.
    """
    plt.figure(figsize=(8, 8))  # Direct creation of a figure with specified size

    # Projection mapping data and normalization
    x_values, y_values = result.get_projection_id()
    x_values_normalized = normalize_values(x_values, substrate.offset, substrate.cols - substrate.offset)
    max_val = len(y_values) - 1
    y_values_normalized = normalize_values(y_values, 0, max_val)

    # Segment data into mutated and non-mutated
    mutated_x = [x for i, x in enumerate(x_values_normalized) if i in mutated_indexes]
    mutated_y = [y for i, y in enumerate(y_values_normalized) if i not in mutated_indexes]
    non_mutated_x = [x for i, x in enumerate(x_values_normalized) if i not in mutated_indexes]
    non_mutated_y = [y for i, y in enumerate(y_values_normalized) if i not in mutated_indexes]

    # Cubic polynomial fitting for non-mutated data
    if non_mutated_x and non_mutated_y:
        nm_coeffs = np.polyfit(non_mutated_x, non_mutated_y, 3)
        nm_poly = np.poly1d(nm_coeffs)
        nm_x_new = np.linspace(min(non_mutated_x), max(non_mutated_x), 300)
        nm_y_new = nm_poly(nm_x_new)
        plt.plot(non_mutated_x, non_mutated_y, 'b*', label=label_first)
        plt.plot(nm_x_new, nm_y_new, 'b-')

    # Cubic polynomial fitting for mutated data
    if mutated_x and mutated_y:
        m_coeffs = np.polyfit(mutated_x, mutated_y, 3)
        m_poly = np.poly1d(m_coeffs)
        m_x_new = np.linspace(min(mutated_x), max(mutated_x), 300)
        m_y_new = m_poly(m_x_new)
        plt.plot(mutated_x, mutated_y, 'r*', label=label_second)
        plt.plot(m_x_new, m_y_new, 'r-')

    plt.title("Projection Mapping")
    plt.xlabel("% a-p Axis of Target")
    plt.ylabel("% n-t Axis of Retina")
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.legend()

    plt.show()


def normalize_values(values, min_val, max_val):
    """
    Normalize the given values to a range between 0 and 100.
    """
    return (values - min_val) / (max_val - min_val) * 100


def visualize_trajectories(growth_cones, trajectory_freq=50):
    """
    Visualize the trajectories of growth cones.

    :param growth_cones: List of GrowthCone objects.
    """
    plt.figure()
    for growth_cone in growth_cones:
        trajectory_x, trajectory_y = zip(*growth_cone.history.position[::trajectory_freq])
        plt.plot(trajectory_x, trajectory_y, label=f'Growth Cone {growth_cones.index(growth_cone)}')

    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Growth Cone Trajectories')
    plt.legend()
    plt.show()


def visualize_adaptation(growth_cones):
    # Create a figure with 2 rows and 2 columns of subplots
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))  # Adjust figsize as needed

    # Determine the maximum number of steps across all growth cones
    max_steps = max(len(gc.history.potential) for gc in growth_cones)

    # Plotting potentials on the first subplot
    for gc in growth_cones:
        axs[0, 0].plot(gc.history.potential, label=gc.id)
    axs[0, 0].set_xlabel('Step')
    axs[0, 0].set_ylabel('Potential')
    axs[0, 0].set_title('Guidance Potentials')
    axs[0, 0].set_xlim(0, max_steps)
    axs[0, 0].legend()

    # Plotting adaptation coefficients on the second subplot
    for gc in growth_cones:
        axs[0, 1].plot(gc.history.adap_co, label=gc.id)
    axs[0, 1].set_xlabel('Step')
    axs[0, 1].set_ylabel('Adaptation Coefficient')
    axs[0, 1].set_title('Adaptation Coefficients')
    axs[0, 1].set_xlim(0, max_steps)
    axs[0, 1].legend()

    # Placeholder for third plot
    # For example, plotting another metric here
    for gc in growth_cones:
        axs[1, 0].plot(gc.history.ligand, label=gc.id)
    axs[1, 0].set_xlabel('Step')
    axs[1, 0].set_ylabel('Ligand')
    axs[1, 0].set_title('Ligand Value')
    axs[1, 0].set_xlim(0, max_steps)
    axs[1, 0].set_yscale('log')  # Set the y-axis to logarithmic scale
    axs[1, 0].legend()

    # Placeholder for fourth plot
    # For example, plotting yet another metric here
    for gc in growth_cones:
        axs[1, 1].plot(gc.history.reset_force_ligand, label=gc.id)
    axs[1, 1].set_xlabel('Step')
    axs[1, 1].set_ylabel('Reset force')
    axs[1, 1].set_title('Reset Force for Ligand')
    axs[1, 1].set_xlim(0, max_steps)
    axs[1, 1].set_ylim(top=0.05)
    axs[1, 1].set_yscale('symlog')  # Set the y-axis to logarithmic scale
    axs[1, 1].legend()

    # Adjust layout and show the figure
    plt.tight_layout()
    plt.show()
