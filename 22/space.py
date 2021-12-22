class Space:
    def __init__(self, side):
        self._side = side
        space = [0]*side
        for i in range(0,side):
            space[i] = [0]*side
            for j in range(0,side):
                space[i][j] = [0]*side
        self._space = space

    def apply(self, i):
        print(i)
        for x in range(i.x_range.start, i.x_range.stop + 1):
            for y in range(i.y_range.start, i.y_range.stop + 1):
                for z in range(i.z_range.start, i.z_range.stop + 1):
                    self._space[x][y][z] = i.on

    def count(self, state):
        n = 0
        for i in range(self._side):
            for j in range(self._side):
                for k in range(self._side):
                    if self._space[i][j][k] == state:
                        n += 1
        return n

    def get_volume(self):
        return len(self._space) * len(self._space[0]) * len(self._space[0][0])
