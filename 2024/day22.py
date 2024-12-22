import argparse
from collections import *
from typing import *

import utils


def mix(n, v):
    return n ^ v

def prune(n):
    return n % 16777216


def next_secret(n):
    x = prune(mix(n, n * 64))
    x = prune(mix(x, x // 32))
    return prune(mix(x, x * 2048))


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        s = 0
        for line in lines:
            n = int(line)
            for _ in range(2000):
                n = next_secret(n)
            s += n
        print(s)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()

        seq_to_price = defaultdict(int)
        for line in lines:
            p = []
            n = int(line)
            for _ in range(2000):
                n = next_secret(n)
                p.append(n % 10)

            seqs = set()
            for i in range(4, len(p)):
                seq = tuple(p[k+1] - p[k] for k in range(i-4, i))
                if seq not in seqs:
                    seq_to_price[seq] += p[i]
                    seqs.add(seq)

        print(max(seq_to_price.values()))

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
    filename = utils.get_real_input(22)

part_a(filename)
if not args.skip_b:
    part_b(filename)
