import matplotlib
matplotlib.use('Agg')  # Use 'Agg' backend for non-GUI environments
import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots()

# Plot a simple line
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])

# Save the figure
fig.savefig('hello_world.png')
