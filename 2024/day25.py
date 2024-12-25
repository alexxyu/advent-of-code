import argparse
import itertools
from collections import *
from typing import *

import utils

COLS = 5
ROWS = 7


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        schematics = [x.splitlines() for x in f.read().strip().split("\n\n")]

        locks, keys = [], []
        for scheme in schematics:
            size = [0] * COLS
            for r in range(len(scheme)):
                for c in range(5):
                    if scheme[r][c] == "#":
                        size[c] += 1

            if scheme[0][0] == "#":
                locks.append(tuple(size))
            else:
                keys.append(tuple(size))

        s = 0
        for a, b in itertools.product(locks, keys):
            if all(x + y <= ROWS for x, y in zip(a, b, strict=True)):
                s += 1
        print(s)


parser = argparse.ArgumentParser()
parser.add_argument(
    "filename",
    help="the input file, will default to actual AoC input if omitted",
    type=str,
    nargs="?",
    default=None,
)
args = parser.parse_args()

filename = args.filename
if not args.filename:
    filename = utils.get_real_input(25)

part_a(filename)
