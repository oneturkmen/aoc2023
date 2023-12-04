import re
import math

def read_lines():
    lines = []
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]

    return lines


def count_color_products(game):
    # Remove "game %d: " prefix
    game = re.sub("Game \d+: ", "", game)

    max_color_count = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    # Split
    sets = [set_.strip() for set_ in game.split(';')]
    for set_ in sets:
        cubes = [cube.strip() for cube in set_.split(',')]

        for cube in cubes:
            count, color = cube.split(' ')
            max_color_count[color] = max(int(count), max_color_count[color])

    return math.prod(max_color_count.values()) 


def solution(lines):
    ans = 0
    for i, game in enumerate(lines):
        ans += count_color_products(game)

    return ans



        
lines = read_lines()
print(solution(lines))
