from functools import lru_cache

DAYS = 256

@lru_cache(maxsize=None)
def calculate(timer, days=DAYS):
    if days <= timer:
        return 0

    n_spawned = 1 + (days - (timer + 1)) // 7
    s = n_spawned

    days -= (timer + 1)
    for _ in range(n_spawned):
        s += calculate(8, days)
        days -= 7
    return s

with open('day6.txt', 'r') as f:
    line = f.readline()
    fish = [int(k) for k in line.strip().split(',')]

    s = len(fish) + sum(map(calculate, fish))

    print(s)
    