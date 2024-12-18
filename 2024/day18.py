import argparse
from collections import *
from typing import *

import utils

ROWS = 71
COLS = 71
NBYTES = 1024

def find_path(grid: List[List[str]]):
    steps = 0
    q = [(0, 0)]
    seen = set()
    while q:
        N = len(q)
        for _ in range(N):
            (r, c), q = q[0], q[1:]
            if (r, c) in seen:
                continue
            seen.add((r, c))

            if (r, c) == (ROWS-1, COLS-1):
                return steps

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) in seen:
                    continue
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == "#":
                    continue
                q.append((nr, nc))
        steps += 1

    return None


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        grid = [["." for _ in range(COLS)] for _ in range(ROWS)]
        for line in lines[:NBYTES]:
            c, r = utils.parse_nums(line)
            grid[r][c] = "#"
        print(find_path(grid))


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()

        for n in range(NBYTES+1, len(lines)):
            grid = [["." for _ in range(COLS)] for _ in range(ROWS)]
            for line in lines[:n]:
                c, r = utils.parse_nums(line)
                grid[r][c] = "#"

            if find_path(grid) is None:
                print(lines[n-1])
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
    filename = utils.get_real_input(18)

part_a(filename)
if not args.skip_b:
    part_b(filename)
