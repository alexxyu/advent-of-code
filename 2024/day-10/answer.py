import argparse
from collections import *
from typing import *

import utils


def generate_dfs(grid: List[List[int]], on_success: Callable[[int, int], None]) -> Callable[[int, int, int], None]:
    def dfs(r: int, c: int, t: int = 0):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
            return
        if grid[r][c] != t:
            return

        if grid[r][c] == 9:
            on_success(r, c)
        else:
            for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r+dr, c+dc
                dfs(nr, nc, t+1)

    return dfs


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        grid = [[int(x) if x.isdigit() else -1 for x in line] for line in lines]

        s = 0
        for (r, c), _ in utils.iter_grid_with_pos(grid):
            seen = set()
            generate_dfs(grid, lambda r, c, seen = seen: seen.add((r, c)))(r, c)
            s += len(seen)
        print(s)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        grid = [[int(x) if x.isdigit() else -1 for x in line] for line in lines]

        s = 0
        def increment(_r, _c):
            nonlocal s
            s += 1

        for (r, c), _ in utils.iter_grid_with_pos(grid):
            generate_dfs(grid, increment)(r, c)
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
    filename = utils.get_real_input(10)

part_a(filename)
if not args.skip_b:
    part_b(filename)
