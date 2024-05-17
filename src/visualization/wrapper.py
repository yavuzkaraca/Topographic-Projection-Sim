# wrapper.py
import matplotlib.pyplot as plt
from src.visualization import visualization as vz


def prepare_single_plot(figsize=(8, 8)):
    """
    Prepare a single plot with specified figure size.
    """
    fig, ax = plt.subplots(figsize=figsize)
    return fig, ax


def prepare_dual_plots(figsize=(10, 5)):
    """
    Prepare two subplots side by side with specified figure size.
    """
    fig, axes = plt.subplots(1, 2, figsize=figsize)
    return fig, axes


def visualize_substrate_combined(substrate, title="Combined Ligands and Receptors"):
    """
    Customize and show the substrate visualization with specific titles.
    """
    fig, ax = prepare_single_plot()
    ax = vz.visualize_substrate_combined(ax, substrate)
    ax.set_title(title)
    plt.show()


def visualize_substrate_separately(substrate):
    """
    Customize and show ligands and receptors separately with specific titles.
    """
    fig, axes = prepare_dual_plots()
    axes = vz.visualize_substrate_separately(axes, substrate)
    axes[0].set_title("Ligands")
    axes[1].set_title("Receptors")
    plt.show()


def visualize_results_on_substrate(result, substrate):
    """
    Customize and show the visualization of tectum end-positions on the substrate.

    :param result: Result object containing tectum end-positions.
    :param substrate: The Substrate object containing ligand and receptor values.
    """
    fig, ax = prepare_single_plot()
    ax = vz.visualize_results_on_substrate(ax, result, substrate)
    ax.set_title("Tectum End-positions on Color-Mixed Substrate")
    ax.legend()
    plt.show()


def visualize_projection(result, substrate):
    """
    Setup and customize the projection mapping plot.
    """
    fig, ax = plt.subplots(figsize=(10, 10))  # Adjust size as needed
    vz.plot_projection_mapping(ax, result, substrate)
    ax.set_title("Projection Mapping")
    ax.set_xlabel("% a-p Axis of Target")
    ax.set_ylabel("% n-t Axis of Retina")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.legend()
    plt.show()


def visualize_projection_disjunctsets(result, substrate, marked_indexes,
                                      title="Projection Mapping Disjunction",
                                      label_first="Default Label 1", label_second="Default Label 2"):
    """
    Visualize and customize the projection mapping of two different sets.
    Title, labels, and other specifics are set within the function.
    """
    xlabel = "% a-p Axis of Target"
    ylabel = "% n-t Axis of Retina"

    fig, ax = plt.subplots(figsize=(10, 10))
    vz.plot_disjunct_projection_sets(ax, result, substrate, marked_indexes)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.legend()
    plt.show()
