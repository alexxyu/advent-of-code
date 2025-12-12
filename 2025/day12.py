import argparse
from collections import *
from typing import *

import numpy as np
import utils
from utils import iter_grid, parse_nums


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        sections = f.read().strip().split("\n\n")
        shape_sections, regions = sections[:-1], sections[-1]

        shape_sizes = []
        for shape in shape_sections:
            s = 0
            for c in iter_grid(shape.splitlines()[1:]):
                if c == "#":
                    s += 1
            shape_sizes.append(s)

        s = 0
        for r in regions.splitlines():
            size, counts = r.split(": ")
            rows, cols = list(map(int, size.split("x")))
            counts = parse_nums(counts)

            total_size = rows * cols
            need_size = np.sum([shape_sizes[i] * k for i, k in enumerate(counts)])
            if total_size >= need_size:
                s += 1

        print(s)

parser = argparse.ArgumentParser()
parser.add_argument(
    "filename",
    help="the input file, will default to actual AoC input if omitted",
    type=str,
    nargs="?",
    default=None,
)
args = parser.parse_args()

filename = args.filename
if not args.filename:
    filename = utils.get_real_input(12)

part_a(filename)
