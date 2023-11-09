import matplotlib.pyplot as plt
import numpy as np

cmap_custom = plt.get_cmap('coolwarm')
cmap_custom = cmap_custom.reversed()


def visualize_substrate(substrate):
    plt.imshow(substrate.ligands, cmap=cmap_custom)
    plt.title("Ligands")
    plt.show()

    plt.imshow(substrate.receptors, cmap=cmap_custom)
    plt.title("Receptors")
    plt.show()


def visualize_result(result):
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
