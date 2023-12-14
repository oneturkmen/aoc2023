import re
import collections
from functools import cache
import itertools

"""
"""

from collections import Counter, defaultdict

def calculate_groups(s):
    if '?' in s:
        return -1

    groups = [subs for subs in s.split('.') if subs != '']
    num_of_groups = [len(group) for group in groups]

    return num_of_groups

def read_lines():
    with open("input_large.txt") as file:
        lines = []
        for line in file:
            record, groups = line.strip().split(' ')
            groups = [int(n) for n in groups.split(',')]
            lines.append([record, groups])
        return lines

@cache
def backtrack(record, groups, group_size):
    if record == '':
        if len(groups) == 0 and group_size == 0:
            return 1
        elif len(groups) == 1 and groups[0] == group_size:
            return 1
        else:
            return 0

    spring = record[0]
    rest_of_record = record[1:]
    curr_group = groups[0] if len(groups) > 0 else 0
    rest_of_groups = groups[1:]

    if spring == '?':
        options_with_hash = backtrack('#' + rest_of_record, groups, group_size)
        options_with_dot = backtrack('.' + rest_of_record, groups, group_size)
        return options_with_hash + options_with_dot
    elif spring == '#':
        if curr_group == 0:
            return 0
        elif group_size > curr_group:
            return 0
        else:
            return backtrack(rest_of_record, groups, group_size + 1)

    elif spring == '.':
        if group_size == curr_group:
            return backtrack(rest_of_record, rest_of_groups, 0)
        elif group_size == 0:
            return backtrack(rest_of_record, groups, 0)
        else:
            return 0


def solution(lines):
    part1 = False
    ans = 0
    for record, groups in lines:
        ways = 0
        if part1:
            ways = backtrack(record, tuple(groups), 0)
        else:
            ways = backtrack('?'.join([record] * 5), tuple(groups) * 5, 0) 
        ans += ways
        #print(f"'{record}' has {ways} ways")
    return ans


lines = read_lines()
print(solution(lines))
