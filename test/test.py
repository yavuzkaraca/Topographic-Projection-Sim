import tkinter as tk
from tkinter import Label, Entry
import numpy as np
from src.substrate import Substrate  # Import the Substrate class from your substrate module
from src.visualization import visualize_substrate
from src.potential_calculation import intersection_area
import src.config as cfg

test_config = {
    cfg.SUBSTRATE_TYPE: cfg.CONTINUOUS_GRADIENTS,
    cfg.CUSTOM_FIRST: 2,
    cfg.CUSTOM_SECOND: 40,
    cfg.ROWS: 50,
    cfg.COLS: 100,
    cfg.ADAPTATION: False,
    cfg.GC_COUNT: 20,
    cfg.GC_SIZE: 5,
    cfg.STEP_SIZE: 5,
    cfg.STEP_AMOUNT: 10000,
    cfg.X_STEP_POSSIBILITY: 0.45,
    cfg.Y_STEP_POSSIBILITY: 0.25,
    cfg.SIGMA: 1.0
}


def test_gui():
    app = tk.Tk()
    app.title("Simulation Configuration")

    # Substrate Type
    Label(app, text="Substrate Type").grid(row=0, column=0)
    substrate_type_entry = Entry(app)
    substrate_type_entry.grid(row=0, column=1)

    # Substrate Size (X and Y)
    Label(app, text="Substrate Size (X)").grid(row=1, column=0)
    substrate_size_x_entry = Entry(app)
    substrate_size_x_entry.grid(row=1, column=1)

    Label(app, text="Substrate Size (Y)").grid(row=2, column=0)
    substrate_size_y_entry = Entry(app)
    substrate_size_y_entry.grid(row=2, column=1)

    # Button to create configuration dictionary
    create_button = tk.Button(app, text="Create Config")
    create_button.grid(row=3, columnspan=2)

    app.mainloop()


def test_substrate():
    substrate = Substrate(test_config)
    visualize_substrate(substrate)


def test_intersection():
    gc1_pos = (5, 5)
    gc2_pos = (6, 6)
    size = 2
    area = intersection_area(gc1_pos, gc2_pos, size)
    print(area)


def test_matrix():
    matrix = np.array([[1, 2],
                       [3, 4]])
    print(matrix[0, 1])
