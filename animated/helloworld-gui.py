import matplotlib
matplotlib.use('TkAgg')  # Use the Tkinter backend
import matplotlib.pyplot as plt

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Set a title for the axes
ax.set_title('Hello World')

# Hide the axes
ax.axis('off')

# Show the plot
plt.show()

