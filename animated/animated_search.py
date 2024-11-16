import numpy as np
from queue import PriorityQueue
import matplotlib
matplotlib.use('TkAgg')  # Use the Tkinter backend
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque
import time
import sys

# Constants for the maze
WALL = 1
PATH = 0
first = True

if not (3 <= len(sys.argv) <= 4):
    print("Syntax: python", sys.argv[0], "[dfs bfs best astar] MazeFile (speed in ms)")
    sys.exit(1)
if len(sys.argv) == 4:
    speed=sys.argv[3]
else:
    speed=100

# Read the maze from the file and convert it into a NumPy array
# Spaces become 0's, #'s become 1's, A becomes 2, B becomes 3
file_path = sys.argv[2]
with open(file_path, 'r') as file:
    maze = np.array([[" #AB".index(char) for char in line.rstrip('\n')] for line in file])

# Set start, fix maze
row, col = np.where(maze == 2)
start = (row[0], col[0])
maze[start] = PATH

# Set end, fix maze
row, col = np.where(maze == 3)
end = (row[0], col[0])
maze[end] = PATH

# Set up the figure and axes
fig, ax = plt.subplots()
fig.canvas.manager.window.title(file_path)

# Depth-first Search
def dfs(maze, start, end, pause=True):
    stack = [(start, [start])]
    visited = set()
    visited_paths = set()
    yields = 0
    if pause:
        input("Start Depth First Search? ")
        start_time = time.time()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            visited_paths.add(tuple(path))
            if vertex == end:
                yields += 1
                yield (path, visited_paths)
                elapsed_time = round(time.time() - start_time)
                print(f"Path steps: {len(path)}.  Steps tried: {yields}.  Elapsed time: {elapsed_time} seconds.")
                return
            visited.add(vertex)
            for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                next_cell = (vertex[0] + direction[0], vertex[1] + direction[1])
                if (0 <= next_cell[0] < maze.shape[0] and
                        0 <= next_cell[1] < maze.shape[1] and
                        maze[next_cell] == PATH and
                        next_cell not in visited):
                    stack.append((next_cell, path + [next_cell]))
            yields += 1
            yield (path, visited_paths)

# Breadth-first Search
def bfs(maze, start, end, pause=True):
    queue = deque([(start, [start])])
    visited = set()
    visited_paths = set()
    yields = 0
    if pause:
        input("Start Breadth First Search? ")
        start_time = time.time()
    while queue:
        (vertex, path) = queue.popleft()
        if vertex not in visited:
            visited_paths.add(tuple(path))
            if vertex == end:
                yields += 1
                yield (path, visited_paths)
                elapsed_time = round(time.time() - start_time)
                print(f"Path steps: {len(path)}.  Steps tried: {yields}.  Elapsed time: {elapsed_time} seconds.")
                return
            visited.add(vertex)
            for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                next_cell = (vertex[0] + direction[0], vertex[1] + direction[1])
                if (0 <= next_cell[0] < maze.shape[0] and
                        0 <= next_cell[1] < maze.shape[1] and
                        maze[next_cell] == PATH and
                        next_cell not in visited):
                    queue.append((next_cell, path + [next_cell]))
            yields += 1
            yield (path, visited_paths)

# Manhattan distance heuristic
def h(current, end):
    return abs(current[0] - end[0]) + abs(current[1] - end[1])

# Best-first Search
def bestfs(maze, start, end, pause=True):
    frontier = PriorityQueue()
    frontier.put((0, start, [start]))  # (priority, current_node, path)
    visited = set()
    visited_paths = set()
    yields = 0
    if pause:
        input("Start Best First Search? ")
        start_time = time.time()
    while not frontier.empty():
        _, current, path = frontier.get()
        if current in visited:
            continue
        visited.add(current)
        visited_paths.add(tuple(path))

        # Yield the current path
        yields += 1
        yield (path, visited_paths)

        if current == end:
            elapsed_time = round(time.time() - start_time)
            print(f"Path steps: {len(path)}.  Steps tried: {yields}.  Elapsed time: {elapsed_time} seconds.")
            return  # Stop the generator once the end is reached

        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_cell = (current[0] + direction[0], current[1] + direction[1])
            if (0 <= next_cell[0] < maze.shape[0] and
                    0 <= next_cell[1] < maze.shape[1] and
                    maze[next_cell] == PATH and
                    next_cell not in visited):
                new_path = path + [next_cell]
                priority = h(next_cell, end)
                frontier.put((priority, next_cell, new_path))

def astar(maze, start, end, pause=True):
    frontier = PriorityQueue()
    frontier.put((0, start, [start]))  # (priority, current_node, path)
    g_costs = {start: 0}
    visited = set()
    visited_paths = set()
    yields = 0
    if pause:
        input("Start A* Search? ")
        start_time = time.time()
    while not frontier.empty():
        _, current, path = frontier.get()
        if current in visited:
            continue
        visited.add(current)
        visited_paths.add(tuple(path))

        # Yield the current path
        yields += 1
        yield (path, visited_paths)

        if current == end:
            elapsed_time = round(time.time() - start_time)
            print(f"Path steps: {len(path)}.  Steps tried: {yields}.  Elapsed time: {elapsed_time} seconds.")
            return  # Stop the generator once the end is reached

        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_cell = (current[0] + direction[0], current[1] + direction[1])
            if (0 <= next_cell[0] < maze.shape[0] and
                    0 <= next_cell[1] < maze.shape[1] and
                    maze[next_cell] == PATH and
                    next_cell not in visited):
                new_g = g_costs[current] + 1  # Assuming each step costs 1
                if next_cell not in g_costs or new_g < g_costs[next_cell]:
                    g_costs[next_cell] = new_g
                    priority = new_g + h(next_cell, end)
                    new_path = path + [next_cell]
                    frontier.put((priority, next_cell, new_path))


# Animation update function
def update(frame):
    path, visited_paths = frame
    ax.clear()
    ax.imshow(maze, cmap='binary')
    ax.set_xticks([])
    ax.set_yticks([])

    # Plot all visited_paths in orange
    for visited_path in visited_paths:
        if visited_path != path:
            ys, xs = zip(*visited_path)
            ax.plot(xs, ys, color="orange", linewidth=1)
    
    # Plot the current path in blue
    if path:
        ys, xs = zip(*path)
        ax.plot(xs, ys, color="blue", linewidth=2)
        
    ax.plot(start[1], start[0], 'go', markersize=10)  # 'go' means green circle
    ax.plot(end[1], end[0], 'ro', markersize=10)      # 'ro' means red circle

# Initialize the first frame
start_time = time.time()

first_frame = next(dfs(maze, start, end, False))
update(first_frame)

# Create the animation
if sys.argv[1] == "dfs":
    anim = FuncAnimation(fig, update, frames=dfs(maze, start, end), interval=speed, cache_frame_data=False, repeat=False)
elif sys.argv[1] == "best":
    anim = FuncAnimation(fig, update, frames=bestfs(maze, start, end), interval=speed, cache_frame_data=False, repeat=False)
elif sys.argv[1] == "astar":
    anim = FuncAnimation(fig, update, frames=astar(maze, start, end), interval=speed, cache_frame_data=False, repeat=False)
else:
    anim = FuncAnimation(fig, update, frames=bfs(maze, start, end), interval=speed, cache_frame_data=False, repeat=False)

plt.show()
