import re
import functools
import pprint

from collections import deque

"""
"""
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(100000000)

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
    
    def find_start_pos(self, grid):
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

        return s_i, s_j

    def valid_move(self, i, j, c, direction, n, m):
        if not (i >= 0 and i < n and j >= 0 and j < m):
            return False

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

        return direction in valid_dirs.get(c, [])

    def init_queue(self, grid):
        n = len(grid)
        m = len(grid[0])
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
    
    def get_starting_positions_for_walking(self, s_i, s_j, grid):
        n = len(grid)
        m = len(grid[0])
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

    def flood_fill(self, queue, grid):
        n = len(grid)
        m = len(grid[0])
        while len(queue) > 0:
            i, j = queue.pop(0)
            for di, dj in [[0, -1], [-1, 0], [1, 0], [0, 1]]:
                ni, nj = i + di, j + dj
                if ni >= 0 and ni < n and nj >= 0 and nj < m and grid[ni][nj] != '#':
                    grid[ni][nj] = '#'
                    queue.append((ni, nj))
        return grid

    def solution(self, grid):
        grid = self.expand_grid(grid)
        s_i, s_j = self.find_start_pos(grid)

        q = deque()
        n = len(grid)
        m = len(grid[0])

        grid[s_i][s_j] = '#'
        q.extend(self.get_starting_positions_for_walking(s_i, s_j, grid))
        while len(q) > 0:
            i, j = q.popleft()
            if grid[i][j] == '#':
                continue

            c = grid[i][j]
            grid[i][j] = '#'

            # Left
            if self.valid_move(i, j - 1, c, "left", n, m) and grid[i][j - 1] in ["F", "L", "-", "="]:
                q.append((i, j - 1))
            # Bottom
            elif self.valid_move(i + 1, j, c, "bottom", n, m) and grid[i + 1][j] in ["J", "L", "|", "!"]:
                q.append((i + 1, j))
            # Right
            elif self.valid_move(i, j + 1, c, "right", n, m) and grid[i][j + 1] in ["J", "7", "-", "="]:
                q.append((i, j + 1))
            # Up
            elif self.valid_move(i - 1, j, c, "up", n, m) and grid[i - 1][j] in ["7", "F", "|", "!"]:
                q.append((i - 1, j))

        # Flooding! 
        queue = self.init_queue(grid)
        grid = self.flood_fill(queue, grid)

        ans = 0
        ignored_chars = set(['#', ' ', '!', '='])
        for row in [''.join(row) for row in grid]:
            ans += len(list(filter(lambda c : c not in ignored_chars, row)))

        return ans

grid = read_lines()
print(Solution().solution(grid))
