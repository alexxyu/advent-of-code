import argparse
from collections import *
from typing import *

import utils


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        grid = f.read().strip().splitlines()

        def traverse(i, j, acc, direction):
            if len(acc) == 4:
                return 1 if acc == "XMAS" else 0
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
                return 0

            s = 0
            i_n, j_n = i + direction[0], j + direction[1]
            if 0 <= i_n < len(grid) and 0 <= j_n < len(grid[i_n]):
                c_n = grid[i_n][j_n]
                s += traverse(i_n, j_n, acc + c_n, direction)
            return s

        s = 0
        for (i, j), c in utils.iter_grid_with_pos(grid):
            for direction in [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                s += traverse(i, j, c, direction)
        print(s)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        grid = f.read().strip().splitlines()

        def traverse(i, j, acc, direction):
            if len(acc) == 3:
                return 1 if acc == "MAS" or acc =="SAM" else 0
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
                return 0

            s = 0
            i_n, j_n = i + direction[0], j + direction[1]
            if 0 <= i_n < len(grid) and 0 <= j_n < len(grid[i_n]):
                c_n = grid[i_n][j_n]
                s += traverse(i_n, j_n, acc + c_n, direction)
            return s

        s = 0
        for (i, j), c in utils.iter_grid_with_pos(grid):
            r = traverse(i, j, c, (1, 1))
            if r > 0:
                i_n = i + 2
                if i_n < len(grid):
                    t = traverse(i_n, j, grid[i_n][j], (-1, 1))
                    if t > 0:
                        s += 1
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
    filename = utils.get_real_input(4)

part_a(filename)
if not args.skip_b:
    part_b(filename)
