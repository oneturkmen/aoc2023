import re
import collections
import functools
import math
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

    targets = []
    for node in connections.keys():
        if node.endswith("A"):
            targets.append(node)

    steps = []
    for curr_node in targets:
        queue = [curr_node]
        i = 0
        ans = 0

        while len(queue) > 0:
            n = len(queue)

            finish = True
            for j in range(n):
                if not queue[j].endswith("Z"):
                    finish = False
                    break

            if finish:
                break

            for j in range(n):
                conns = connections[queue.pop(0)]
                queue.append(conns[int(instructions[i % len(instructions)])])

            ans += 1
            i += 1

        steps.append(ans)
    
    return math.lcm(*steps)

instructions, connections = read_lines()
print(solution(instructions, connections))
