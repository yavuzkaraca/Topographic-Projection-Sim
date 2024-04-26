import numpy as np
import matplotlib.pyplot as plt

# Growth Cone Parameters
num_growth_cones = 20  # Number of growth cones != 1

# Field Parameters
field_size_x = 50
field_size_y = 8

# Constants
fs_fac = 50 / field_size_x  # Field size factor

# Matrix initialization
axon_receptor = np.zeros(num_growth_cones)
axon_ligand = np.zeros(num_growth_cones)

# Initialization of receptor and ligand values
for n in range(num_growth_cones):
    position_factor = (field_size_y - 1) / (num_growth_cones - 1)
    position_offset = (num_growth_cones - field_size_y) / (num_growth_cones - 1)
    yt = np.round(position_factor * n + position_offset)

    # Calculate receptor values
    receptor_exponent = fs_fac * 0.05 * (yt - field_size_x / 2)
    axon_receptor[n] = np.exp(receptor_exponent)

    # Calculate ligand values
    ligand_exponent = fs_fac * -0.05 * (yt - 1 - field_size_x / 2)
    axon_ligand[n] = np.exp(ligand_exponent)


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
