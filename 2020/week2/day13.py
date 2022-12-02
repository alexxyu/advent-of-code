import math

# Part 1
with open('input/day13.txt', 'r') as f:
    lines = f.read().splitlines()

    earliest = int(lines[0])
    buses = [int(bus) for bus in lines[1].split(',') if bus != 'x']

    min_wait = math.inf
    min_bus = 0
    for b in buses:
        earliest_div = earliest - (earliest % b) + b

        if earliest_div < min_wait:
            min_wait = earliest_div
            min_bus = b

    min_wait -= earliest
    print(min_bus * min_wait)

from itertools import count

# Part 2 - credit to noblematt20 for clever solution
with open('input/day13.txt', 'r') as f:
    lines = f.read().splitlines()

    n = 0
    buses = [(i, int(bus)) for i, bus in enumerate(lines[1].split(',')) if bus != 'x']

    step = 1
    for i, b in buses:
        n = next(c for c in count(n, step) if (c + i) % b == 0)
        step *= b

    print(n)
