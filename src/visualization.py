import matplotlib.pyplot as plt

# Your substrate string representation (replace this with your actual string)
substrate_str = "(1,0) (0.5, 0.5) (0,1)\n(1,0) (0.5, 0.5) (0,1)\n(1,0) (0.5, 0.5) (0,1)"

# Split the string into rows
rows = substrate_str.split('\n')

# Initialize arrays to store ligand and receptor values
ligand_values = []
receptor_values = []

# Parse the rows and extract ligand and receptor values
for row in rows:
    values = row.split(' ')
    ligand_values_row = []
    receptor_values_row = []
    for value in values:
        # Split by ',' and handle empty strings
        parts = value.strip('()').split(',')
        if len(parts) == 2:
            ligand, receptor = parts
            ligand_values_row.append(float(ligand))
            receptor_values_row.append(float(receptor))
    ligand_values.append(ligand_values_row)
    receptor_values.append(receptor_values_row)

# Create a simple visualization using imshow
plt.figure(figsize=(6, 6))

# Visualize ligand values
plt.subplot(121)
plt.imshow(ligand_values, cmap='viridis')
plt.title("Ligand")

# Visualize receptor values
plt.subplot(122)
plt.imshow(receptor_values, cmap='viridis')
plt.title("Receptor")

plt.show()
