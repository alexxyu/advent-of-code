import argparse
from collections import *
from typing import *

import utils


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        ranges, ids = f.read().strip().split("\n\n")
        fresh = []
        for r in ranges.split():
            a, b = r.split("-")
            fresh.append([int(a), int(b)])

        s = 0
        for n in ids.split():
            if any(r[0] <= int(n) <= r[1] for r in fresh):
                s += 1

        print(s)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        ranges, _ = f.read().strip().split("\n\n")
        fresh = []
        for r in ranges.split():
            a, b = r.split("-")
            fresh.append([int(a), int(b)])

        s = 0
        fresh.sort()

        merged, last = [fresh[0]], fresh[0]
        for curr in fresh[1:]:
            if curr[0] <= last[1]:
                last[1] = max(last[1], curr[1])
            else:
                merged.append(curr)
                last = curr

        s = sum(r[1] - r[0] + 1 for r in merged)
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
    filename = utils.get_real_input(5)

part_a(filename)
if not args.skip_b:
    part_b(filename)
