import re
import functools
import pprint

from collections import deque

"""
"""
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(1000000000)
import threading
threading.stack_size(134217728)   # for your needs

def read_lines():
    with open("input_large.txt") as file:
        grid = []
        for line in file:
            grid.append(list(line.strip()))

        return grid 

def bounds_ok(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

class Solution:
    def expand_grid(self, grid):
        n = len(grid)
        m = len(grid[0])
        expanded_grid = [[' ' for x in range(2*m-1)] for y in range(2*n-1)]

        for i, row in enumerate(expanded_grid):
            for j, c in enumerate(row):
                if i % 2 == 0 and j % 2 == 0:
                    expanded_grid[i][j] = grid[i // 2][j // 2]
                elif i % 2 == 0 and j % 2 != 0:
                    expanded_grid[i][j] = '='
                elif i % 2 != 0 and j % 2 == 0:
                    expanded_grid[i][j] = '!'

        return expanded_grid

    def solution(self, grid):
        grid = self.expand_grid(grid)

        n = len(grid)
        m = len(grid[0])
        s_i, s_j = 0, 0
        for i in range(n):
            found = False
            for j in range(m):
                if grid[i][j] == 'S':
                    s_i = i
                    s_j = j
                    found = True
                    break
            if found:
                break

        self.step = 0

        valid_dirs = {
            "F": ["bottom", "right"],
            "L": ["up", "right"],
            "|": ["up", "bottom"],
            "-": ["left", "right"],
            "7": ["left", "bottom"],
            "J": ["left", "up"],
            "=": ["left", "right"],
            "!": ["up", "bottom"],
        }
        #steps = [[0 for c in range(m)] for r in range(n)]
        def valid(i, j, c, direction):
            if not (i >= 0 and i < n and j >= 0 and j < m):
                return False

            return direction in valid_dirs.get(c, [])

        def init_start(s_i, s_j, n, m):
            start_positions = []

            if bounds_ok(s_i - 2, s_j, n, m) and grid[s_i - 2][s_j] in {'F', '|', '7'}:
                grid[s_i-1][s_j] = '#'
                start_positions.append([s_i - 2, s_j])

            if bounds_ok(s_i + 2, s_j, n, m) and grid[s_i + 2][s_j] in {'J', '|', 'L'}:
                grid[s_i+1][s_j] = '#'
                start_positions.append([s_i + 2, s_j])

            if bounds_ok(s_i, s_j - 2, n, m) and grid[s_i][s_j - 2] in {'F', '-', 'L'}:
                grid[s_i][s_j-1] = '#'
                start_positions.append([s_i, s_j - 2])

            if bounds_ok(s_i, s_j + 2, n, m) and grid[s_i][s_j + 2] in {'J', '-', '7'}:
                grid[s_i][s_j+1] = '#'
                start_positions.append([s_i, s_j + 2])

            return start_positions


        grid[s_i][s_j] = '#'
        q = deque()
        q.extend(init_start(s_i, s_j, n, m))
        while len(q) > 0:
            i, j = q.popleft()
            if grid[i][j] == '#':
                continue

            c = grid[i][j]
            grid[i][j] = '#'

            # Left
            if valid(i, j - 1, c, "left") and grid[i][j - 1] in ["F", "L", "-", "="]:
                q.append((i, j - 1))
            # Bottom
            elif valid(i + 1, j, c, "bottom") and grid[i + 1][j] in ["J", "L", "|", "!"]:
                q.append((i + 1, j))
            # Right
            elif valid(i, j + 1, c, "right") and grid[i][j + 1] in ["J", "7", "-", "="]:
                q.append((i, j + 1))
            # Up
            elif valid(i - 1, j, c, "up") and grid[i - 1][j] in ["7", "F", "|", "!"]:
                q.append((i - 1, j))

        def init_queue():
            positions = []


            for i in range(n):
                # Add first and last columns
                if grid[i][0] != '#':
                    positions.append((i, 0))
                if grid[i][m-1] != '#':
                    positions.append((i, m-1))

            for j in range(m):
                # Add first and last rows
                if grid[0][j] != '#':
                    positions.append((0, j))
                if grid[n-1][j] != '#':
                    positions.append((n-1, j))

            return positions
            
        
        queue = init_queue()

        while len(queue) > 0:
            i, j = queue.pop(0)
            for di, dj in [[0, -1], [-1, 0], [1, 0], [0, 1]]:
                ni, nj = i + di, j + dj
                if ni >= 0 and ni < n and nj >= 0 and nj < m and grid[ni][nj] != '#':
                    grid[ni][nj] = '#'
                    queue.append((ni, nj))

        walked_grid = [''.join(row) for row in grid]

        ans = 0
        for row in walked_grid:
            ans += len(list(filter(lambda c : c != '#' and c != ' ' and c != '!' and c != '=', row)))

        return ans

grid = read_lines()
print(Solution().solution(grid))
