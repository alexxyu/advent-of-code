import networkx as nx
from networkx.algorithms import bfs_edges, edge_dfs

# Part 1
G = nx.DiGraph()

edges = []
with open('input/day7.txt', 'r') as f:
    lines = f.read().splitlines()
    for line in lines:
        parts = line.split(' contain ')
        container_bag = parts[0][:-1]
        contained_bags = parts[1][:-1]

        if 'no other bags' in contained_bags:
            continue

        contained_bags = contained_bags.split(', ')
        for bag in contained_bags:
            qty = int(bag[:bag.find(' ')])
            contained_bag = bag[bag.find(' ')+1:]

            if qty != 1:
                contained_bag = contained_bag[:-1]

            edges.append((contained_bag, container_bag))

G.add_edges_from(edges)
edges = bfs_edges(G, 'shiny gold bag')

unique_bags = sum([1 for x in edges])
print(unique_bags)

# Part 2
G.clear()

edges = []
with open('input/day7.txt', 'r') as f:
    lines = f.read().splitlines()
    for line in lines:
        parts = line.split(' contain ')
        container_bag = parts[0][:-1]
        contained_bags = parts[1][:-1]

        if 'no other bags' in contained_bags:
            continue

        contained_bags = contained_bags.split(', ')
        for bag in contained_bags:
            qty = int(bag[:bag.find(' ')])
            contained_bag = bag[bag.find(' ')+1:]

            if qty != 1:
                contained_bag = contained_bag[:-1]

            #edges.append((container_bag, contained_bag, qty))
            edges.append((contained_bag, container_bag, qty))

G.add_weighted_edges_from(edges)
edges = edge_dfs(G, 'shiny gold bag')

cnt = 0
bags = list(G.nodes)
for bag in bags:
    if bag == 'shiny gold bag':
        continue
    for path in nx.all_simple_paths(G, source=bag, target='shiny gold bag'):
        mult = 1
        for i in range(1, len(path)):
            mult *= G.get_edge_data(path[i-1], path[i])['weight']
        cnt += mult

print(cnt)