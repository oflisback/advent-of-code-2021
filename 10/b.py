from collections import deque

with open('input.txt') as file:
    rows = [[c for c in row.strip()] for row in file.readlines()]

start_to_end = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>',
}

incomplete_rows = []

def is_invalid(line):
    stack = deque()
    for c in line:
        if c in start_to_end:
            stack.append(c)
        else:
            v = stack.pop()
            if c != start_to_end.get(v):
#                print(f"Expected {start_to_end.get(v)}, but found {c} instead.")
                return True
    return False

for row in rows:
    if not is_invalid(row):
        incomplete_rows.append(row)

end_to_start = {
    ')': '(',
    '}': '{',
    ']': '[',
    '>': '<',
}

fix_to_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def score_incomplete_word(line):
    stack = deque()
    word_score = 0
    for c in line:
        if c in start_to_end:
            stack.append(c)
        else:
            stack.pop()
    while len(stack) > 0:
        v = stack.pop()
        word_score = 5 * word_score + fix_to_points[start_to_end[v]]
    return word_score

scores = []
for row in incomplete_rows:
    scores.append(score_incomplete_word(row))

scores.sort()
print(scores[int((len(scores)-1)/2)])

