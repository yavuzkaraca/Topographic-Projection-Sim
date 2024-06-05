import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class ConfiguratorApp:
    def __init__(self, root):
        self.root = root
        root.title('Configuration and Visualization App')

        # Set up the main frames
        self.frame_left = tk.Frame(root, width=600, height=400)
        self.frame_right = tk.Frame(root)
        self.frame_buttons = tk.Frame(root)

        self.frame_left.grid(row=0, column=0, padx=10, pady=10)
        self.frame_right.grid(row=0, column=1, padx=10, pady=10, sticky='n')
        self.frame_buttons.grid(row=1, column=0, columnspan=2, pady=10)

        # Setup matplotlib figure
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, self.frame_left)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill=tk.BOTH, expand=True)

        # Dictionary to store the input fields
        self.entries = {}

        # Labels and entry fields for each config
        self.configs = {
            "SUBSTRATE_TYPE": "CONTINUOUS_GRADIENTS",
            "CUSTOM_FIRST": 0,
            "CUSTOM_SECOND": 0,
            "ROWS": 100,
            "COLS": 100,
            "GC_COUNT": 20,
            "GC_SIZE": 5,
            "STEP_SIZE": 1,
            "STEP_AMOUNT": 16000,
            "X_STEP_POSSIBILITY": 0.55,
            "Y_STEP_POSSIBILITY": 0.50,
            "SIGMOID_GAIN": 8,
            "SIGMOID_SHIFT": -4,
            "SIGMA": 0.12,
            "FORCE": False,
            "FORWARD_SIG": True,
            "REVERSE_SIG": True,
            "FF_INTER": True,
            "FT_INTER": True,
            "ADAPTATION_ENABLED": True,
            "ADAPTATION_MU": 0.006,
            "ADAPTATION_LAMBDA": 0.0045,
            "ADAPTATION_HISTORY": 50
        }

        row = 0
        for key, value in self.configs.items():
            label = tk.Label(self.frame_right, text=f'{key}:')
            label.grid(row=row, column=0, sticky='e', padx=10, pady=5)

            entry = tk.Entry(self.frame_right, width=20)
            entry.insert(0, str(value))
            entry.grid(row=row, column=1, padx=10, pady=5)
            self.entries[key] = entry

            row += 1

        # Buttons to start and stop the process
        self.start_button = tk.Button(self.frame_buttons, text='Start', command=self.start_process)
        self.stop_button = tk.Button(self.frame_buttons, text='Stop', command=self.stop_process)
        self.save_button = tk.Button(self.frame_buttons, text='Save', command=self.update_config)

        self.start_button.pack(side=tk.LEFT, padx=50, pady=10, ipadx=10, ipady=10)
        self.stop_button.pack(side=tk.LEFT, padx=50, pady=10, ipadx=10, ipady=10)
        self.save_button.pack(side=tk.LEFT, padx=50, pady=10, ipadx=10, ipady=10)

    def update_config(self):
        # Update the dictionary with new entries
        for key in self.configs:
            entry_value = self.entries[key].get()
            try:
                # Try to convert the value
                if entry_value.lower() in ['true', 'false']:
                    self.configs[key] = entry_value.lower() == 'true'
                else:
                    self.configs[key] = int(entry_value) if '.' not in entry_value else float(entry_value)
            except ValueError:
                self.configs[key] = entry_value  # keep as string if conversion fails
        print("Configuration Saved:")
        for key, value in self.configs.items():
            print(f"{key}: {value}")

    def start_process(self):
        print("Process started")
        # Implement the starting logic here

    def stop_process(self):
        print("Process stopped")
        # Implement the stopping logic here


# Set up the root window
root = tk.Tk()
root.geometry("1200x500")  # Adjust size as needed
app = ConfiguratorApp(root)

# Start the application
root.mainloop()
