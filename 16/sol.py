import re
import collections
import functools
import itertools
import pprint
import copy

from collections import Counter, defaultdict

def read_lines():
    with open("input_large.txt") as file:
        grid = []
        for line in file:
            grid.append(list(line.strip()))
        return grid



def solution(grid, filler):
    n = len(grid)
    m = len(grid[0])

    visited = set()

    def valid(i, j):
        return 0 <= i < n and 0 <= j < m

    def helper(i, j, direction):
        if (i, j, direction) in visited:
            return

        visited.add((i, j, direction))

        # Direction {0, 1, 2, 3}
        # 1 - right
        # 2 - down
        # 3 - left
        # 4 - up
        # Moving right first
        if direction == 1:
            while valid(i, j) and (grid[i][j] == '.' or grid[i][j] == '-'):
                filler[i][j] = '#'
                visited.add((i, j, direction))
                j += 1

            if not valid(i, j):
                return

            filler[i][j] = '#'
            if grid[i][j] == '\\':
                # Go down
                helper(i + 1, j, 2)
            elif grid[i][j] == '/':
                # Go up
                helper(i - 1, j, 4)
            elif grid[i][j] == '|':
                # Go down
                helper(i + 1, j, 2)
                # Go up
                helper(i - 1, j, 4)
        if direction == 2:
            while valid(i, j) and (grid[i][j] == '.' or grid[i][j] == '|'):
                filler[i][j] = '#'
                visited.add((i, j, direction))
                i += 1

            print(i, j)
            if not valid(i, j):
                return

            filler[i][j] = '#'
            if grid[i][j] == '\\':
                # Go right
                helper(i, j + 1, 1)
            elif grid[i][j] == '/':
                # Go left
                helper(i, j - 1, 3)
            elif grid[i][j] == '-':
                # Go right
                helper(i, j + 1, 1)
                # Go left
                helper(i, j - 1, 3)
        if direction == 3:
            while valid(i, j) and (grid[i][j] == '.' or grid[i][j] == '-'):
                filler[i][j] = '#'
                visited.add((i, j, direction))
                j -= 1

            if not valid(i, j):
                return

            filler[i][j] = '#'
            if grid[i][j] == '\\':
                # Go up
                helper(i - 1, j, 4)
            elif grid[i][j] == '/':
                # Go down
                helper(i + 1, j, 2)
            elif grid[i][j] == '|':
                # Go up
                helper(i - 1, j, 4)
                # Go down
                helper(i + 1, j, 2)
        if direction == 4:
            while valid(i, j) and (grid[i][j] == '.' or grid[i][j] == '|'):
                filler[i][j] = '#'
                visited.add((i, j, direction))
                i -= 1
            if not valid(i, j):
                return

            filler[i][j] = '#'
            if grid[i][j] == '\\':
                # Go left
                helper(i, j - 1, 3)
            elif grid[i][j] == '/':
                # Go right
                helper(i, j + 1, 1)
            elif grid[i][j] == '-':
                # Go left
                helper(i, j - 1, 3)
                # Go right
                helper(i, j + 1, 1)


    helper(0, 0, 1)
    ans = 0
    for i in range(n):
        for j in range(m):
            if filler[i][j] == '#':
                ans += 1
    return ans


grid = read_lines()
filler = copy.deepcopy(grid) 
print(solution(grid, filler))
