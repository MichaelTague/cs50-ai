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
start = (1, 0)
end = (4, 4)

# Set up the figure and axes
fig, ax = plt.subplots()

# DFS algorithm with generator for animation
def dfs(maze, start, end):
    print("dfs just entered")
    stack = [(start, [start])]
    visited = set()
    while stack:
        print()
        print("stack", stack)
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
                    print("Just appended:", stack)
            yield path

# Animation update function
def update(frame):
    print(frame)
    ax.clear()
    ax.imshow(maze, cmap='binary')
    ax.set_xticks([])
    ax.set_yticks([])

    if frame:  # Check if the frame is not empty
        ys, xs = zip(*frame)
        ax.plot(xs, ys, color="blue", linewidth=2)
    ax.plot(start[1], start[0], 'go', markersize=10)  # 'go' means green circle
    ax.plot(end[1], end[0], 'ro', markersize=10)      # 'ro' means red circle

# Initialize the first frame
first_frame = next(dfs(maze, start, end))
update(first_frame)
print("begin animation")
# Create the animation
anim = FuncAnimation(fig, update, frames=dfs(maze, start, end), interval=500, cache_frame_data=False, repeat=False)


#print("start")
#for value in dfs(maze, start, end):
#    print(value)


plt.show()
