from board import Board
from util import get_lines

lines = get_lines('input.txt')

board = Board(1000)
for line in lines:
    board.fill_line(line)
print(board.get_nbr_coords_two_or_more())
