import re
import collections
import functools

"""
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

from collections import Counter, defaultdict

ALPHABET = {
    "A": 0,
    "K": 1,
    "Q": 2,
    "T": 3,
    "9": 4,
    "8": 5,
    "7": 6,
    "6": 7,
    "5": 8,
    "4": 9,
    "3": 10,
    "2": 11,
    "J": 12,
}

def read_lines():
    with open("input_large.txt") as file:
        lines = []
        for line in file:
            lines.append(line.strip().split(' '))

        return lines

def string_comp(x, y):
    for i in range(len(x)):
        if x[i] != y[i]:
            if ALPHABET[x[i]] > ALPHABET[y[i]]:
                return 1
            else:
                return -1
    return 0

def fix_dict(freq, hand):
    if 'J' in hand:
        most_common = Counter(freq).most_common()

        if hand == 'JJJJJ':
            return freq
        else:
            leftover_chars = sorted([c for c in hand if c != 'J'], key=functools.cmp_to_key(string_comp))

            freq[leftover_chars[0]] += freq['J']
            del freq['J']

    return freq

def is_five_of_kind(hand):
    freq = dict(Counter(hand))
    freq = fix_dict(freq, hand)

    return len(freq.keys()) == 1

def is_four_of_kind(hand):
    freq = dict(Counter(hand))
    freq = fix_dict(freq, hand)

    if len(freq.keys()) == 2:
        for k, v in freq.items():
            if v == 4:
                return True
    else:
        return False

def is_full_house(hand):
    freq = dict(Counter(hand))
    freq = fix_dict(freq, hand)

    if len(freq.keys()) == 2:
        for k, v in freq.items():
            if v == 3:
                return True
    else:
        return False

def is_three_of_kind(hand):
    freq = dict(Counter(hand))
    freq = fix_dict(freq, hand) 

    for k, v in freq.items():
        if v == 3:
            return True
    return False

def is_two_pair(hand):
    freq = dict(Counter(hand))
    freq = fix_dict(freq, hand) 

    return len(freq.keys()) == 3

def is_one_pair(hand):
    freq = dict(Counter(hand))
    freq = fix_dict(freq, hand) 

    return len(freq.keys()) == 4

def determine_kind(hand):
    lambdas = [is_five_of_kind, is_four_of_kind, is_full_house, is_three_of_kind, is_two_pair, is_one_pair]

    for i, f in enumerate(lambdas):
        if f(hand):
            return i
    if 'J' in hand:
        print(hand)
    
    return len(lambdas)


def comparator(x, y):
    x_kind = determine_kind(x[0])
    y_kind = determine_kind(y[0])

    if x_kind == y_kind:
        vals = [x[0], y[0]]
        vals = sorted(vals, key=functools.cmp_to_key(string_comp))

        if string_comp(x[0], y[0]) == 0:
            return 0
        elif string_comp(x[0], y[0]) == 1:
            return 1
        else:
            return -1
    else:
        return x_kind - y_kind

def solution(hands):
    sorted_hands = list(reversed(sorted(hands, key=functools.cmp_to_key(comparator))))
    ans = 0
    for i in range(1, len(sorted_hands) + 1):
        ans += int(sorted_hands[i - 1][1]) * i

    return ans

text = read_lines()
print(solution(text))
