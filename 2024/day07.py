import argparse
from collections import *
from typing import *

import utils

OPERATIONS = [lambda x, y: x + y, lambda x, y: x * y]


def apply_operation(nums, target, acc, operator = lambda x, y: x + y):
    if acc > target:
        return False
    if len(nums) == 0:
        return acc == target
    nacc = operator(acc, nums[0])
    return any(apply_operation(nums[1:], target, nacc, op) for op in OPERATIONS)


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()

        s = 0
        for line in lines:
            lhs, rhs = line.split(": ")
            nums = [int(n) for n in rhs.split()]
            target = int(lhs)

            if apply_operation(nums, target, 0):
                s += target
        print(s)



def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()

        OPERATIONS.append(lambda x, y: int(str(x) + str(y)))

        s = 0
        for line in lines:
            lhs, rhs = line.split(": ")
            nums = [int(n) for n in rhs.split()]
            target = int(lhs)

            if apply_operation(nums, target, 0):
                s += target
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
    filename = utils.get_real_input(7)

part_a(filename)
if not args.skip_b:
    part_b(filename)
