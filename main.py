from collections import deque
from queue import PriorityQueue
from time import time
import random
import math
import sys

sys.setrecursionlimit(20000)

MAX_DEPTH = 30
SOLVABLE_15 = [9, 1, 5, 4, 2, 16, 11, 15, 10, 3, 6, 8, 13, 7, 14, 12]
SOLV = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 15]
UNSOLVABLE_15 = [11, 6, 16, 8, 15, 4, 12, 7, 5, 9, 3, 2, 1, 13, 10, 14]
SOLVABLE_8 = [8, 7, 4, 9, 2, 3, 5, 6, 1]
UNSOLVABLE_8 = [5, 8, 9, 2, 7, 6, 3, 1, 4]


board = Board(4)
solver = Solver(board)
print("Initial State:\n")
print(board.initial_state.to_sequence())
print("\nSolving using Breadth First Search")
solver.solve(Search.BFS)
print("\nSolving using A Star with Manhattan Disticant heuristic")
solver.solve(Search.AStar)
