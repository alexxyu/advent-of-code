from collections import defaultdict

with open('day5.txt', 'r') as f:
    lines = f.read().splitlines()

    point_counts = defaultdict(int)
    for line in lines:
        lhs, rhs = line.split(' -> ')
        x1s, y1s = lhs.split(',')
        x2s, y2s = rhs.split(',')

        x1, y1, x2, y2 = int(x1s), int(y1s), int(x2s), int(y2s)

        if x1 == x2:
            y_min, y_max = min(y1, y2), max(y1, y2)
            for y in range(y_min, y_max+1):
                point_counts[(x1, y)] += 1
        elif y1 == y2:
            x_min, x_max = min(x1, x2), max(x1, x2)
            for x in range(x_min, x_max+1):
                point_counts[(x, y1)] += 1
        else:
            if x2 < x1:
                tmp = x1
                x1, x2 = x2, tmp
                tmp = y1
                y1, y2 = y2, tmp

            if y2 < y1:
                dy = -1
            else:
                dy = 1

            i = 0
            while i+x1 <= x2:
                point_counts[(x1+i, y1+dy*i)] += 1
                i += 1

    res = 0
    for p, v in point_counts.items():
        if v >= 2:
            res += 1

    print(res)
