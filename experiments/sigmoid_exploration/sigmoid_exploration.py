from matplotlib import pyplot as plt
from simulation.simulation import calculate_ff_coef

# Configuration for the scenarios
configs = [
    {'sigmoid_gain': 2, 'sigmoid_shift': 0},
    {'sigmoid_gain': 2, 'sigmoid_shift': 0.3},
    {'sigmoid_gain': 2, 'sigmoid_shift': -0.3},
    {'sigmoid_gain': 8, 'sigmoid_shift': -0.4},
    {'sigmoid_gain': 10, 'sigmoid_shift': 0}

]

num_steps = 1000
steps = range(num_steps)  # Creating a range for the step numbers

# Plotting
plt.figure(figsize=(10, 8))
for config in configs:
    # Calculating step ratios for each configuration
    step_ratios = [calculate_ff_coef(step, num_steps, config['sigmoid_gain'], config['sigmoid_shift'])
                   for step in steps]
    plt.plot(steps, step_ratios, label=f"Gain (k): {config['sigmoid_gain']}, Shift: {config['sigmoid_shift']}")

plt.title('Step Ratio Across Different Sigmoid Configurations')
plt.xlabel('Step Number')
plt.ylabel('Step Ratio')
plt.legend()
plt.grid(True)
plt.show()
