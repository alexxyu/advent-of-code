import argparse
from collections import *
from typing import *

import utils


def is_safe(lvls):
    is_increasing = True
    is_decreasing = True
    within_range = True
    for i in range(1, len(lvls)):
        if lvls[i] < lvls[i-1]:
            is_increasing = False
        if lvls[i] > lvls[i-1]:
            is_decreasing = False

        diff = abs(lvls[i] - lvls[i-1])
        if diff < 1 or diff > 3:
            within_range = False

    return (is_increasing or is_decreasing) and within_range



def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        count = sum(is_safe(list(map(int, line.split()))) for line in lines)
        print(count)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        count = 0
        for line in lines:
            lvls = list(map(int, line.split()))

            if is_safe(lvls):
                count += 1
            else:
                for i in range(len(lvls)):
                    lvls_try = lvls[:i] + lvls[i+1:]
                    if is_safe(lvls_try):
                        count += 1
                        break

        print(count)


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
    filename = utils.get_real_input(2)

part_a(filename)
if not args.skip_b:
    part_b(filename)
