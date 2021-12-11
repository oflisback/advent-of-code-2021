with open('input.txt') as file:
    m = [[int(c) for c in row.strip()] for row in file.readlines()]

Y, X = [len(m), len(m[0])]

def run_step(step_nbr, step_flashes = 0, run = True):
    for y in range(Y):
        for x in range(X):
            m[y][x] += 1
    has_flashed = []
    while run:
        iteration_flashes = 0
        for y in range(Y):
            for x in range(X):
                if m[y][x] > 9 and (y, x) not in has_flashed:
                    iteration_flashes +=1
                    has_flashed.append((y, x))
                    for c in ((y-1,x-1),(y-1,x),(y-1,x+1),(y,x-1),
                                    (y,x+1), (y+1,x-1), (y+1,x), (y+1,x+1)):
                        if 0 <= c[0] < Y and 0 <= c[1] < X:
                            m[c[0]][c[1]] += 1
        run = iteration_flashes > 0
        step_flashes += iteration_flashes
    for y in range(Y):
        for x in range(X):
            if m[y][x] > 9: m[y][x] = 0
    if step_flashes == X * Y:
        print(f"Synchronized at iteration: {step_nbr}")
        quit()
    return step_flashes

total = 0
for i in range(500):
    total += run_step(i + 1)
    if i == 99: print(f"Total at iteration 100: {total}")
