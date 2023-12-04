import re
import math

def read_lines():
    lines = []
    with open("input_large.txt") as file:
        lines = [line.rstrip() for line in file]

    return lines

def valid(text, i, j, n, m):
    return i >= 0 and i < n and j >= 0 and j < m and text[i][j].isdigit()

def parse_num(row, i, n):
    start = i
    while start >= 0 and row[start].isdigit():
        start -= 1
    start += 1

    end = i
    while end < n and row[end].isdigit():
        end += 1

    num = int(str(''.join(row[start:end])))

    for k in range(start, end):
        row[k] = '.'

    print("Row is ...")
    print(''.join(row))
    print(start, end)

    return num


def dfs(text, i, j, n, m):
    directions = ((0, -1), (-1, -1), (-1, 0), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))

    numbers = []

    print('kek')
    for x, y in directions:
        new_x = i + x
        new_y = j + y
        if valid(text, new_x, new_y, n, m):
            numbers.append(parse_num(text[new_x], new_y, m))

    if len(numbers) < 2:
        return 0
    print(numbers)
    assert len(numbers) == 2

    return numbers[0] * numbers[1]

def solution(text):
    text = list([list(row) for row in text])
    ans = 0
    n = len(text)
    m = len(text[0])
    print(text)

    for i in range(n):
        for j in range(m):
            if text[i][j] == '*':
                text[i][j] = '.'
                ans += dfs(text, i, j, n, m)
    return ans

text = read_lines()
print(solution(text))
