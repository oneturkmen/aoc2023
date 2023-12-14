import re
import collections
import functools
import itertools
import pprint

from collections import Counter, defaultdict

def read_lines():
    with open("input_large.txt") as file:
        grids = []
        grid = []
        for line in file:
            if line.strip() == '':
                grids.append(grid)
                grid = []
            else:
                grid.append(list(line.strip()))
        grids.append(grid)

        return grids

def horizontal_mirror(grid, prev_h):
    for i in range(len(grid) - 1):
        start = i
        end = i + 1
        mirror = True
        while start >= 0 and end < len(grid):
            if grid[start] != grid[end]:
                mirror = False
                break

            start -= 1
            end += 1

        if mirror and prev_h != i + 1:
            return i + 1

    return 0

def equal_columns(grid, col1, col2):
    for row in grid:
        if row[col1] != row[col2]:
            return False
    return True

def vertical_mirror(grid, prev_v):
    column_sz = len(grid[0])
    for column_i in range(column_sz - 1):
        start = column_i
        end = column_i + 1

        mirror = True
        
        while start >= 0 and end < column_sz:
            if not equal_columns(grid, start, end):
                mirror = False
                break
            start -= 1
            end += 1

        if mirror and prev_v != column_i + 1:
            return column_i + 1

    return 0

def backtrack(grid):
    h, v = horizontal_mirror(grid, -1), vertical_mirror(grid, -1)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = '#' if grid[i][j] == '.' else '.'
            new_h, new_v = horizontal_mirror(grid, h), vertical_mirror(grid, v)
            grid[i][j] = '#' if grid[i][j] == '.' else '.'

            if new_h != 0:
                return new_h * 100
            if new_v != 0:
                return new_v 

def solution(grids):
    part1 = True
    ans = 0
    for grid in grids:
        if part1:
            ans += 100 * horizontal_mirror(grid, -1)
            ans += vertical_mirror(grid, -1)
        else:
            ans += backtrack(grid)
    return ans

grids = read_lines()
print(solution(grids))
