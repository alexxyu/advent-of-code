import numpy as np

def is_same(seating, next):
    for i1, i2 in zip(seating, next):
        for j1, j2 in zip(i1, i2):
            if j1 != j2:
                return False

    return True

# Part 1
seating = list(np.loadtxt('input/day11.txt', dtype=str))
seating = [[c for c in s] for s in seating]

while True:
    next = [[c for c in s] for s in seating]
    
    # for r in seating:
    #     print(''.join(r))
    # print()

    for i in range(len(seating)):
        for j in range(len(seating[0])):
            if seating[i][j] == '.':
                continue

            occupied = 0

            if i-1 >= 0 and seating[i-1][j] == '#':
                occupied += 1
            if i+1 < len(seating) and seating[i+1][j] == '#':
                occupied += 1
            if j-1 >= 0 and seating[i][j-1] == '#':
                occupied += 1
            if j+1 < len(seating[0]) and seating[i][j+1] == '#':
                occupied += 1

            if i-1 >= 0 and j-1 >= 0 and seating[i-1][j-1] == '#':
                occupied += 1
            if i-1 >= 0 and j+1 < len(seating[0]) and seating[i-1][j+1] == '#':
                occupied += 1
            if i+1 < len(seating) and j-1 >= 0 and seating[i+1][j-1] == '#':
                occupied += 1
            if i+1 < len(seating) and j+1 < len(seating[0]) and seating[i+1][j+1] == '#':
                occupied += 1

            if seating[i][j] == 'L' and occupied == 0:
                next[i][j] = '#'
            elif seating[i][j] == '#' and occupied >= 4:
                next[i][j] = 'L'

    if is_same(seating, next):
        break

    seating = next

occupied = 0
for i in range(len(seating)):
    for j in range(len(seating[0])):
        if seating[i][j] == '#':
            occupied += 1

print(occupied)

# Part 2
seating = list(np.loadtxt('input/day11.txt', dtype=str))
seating = [[c for c in s] for s in seating]

while True:
    next = [[c for c in s] for s in seating]
    
    # for r in seating:
    #     print(''.join(r))
    # print()

    for i in range(len(seating)):
        for j in range(len(seating[0])):
            if seating[i][j] == '.':
                continue

            occupied = 0

            # Check above
            x, y = i-1, j
            while x >= 0 and seating[x][y] == '.':
                x -= 1
            if x >= 0 and seating[x][y] == '#':
                occupied += 1

            # Check below
            x, y = i+1, j
            while x < len(seating) and seating[x][y] == '.':
                x += 1
            if x < len(seating) and seating[x][y] == '#':
                occupied += 1

            # Check to the left
            x, y = i, j-1
            while y >= 0 and seating[x][y] == '.':
                y -= 1
            if y >= 0 and seating[x][y] == '#':
                occupied += 1

            # Check to the right
            x, y = i, j+1
            while y < len(seating[0]) and seating[x][y] == '.':
                y += 1
            if y < len(seating[0]) and seating[x][y] == '#':
                occupied += 1

            # Check to the upper-left
            x, y = i-1, j-1
            while x >= 0 and y >= 0 and seating[x][y] == '.':
                x -= 1
                y -= 1
            if x >= 0 and y >= 0 and seating[x][y] == '#':
                occupied += 1

            # Check to the upper-right
            x, y = i-1, j+1
            while x >= 0 and y < len(seating[0]) and seating[x][y] == '.':
                x -= 1
                y += 1
            if x >= 0 and y < len(seating[0]) and seating[x][y] == '#':
                occupied += 1

            # Check to the lower-left
            x, y = i+1, j-1
            while x < len(seating) and y >= 0 and seating[x][y] == '.':
                x += 1
                y -= 1
            if x < len(seating) and y >= 0 and seating[x][y] == '#':
                occupied += 1

            # Check to the lower-right
            x, y = i+1, j+1
            while x < len(seating) and y < len(seating[0]) and seating[x][y] == '.':
                x += 1
                y += 1
            if x < len(seating) and y < len(seating[0]) and seating[x][y] == '#':
                occupied += 1

            if seating[i][j] == 'L' and occupied == 0:
                next[i][j] = '#'
            elif seating[i][j] == '#' and occupied >= 5:
                next[i][j] = 'L'

    if is_same(seating, next):
        break

    seating = next

occupied = 0
for i in range(len(seating)):
    for j in range(len(seating[0])):
        if seating[i][j] == '#':
            occupied += 1

print(occupied)