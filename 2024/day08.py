import argparse
import itertools
from collections import *
from typing import *

from utils import get_real_input, iter_grid_with_pos


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        grid = f.read().strip().splitlines()
        freq_to_locs = defaultdict(list)

        antinodes = set()
        for (r, c), p in iter_grid_with_pos(grid):
            if p != ".":
                freq_to_locs[p].append((r, c))

        for nodes in freq_to_locs.values():
            for a, b in itertools.combinations(nodes, 2):
                dr, dc = b[0] - a[0], b[1] - a[1]

                r0, c0 = a[0] - dr, a[1] - dc
                if 0 <= r0 < len(grid) and 0 <= c0 < len(grid[0]):
                   antinodes.add((r0, c0))

                r1, c1 = b[0] + dr, b[1] + dc
                if 0 <= r1 < len(grid) and 0 <= c1 < len(grid[0]):
                   antinodes.add((r1, c1))

        print(len(antinodes))



def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        grid = f.read().strip().splitlines()
        freq_to_locs = defaultdict(list)

        antinodes = set()
        for (r, c), p in iter_grid_with_pos(grid):
            if p != ".":
                freq_to_locs[p].append((r, c))

        for nodes in freq_to_locs.values():
            for a, b in itertools.combinations(nodes, 2):
                dr, dc = b[0] - a[0], b[1] - a[1]

                r0, c0 = a[0], a[1]
                while True:
                    if 0 <= r0 < len(grid) and 0 <= c0 < len(grid[0]):
                        antinodes.add((r0, c0))
                    else:
                        break
                    r0, c0 = r0 - dr, c0 - dc

                r1, c1 = a[0], a[1]
                while True:
                    if 0 <= r1 < len(grid) and 0 <= c1 < len(grid[0]):
                        antinodes.add((r1, c1))
                    else:
                        break
                    r1, c1 = r1 + dr, c1 + dc

        print(len(antinodes))


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
    filename = get_real_input(8)

part_a(filename)
if not args.skip_b:
    part_b(filename)
