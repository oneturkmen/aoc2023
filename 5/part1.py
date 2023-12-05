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
    seeds = [int(seed) for seed in text[0][0].replace("seeds: ", "").split(' ')]

    d1 = get_range_dictionary(text[1][1:])
    d2 = get_range_dictionary(text[2][1:])
    d3 = get_range_dictionary(text[3][1:])
    d4 = get_range_dictionary(text[4][1:])
    d5 = get_range_dictionary(text[5][1:])
    d6 = get_range_dictionary(text[6][1:])
    d7 = get_range_dictionary(text[7][1:])

    print(text)
    
    locations = []
    for seed in seeds:
        v1 = get_value(seed, d1)
        v2 = get_value(v1, d2)
        v3 = get_value(v2, d3)
        v4 = get_value(v3, d4)
        v5 = get_value(v4, d5)
        v6 = get_value(v5, d6)
        v7 = get_value(v6, d7)

        locations.append(v7)
    return min(locations)

    """
    ['seed-to-soil map:', '50 98 2', '52 50 48'],
    ['soil-to-fertilizer map:', '0 15 37', '37 52 2', '39 0 15'], 
    ['fertilizer-to-water map:', '49 53 8', '0 11 42', '42 0 7', '57 7 4'], 
    ['water-to-light map:', '88 18 7', '18 25 70'],
    ['light-to-temperature map:', '45 77 23', '81 45 19', '68 64 13'],
    ['temperature-to-humidity map:', '0 69 1', '1 0 69']]
    """


text = read_lines()
print(solution(text))
