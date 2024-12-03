import argparse
import re
from collections import *
from typing import *

import utils


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        s = 0
        for line in lines:
            matches = re.findall(r"mul\(([0-9]+),([0-9]+)\)", line)

            for match in matches:
                a, b = int(match[0]), int(match[1])
                s += a * b
        print(s)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        s = 0

        enabled = True
        for line in lines:
            matches = re.finditer(r"mul\(([0-9]+),([0-9]+)\)|do\(\)|don't\(\)", line)

            for match in matches:
                m = match.group()
                if m.startswith("mul(") and enabled:
                    a, b = int(match.groups()[0]), int(match.groups()[1])
                    s += a * b
                elif m == "don't()":
                    enabled = False
                elif m == "do()":
                    enabled = True

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
    filename = utils.get_real_input(3)

part_a(filename)
if not args.skip_b:
    part_b(filename)
