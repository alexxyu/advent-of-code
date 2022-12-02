# Part 1
max_id = 0
with open('input/day5.txt', 'r') as f:
    for line in f:
        row = 0
        for k, c in enumerate(line[:7]):
            if c == 'B':
                row += 2**(7 - (k+1))

        col = 0
        for k, c in enumerate(line[7:]):
            if c == 'R':
                col += 2**(3 - (k+1))

        id = row * 8 + col
        max_id = max(max_id, id)

print(max_id)

# Part 2
ids = []
with open('input/day5.txt', 'r') as f:
    for line in f:
        row = 0
        for k, c in enumerate(line[:7]):
            if c == 'B':
                row += 2**(7 - (k+1))

        col = 0
        for k, c in enumerate(line[7:]):
            if c == 'R':
                col += 2**(3 - (k+1))

        id = row * 8 + col
        ids.append(id)

ids.sort()
for i in range(1, len(ids)):
    if ids[i] != ids[i-1]+1:
        print(f"{ids[i-1]} ... {ids[i]} ... {ids[i+1]}")
