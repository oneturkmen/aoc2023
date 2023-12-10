import re
import collections
import functools
import pprint

"""
"""
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(20000)

from collections import Counter, defaultdict

def read_lines():
    with open("input_large.txt") as file:
        grid = []
        for line in file:
            grid.append(list(line.strip()))

        return grid 

class Solution:
    def solution(self, grid):
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

        curr_i, curr_j = s_i, s_j
        self.step = 0

        #print(curr_i, curr_j)

        #steps = [[0 for c in range(m)] for r in range(n)]
        def valid(i, j, c, direction):
            if not (i >= 0 and i < n and j >= 0 and j < m):
                return False
            
            if c == 'S':
                return True

            valid_dirs = {
                "F": ["bottom", "right"],
                "L": ["up", "right"],
                "|": ["up", "bottom"],
                "-": ["left", "right"],
                "7": ["left", "bottom"],
                "J": ["left", "up"],
            }

            return direction in valid_dirs.get(c, [])

        #self.valid_conns = {
        #    "F": ["J", "7", "-", "|", "L"],
        #    "L": ["J", "7", "-", "|", "F"],
        #    "J": ["F", "L", "-", "|", "7"],
        #    "-": ["J", "7", "F", "L"],
        #    "|": ["7", "F", "J", "F"],
        #    "S": ["7", "F", "J", "-", "|"]
        #}

        #pprint.pprint(grid)

        def helper(i, j):
            if grid[i][j] == '.':
                return

            c = grid[i][j]

            # Visited
            #if grid[i][j] != 'S':
            #    for di, dj in self.valid_dirs[grid[i][j]]:
            #        new_i = i + di
            #        new_j = j + dj
            #        if valid(new_j, new_j) and grid[new_i][new_j] in self.valid_conns[grid[i][j]] and grid[new_i][new_j] != '.':
            #            grid[i][j] = '.'
            #            return helper(new_i, new_j)
            #else:
            # Left
            if valid(i, j - 1, c, "left") and grid[i][j - 1] in ["F", "L", "-"]:
                #print("left")
                grid[i][j] = '.'
                self.step += 1
                helper(i, j - 1)
            # Bottom
            elif valid(i + 1, j, c, "bottom") and grid[i + 1][j] in ["J", "L", "|"]:
                #print("bottom")
                grid[i][j] = '.'
                self.step += 1
                helper(i + 1, j)
            # Right
            elif valid(i, j + 1, c, "right") and grid[i][j + 1] in ["J", "7", "-"]:
                #print("right")
                grid[i][j] = '.'
                self.step += 1
                helper(i, j + 1)
            # Up
            elif valid(i - 1, j, c, "up") and grid[i - 1][j] in ["7", "F", "|"]:
                #print("up")
                grid[i][j] = '.'
                self.step += 1
                helper(i - 1, j)

        helper(s_i, s_j)

        return (self.step+1) // 2


grid = read_lines()
print(Solution().solution(grid))
