import argparse
import heapq
import itertools
import math
import re
from collections import *
from copy import deepcopy
from dataclasses import dataclass
from enum import Enum
from functools import cmp_to_key, lru_cache, reduce
from typing import *
import utils


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        sections = f.read().strip().split("\n\n")
        seeds = utils.parse_list_nums(sections[0].split(": ")[1])

        mappings = []
        for s in sections:
            mapping = {}
            lines = s.split("\n")
            for line in lines[1:]:
                dst, src, rng = utils.parse_list_nums(line)
                mapping[(src, src+rng)] = dst - src
            mappings.append(mapping)

        k = []
        for s in seeds:
            for mapping in mappings:
                for (start, end), v in mapping.items():
                    if start <= s < end:
                        s += v
                        break
            k.append(s)
        print(min(k))


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        parts = f.read().strip().split("\n\n")
        seeds = utils.parse_list_nums(parts[0].split(": ")[1])

        ranges = []
        for (s, t) in zip(seeds[::2], seeds[1::2]):
            ranges.append([s, s+t-1])

        mappings = []
        for s in parts:
            mapping = {}
            lines = s.split("\n")
            for line in lines[1:]:
                dst, src, rng = utils.parse_list_nums(line)
                mapping[(src, src+rng-1)] = dst - src
            mappings.append(mapping)

        for mapping in mappings:
            new_ranges = []
            for (s, e), v in mapping.items():
                to_check = []
                for r in ranges:
                    ns, ne = max(s, r[0]), min(e, r[1])
                    if ns <= ne:
                        new_ranges.append([ns + v, ne + v])
                        if r[0] < ns:
                            to_check.append([r[0], ns - 1])
                        if r[1] > ne:
                            to_check.append([ne + 1, r[1]])
                    else:
                        to_check.append(r)
                ranges = to_check
            ranges += new_ranges

        print(min(r[0] for r in ranges))


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file, will default to actual AoC input if omitted', type=str, nargs='?', default=None)
parser.add_argument('--skip-b', help='skip running part b', action='store_true')
args = parser.parse_args()

filename = args.filename
if not args.filename:
    filename = utils.get_real_input(5)

part_a(filename)
if not args.skip_b:
    part_b(filename)
