import re

def read_lines():
    lines = []
    with open("input_large.txt") as file:
        lines = [line.rstrip() for line in file]

    return lines

def valid(text, i, j, n, m):
    return i >= 0 and i < n and j >= 0 and j < m and text[i][j].isdigit() and text[i][j] != '.'

def dfs(text, i, j, n, m):
    directions = ((0, -1), (-1, -1), (-1, 0), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))

    curr_row = list(text[i])
    curr_row[j] = '.'
    text[i] = ''.join(curr_row)

    for x, y in directions:
        new_x = i + x
        new_y = j + y
        if valid(text, new_x, new_y, n, m) and text[new_x][new_y] != '.':
            dfs(text, new_x, new_y, n, m)

    return None

def solution(text):
    total = 0
    ans = 0
    n = len(text)
    m = len(text[0])

    for i in range(n):
        total += sum([int(num) for num in re.findall("\d+", text[i])])

    for i in range(n):
        for j in range(m):
            if not text[i][j].isdigit() and text[i][j] != '.':
                dfs(text, i, j, n, m)

    print(text)
    for i in range(n):
        ans += sum([int(num) for num in re.findall("\d+", text[i])])

    return total - ans

text = read_lines()
print(solution(text))
