import argparse
from collections import *
from typing import *

import numpy as np
import utils


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        grid = [[int(x) for x in line.split()] for line in lines[:-1]]
        grid = np.array(grid).T

        s = 0
        for i, op in enumerate(lines[-1].split()):
            if op == "+":
                s += np.sum(grid[i])
            elif op == "*":
                s += np.prod(grid[i])
        print(s)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().splitlines()
        grid = [list(x) for x in lines[:-1]]
        grid = np.array(grid, dtype=object).T

        nums = ["".join(x).strip() for x in grid]
        collect = [[]]
        for n in nums:
            if n == "":
                collect.append([])
            else:
                collect[-1].append(int(n))

        s = 0
        for op, nums in zip(lines[-1].split(), collect, strict=True):
            if op == "+":
                s += np.sum(nums)
            elif op == "*":
                s += np.prod(nums)

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
