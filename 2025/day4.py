import argparse
from collections import *
from typing import *

import utils
from utils import (
    iter_grid_neighbors,
    iter_grid_with_pos,
)


def get_accessible_rolls(grid):
    positions = set()
    for (r, c), k in iter_grid_with_pos(grid):
        if k != "@":
            continue
        t = sum(p == "@" for p in iter_grid_neighbors(grid, r, c))
        if t < 4:
            positions.add((r, c))
    return positions


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()

        s = len(get_accessible_rolls(lines))
        print(s)

def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        lines = [list(line) for line in lines]

        s = 0
        while (rolls := get_accessible_rolls(lines)) and len(rolls) > 0:
            for r, c in rolls:
                lines[r][c] = "."
            s += len(rolls)

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
