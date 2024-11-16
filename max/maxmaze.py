import matplotlib
matplotlib.use('TkAgg')  # Use the Tkinter backend
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from random import shuffle

# Maze generation using recursive backtracking
def generate_maze(width, height):
    # Initialize maze grid
    maze = np.zeros((height, width))

    # Define cell and wall
    CELL, WALL = 0, 1

    # Directions to move in the maze
    directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]

    def carve_passages(cx, cy):
        maze[cy, cx] = CELL

        dirs = directions[:]
        shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny, nx] == WALL:
                maze[cy + dy // 2, cx + dx // 2] = CELL
                carve_passages(nx, ny)

    # Start carving passages
    carve_passages(1, 1)
    return maze

# Depth-First Search
def depth_first_search(maze, start, end):
    stack = [start]
    path = []
    visited = set()

    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue

        visited.add((x, y))
        path.append((x, y))

        if (x, y) == end:
            return path

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if maze[ny, nx] == 0 and (nx, ny) not in visited:
                stack.append((nx, ny))

    return path

# Initialize maze
maze_width, maze_height = 21, 21  # Should be odd numbers
maze = generate_maze(maze_width, maze_height)
print(maze)
exit

# Define start and end points
start_point = (1, 1)
end_point = (maze_width - 2, maze_height - 2)

# Perform DFS
path = depth_first_search(maze, start_point, end_point)

# Animation
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(maze, cmap='binary')
ax.set_xticks([])
ax.set_yticks([])

path_x, path_y = zip(*path)
line, = ax.plot(path_x[0], path_y[0], color='red', linewidth=2)

def update(num):
    line.set_data(path_x[:num], path_y[:num])
    return line,

ani = animation.FuncAnimation(fig, update, len(path), interval=50, blit=True)
plt.show()
