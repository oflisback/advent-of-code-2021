from board import Board
from util import get_boards_and_numbers

boards, numbers = get_boards_and_numbers()

last_board = None
for number in numbers:
    for board in boards:
        board.mark(number)
        if board.has_bingo():
            board.done = True
            last_board = board
    boards = [b for b in boards if not b.done]
    if len(boards) == 0:
        print(f"Result: {last_board.get_unmarked_number_sum() * number}")
        break
