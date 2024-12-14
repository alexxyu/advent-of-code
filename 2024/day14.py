import argparse
import re
from collections import *
from typing import *

import utils

ROWS = 103
COLS = 101

def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()

        robots = []
        for line in lines:
            c, r, vc, vr = [int(x) for x in re.findall(r"-?\d+", line)]
            robots.append((r, c, vr, vc))

        for _ in range(100):
            for i, (r, c, vr, vc) in enumerate(robots):
                nr, nc = r + vr, c + vc
                nr = nr % ROWS
                nc = nc % COLS
                robots[i] = (nr, nc, vr, vc)

        q = [0] * 4
        for (r, c, _, _) in robots:
            if r < ROWS // 2:
                if c < COLS // 2:
                    q[0] += 1
                elif c > COLS // 2:
                    q[1] += 1
            elif r > ROWS // 2:
                if c < COLS // 2:
                    q[2] += 1
                elif c > COLS // 2:
                    q[3] += 1
        print(q[0] * q[1] * q[2] * q[3])


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()

        robots = []
        for line in lines:
            c, r, vc, vr = [int(x) for x in re.findall(r"-?\d+", line)]
            robots.append((r, c, vr, vc))

        def is_christmas_tree(threshold):
            n_neighbors = 0
            positions = {(r, c) for (r, c, _, _) in robots}
            for (r1, c1, _, _) in robots:
                for (r2, c2) in [(r1 - 1, c1 - 1), (r1 - 1, c1), (r1, c1 - 1)]:
                    if r2 < 0 or c2 < 0 or (r2, c2) not in positions:
                        continue
                    n_neighbors += 1

            return n_neighbors >= threshold

        k, threshold = 0, 200
        while True:
            k += 1
            for i, (r, c, vr, vc) in enumerate(robots):
                nr, nc = r + vr, c + vc
                nr = nr % ROWS
                nc = nc % COLS
                robots[i] = (nr, nc, vr, vc)

            if is_christmas_tree(threshold):
                print(k)

                positions = {(r, c) for (r, c, _, _) in robots}
                grid = [["#" if (r, c) in positions else "." for c in range(COLS)] for r in range(ROWS)]
                print("\n".join(["".join(row) for row in grid]))
                break


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
    filename = utils.get_real_input(14)

part_a(filename)
if not args.skip_b:
    part_b(filename)
