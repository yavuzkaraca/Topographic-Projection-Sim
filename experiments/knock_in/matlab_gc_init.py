import numpy as np
import matplotlib.pyplot as plt

# Growth Cone Parameters
num_growth_cones = 40  # Number of growth cones

# Field Parameters
field_size_x = 50
field_size_y = 50

# Constants
fs_fac = 50 / field_size_x  # Field size factor

# Matrix initialization
axon_receptor = np.zeros(num_growth_cones)
axon_ligand = np.zeros(num_growth_cones)

# Initialization of receptor and ligand values
yt_values = []  # List to store yt values

for n in range(num_growth_cones):
    # Calculate the y-coordinate position for the current growth cone
    # Ensures even distribution along the y-axis within the field
    yt = np.round((field_size_y - 1) / (num_growth_cones - 1) * n +
                  (num_growth_cones - field_size_y) / (num_growth_cones - 1))
    yt_values.append(yt)  # Append yt value to the list

    # Calculate sensor values
    axon_receptor[n] = np.exp(fs_fac * 0.05 * (yt - field_size_x / 2))
    axon_ligand[n] = np.exp(fs_fac * -0.05 * (yt - 1 - field_size_x / 2))

# Assuming axon_receptor and axon_ligand are populated as per the Python script
plt.figure(figsize=(10, 6))
plt.plot(axon_receptor, 'o-', label='Growth Cone Receptors')
plt.plot(axon_ligand, 'o-', color='red', label='Growth Cone Ligands')
plt.xlabel('Growth Cone Index')
plt.ylabel('Concentration of Signal Molecules')
plt.title('Initialization of Receptors and Ligands in Growth Cones')
plt.legend()
plt.grid(True)
plt.show()

# Create a scatter plot to visualize the distribution of yt values
plt.figure(figsize=(10, 6))
plt.scatter(range(num_growth_cones), yt_values, color='green', label='yt Values')
plt.xlabel('Growth Cone Index')
plt.ylabel('yt Values')
plt.title('Distribution of yt Values Across Growth Cones')
plt.legend()
plt.grid(True)
plt.show()

# Apply knock-in condition
knockIn = 1  # Adjust knockIn value as needed
for f in range(1, num_growth_cones // 2 + 1):
    n = 2 * f - 1
    axon_receptor[n] += knockIn
    axon_ligand[n] = 1 / axon_receptor[n]  # Adjust ligand based on receptor

# Visualize the distribution of receptors and ligands after knock-in
plt.figure(figsize=(10, 6))
plt.plot(axon_receptor, 'o-', label='Growth Cone Receptors (After Knock-In)')
plt.plot(axon_ligand, 'o-', color='red', label='Growth Cone Ligands (After Knock-In)')
plt.xlabel('Growth Cone Index')
plt.ylabel('Concentration of Signal Molecules')
plt.title('Distribution of Receptors and Ligands in Growth Cones After Knock-In')
plt.legend()
plt.grid(True)
plt.show()