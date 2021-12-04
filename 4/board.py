class Board:
    def __init__(self, text_lines):
        self._done = False
        self.lines = []
        self.marked = [[False]*5 for i in range(5)]
        for line in text_lines:
            self.lines.append([int(value) for value in line.split()])

    def has_bingo(self):
        for row in range(0,5):
            if len([v for v in self.marked[row] if v == True]) == 5:
                return True
        for col in range(0,5):
            column = [v[col] for v in self.marked]
            if len([v for v in column if v == True]) == 5:
                return True
        return False

    def mark(self, number):
        for row in range(0,5):
            for col in range(0,5):
                if self.lines[col][row] == number:
                    self.marked[col][row] = True

    def get_unmarked_number_sum(self):
        sum = 0
        for row in range(0,5):
            for col in range(0,5):
                if not self.marked[col][row]:
                    sum += self.lines[col][row]
        return sum

    @property
    def done(self):
        return self._done

    @done.setter
    def done(self, value):
        self._done = value
