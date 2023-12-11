import re
import collections
import functools
import itertools

"""
"""

from collections import Counter, defaultdict

def read_lines():
    with open("input_large.txt") as file:
        lines = []
        for line in file:
            l = line.strip()
            lines.append(l)

        return lines

def expand_image(space):
    n = len(space)
    m = len(space[0])

    empty_rows = [0] * (len(space[0]) + 1)
    if set(space[0]) == { '.' }:
        empty_rows[0] = 1
    for i in range(1, len(space)):
        empty_rows[i] = empty_rows[i - 1]
        if set(space[i]) == { '.' }:
            empty_rows[i] += 1#0000

    empty_columns = [0] * (len(space[0]) + 1)
    column = '' 
    for i in range(len(space)):
        column += space[i][0]

    if set(column) ==  { '.' }:
        empty_columns[0] = 1
    for i in range(1, len(space[0])):
        empty_columns[i] = empty_columns[i - 1]
        column = ''
        for r in range(len(space)):
            column += space[r][i]
        if set(column) == { '.' }:
            empty_columns[i] += 1#0000

    return empty_rows, empty_columns

def solution(space):
    empty_rows, empty_columns = expand_image(space)
    n = len(space)
    m = len(space[0])
    galaxies = []
    for i in range(n):
        for j in range(m):
            if space[i][j] == '#':
                galaxies.append((i, j))
    pairs = itertools.product(galaxies, galaxies)
    ans = 0
    seen = set()
    for g1, g2 in pairs:
        if str(g2)+str(g1) in seen:
            continue
        seen.add(str(g1)+str(g2))
        x1, y1 = g1
        x2, y2 = g2
        # gotta subtract -1 from 1_000_000
        x2 += (empty_rows[x2] - empty_rows[x1]) * 999999
        y2 += (empty_columns[y2] - empty_columns[y1]) * 999999
        d = abs(x2 - x1) + abs(y2 - y1)# + abs(empty_rows[x2] - empty_rows[x1]) + abs(empty_columns[y2] - empty_columns[y1])
        ans += d
    return ans 

space = read_lines()
print(solution(space))
