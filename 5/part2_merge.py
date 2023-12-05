import re
import collections

def read_lines():
    lines = []
    with open("input.txt") as file:
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
        d.append([(start,start+length-1),(end,end+length-1)])
    return d

def get_value(from_intervals, to_intervals):
    intervals = []
    print(f"Input {from_intervals}")
    for a, b in from_intervals:
        found = False
        for left, right in to_intervals:
            if left[0] <= b <= left[0] + left[1]:
                left_upper = min(b, left[0] + left[1])
                intervals.append((right[0], right[0] + left_upper - left[0]))
                found = True

        if not found:
            intervals.append((a, b))

    print(f"Output {intervals}")
    return intervals

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

    min_val = 10**11 + 10
    for seed, length in seeds:
        init_interval = [(seed, seed + length)]
        v1 = get_value(init_interval, d1)
        v2 = get_value(v1, d2)
        v3 = get_value(v2, d3)
        v4 = get_value(v3, d4)
        v5 = get_value(v4, d5)
        v6 = get_value(v5, d6)
        v7 = get_value(v6, d7)

        min_val = min(min_val, min([a for a, _ in v7]))
        break

    return min_val 

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
