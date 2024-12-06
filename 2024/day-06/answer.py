import argparse
from collections import *
from typing import *

import utils
from utils import Direction, Position2D, iter_grid_with_pos


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        grid = f.read().strip().splitlines()

        pos = None
        for (r, c), p in iter_grid_with_pos(grid):
            if p == "^":
                pos = Position2D(r, c)

        positions = set()
        direction = Direction.UP
        while 0 <= pos.row < len(grid) and 0 <= pos.col < len(grid[0]):
            positions.add(pos)
            next_pos = pos + direction
            if next_pos.row < 0 or next_pos.col < 0 or next_pos.row >= len(grid) or next_pos.col >= len(grid[0]):
                break
            if grid[next_pos.row][next_pos.col] == "#":
                direction = Direction.rot90(direction)
            else:
                pos = next_pos

        print(len(positions))


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        grid = list(map(list, f.read().strip().splitlines()))

        start = None
        for (r, c), p in iter_grid_with_pos(grid):
            if p == "^":
                start = Position2D(r, c)

        s = 0
        for (r, c), p in iter_grid_with_pos(grid):
            if p != ".":
                continue
            grid[r][c] = "#"

            positions = set()
            pos = start
            direction = Direction.UP
            while 0 <= pos.row < len(grid) and 0 <= pos.col < len(grid[0]):
                if (pos, direction) in positions:
                    s += 1
                    break

                positions.add((pos, direction))
                next_pos = pos + direction
                if next_pos.row < 0 or next_pos.col < 0 or next_pos.row >= len(grid) or next_pos.col >= len(grid[0]):
                    break
                if grid[next_pos.row][next_pos.col] == "#":
                    direction = Direction.rot90(direction)
                else:
                    pos = next_pos

            grid[r][c] = "."
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
    filename = utils.get_real_input(6)

part_a(filename)
if not args.skip_b:
    part_b(filename)
