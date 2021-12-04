from board import Board
from util import get_boards_and_numbers

boards, numbers = get_boards_and_numbers()

for number in numbers:
    for board in boards:
        board.mark(number)
        if board.has_bingo():
            print(f"Result: {board.get_unmarked_number_sum() * number}")
            quit()
