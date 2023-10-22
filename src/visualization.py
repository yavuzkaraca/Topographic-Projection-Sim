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
    pass
