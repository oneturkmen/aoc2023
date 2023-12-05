import re
import collections

def read_lines():
    lines = []
    with open("input_large.txt") as file:
        curr_line = []
        for line in file:
            if line.strip():
                curr_line.append(line.strip())
            else:
                lines.append(curr_line)
                curr_line = []
        if curr_line != []:
            lines.append(curr_line)

    return lines

def get_range_dictionary(list_of_nums):
    d = []
    for nums in list_of_nums:
        end, start, length = [int(num) for num in nums.split(' ')]
        d.append([(start,length-1),(end,length-1)])
    return d

def get_value(key, intervals):
    for left, right in intervals:
        if left[0] <= key <= left[0] + left[1]:
            return right[0] + key - left[0]
    return key

def solution(text):
    seeds = []
    raw_seeds = text[0][0].replace("seeds: ", "").split(' ')
    for i in range(0, len(raw_seeds), 2):
        seeds.append((int(raw_seeds[i]), int(raw_seeds[i + 1])-1))

    d1 = get_range_dictionary(text[1][1:])
    d2 = get_range_dictionary(text[2][1:])
    d3 = get_range_dictionary(text[3][1:])
    d4 = get_range_dictionary(text[4][1:])
    d5 = get_range_dictionary(text[5][1:])
    d6 = get_range_dictionary(text[6][1:])
    d7 = get_range_dictionary(text[7][1:])

    locations = []
    cache = []
    min_val = 10**11 + 10
    for seed, length in seeds:
        i = seed
        print(f"Looking at seed {seed}")

        found = False
        for checked_from, checked_to in cache:
            if checked_from <= seed <= checked_to:
                print(f"!! Used cache !!")
                found = True
                break
        if found:
            continue

        min_seed_range = 10**11 + 10
        while i <= seed + length:
            v1 = get_value(i, d1)
            v2 = get_value(v1, d2)
            v3 = get_value(v2, d3)
            v4 = get_value(v3, d4)
            v5 = get_value(v4, d5)
            v6 = get_value(v5, d6)
            v7 = get_value(v6, d7)
            i += 1

            min_seed_range = min(min_seed_range, v7)
            min_val = min(min_val, v7)

        cache.append((seed,length-1))

    return min_val 


text = read_lines()
print(solution(text))
