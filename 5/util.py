from board import Board
from line import Line

def string_to_coord(str):
    parts = str.split(',')
    return [int(parts[0]), int(parts[1])]

def get_lines(input_file):
    lines = []
    with open(input_file) as file:
        input_lines = [l.strip().split(' ') for l in file.readlines()]
        for input_line in input_lines:
            parts = [input_line[0], input_line[2]]
            lines.append(Line(string_to_coord(parts[0]), string_to_coord(parts[1])))
    return lines
