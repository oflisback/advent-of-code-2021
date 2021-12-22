# ok man kan inte hålla reda på hela rymden. Man måste clippa och ha sig.
# måste hitta på en annan representation av rätblocken :)

from instruction import Instruction
from space import Space

with open('test-b-input.txt') as file:
    rows = [row for row in file.readlines()]

def get_capped_range(r):
    if r.start < 0:
        start = 0
    elif r.start > 100:
        return None
    else:
        start = r.start
    if r.stop < 0:
        return None
    elif r.stop > 100:
        stop = 100
    else:
        stop = r.stop
    return range(start, stop)

instructions = []

for row in rows:
    split = row.split(' ')
    state = row.split(' ')[0] == 'on'
    ranges = []
    for r in split[1].split(','):
        vals = r.split('..')
        ranges.append(get_capped_range(range(50 + int(vals[0][2:]), 50 + int(vals[1]))))
    if (ranges[0] is not None and ranges[1] is not None and ranges[2] is not None):
        instructions.append(Instruction(state, ranges[0], ranges[1], ranges[2]))

space = Space(101)

for i in instructions:
    space.apply(i)
    print(space.count(True))

