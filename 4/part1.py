import re

def read_lines():
    lines = []
    with open("input_large.txt") as file:
        lines = [line.rstrip() for line in file]

    return lines

def get_points(card):
    winning, losing = card.split(' | ')
    winning = winning.split()
    losing = losing.split()

    points = [x for x in losing for y in winning if x == y]
    print(points)
    if points == []:
        return 0
    return 2**(len(points) - 1)

def solution(text):
    points = 0
    for card in text:
        card = re.sub("Card \d+: ", "", card)
        points += get_points(card) 
    return points

text = read_lines()
print(solution(text))
