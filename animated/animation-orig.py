import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Use the Tkinter backend
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

# Constants for the maze
WALL = 1
PATH = 0

# Create a maze, 0 is a path, 1 is a wall
maze = np.array([
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
])

# Define start and end points
start = (0, 0)
end = (4, 4)

# Set up the figure
fig, ax = plt.subplots()
ax.imshow(maze, cmap='binary')

# Disable tick marks and labels
ax.set_xticks([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_yticklabels([])

# Remove the axes' spines
for spine in ax.spines.values():
    spine.set_visible(True)

# You can remove this section if you prefer the look without the gridlines
#ax.set_xticks(np.arange(-.5, maze.shape[1], 1), minor=True)
#ax.set_yticks(np.arange(-.5, maze.shape[0], 1), minor=True)
#ax.grid(which="minor", color="grey", linestyle='-', linewidth=2)
#ax.tick_params(which="minor", size=0)

# Set up the figure
#fig, ax = plt.subplots()
#ax.imshow(maze, cmap='binary')
#ax.set_xticks(np.arange(-.5, maze.shape[1], 1), minor=True)
#ax.set_yticks(np.arange(-.5, maze.shape[0], 1), minor=True)
#ax.grid(which="minor", color="grey", linestyle='-', linewidth=2)
#ax.tick_params(which="minor", size=0)

# DFS algorithm with generator for animation
def dfs(maze, start, end):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == end:
                yield path
                return
            visited.add(vertex)
            for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # right, down, left, up
                next_cell = (vertex[0] + direction[0], vertex[1] + direction[1])
                if (0 <= next_cell[0] < maze.shape[0] and
                        0 <= next_cell[1] < maze.shape[1] and
                        maze[next_cell] == PATH and
                        next_cell not in visited):
                    stack.append((next_cell, path + [next_cell]))
            yield path

# Animation update function
def update(frame):
    path = frame
    ax.clear()
    ax.imshow(maze, cmap='binary')
    ax.grid(which="minor", color="grey", linestyle='-', linewidth=2)
    ys, xs = zip(*path)
    ax.plot(xs, ys, color="blue", linewidth=2, markersize=12)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(True)
           
# Create the animation
anim = FuncAnimation(fig, update, frames=dfs(maze, start, end), interval=500, cache_frame_data=False)

plt.show()

