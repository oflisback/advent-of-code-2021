import math

with open('input.txt') as file:
    rows = [[int(v) for v in row.strip()] for row in file.readlines()]

X = len(rows[0])
Y = len(rows)

def is_minima(r, c):
    v = rows[r][c]
    if c < X - 1 and rows[r][c+1] <= v:
        return False
    if c > 0 and rows[r][c-1] <= v:
        return False
    if r < Y - 1 and rows[r+1][c] <= v:
        return False
    if r > 0 and rows[r-1][c] <= v:
        return False
    return True

risk = 0
minimas = []
for c in range(X):
    for r in range(Y):
        if is_minima(r, c):
            minimas.append((r,c))
            risk += rows[r][c] + 1
print(f"Risk: {risk}")

# part 2
sizes = []
for minima in minimas:
    basin = []

    def belongs_to_basin(r, c):
        if r < 0 or c < 0 or r >= Y or c >= X:
            return False
        if rows[r][c] == 9:
            return False
        return True

    def add_to_basin(r, c):
        if (r, c) in basin or not belongs_to_basin(r, c):
            return
        basin.append((r, c))
        for coord in [(r,c+1),(r,c-1),(r+1,c),(r-1,c)]:
            add_to_basin(*coord)

    add_to_basin(*minima)
    sizes.append(len(basin))
sizes.sort()
print(f"Product: {math.prod(sizes[-3:])}")
