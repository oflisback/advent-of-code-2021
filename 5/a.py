from board import Board
from util import get_lines

hor_vert_lines = [l for l in get_lines('input.txt') if l.is_hor_or_vert()]

board = Board(1000)
for line in hor_vert_lines:
    board.fill_line(line)
print(board.get_nbr_coords_two_or_more())
