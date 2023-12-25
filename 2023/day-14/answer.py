import argparse
from functools import lru_cache

import numpy as np
import utils


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        grid = [list(line) for line in lines]
        s = 0
        for c in range(len(grid[0])):
            for i, row in enumerate(grid):
                if row[c] == "O":
                    r = i
                    while r > 0 and grid[r - 1][c] == ".":
                        r -= 1
                    grid[i][c] = "."
                    grid[r][c] = "O"
                    s += len(grid) - r
        print(s)


@lru_cache
def cycle(grid):
    def move(g):
        arrayed = np.array(g)
        for c in range(len(arrayed[0])):
            for i, row in enumerate(arrayed):
                if row[c] == "O":
                    r = i
                    while r > 0 and arrayed[r - 1][c] == ".":
                        r -= 1
                    arrayed[i][c] = "."
                    arrayed[r][c] = "O"
        rotated = np.rot90(arrayed, k=-1)
        return tuple(tuple(r) for r in rotated)

    return move(move(move(move(grid))))


memo = {}


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        grid = tuple(tuple(c for c in line) for line in lines)

        i, N = 0, int(1e9)
        while i < N:
            grid = cycle(grid)
            if grid in memo:
                k = i - memo[grid]
                r = N - i
                skip = (r // k) * k
                i += skip
            else:
                memo[grid] = i
            i += 1

        s = 0
        for i, row in enumerate(grid):
            for c in row:
                if c == "O":
                    s += len(grid) - i
        print(s)


parser = argparse.ArgumentParser()
parser.add_argument(
    "filename",
    help="the input file, will default to actual AoC input if omitted",
    type=str,
    nargs="?",
    default=None,
)
parser.add_argument("--skip-b", help="skip running part b", action="store_true")
args = parser.parse_args()

filename = args.filename
if not args.filename:
    filename = utils.get_real_input(14)

part_a(filename)
if not args.skip_b:
    part_b(filename)
