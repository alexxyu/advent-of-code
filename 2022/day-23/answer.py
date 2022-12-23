import argparse
from collections import *


DIRECTIONS = [
    [(-1, -1), (-1, 0), (-1, 1)],   # North
    [(1, -1), (1, 0), (1, 1)],      # South
    [(-1, -1), (0, -1), (1, -1)],   # West
    [(-1, 1), (0, 1), (1, 1)]       # East
]


def construct_grid_from_elves(elves):
    min_r = min(elves, key=lambda x: x[0])[0]
    max_r = max(elves, key=lambda x: x[0])[0]
    min_c = min(elves, key=lambda x: x[1])[1]
    max_c = max(elves, key=lambda x: x[1])[1]

    grid = [['.' for _ in range(max_c - min_c + 1)]
            for _ in range(max_r - min_r + 1)]
    for (r, c) in elves:
        grid[r - min_r][c - min_c] = '#'
    return grid


def find_empty_spaces_in_grid(elves, debug=False):
    grid = construct_grid_from_elves(elves)
    c = 0
    for r in grid:
        for k in r:
            if k == '.':
                c += 1
        if debug:
            print(''.join(r))
    return c


def can_move(r, c, elves):
    for (dr, dc) in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        nr, nc = r+dr, c+dc
        if (nr, nc) in elves:
            return True
    return False


def is_available_in_direction(r, c, d, elves):
    def is_available(r, c, dr, dc):
        nr, nc = r+dr, c+dc
        if (nr, nc) in elves:
            return False
        return True
    return all(is_available(r, c, dr, dc) for (dr, dc) in d)


def simulate_round(elves, directions):
    proposed = defaultdict(list)
    for (r, c) in elves:
        if not can_move(r, c, elves):
            continue
        for d in directions:
            if is_available_in_direction(r, c, d, elves):
                nr, nc = r+d[1][0], c+d[1][1]
                proposed[(nr, nc)].append((r, c))
                break

    for (nr, nc), old_elves in proposed.items():
        if len(old_elves) == 1:
            elves.add((nr, nc))
            elves.remove(old_elves[0])

    directions.rotate(-1)

    if all([len(v) > 1 for v in proposed.values()]):
        return False

    return True


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        grid = f.read().splitlines()
        grid = list(map(list, grid))
        M, N = len(grid), len(grid[0])

        elves = set()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '#':
                    elves.add((i, j))

        directions = deque(DIRECTIONS)
        for _ in range(10):
            simulate_round(elves, directions)

        print(find_empty_spaces_in_grid(elves))


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        grid = f.read().splitlines()
        grid = list(map(list, grid))
        M, N = len(grid), len(grid[0])

        elves = set()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '#':
                    elves.add((i, j))

        i = 1
        directions = deque(DIRECTIONS)
        while simulate_round(elves, directions):
            i += 1
        print(i)


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true',
                    help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
