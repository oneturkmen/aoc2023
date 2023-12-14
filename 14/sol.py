import re
import collections
import functools
import itertools
import pprint

from collections import Counter, defaultdict

def read_lines():
    with open("input_large.txt") as file:
        grid = []
        for line in file:
            grid.append(list(line.strip()))
        return grid

def tilt(grid):
    n = len(grid)
    m = len(grid[0])
    for c in range(m):
        top = 0
        while grid[top][c] == 'O' or grid[top][c] == '#':
            top += 1

        for r in range(n):
            if grid[r][c] == 'O' and r > top:
                grid[top][c] = 'O'
                grid[r][c] = '.'
                top += 1
            elif grid[r][c] == '#':
                top = r + 1
                while top < n and grid[top][c] == 'O':
                    top += 1
    return grid

def calc(grid):
    n = len(grid)
    m = len(grid[0])
    ans = 0
    for r in range(n):
        counts = len([char for char in grid[r] if char == 'O'])
        ans += counts * (n - r)
    return ans

def solution(grid):
    grid = tilt(grid)
    pprint.pprint([''.join(r) for r in grid])
    return calc(grid)

grid = read_lines()
print(solution(grid))
