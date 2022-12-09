import argparse

DIRECTIONS = {
    'L': (-1, 0),
    'R': (1, 0),
    'U': (0, -1),
    'D': (0, 1),
}


def debug(pos):
    min_x = min(pos, key=lambda x: x[0])[0]
    min_y = min(pos, key=lambda x: x[1])[1]
    max_x = max(pos, key=lambda x: x[0])[0]
    max_y = max(pos, key=lambda x: x[1])[1]

    M = max_y - min_y + 1
    N = max_x - min_x + 1

    grid = [['.' for _ in range(N)] for _ in range(M)]
    for i, (x, y) in enumerate(pos):
        x, y = (x - min_x), (y - min_y)
        grid[y][x] = str(i)
    for row in grid:
        print(''.join(row))


def is_adjacent(ax, ay, bx, by):
    return abs(ax - bx) <= 1 and abs(ay - by) <= 1


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().splitlines()
        positions = set([(0, 0)])

        h, t = (0, 0), (0, 0)
        for line in lines:
            d, n = line.split()
            n = int(n)

            (tx, ty), (hx, hy) = t, h
            dx, dy = DIRECTIONS[d]

            for _ in range(n):
                hx += dx
                hy += dy
                if not is_adjacent(hx, hy, tx, ty):
                    tx += dx
                    ty += dy

                    # When the head moves horizontally, the tail must necessarily
                    # move to the same row in order to stay adjacent. Similar logic
                    # holds when the head moves vertically.
                    if dx != 0:
                        ty = hy
                    elif dy != 0:
                        tx = hx

                    positions.add((tx, ty))

            h = (hx, hy)
            t = (tx, ty)

        print(len(positions))


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()
        positions = set([(0, 0)])
        rope = [(0, 0) for _ in range(10)]

        for line in lines:
            d, n = line.split()
            n = int(n)

            dx, dy = DIRECTIONS[d]
            for _ in range(n):
                (hx, hy) = rope[0]
                (hx, hy) = rope[0] = (hx+dx, hy+dy)
                for i in range(1, 10):
                    (tx, ty) = rope[i]

                    if not is_adjacent(hx, hy, tx, ty):
                        if hx > tx:
                            tx += 1
                            if hy > ty:
                                ty += 1
                            elif hy < ty:
                                ty -= 1
                        elif hx < tx:
                            tx -= 1
                            if hy > ty:
                                ty += 1
                            elif hy < ty:
                                ty -= 1
                        elif hy > ty:
                            ty += 1
                        elif hy < ty:
                            ty -= 1

                        if i == 9:
                            positions.add((tx, ty))

                    (hx, hy) = rope[i] = (tx, ty)

        print(len(positions))


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true',
                    help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
