from collections import deque

with open('input.txt') as file:
    rows = [[c for c in row.strip()] for row in file.readlines()]

stack = deque()

start_to_end = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>',
}

error_to_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

score = 0
for row in rows:
    for c in row:
        if c in start_to_end:
            stack.append(c)
        else:
            v = stack.pop()
            if c != start_to_end.get(v):
#                print(f"Expected {start_to_end.get(v)}, but found {c} instead.")
                score += error_to_points.get(c)
print(score)

