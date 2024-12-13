import argparse
import re
from collections import *
from typing import *

import utils
from sympy import Symbol, solve

type Position = Tuple[int, int]

def parse_machine(section: str, prize_modifier: int = 0) -> Tuple[Position, Position, Position]:
    a, b, prize = section.split("\n")
    ax, ay = [int(n) for n in re.findall(r"\+(\d+)", a)]
    bx, by = [int(n) for n in re.findall(r"\+(\d+)", b)]
    px, py = [int(n) for n in re.findall(r"=(\d+)", prize)]
    return (ax, ay), (bx, by), (px + prize_modifier, py + prize_modifier)


def get_cost(a: Position, b: Position, p: Position):
    # https://imgflip.com/i/9dmfs9
    r, s = Symbol("r", integer=True), Symbol("s", integer=True)
    sol = solve([r*a[0] + s*b[0] - p[0], r*a[1] + s*b[1] - p[1]], [r, s])

    if len(sol) == 0:
        return 0

    return sol[r] * 3 + sol[s]

def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        machines = f.read().strip().split("\n\n")
        cost = sum(get_cost(*parse_machine(machine)) for machine in machines)
        print(cost)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        machines = f.read().strip().split("\n\n")
        cost = sum(get_cost(*parse_machine(machine, 10000000000000)) for machine in machines)
        print(cost)


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
    filename = utils.get_real_input(13)

part_a(filename)
if not args.skip_b:
    part_b(filename)
