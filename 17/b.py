from collections import namedtuple
from copy import copy

Velocity = namedtuple("Velocity", "x y")


class Area:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


class Tuple:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"


def in_area(area, x, y):
    return area.x1 <= x <= area.x2 and area.y1 <= y <= area.y2


def step(p, v):
    p.x += v.x
    p.y += v.y
    if v.x != 0:
        v.x = v.x + 1 if v.x < 1 else v.x - 1
    v.y -= 1
    return p, v


def shoot(targetArea, initialVelocity):
    p = Tuple(0, 0)
    v = copy(initialVelocity)
    peakY = 0

    nbrSteps = 0
    while True:
        p, v = step(p, v)
        if p.y > peakY:
            peakY = p.y
        if in_area(targetArea, p.x, p.y):
            print(
                "Hit for initalVelocity: "
                + str(initialVelocity.x)
                + ","
                + str(initialVelocity.y)
            )
            return True
        nbrSteps += 1
        if nbrSteps > 1000:
            return False


targetArea = Area(70, 125, -159, -121)
# targetArea = Area(20, 30, -10, -5)

print("Target width: " + str(targetArea.x2 - targetArea.x1))

maxY = 158

nbrHit = 0
for x in range(0, 300 + 1):
    for y in range(-300, maxY + 1):
        v = Tuple(x, y)
        hit = shoot(targetArea, v)
        if hit == True:
            nbrHit += 1

print("nbrHit: " + str(nbrHit))
