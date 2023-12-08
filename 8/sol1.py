import re
import collections
import functools

"""
"""

from collections import Counter, defaultdict

def read_lines():
    with open("input_large.txt") as file:
        instructions = file.readline().strip('\n')
        file.readline()

        connections = {}

        for line in file:
            items = line.strip().split(' ')
            connections[items[0]] = [items[2][1:-1], items[3][:-1]]

        return instructions, connections
    
def solution(instructions, connections):
    instructions = list(map(lambda c : '0' if c == 'L' else '1', instructions))

    initial_list = {}
    queue = ["AAA"]
    i = 0
    ans = 0
    while len(queue) > 0:
        curr = queue.pop()
        if curr == "ZZZ":
            return ans
        ans += 1
        conns = connections[curr]
        queue.append(conns[int(instructions[i % len(instructions)])])
        i += 1

instructions, connections = read_lines()
print(solution(instructions, connections))
