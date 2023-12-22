import argparse
import heapq
import itertools
import math
import re
from collections import *
from copy import deepcopy
from dataclasses import dataclass
from enum import Enum
from functools import cmp_to_key, lru_cache, reduce
from typing import *
import utils
from utils import Position2D, Direction


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().splitlines()

        start = None
        for i, r in enumerate(lines):
            for j, c in enumerate(r):
                if c == 'S':
                    start = Position2D(i, j)

        res = simulate(lines, start, 64)
        print(len(res))


class TraversalDirection(Enum):
    EAST = 0
    NORTHEAST = 1
    NORTH = 2
    NORTHWEST = 3
    WEST = 4
    SOUTHWEST = 5
    SOUTH = 6
    SOUTHEAST = 7


def simulate(grid: list[str], start: Position2D, steps: int):
    q = set([start])
    for _ in range(steps):
        nq = set()
        for p in q:
            for np in p.iter_neighbors():
                nr, nc = np
                if np.is_inside_grid(grid) and grid[nr][nc] in '.S':
                    nq.add(np)
        q = nq
    return q


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()

        start = None
        for i, r in enumerate(lines):
            for j, c in enumerate(r):
                if c == 'S':
                    start = Position2D(i, j)

        # Grid is 131 x 131, with 'S' at (65, 65)
        assert start == Position2D(65, 65)
        S = 26501365
        W = (S - 65) // 131

        # plots_odd = 7262
        # plots_even = 7232
        plots_odd = len(simulate(lines, start, 131))
        plots_even = len(simulate(lines, start, 2*131))

        # plots_east = 5508
        # plots_north = 5515
        # plots_west = 5479
        # plots_south = 5472
        plots_east   = len(simulate(lines, Position2D(65, 0), 131-1))
        plots_north  = len(simulate(lines, Position2D(130, 65), 131-1))
        plots_west   = len(simulate(lines, Position2D(65, 130), 131-1))
        plots_south  = len(simulate(lines, Position2D(0, 65), 131-1))

        # plots_ne_sm = 909
        # plots_nw_sm = 935
        # plots_sw_sm = 944
        # plots_se_sm = 902
        plots_ne_sm  = len(simulate(lines, Position2D(130, 0), 65-1))
        plots_nw_sm  = len(simulate(lines, Position2D(130, 130), 65-1))
        plots_sw_sm  = len(simulate(lines, Position2D(0, 130), 65-1))
        plots_se_sm  = len(simulate(lines, Position2D(0, 0), 65-1))

        # plots_nw_lg = 6384
        # plots_sw_lg = 6357
        # plots_ne_lg = 6393
        # plots_se_lg = 6377
        plots_ne_lg  = len(simulate(lines, Position2D(130, 0), 131+65-1))
        plots_nw_lg  = len(simulate(lines, Position2D(130, 130), 131+65-1))
        plots_sw_lg  = len(simulate(lines, Position2D(0, 130), 131+65-1))
        plots_se_lg  = len(simulate(lines, Position2D(0, 0), 131+65-1))

        # n_odd  = 4 + 12 + 20 + ...     = 40924885401
        # n_even = 1 + 8 + 16 + 24 + ... = 40925290000
        n_odd, n_even = 1, 0
        for i in range(W):
            if i % 2 == 0:
                n_odd += 4*i
            else:
                n_even += 4*i

        s = 0

        # Add the plots from the entirely-covered plots
        s += n_odd * plots_odd + n_even * plots_even

        # Add the plots from the east, north, west, and south ends
        s += plots_east + plots_north + plots_west + plots_south

        # Add the plots from the large and small diagonal ends
        # Every time we step over to a new grid, we add a new one of these diagonal ends
        s += (W-1) * (plots_ne_lg + plots_nw_lg + plots_sw_lg + plots_se_lg)
        s += W * (plots_ne_sm + plots_nw_sm + plots_sw_sm + plots_se_sm)

        print(s)


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file, will default to actual AoC input if omitted', type=str, nargs='?', default=None)
parser.add_argument('--skip-b', help='skip running part b', action='store_true')
args = parser.parse_args()

filename = args.filename
if not args.filename:
    filename = utils.get_real_input(21)

part_a(filename)
if not args.skip_b:
    part_b(filename)
