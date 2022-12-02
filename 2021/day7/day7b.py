import math
import statistics

with open('day7.txt', 'r') as f:
    line = f.readline()
    crabs = [int(pos) for pos in line.strip().split(',')]
    
    target_floor = math.floor(statistics.mean(crabs))
    dists_floor = [abs(target_floor - c) for c in crabs]

    target_ceil = math.ceil(statistics.mean(crabs))
    dists_ceil = [abs(target_ceil - c) for c in crabs]

    print(min(
        round(sum([d*(d+1)/2 for d in dists_floor])),
        round(sum([d*(d+1)/2 for d in dists_ceil]))
    ))
