def in_bounds(grid, r, c):
    return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0])

def get_basin_size(grid, r, c, visited):
    if (r, c) in visited or grid[r][c] == 9:
        return 0

    s = 1
    visited.add((r, c))

    for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if in_bounds(grid, r+a, c+b):
            s += get_basin_size(grid, r+a, c+b, visited)

    return s

with open('day9.txt', 'r') as f:
    lines = f.read().splitlines()
    grid = [[int(c) for c in line] for line in lines]

    basins = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if  (i > 0 and grid[i][j] >= grid[i-1][j]) or \
                (i < len(grid)-1 and grid[i][j] >= grid[i+1][j]) or \
                (j > 0 and grid[i][j] >= grid[i][j-1]) or \
                (j < len(grid[i])-1 and grid[i][j] >= grid[i][j+1]):
                continue

            k = get_basin_size(grid, i, j, set())
            basins.append(k)

    basins.sort(reverse=True)
    print(basins[0] * basins[1] * basins[2])
