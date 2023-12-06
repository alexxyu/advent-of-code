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
        lines = f.read().splitlines()
        times = utils.parse_list_nums(lines[0].split(":")[1])
        dists = utils.parse_list_nums(lines[1].split(":")[1])

        p = 1
        for t, d in zip(times, dists):
            count = 0
            for tt in range(1, t+1):
                dd = (t - tt) * tt
                if dd > d:
                    count += 1
            p *= count
        print(p)


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()
        times = utils.parse_list_nums(lines[0].split(":")[1])
        actual_time = ""
        for t in times:
            actual_time += str(t)
        actual_time = int(actual_time)

        dists = utils.parse_list_nums(lines[1].split(":")[1])
        actual_dist = ""
        for d in dists:
            actual_dist += str(d)
        actual_dist = int(actual_dist)

        count = 0
        for tt in range(1, actual_time+1):
            dd = (actual_time - tt) * tt
            if dd > actual_dist:
                count += 1
        print(count)


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file, will default to actual AoC input if omitted', type=str, nargs='?', default=None)
parser.add_argument('--skip-b', help='skip running part b', action='store_true')
args = parser.parse_args()

filename = args.filename
if not args.filename:
    filename = utils.get_real_input(6)

part_a(filename)
if not args.skip_b:
    part_b(filename)
