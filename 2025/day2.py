import argparse
import re
from collections import *
from typing import *

import utils


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        ranges = "".join(lines).split(",")

        s = 0
        for r in ranges:
            a, b = r.split("-")
            for n in range(int(a), int(b)+1):
                n_str = str(n)
                x, y = n_str[:len(n_str)//2], n_str[len(n_str)//2:]
                if x == y:
                    s += n

        print(s)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        ranges = "".join(lines).split(",")

        s = 0
        for r in ranges:
            a, b = r.split("-")
            for n in range(int(a), int(b)+1):
                n_str = str(n)
                if re.match(r"^(\d+)\1+$", n_str):
                    s += n

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
    filename = utils.get_real_input(2)

part_a(filename)
if not args.skip_b:
    part_b(filename)
