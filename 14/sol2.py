import re
import collections
import functools
import itertools
import pprint

from functools import cache

from collections import Counter, defaultdict

def read_lines():
    with open("input_large.txt") as file:
        grid = []
        for line in file:
            grid.append(list(line.strip()))
        return grid

def tilt_north(grid, south=False):
    n = len(grid)
    m = len(grid[0])
    if south:
        grid = grid[::-1]
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

    if south:
        grid = grid[::-1]

def tilt_west(grid, east=False):
    n = len(grid)
    m = len(grid[0])
    for r in range(n):
        if east:
            grid[r] = grid[r][::-1]

        top = 0
        while grid[r][top] == 'O' or grid[r][top] == '#':
            top += 1

        for c in range(m):
            if grid[r][c] == 'O' and c > top:
                grid[r][top] = 'O'
                grid[r][c] = '.'
                top += 1
            elif grid[r][c] == '#':
                top = c + 1
                while top < m and grid[r][top] == 'O':
                    top += 1

        if east:
            grid[r] = grid[r][::-1]

def calc(grid):
    n = len(grid)
    m = len(grid[0])
    ans = 0
    for r in range(n):
        counts = len([char for char in grid[r] if char == 'O'])
        ans += counts * (n - r)
    return ans

def solution(grid):
    counts = defaultdict(lambda: [])
    ans = 0
    # 1000 cycles matches 1_000_000_000, because they have the same remainder when divided by 7.
    # Why divided by 7? The sequence keeps repeating itself after 7 numbers, so it's some kind of a cycle.
    for i in range(1000):
        tilt_north(grid)
        tilt_west(grid)
        tilt_north(grid, south=True)
        tilt_west(grid, east=True)
        ans = calc(grid)
        counts[ans].append(i)

    return ans 

grid = read_lines()
print(solution(grid))
