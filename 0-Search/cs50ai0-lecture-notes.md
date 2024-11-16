Ctrl-Shift-V to Preview

# CS50 Introduction to Artifical Intelligence
## Lesson 0
- Agent (entity that perceives env and acts on it)
- State (config of an agent)
- Action (choices that can be made)
- Transition Model (description of what state results from performing any possible action.
  Defined as a Function:
  Function (state, action) -> state (transition model)
- State Space (set of all states reachable)
- Goal test (how to know you finished)
- Path cost (numerical cost to take this path) [possible minimization of the path cost]

Search Problem
- Initial state
- actions
- transition model
- goal test
- path cost Function

Would like "Optimal Solution" (lowest cost)

Node - a data structure
- a state
- a parent (node that generated this node)
- an action (the action applied to parent to get to node)
- a path cost (from initial state to node)

Approach
- Start with a frontier that contains the initial state
- Start with empty explored set
- Repeat:
  - if the frontier is empty, then no Solution
  - Remove a node from the frontier.
  - If node contains goal state, return the Solution
  - Add the node to the explored set
  - Expand node, add resulting nodes to the frontier (if they are not already in the explored set)

Stack: last-in, first-out (LIFO)
- Depth-first search

Queue: first-in, first-out (FIFO)
- Breadth-first search

Uninformed Search: Depth-first or Breadth-first
Informed Search: using additional information.

Greedy best-first search
- use huristic h(n) to decide which next step when choices (closest to goal)

A* search
- h(n) huristic cost
- g(n) number of steps I had to take to get here
- compare h(n) + g(n) for one way to another
- A* **IS** optimal
  - Admissible h(s) (never overestimates the true cost) and
  - Consistent h(n) (for every node n and successor n' with step c, h(n) <= h(n') + c)

Adversarial Search
- Minimax

Minimax
- MAX playmer aims to maximize score
- MIN player aims to minimize score

Game
- S0 initial state
- Player(s): returns which player to move in state s
- Action(s): returns legal moves in state s
- Result(s,a): returns state after action a taken in state s
- Terminal(s): checks if state s is a terminal state
- Utility(s): final numerical value of terminal state (who won).

Game Minimax optimizations
- Alpha-Beta Pruning (alpha: best I can do so far; beta: worst I can do so far)
- Depth-Limited Minimax (dont' go too deep); uses **Evaluation** function
  - Need an Evaluation function since you can't know which is the win state.

QUIZ - Limit of 8 attempts in a calendar year!!
Got a 3 of 4 (pass)
missed Question 2:
![Q0 Question2](./cs50-ai_notes_quiz0_quest2.png)
