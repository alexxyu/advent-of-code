import argparse
import re
from collections import defaultdict

import utils


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().splitlines()
        s = 0
        for r, line in enumerate(lines):
            nums = re.finditer(r"\d+", line)
            for n in nums:
                is_part = False
                for c in range(n.start(), n.end()):
                    for neighbor in utils.iter_grid_neighbors(lines, r, c):
                        if neighbor != "." and not neighbor.isdigit():
                            is_part = True
                if is_part:
                    s += int(line[n.start(): n.end()])
        print(s)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().splitlines()
        gear_to_parts = defaultdict(list)
        for r, line in enumerate(lines):
            nums = re.finditer(r"\d+", line)
            for n in nums:
                gear = None
                for c in range(n.start(), n.end()):
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            nr, nc = r + dr, c + dc
                            try:
                                if lines[nr][nc] == "*":
                                    gear = (nr, nc)
                            except IndexError:
                                pass
                if gear:
                    gear_to_parts[gear].append(int(line[n.start(): n.end()]))

        g = 0
        for p in gear_to_parts.values():
            if len(p) == 2:
                g += p[0] * p[1]

        print(g)


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
    filename = utils.get_real_input(3)

part_a(filename)
if not args.skip_b:
    part_b(filename)
