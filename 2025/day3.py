import argparse
from collections import *
from typing import *

import numpy as np
import utils


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()

        s = 0
        for line in lines:
            digits = [int(c) for c in line]
            m = 0
            for i in range(len(digits)):
                for j in range(i+1, len(digits)):
                    m = max(m, digits[i] * 10 + digits[j])
            s += m
        print(s)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()

        s = 0
        for line in lines:
            digits = [int(c) for c in line]

            dp = np.zeros((len(digits), 12))
            for i in range(len(digits)):
                if i == 0:
                    dp[i][0] = digits[i]
                else:
                    dp[i][0] = max(digits[i], dp[i-1][0])

            for i in range(1, len(digits)):
                for j in range(1, 12):
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] * 10 + digits[i])

            s += int(dp[-1][-1])
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
