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

def horizontal_mirror(grid):
    for i in range(len(grid) - 1):
        start = i
        end = i + 1
        complete_reflection = True
        while start >= 0 and end < len(grid):
            if grid[start] != grid[end]:
                complete_reflection = False
                break

            start -= 1
            end += 1

        if complete_reflection:
            return i + 1

    return 0

def equal_columns(grid, col1, col2):
    for row in grid:
        if row[col1] != row[col2]:
            return False
    return True

def vertical_mirror(grid):
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

        if mirror:
            return column_i + 1

    return 0

def backtrack(grid):
    lines = horizontal_mirror(grid), vertical_mirror(grid)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = '#' if grid[i][j] == '.' else '.'
            new_lines = horizontal_mirror(grid), vertical_mirror(grid)
            grid[i][j] = '#' if grid[i][j] == '.' else '.'

            print(lines, new_lines)

            if new_lines[0] != 0 and lines[0] != new_lines[0]:
                return new_lines[0] * 100
            if new_lines[1] != 0 and lines[1] != new_lines[1]:
                return new_lines[1]

def solution(grids):
    ans = 0
    for grid in grids:
        #ans += 100 * horizontal_mirror(grid)
        #ans += vertical_mirror(grid)
        ans += backtrack(grid)
    return ans

grids = read_lines()
print(solution(grids))
