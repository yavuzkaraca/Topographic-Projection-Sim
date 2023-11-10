import matplotlib.pyplot as plt


def visualize_substrate(substrate):
    # TODO: visualize both substrate onto each other
    plt.imshow(substrate.ligands, cmap='Reds')
    plt.title("Ligands")
    plt.show()

    plt.imshow(substrate.receptors, cmap='Blues')
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
