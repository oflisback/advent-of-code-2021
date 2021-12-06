with open('input.txt') as file:
    initial_ticks = [int(tick) for tick in file.readlines()[0].strip().split(',')]

def get_nbr_fish_at_day(last_day):
    nbr_fish_at_tick = [0]*9

    for tick in initial_ticks:
        nbr_fish_at_tick[tick] +=1
    for _ in range(1, last_day + 1):
        new_state = [0]*9
        for i in range(8):
            new_state[i] = nbr_fish_at_tick[i+1]
        new_state[6] += nbr_fish_at_tick[0]
        new_state[8] = nbr_fish_at_tick[0]
        nbr_fish_at_tick = new_state
    return sum(nbr_fish_at_tick)

print(f"Nbr fish at day 80: {get_nbr_fish_at_day(80)}")
print(f"Nbr fish at day 256: {get_nbr_fish_at_day(256)}")
