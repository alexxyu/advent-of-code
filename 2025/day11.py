import argparse
import functools
from collections import *
from typing import *

import utils


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        graph = defaultdict(list)
        for line in lines:
            device, outs = line.split(": ")
            outs = outs.split()
            graph[device] = outs

        @functools.lru_cache
        def count_paths_from(n):
            if n == "out":
                return 1

            return sum(count_paths_from(v) for v in graph[n])

        print(count_paths_from("you"))


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        graph = defaultdict(list)
        for line in lines:
            device, outs = line.split(": ")
            outs = outs.split()
            graph[device] = outs

        @functools.lru_cache
        def count_paths_from(n, tgt):
            if n == tgt:
                return 1

            return sum(count_paths_from(v, tgt) for v in graph[n])

        # svr -> dac -> fft -> out
        a1 = count_paths_from("svr", "dac")
        b1 = count_paths_from("dac", "fft")
        c1 = count_paths_from("fft", "out")
        s1 = a1 * b1 * c1

        # svr -> fft -> dac -> out
        a2 = count_paths_from("svr", "fft")
        b2 = count_paths_from("fft", "dac")
        c2 = count_paths_from("dac", "out")
        s2 = a2 * b2 * c2

        print(s1 + s2)


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
    filename = utils.get_real_input(11)

part_a(filename)
if not args.skip_b:
    part_b(filename)
