with open('input.txt') as file:
    rows = [row.strip() for row in file.readlines()]

dots = []
folds = []
out_of_dots = False
for row in rows:
    if len(row) == 0:
        out_of_dots = True
        continue
    if out_of_dots:
        folds.append(row.split()[2].split('='))
    else:
        dots.append([int(v) for v in row.split(',')])

max_x = max([dot[0] for dot in dots])
max_y = max([dot[1] for dot in dots])

def make_paper(width, height):
    return [['.' for _ in range(width)] for _ in range(height)]

paper = make_paper(max_x + 1, max_y + 1)
for dot in dots:
    paper[dot[1]][dot[0]] = 'X'

def get_nbr_markers(p):
    count = 0
    dims = get_dims(p)
    for y in range(dims['height']):
        for x in range(dims['width']):
            if p[y][x] == 'X':
                count += 1
    return count

def draw(p):
    for y in range(len(p)):
        print(''.join(p[y]))

def reverse(p, axis):
    if axis == 'x':
        return [row[::-1] for row in p]
    else:
        return p[::-1]

def get_dims(p):
    return { 'width': len(p[0]), 'height': len(p)}

def paste(target, overlap, start_x, start_y):
    dims = get_dims(overlap)
    for y in range(start_y, start_y + dims['height']):
        for x in range(start_x, start_x + dims['width']):
            current = overlap[y - start_y][x - start_x]
            target[y][x] = current if current == "X" else target[y][x]
    return target

def fold(p, axis, offset):
    dims = get_dims(p)
    if axis == 'x':
        first = [row[:offset] for row in p]
        second = [row[offset+1:] for row in p]
        new_paper = make_paper(max(offset, dims['width'] - offset) - 1, dims['height'])
        p = paste(new_paper, first, 0, 0)
        second_reverse = reverse(second, 'x')
        reverse_dims = get_dims(second_reverse)
        p = paste(new_paper, reverse(second, 'x'), offset-reverse_dims['width'] , 0)
        return p
    else:
        first = p[:offset]
        second = p[offset+1:]
        new_paper = make_paper(dims['width'], max(offset, dims['height'] - offset) - 1)
        first_dims = get_dims(first)
        new_paper_dims = get_dims(new_paper)
        p = paste(new_paper, first, 0, new_paper_dims["height"] - first_dims["height"])
        second_reverse = reverse(second, 'y')
        reverse_dims = get_dims(second_reverse)
        p = paste(new_paper, reverse(second, 'y'), 0, new_paper_dims['height']-reverse_dims['height'])
        return p

for i, f in enumerate(folds):
    if i == 1: print(f"Nbr meh: {get_nbr_markers(paper)}")
    paper = fold(paper, f[0], int(f[1]))
draw(paper)
