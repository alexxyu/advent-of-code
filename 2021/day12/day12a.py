from collections import defaultdict

with open('day12.txt', 'r') as f:
    neighbors = defaultdict(set)
    lines = f.read().splitlines()

    for line in lines:
        a, b = line.split('-')
        neighbors[a].add(b)
        neighbors[b].add(a)

    def count_paths(curr, visited):
        if curr == 'end':
            return 1
        
        paths = 0
        for neighbor in neighbors[curr]:
            if neighbor.isupper() or neighbor not in visited:
                paths += count_paths(neighbor, visited | {curr})

        return paths

    print( count_paths('start', set()) )
