import sys
import ast
import webbrowser

with open('maze1.list', 'r') as file:
    maze_string = file.read().replace('\n', '').replace(' ', '')
    maze = ast.literal_eval(maze_string)
rows = len(maze)
columns = len(maze[0])

for i in range(rows):
    for j in range(columns):
        if maze[i][j] == "A":
            a = [i, j]
        if maze[i][j] == "B":
            b = [i, j]

h = [[None for _ in range(rows)] for _ in range(columns)]
for i in range(rows):
    for j in range(columns):
        h = i
        if maze[i][j] == "A":
            a = [i, j]
        if maze[i][j] == "B":
            b = [i, j]

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier():
    def __init__(self):
        self.frontier = []
    
    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

    def QueueFrontier(StackFrontier):

        def remove(self):
            if self.empty():
                raise Exception("empty frontier")
            else:
                node = self.frontier[0]
                self.frontier = self.frontier[1:]
                return node

class Maze():
    def __init__(self, filename):

webbrowser.open("file:///home/mt/projects/cs50-ai/maze/maze.html?maze=" + maze_string)
