import argparse
from collections import *
from typing import *

import utils


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        towels, designs = f.read().strip().split("\n\n")
        towels = towels.split(", ")
        designs = designs.split("\n")

        s = 0
        for design in designs:
            q = [design]
            seen = set()
            while q != []:
                curr, q = q[0], q[1:]
                if curr == "":
                    s += 1
                    break

                for towel in towels:
                    if curr.startswith(towel) and (rem := curr[len(towel):]) not in seen:
                        seen.add(rem)
                        q.append(rem)
        print(s)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        towels, designs = f.read().strip().split("\n\n")
        towels = towels.split(", ")
        designs = designs.split("\n")

        s = 0
        for design in designs:
            dp = [0] * (len(design) + 1)
            dp[0] = 1
            for i in range(1, len(design) + 1):
                for towel in towels:
                    if i >= len(towel) and design[i - len(towel): i] == towel:
                        dp[i] += dp[i - len(towel)]
            s += dp[-1]
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
    filename = utils.get_real_input(19)

part_a(filename)
if not args.skip_b:
    part_b(filename)
