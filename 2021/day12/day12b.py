from collections import defaultdict

with open('day12.txt', 'r') as f:
    neighbors = defaultdict(set)
    lines = f.read().splitlines()

    for line in lines:
        a, b = line.split('-')
        neighbors[a].add(b)
        neighbors[b].add(a)

    def count_paths(curr, visited, revisited_small):
        if curr == 'end':
            return 1
        
        paths = 0
        for neighbor in neighbors[curr]:
            if neighbor == 'start':
                continue

            if neighbor.isupper():
                paths += count_paths(neighbor, visited, revisited_small)
            elif neighbor not in visited:
                paths += count_paths(neighbor, visited | {neighbor}, revisited_small)
            elif not revisited_small:
                paths += count_paths(neighbor, visited, True)

        return paths

    print( count_paths('start', set(), False) )
