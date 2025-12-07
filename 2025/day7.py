import argparse
from collections import *
from typing import *

import utils
from utils import find_grid_pos_with_value


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        grid = f.read().strip().splitlines()
        start = find_grid_pos_with_value(grid, "S")

        s = 0
        cols = {start[0].col}
        for row in range(1, len(grid)):
            new_cols = set()
            for col in cols:
                if grid[row][col] == "^":
                    new_cols.add(col-1)
                    new_cols.add(col+1)
                    s += 1
                elif grid[row][col] == ".":
                    new_cols.add(col)
            cols = new_cols

        print(s)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        grid = f.read().strip().splitlines()
        grid = [list(x) for x in grid]
        start = find_grid_pos_with_value(grid, "S")

        dp = defaultdict(int)
        dp[start[0].col] = 1

        for row in range(1, len(grid)):
            new_dp = defaultdict(int)
            for col, v in dp.items():
                if grid[row][col] == "^":
                    new_dp[col-1] += v
                    new_dp[col+1] += v
                elif grid[row][col] == ".":
                    new_dp[col] += v
            dp = new_dp

        print(sum(dp.values()))

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
    filename = utils.get_real_input(7)

part_a(filename)
if not args.skip_b:
    part_b(filename)
