import argparse
from collections import *
from typing import *

import utils
import z3


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()

        t = 0
        for line in lines:
            segments = line.split()
            schematic = [1 if x == "#" else 0 for x in segments[0][1:-1]]

            buttons = []
            for b in segments[1:-1]:
                buttons.append([int(x) for x in b[1:-1].split(",")])

            s = z3.Optimize()
            presses = [z3.Int(f"{i}") for i in range(len(buttons))]
            for p in presses:
                s.add(p >= 0)

            for k, n in enumerate(schematic):
                tgt = [presses[i] for i, b in enumerate(buttons) if k in b]
                s.add(z3.Sum(tgt) % 2 == n)

            s.minimize(z3.Sum(presses))
            if s.check() == z3.sat:
                model = s.model()
                t += sum(model[p].as_long() for p in presses)

        print(t)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()

        t = 0
        for line in lines:
            segments = line.split()
            buttons = []
            for b in segments[1:-1]:
                buttons.append([int(x) for x in b[1:-1].split(",")])

            joltages = [int(x) for x in segments[-1][1:-1].split(",")]

            s = z3.Optimize()
            presses = [z3.Int(f"{i}") for i in range(len(buttons))]
            for p in presses:
                s.add(p >= 0)

            for j, jolt in enumerate(joltages):
                tgt = [presses[i] for i, b in enumerate(buttons) if j in b]
                s.add(z3.Sum(tgt) == jolt)

            s.minimize(z3.Sum(presses))
            if s.check() == z3.sat:
                model = s.model()
                t += sum(model[p].as_long() for p in presses)

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
    filename = utils.get_real_input(10)

part_a(filename)
if not args.skip_b:
    part_b(filename)
