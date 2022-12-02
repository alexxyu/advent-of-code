import statistics

with open('day7.txt', 'r') as f:
    line = f.readline()
    crabs = [int(pos) for pos in line.strip().split(',')]
    
    target = int(statistics.median(crabs))
    
    print(sum([abs(target - c) for c in crabs]))
