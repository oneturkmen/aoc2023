import re
import collections
import functools
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

def worth_checking_further(record, groups):
    partitions = [p for p in record.split('.') if p != '']

    i = 0
    for partition in partitions:
        if '?' in partition:
            return True
        elif i < len(groups) and len(partition) != groups[i]:
            return False
        else:
            i += 1
    return True


def backtrack(record, groups, seen):
    if record in seen:
        return seen[record]

    if '.' in record and not worth_checking_further(record, groups):
        seen[record] = 0
        return 0

    if '?' not in record:
        if calculate_groups(record) == groups:
            seen[record] = 1
            return 1
        else:
            seen[record] = 0
            return 0

    so_far = 0
    for i, c in enumerate(record):
        if c == '?':
            dotted = record[:i] + '.' + record[i+1:]
            hashed = record[:i] + '#' + record[i+1:] 
            so_far = max(so_far, backtrack(dotted, groups, seen) + backtrack(hashed, groups, seen))
    seen[record] = so_far
    return so_far
    

def solution(lines):
    ans = 0
    for record, groups in lines:
        seen = dict()
        ways = backtrack(record, groups, seen)
        ans += ways
        print(f"'{record}' has {ways} ways")
    return ans


lines = read_lines()
print(solution(lines))
