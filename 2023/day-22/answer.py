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


@dataclass
class Brick:
    start: (int, int, int)
    end:   (int, int, int)


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().strip().splitlines()

        bricks = []
        for line in lines:
            a, b = line.split('~')
            start = utils.parse_list_nums(a, ',')
            end   = utils.parse_list_nums(b, ',')
            bricks.append(Brick(start, end))

        bricks.sort(key=lambda b: b.end[2])

        s = set()
        d = dict()
        for i, b in enumerate(bricks):
            max_z = 0
            supporters = set()
            for (x, y) in itertools.product(range(b.start[0], b.end[0]+1), range(b.start[1], b.end[1]+1)):
                if (x, y) in d:
                    z, k = d[(x, y)]
                    if z > max_z:
                        max_z = z
                        supporters = {k}
                    elif z == max_z:
                        supporters.add(k)

            if len(supporters) == 1:
                s.add(next(iter(supporters)))

            dz = b.start[2] - max_z
            b.start[2] -= dz
            b.end[2] -= dz

            for (x, y) in itertools.product(range(b.start[0], b.end[0]+1), range(b.start[1], b.end[1]+1)):
                d[(x, y)] = (b.end[2]+1, i)

        print(len(bricks) - len(s))


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().strip().splitlines()

        bricks = []
        for line in lines:
            a, b = line.split('~')
            start = utils.parse_list_nums(a, ',')
            end   = utils.parse_list_nums(b, ',')
            bricks.append(Brick(start, end))

        bricks.sort(key=lambda b: b.end[2])

        d = dict()
        supporting = defaultdict(list)
        for i, b in enumerate(bricks):
            max_z = 0
            supporters = set()
            for (x, y) in itertools.product(range(b.start[0], b.end[0]+1), range(b.start[1], b.end[1]+1)):
                if (x, y) in d:
                    z, k = d[(x, y)]
                    if z > max_z:
                        max_z = z
                        supporters = {k}
                    elif z == max_z:
                        supporters.add(k)

            for s in supporters:
                supporting[s].append(i)

            dz = b.start[2] - max_z
            b.start[2] -= dz
            b.end[2] -= dz

            for (x, y) in itertools.product(range(b.start[0], b.end[0]+1), range(b.start[1], b.end[1]+1)):
                d[(x, y)] = (b.end[2]+1, i)

        print(sum(count_chain(dict(supporting), k) for k in supporting))


def count_chain(supporting, n):
    supported = defaultdict(int)
    for k in supporting:
        for t in supporting[k]:
            supported[t] += 1

    s = 0
    q = [n]
    while q:
        s += 1
        n, q = q[0], q[1:]
        if n in supporting:
            for k in supporting[n]:
                supported[k] -= 1
                if supported[k] == 0:
                    q.append(k)
    return s-1


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file, will default to actual AoC input if omitted', type=str, nargs='?', default=None)
parser.add_argument('--skip-b', help='skip running part b', action='store_true')
args = parser.parse_args()

filename = args.filename
if not args.filename:
    filename = utils.get_real_input(22)

part_a(filename)
if not args.skip_b:
    part_b(filename)
