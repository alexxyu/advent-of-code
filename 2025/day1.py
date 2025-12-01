import argparse
from collections import *
from typing import *

import utils


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()

        pos = 50
        t = 0
        for line in lines:
            direction, steps = line[0], int(line[1:])
            if direction == "R":
                pos = (pos + steps) % 100
            elif direction == "L":
                pos = (pos - steps) % 100

            if pos == 0:
                t += 1

        print(t)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()

        pos = 50
        t = 0
        for line in lines:
            direction, steps = line[0], int(line[1:])

            t += steps // 100
            steps = steps % 100

            if direction == "R":
                new_pos = pos + steps
                if pos != 0 and new_pos >= 100:
                    t += 1
            elif direction == "L":
                new_pos = pos - steps
                if pos != 0 and new_pos <= 0:
                    t += 1

            pos = new_pos % 100

        print(t)


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
    filename = utils.get_real_input(1)

part_a(filename)
if not args.skip_b:
    part_b(filename)
