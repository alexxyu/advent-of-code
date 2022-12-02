# Part 1
valid_tickets = []
with open('input/day16.txt', 'r') as f:
    lines = f.read().splitlines()

    i=0
    fields = dict()
    while lines[i] != '':
        line = lines[i].split(': ')
        field_name = line[0]
        ranges = line[1].split(' or ')
        
        field_ranges = []
        for r in ranges:
            a, b  = r.split('-')
            field_ranges.append((int(a), int(b)))
        fields[field_name] = field_ranges

        i += 1

    i += 2
    # My ticket is here

    i += 3
    error_rate = 0
    while i < len(lines):
        values = [int(n) for n in lines[i].split(',')]
        
        is_completely_invalid = False
        for value in values:
            matches_field = False
            for field, ranges in fields.items():
                is_valid = False
                for r in ranges:
                    if value >= r[0] and value <= r[1]:
                        is_valid = True
                        break
                if is_valid:
                    matches_field = True
                    break
            if not matches_field:
                error_rate += value
                is_completely_invalid = True
        if not is_completely_invalid:
            valid_tickets.append(lines[i])

        i += 1
                
    print(error_rate)

import networkx as nx
from networkx.algorithms import bipartite

# Part 2
with open('input/day16.txt', 'r') as f:
    lines = f.read().splitlines()

    i=0
    fields = dict()
    while lines[i] != '':
        line = lines[i].split(': ')
        field_name = line[0]
        ranges = line[1].split(' or ')
        
        field_ranges = []
        for r in ranges:
            a, b  = r.split('-')
            field_ranges.append((int(a), int(b)))
        fields[field_name] = field_ranges

        i += 1

    i += 2
    my_values = [int(v) for v in lines[i].split(',')]

    i += 3
    candidates = []
    for f in fields.keys():
        s = set(fields.keys())
        candidates.append(s)

    for line in valid_tickets:
        values = [int(n) for n in line.split(',')]
        for k, value in enumerate(values):
            for field, ranges in fields.items():
                is_valid = False
                for r in ranges:
                    if value >= r[0] and value <= r[1]:
                        is_valid = True
                        break
                if not is_valid and field in candidates[k]:
                    candidates[k].remove(field)

    # Perform bipartite matching between indices and candidate solutions
    G = nx.Graph()
    G.add_nodes_from([n for n in range(len(fields))], bipartite=0)
    G.add_nodes_from(fields.keys(), bipartite=1)

    for j, s in enumerate(candidates):
        for candidate in list(s):
            G.add_edge(j, candidate)
    
    matching = nx.bipartite.maximum_matching(G)
    matching = { key: matching[key] for key in matching.keys() if isinstance(key, int) }
    
    product = 1
    for index, field in matching.items():
        if 'departure' in field:
            product *= my_values[index]

    print(product)
