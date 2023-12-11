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

    new_space = space

    i = 0
    while i < n:
        if space[i] == '.' * n:
            new_space.insert(i, '.' * n)
            i += 1
        i += 1

    j = 0
    while j < len(space[0]):
        column = ''
        for i in range(len(space)): 
            column += space[i][j]
        if column == '.' * len(space):
            for i in range(len(space)):
                s = list(new_space[i])
                s.insert(j, '.')
                new_space[i] = ''.join(s)
            j += 1
        j += 1

    return new_space

def solution(space):
    space = expand_image(space)
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
        d = abs(x2 - x1) + abs(y2 - y1)
        ans += d
    return ans

space = read_lines()
print(solution(space))
