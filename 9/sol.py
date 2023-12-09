import re
import collections
import functools

"""
"""

from collections import Counter, defaultdict

def read_lines():
    with open("input.txt") as file:
        tests = []
        for line in file:
            items = [int(num) for num in line.strip().split(' ')]
            tests.append(items)

        return tests 

def get_pred(nums):
    k = len(nums) - 1
    while k >= 0 and nums[0:k] != [0] * k:
        for i in range(k):
            nums[i] = nums[i + 1] - nums[i]

        k -= 1
    return sum(nums)

part2 = False
def solution(tests):
    ans = 0
    for nums in tests:
        if part2:
            nums = list(reversed(nums))
        n = get_pred(nums)
        ans += n
    return ans

tests = read_lines()
print(solution(tests))
