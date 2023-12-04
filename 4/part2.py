from collections import defaultdict
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
    return points

def solution(text):
    freq = defaultdict(lambda: 1)

    for card_no in range(1, len(text) + 1):
        orig_card = text[card_no - 1]
        card = re.sub("Card\s+\d+:\s+", "", orig_card)
        points = get_points(card) 

        copies = freq[card_no]

        for _ in range(copies):
            for newly_copied_card in range(card_no + 1, card_no + len(points) + 1):
                freq[newly_copied_card] += 1

    return sum(freq.values())

text = read_lines()
print(solution(text))
