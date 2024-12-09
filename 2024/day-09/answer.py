import argparse
from collections import *
from typing import *

import utils


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        line = list(map(int, lines[0]))

        fs = []
        for i, size in enumerate(line):
            fd = i // 2 if i % 2 == 0 else None
            fs.extend([fd] * size)

        a, b = 0, len(fs)-1
        while a < b:
            while a < b and fs[a] is not None:
                a += 1
            while a < b and fs[b] is None:
                b -= 1
            fs[a], fs[b] = fs[b], fs[a]

        checksum = 0
        for i, s in enumerate(fs):
            if s is not None:
                checksum += i * s
        print(checksum)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        line = map(int, lines[0])

        fs = []
        for i, size in enumerate(line):
            fd = i // 2 if i % 2 == 0 else None
            fs.append((fd, size))

        k = len(fs) - 1
        while k > 0:
            (curr_fd, curr_size) = fs[k]
            if curr_fd is None:
                k -= 1
                continue

            needs_decrement = True
            for i in range(k):
                (cmp_fd, cmp_size) = fs[i]
                if cmp_fd is None and cmp_size >= curr_size:
                    fs[i] = (curr_fd, curr_size)
                    fs[k] = (None, curr_size)

                    (next_fd, next_size) = fs[i+1]
                    if (left := cmp_size - curr_size) > 0:
                        if next_fd is None:
                            fs[i+1] = (None, next_size + left)
                        else:
                            fs.insert(i+1, (None, left))
                            needs_decrement = False
                    break

            if needs_decrement:
                k -= 1

        def s_n(n):
            return ((n + 1) * n) // 2

        k, checksum = 0, 0
        for (fd, size) in fs:
            if fd is not None:
                checksum += fd * (s_n(k + size - 1) - s_n(k - 1))
            k += size
        print(checksum)


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
    filename = utils.get_real_input(9)

part_a(filename)
if not args.skip_b:
    part_b(filename)
