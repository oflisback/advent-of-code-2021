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


def past_area(area, p):
    if p.x > area.x2 or p.y < area.y2:
        return p.x - (area.x1 + area.x2) / 2
    return "still_hope"


def step(p, v):
    p.x += v.x
    p.y += v.y
    v.x = max(v.x - 1, 0)
    v.y -= 1
    return p, v


# Får väl hitta något sätt att returnera success från shoot också ...


def debugPrintPlayingField(area, historicalPositions):
    coords = [
        p
        for p in (
            historicalPositions
            + [
                Tuple(area.x1, area.y1),
                Tuple(area.x2, area.y2),
            ]
        )
    ]

    minX = min(c.x for c in coords)
    maxX = max(c.x for c in coords)
    minY = min(c.y for c in coords)
    maxY = max(c.y for c in coords)

    for y in reversed(range(minY, maxY + 1)):
        for x in range(minX, maxX + 1):
            if any(p.x == x and p.y == y for p in historicalPositions):
                print("X", end="")
            elif in_area(area, x, y):
                print("O", end="")
            else:
                print(".", end="")
        print()
    input()


def shoot(targetArea, initialVelocity, historicalPositions):
    p = Tuple(0, 0)
    #    historicalPositions.append(copy(p))
    v = copy(initialVelocity)
    peakY = 0

    while True:
        #        print(f"position: {p} velocity: {v}")
        #        debugPrintPlayingField(targetArea, historicalPositions)
        p, v = step(p, v)
        if p.y > peakY:
            peakY = p.y
        #        historicalPositions.append(copy(p))
        if in_area(targetArea, p.x, p.y):
            print(
                "Hit for initalVelocity: "
                + str(initialVelocity.x)
                + ","
                + str(initialVelocity.y)
            )
            return [True, peakY]
        status = past_area(targetArea, p)
        if status != "still_hope":
            return [status, peakY]


# targetArea = Area(20, 30, -10, -5)
targetArea = Area(70, 125, -159, -121)

# 0 = searching, 1 = raising, 2 = done
stage = 0

print("Target size: " + str(targetArea.x2 - targetArea.x1))

res = False
v = Tuple(1, 1)
bestY = 0
peakY = 0
misses = 0
while True:
    historicalPositions = []
    [res, localPeakY] = shoot(targetArea, v, historicalPositions)
    #    debugPrintPlayingField(targetArea, historicalPositions)
    if res == True:
        print("Hit: " + str(v.x) + "," + str(v.y) + "," + str(localPeakY))
        if localPeakY > peakY:
            peakY = localPeakY
        if v.y > bestY:
            bestY = v.y
        if stage == 0:
            stage = 1
            v.y += 1
        if stage == 1:
            v.y += 1
    elif res < 0:
        #           print("Left: " + str(v.x) + "," + str(v.y))
        if stage == 0:
            v.x += 1
        if stage == 1:
            if misses > 200:
                print("Done with 200 misses on x: " + str(v.x))
                v.x -= 1
                v.y = bestY
                misses = 0
            misses += 1
            v.y += 1
            if v.x == 5:
                break
    elif res > 0:
        print("Right: " + str(v.x) + "," + str(v.y))
        if stage == 0:
            v.x -= 1
            v.y += 1
        if stage == 1:
            v.y += 1
#    input()
print(bestY)
print(peakY)
