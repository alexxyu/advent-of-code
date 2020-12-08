# Part 1
cnt = 0
with open('input/day3.txt', 'r') as f:
    x_pos = 0

    next(f)
    for line in f:
        x_pos = (x_pos + 3) % (len(line)-1)
        if line[x_pos] == '#':
            cnt += 1

print(cnt)

# Part 2
cnts = []
with open('input/day3.txt', 'r') as f:

    lines = f.read().splitlines() [1:]

    for right_amt in [1, 3, 5, 7]:
        cnt = 0
        x_pos = 0

        for line in lines:
            x_pos = (x_pos + right_amt) % (len(line))
            if line[x_pos] == '#':
                cnt += 1

        cnts.append(cnt)

    x_pos = 0
    cnt = 0
    for i in range(1, len(lines), 2):
        line = lines[i]
        x_pos = (x_pos + 1) % (len(line))
        if line[x_pos] == '#':
            cnt += 1

    cnts.append(cnt)

product = 1
for n in cnts:
    product *= n

print(product)