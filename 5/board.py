class Board():
    def __init__(self, side_length):
        self._side_length = side_length
        self._board = [[0]*side_length for i in range(side_length)]

    def __repr__(self):
        return "\n".join(["".join(str(self._board[r])) for r in range(self._side_length)])

    # Only horizontal, vertical or 45 degree lines
    def fill_line(self, line):
        x_step = 0
        if line.c1[0] < line.c2[0]:
            x_step = 1
        elif line.c1[0] > line.c2[0]:
            x_step = -1
        y_step = 0
        if line.c1[1] < line.c2[1]:
            y_step = 1
        elif line.c1[1] > line.c2[1]:
            y_step = -1

        x = line.c1[0]
        y = line.c1[1]

        while not (x == line.c2[0] and y == line.c2[1]):
            self._board[y][x] += 1
            x += x_step
            y += y_step

        self._board[y][x] += 1

    def get_nbr_coords_two_or_more(self):
        count = 0
        for c in range(self._side_length):
            for r in range(self._side_length):
                if self._board[c][r] >= 2:
                    count += 1
        return count
