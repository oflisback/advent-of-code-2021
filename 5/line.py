class Line():
    def __init__(self, c1, c2):
        self._c1 = c1
        self._c2 = c2

    def __str__(self):
        return f"{self._c1[0],self._c1[1]} -> {self._c2[0],self._c2[1]}"

    def is_hor_or_vert(self):
        return self._c1[0] == self._c2[0] or self._c1[1] == self._c2[1]

    @property
    def c1(self):
        return self._c1

    @property
    def c2(self):
        return self._c2
