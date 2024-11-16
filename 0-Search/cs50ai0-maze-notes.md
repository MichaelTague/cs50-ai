# 0-Search Maze

The maze dir contains a modified version of the downloadable maze.py from the class along with maze.html which is used to display a web page for the results in addition to the .png file.

It also has been modified to display the attempted search as well as the found path.

## maze.py

Main function:

```Python
#Main
m = Maze(sys.argv[1])
print("Maze:")
m.print()
print("Solving...")
m.solve()
print("States Explored:", m.num_explored)
print("Solution:")
m.print(show_explored=True)
m.output_image("maze.png", show_explored=True)

```

## Modifications
```python
import webbrowser

# This was embeded within the row/column loops
    html_maze = []
        html_maze_row = []
            html_maze_row.append(1)    # print("█", end="")
            html_maze_row.append('A')  # print("A", end="")
            html_maze_row.append('B')  # print("B", end="")
            html_maze_row.append(-1)   # print("*", end="")
            html_maze_row.append(0)    # print(" ", end="")
            html_maze_row.append(-2)   # print(".", end="")
            html_maze.append(html_maze_row)
    html_maze_string = str(html_maze).replace(' ', '').replace("'", "\"")
    webbrowser.open("file:///home/mt/projects/cs50-ai/0-Search/mt1/maze.html?maze=" + html_maze_string)
```
