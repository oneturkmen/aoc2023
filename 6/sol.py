import re
import collections

"""
Time:        61     67     75     71
Distance:   430   1036   1307   1150
"""
def read_lines():
    with open("input.txt") as file:
        lines = []
        for line in file:
            if line.startswith("Time:"):
                line = re.sub("Time:\s+", "", line).strip().split()
            elif line.startswith("Distance:"):
                line = re.sub("Distance:\s+", "", line).strip().split()

            lines.append([int(n) for n in line])

        return list(zip(lines[0], lines[1])) 

def read_lines_pt2():
    with open("input.txt") as file:
        lines = []
        for line in file:
            if line.startswith("Time:"):
                line = re.sub("Time:\s+", "", line).strip().replace(" ", "")
                print(line)
            elif line.startswith("Distance:"):
                line = re.sub("Distance:\s+", "", line).strip().replace(" ", "")

            lines.append(int(line))

        return (lines[0], lines[1])

def solution(pair):
    ways = 1
    time, record_distance = pair
    left = 0
    right = time
    for t in range(1, time):
        curr_distance = t * (time - t)
        if curr_distance > record_distance:
            break
        left += 1

    for t in range(time - 1, 0, -1):
        curr_distance = t * (time - t)
        if curr_distance > record_distance:
            break
        right -= 1

    # '-2' at the end of 0 and time milliseconds, not counted in loops above.
    return right - left + 1 - 2



text = read_lines_pt2()
print(text)
print(solution(text))
