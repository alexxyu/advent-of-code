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
from utils import Direction, Position2D


def solve(grid, a, b):
    memo = defaultdict(lambda: float('inf'))
    seen = set()
    q = [(0, Position2D(0, 0), Direction.DOWN), (0, Position2D(0, 0), Direction.RIGHT)]

    while q:
        s, p, d = heapq.heappop(q)
        if p.row == len(grid)-1 and p.col == len(grid[-1])-1:
            return s
        if (p, d) in seen:
            continue
        seen.add((p, d))

        np, ns = p, s
        for step in range(1, b+1):
            np += d
            if not Position2D.is_inside_grid(grid, np):
                break

            ns += grid[np.row][np.col]
            if step >= a and ns <= memo[(np, d)]:
                memo[(np, d)] = ns

                heapq.heappush(q, (ns, np, utils.Direction.rot90(d, k=1)))
                heapq.heappush(q, (ns, np, utils.Direction.rot90(d, k=-1)))

    return None


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().splitlines()
        grid = utils.parse_grid_digits(lines)
        print(solve(grid, 1, 3))


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()
        grid = utils.parse_grid_digits(lines)
        print(solve(grid, 4, 10))


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file, will default to actual AoC input if omitted', type=str, nargs='?', default=None)
parser.add_argument('--skip-b', help='skip running part b', action='store_true')
args = parser.parse_args()

filename = args.filename
if not args.filename:
    filename = utils.get_real_input(17)

part_a(filename)
if not args.skip_b:
    part_b(filename)
