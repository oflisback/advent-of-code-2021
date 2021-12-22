class Instruction:
    def __init__(self, on, x_range, y_range, z_range):
        self._on = on
        self._x_range = x_range
        self._y_range = y_range
        self._z_range = z_range

    def __str__(self):
        on = "on" if self._on else "off"
        return f"{on} x={self._x_range.start}..{self._x_range.stop},y={self._y_range.start}..{self._y_range.stop},z={self._z_range.start}..{self._z_range.stop}"

    @property
    def on(self):
        return self._on

    @property
    def x_range(self):
        return self._x_range

    @property
    def y_range(self):
        return self._y_range

    @property
    def z_range(self):
        return self._z_range

    def calc_volume(self):
        return (self.x_range.stop - self.x_range.start) * (self.y_range.stop - self.y_range.start) * (self.z_range.stop - self.z_range.start)
