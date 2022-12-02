from functools import lru_cache
from collections import Counter

rules = {}

@lru_cache(maxsize=None)
def generate(a, b, depth=40):
    if depth == 0:
        return Counter()
    x = rules[a+b]
    return Counter(x) + generate(a, x, depth-1) + generate(x, b, depth-1)

with open('day14.txt', 'r') as f:
    lines = f.read().splitlines()
    
    template = lines[0]
    for rule in lines[2:]:
        lhs, rhs = rule.split(' -> ')
        rules[lhs] = rhs

    c = sum(map(generate, template, template[1:]), Counter(template))
    print(max(c.values()) - min(c.values()))
