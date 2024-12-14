import argparse
from collections import *
from typing import *

import numpy as np
import utils


class UnionFind:
    def __init__(self, rows, cols):
        self.parent = {}
        for r in range(rows):
            for c in range(cols):
                self.parent[(r, c)] = (r, c)

    def get_groups(self):
        groups = defaultdict(list)
        for r, c in self.parent:
            groups[self.find(r, c)].append((r, c))
        return groups.values()

    def find(self, r, c):
        if (r, c) != self.parent[(r, c)]:
            self.parent[(r, c)] = self.find(*self.parent[(r, c)])
        return self.parent[(r, c)]

    def union(self, r1, c1, r2, c2):
        r1, c1 = self.find(r1, c1)
        r2, c2 = self.find(r2, c2)
        if r1 != r2 or c1 != c2:
            self.parent[(r2, c2)] = (r1, c1)


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        grid = np.array([list(x) for x in f.read().strip().splitlines()])
        uf = UnionFind(len(grid), len(grid[0]))

        for (r, c), p in utils.iter_grid_with_pos(grid):
            for dr, dc in [(1, 0), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]) and grid[nr, nc] == p:
                    uf.union(r, c, nr, nc)

        regions = uf.get_groups()

        s = 0
        for region in regions:
            perimeter = 0
            for (r, c) in region:
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[nr]) or grid[nr, nc] != grid[r, c]:
                        perimeter += 1
            s += perimeter * len(region)

        print(s)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        grid = np.array([list(x) for x in f.read().strip().splitlines()])
        uf = UnionFind(len(grid), len(grid[0]))

        for (r, c), p in utils.iter_grid_with_pos(grid):
            for dr, dc in [(1, 0), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]) and grid[nr, nc] == p:
                    uf.union(r, c, nr, nc)

        regions = uf.get_groups()

        s = 0
        for region in regions:
            perimeter = 0
            coords = sorted(map(tuple, region))
            for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                seen = set()
                for (r, c) in coords:
                    if (r, c) in seen:
                        continue

                    # Iterate until we reach an edge perpendicular to the current direction
                    nr, nc = r + dr, c + dc
                    if (nr, nc) not in coords:
                        seen.add((r, c))
                        perimeter += 1

                        # Found horizontal edge: scan rightward and skip points on the same edge
                        if dr != 0:
                            t = 0
                            while (r, c+t) in coords and (nr, nc+t) not in coords:
                                seen.add((r, c+t))
                                t += 1

                        # Found vertical edge: scan downward and skip points on the same edge
                        if dc != 0:
                            t = 0
                            while (r+t, c) in coords and (nr+t, nc) not in coords:
                                seen.add((r+t, c))
                                t += 1

            s += perimeter * len(coords)

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
    filename = utils.get_real_input(12)

part_a(filename)
if not args.skip_b:
    part_b(filename)
