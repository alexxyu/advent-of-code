with open('day9.txt', 'r') as f:
    lines = f.read().splitlines()
    grid = [[int(c) for c in line] for line in lines]

    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if  (i > 0 and grid[i][j] >= grid[i-1][j]) or \
                (i < len(grid)-1 and grid[i][j] >= grid[i+1][j]) or \
                (j > 0 and grid[i][j] >= grid[i][j-1]) or \
                (j < len(grid[i])-1 and grid[i][j] >= grid[i][j+1]):
                continue

            res += grid[i][j] + 1

    print(res)
