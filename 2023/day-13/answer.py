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
import numpy as np


def check_columns(grid):
    for c in range(1, len(grid[0])):
        sat = True
        for row in grid:
            k = min(c, len(row)-c)
            a = row[c-k:c]
            b = row[c:c+k]
            if ''.join(a[::-1]) != ''.join(b):
                sat = False
        if sat:
            return c
    return None


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        patterns = f.read().split('\n\n')
        s = 0
        for p in patterns:
            p = [[c for c in r] for r in p.splitlines()]

            if c := check_columns(p):
                s += c
            elif r := check_columns(np.array(p).T):
                s += 100*r
            else:
                print('\n'.join([''.join(c) for c in p]))
        print(s)


def encode(row):
    return int(''.join(['0' if c == '.' else '1' for c in row]), 2)


def count_smudges(a, b):
    x, y = encode(a), encode(b)
    return (x ^ y).bit_count()


def check_columns_with_smudge(grid):
    for c in range(1, len(grid[0])):
        smudges = 0
        for row in grid:
            k = min(c, len(row)-c)
            a = row[c-k:c]
            b = row[c:c+k]
            smudges += count_smudges(a[::-1], b)
        if smudges == 1:
            return c
    return None


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        patterns = f.read().split('\n\n')
        s = 0
        for p in patterns:
            p = [[c for c in r] for r in p.splitlines()]

            if c := check_columns_with_smudge(p):
                s += c
            if r := check_columns_with_smudge(np.array(p).T):
                s += 100*r
        print(s)


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file, will default to actual AoC input if omitted', type=str, nargs='?', default=None)
parser.add_argument('--skip-b', help='skip running part b', action='store_true')
args = parser.parse_args()

filename = args.filename
if not args.filename:
    filename = utils.get_real_input(13)

part_a(filename)
if not args.skip_b:
    part_b(filename)
