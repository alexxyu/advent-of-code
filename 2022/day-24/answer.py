import argparse
from collections import defaultdict
from enum import Enum


class Direction(Enum):
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)
    UP = (-1, 0)


SYMBOL_TO_DIRECTION = {
    '>': Direction.RIGHT,
    '<': Direction.LEFT,
    '^': Direction.UP,
    'v': Direction.DOWN,
}


def simulate(grid, start, end, blizzards):
    M, N = len(grid), len(grid[0])

    def is_oob(r, c):
        return r < 0 or c < 0 or r >= M or c >= N or grid[r][c] == '#'

    def update_blizzards():
        blizzards_updated = defaultdict(list)
        for (r, c), b in blizzards.items():
            for d in b:
                (dr, dc) = d.value
                np = (r+dr, c+dc)
                if is_oob(*np):
                    if d == Direction.RIGHT:
                        np = (r, 1)
                    elif d == Direction.LEFT:
                        np = (r, N-2)
                    elif d == Direction.UP:
                        np = (M-2, c)
                    elif d == Direction.DOWN:
                        np = (1, c)
                blizzards_updated[np].append(d)
        return blizzards_updated

    i, q = 0, [start]
    while q:
        blizzards = update_blizzards()
        next_q = set()
        for _ in range(len(q)):
            (r, c) = q.pop(0)
            if (r, c) == end:
                next_q = {}
                break
            if is_oob(r, c) or (r, c) in blizzards:
                continue
            next_q.add((r, c))
            for d in [v for v in Direction]:
                (dr, dc) = d.value
                nr, nc = r+dr, c+dc
                next_q.add((nr, nc))
        q = list(next_q)
        i += 1

    return i, blizzards


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        grid = list(map(list, f.read().splitlines()))
        M, N = len(grid), len(grid[0])

        blizzards = defaultdict(list)
        for i in range(M):
            for j in range(N):
                if d := SYMBOL_TO_DIRECTION.get(grid[i][j], None):
                    blizzards[(i, j)].append(d)

        start, end = (0, 1), (M-1, N-2)
        n, _ = simulate(grid, start, end, blizzards)
        print(n)


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        grid = list(map(list, f.read().splitlines()))
        M, N = len(grid), len(grid[0])

        blizzards = defaultdict(list)
        for i in range(M):
            for j in range(N):
                if d := SYMBOL_TO_DIRECTION.get(grid[i][j], None):
                    blizzards[(i, j)].append(d)

        start = (0, 1)
        end = (M-1, N-2)

        n1, blizzards = simulate(grid, start, end, blizzards)
        n2, blizzards = simulate(grid, end, start, blizzards)
        n3, blizzards = simulate(grid, start, end, blizzards)
        print(n1, n2, n3, "->", n1+n2+n3)


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true',
                    help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
