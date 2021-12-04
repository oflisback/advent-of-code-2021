from board import Board

def get_boards_and_numbers():
    with open('input.txt') as file:
        lines = [l.strip() for l in file.readlines()]
        numbers = [int(value) for value in lines.pop(0).split(',')]
        rest_of_lines = [l for l in lines if l.strip() != ""]
        boards = []
        while len(rest_of_lines) > 0:
            board_lines, rest_of_lines = rest_of_lines[:5], rest_of_lines[5:]
            boards.append(Board(board_lines))
        return boards, numbers
