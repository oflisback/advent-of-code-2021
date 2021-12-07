with open('input.txt') as file:
    positions = [int(v) for v in file.readlines()[0].strip().split(',')]

min_fuel = 1000000000

costs = [-1]*2000

def get_cost(offset):
    if (costs[offset] != -1):
        return costs[offset]
    cost = 0
    for i in range(offset):
        cost += i + 1
    costs[offset] = cost
    return cost

for i in range(min(positions), max(positions)):
    req_fuel = 0
    for pos in positions:
        req_fuel += get_cost(abs(pos - i))
    if req_fuel < min_fuel:
        min_fuel = req_fuel
print(min_fuel)
