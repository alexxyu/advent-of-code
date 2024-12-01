import argparse
from collections import defaultdict

import utils


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        a, b = [], []

        for line in lines:
            x, y = line.split()
            a.append(int(x))
            b.append(int(y))

        a, b = sorted(a), sorted(b)
        print(sum(abs(a[i] - b[i]) for i in range(len(a))))


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        a, b = [], defaultdict(int)

        for line in lines:
            x, y = line.split()
            a.append(int(x))
            b[int(y)] += 1

        print(sum(n * b[n] for n in a))


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
