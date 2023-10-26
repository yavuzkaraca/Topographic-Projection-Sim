import tkinter as tk
from tkinter import Label, Entry
from src.substrate import Substrate  # Import the Substrate class from your substrate module
from src.visualization import visualize_substrate


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
    create_button = tk.Button(app, text="Create Config", command=create_config_dict)
    create_button.grid(row=3, columnspan=2)

    app.mainloop()



def test_substrate():
    # Create a Substrate instance with your desired rows and columns
    rows = 15
    cols = 15
    substrate = Substrate(rows, cols)

    # Assign the configuration dictionary to the Substrate

    # Initialize the substrate with wedges
    substrate.initialize_substrate()

    # Print the substrate
    print(substrate)

    visualize_substrate(substrate)
