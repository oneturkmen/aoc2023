import re

def read_lines():
    lines = []
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]

    return lines

available = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def possible(game):
    # Remove "game %d: " prefix
    game = re.sub("Game \d+: ", "", game)

    # Split
    sets = [set_.strip() for set_ in game.split(';')]
    for set_ in sets:
        cubes = [cube.strip() for cube in set_.split(',')]

        for cube in cubes:
            count, color = cube.split(' ')

            if available[color] < int(count): 
                return False

    return True


def solution(lines):
    ans = 0
    for i, game in enumerate(lines):
        if possible(game):
            ans += i + 1

    return ans



        
lines = read_lines()
print(solution(lines))
