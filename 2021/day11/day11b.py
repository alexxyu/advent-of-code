with open('day11.txt', 'r') as f:
    lines = f.read().splitlines()

    grid = [[int(c) for c in line] for line in lines]

    def increase_adj(r, c, flashed):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]):
            return 0

        if (r, c) in flashed:
            return 0

        grid[r][c] += 1
        if grid[r][c] > 9:
            grid[r][c] = 0
            flashed.add((r, c))
            s = 1

            for a in [-1, 0, 1]:
                for b in [-1, 0, 1]:
                    if a == 0 and b == 0:
                        continue
                    s += increase_adj(r+a, c+b, flashed)
        else:
            s = 0

        return s

    s = 0
    res = 0
    while s != len(grid)*len(grid[0]):
        flashed = set()
        s = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                s += increase_adj(i, j, flashed)
        res += 1

    print(res)
