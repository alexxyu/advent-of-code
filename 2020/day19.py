import re
import networkx as nx
from networkx.algorithms.dag import topological_sort

# Part 1
with open('input/day19.txt', 'r') as f:
    lines = f.read().splitlines()

    rules = dict()
    G = nx.DiGraph()
    i = 0
    while lines[i] != '':
        id, rule = lines[i].split(': ')
        rule = rule.strip("\"")

        id = int(id)
        G.add_node(id)

        rules[id] = rule
        nums = [int(s) for s in rule.split() if s.isdigit()]

        G.add_nodes_from(nums)
        G.add_edges_from([(n, id) for n in nums])
        i += 1

    for id in topological_sort(G):
        rule = rules[id]

        if not rule.isalpha():
            converted_rule = '('
            bases = [int(s) if s.isdigit() else s for s in rule.split()]

            for base in bases:
                if base == '|':
                    converted_rule += '|'
                else:
                    converted_rule += rules[base]

            converted_rule += ')'
            rules[id] = converted_rule

    res = 0

    i += 1
    while i < len(lines):
        line = lines[i]
        if re.search('^' + rules[0] + '$', line):
            res += 1

        i += 1

    print(res)

# Part 2
with open('input/day19.txt', 'r') as f:
    lines = f.read().splitlines()

    rules = dict()
    G = nx.DiGraph()
    i = 0
    while lines[i] != '':
        id, rule = lines[i].split(': ')
        rule = rule.strip("\"")

        id = int(id)
        G.add_node(id)

        rules[id] = rule
        nums = [int(s) for s in rule.split() if s.isdigit()]

        G.add_nodes_from(nums)
        G.add_edges_from([(n, id) for n in nums])
        i += 1

    for id in topological_sort(G):
        if id == 8:
            rules[id] = '(' + rules[42] + ')+'
            continue
        if id == 11:
            rule = ''
            for k in range(1, 13):
                curr = '(' + rules[42] + '{' + str(k) + '}' + rules[31] + '{' + str(k) + '})'
                rule = rule + '|' + curr
            rules[id] = '(' + rule[1:] + ')'
            continue

        rule = rules[id]

        if not rule.isalpha():
            converted_rule = '('
            bases = [int(s) if s.isdigit() else s for s in rule.split()]

            for base in bases:
                if base == '|':
                    converted_rule += '|'
                else:
                    converted_rule += rules[base]

            converted_rule += ')'
            rules[id] = converted_rule

    res = 0

    i += 1
    while i < len(lines):
        line = lines[i]
        if re.search('^' + rules[0] + '$', line):
            res += 1

        i += 1

    print(res)
