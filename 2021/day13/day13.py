INSTRUCTION_LIMIT = None

with open('day13.txt', 'r') as f:
    lines = f.read().splitlines()
    
    i = 0
    w, h = 0, 0

    dots = []
    while len(lines[i]) > 0:
        c, r = lines[i].split(',')
        r, c = int(r), int(c)
        w = max(w, (c+1))
        h = max(h, (r+1))

        dots.append((c, r))

        i += 1

    grid = [['.' for _ in range(w)] for _ in range(h)]
    for c, r in dots:
        grid[r][c] = '#'

    res = 0
    instructions = lines[i+1:] if not INSTRUCTION_LIMIT else lines[i+1:i+1+INSTRUCTION_LIMIT]
    for i, instruction in enumerate(instructions[:]):
        res = 0
        axis, pos = instruction.split('=')
        axis = axis[-1]
        pos = int(pos)

        if axis == 'y':
            new_grid = [['.' for _ in range(w)] for _ in range(max(h - pos, pos))]

            for i in range(1, pos+1):
                r = pos - i
                for c in range(w):
                    if (pos+i < h and grid[pos + i][c] == '#') or \
                       (pos-i >= 0 and grid[pos - i][c] == '#'):
                        new_grid[r][c] = '#'
                        res += 1
        elif axis == 'x':
            new_grid = [['.' for _ in range(max(w - pos, pos))] for _ in range(h)]

            for i in range(1, pos+1):
                c = pos - i
                for r in range(h):
                    if (pos+i < w and grid[r][pos + i] == '#') or \
                       (pos-i >= 0 and grid[r][pos - i] == '#'):
                        new_grid[r][c] = '#'
                        res += 1

        grid = new_grid
        h, w = len(grid), len(grid[0])
 
    for g in new_grid:
        print(''.join(g))
    print()
    print(res)
