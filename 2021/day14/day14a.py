from collections import defaultdict

def transform(template, rules):
    res = template[0]
    for i in range(len(template)-1):
        pair = template[i:i+2]
        res += rules[pair] + template[i+1]
    return res

with open('day14.txt', 'r') as f:
    lines = f.read().splitlines()
    
    template = lines[0]

    rules = {}
    for rule in lines[2:]:
        lhs, rhs = rule.split(' -> ')
        rules[lhs] = rhs

    res = template
    for i in range(10):
        res = transform(res, rules)

    counts = defaultdict(int)
    for c in res:
        counts[c] += 1
    counts = sorted(counts.items(), key=lambda x: x[1])

    print(counts[-1][1] - counts[0][1])
