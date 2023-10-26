import matplotlib.pyplot as plt
import numpy as np


def visualize_substrate(substrate):
    plt.imshow(substrate.ligands, cmap='viridis')
    plt.title("Ligands")
    plt.show()

    plt.imshow(substrate.receptors, cmap='viridis')
    plt.title("Receptors")
    plt.show()


def visualize_result(result):
    x_values, y_values = result.get_2d_result()

    fig = plt.figure()
    plt.plot(x_values, y_values, '*')
    plt.title("Result")
    plt.show()
