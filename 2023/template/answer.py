import argparse
from collections import *
from copy import deepcopy
from dataclasses import dataclass
from enum import Enum
from functools import cmp_to_key, lru_cache, reduce
from heapq import *
from itertools import *
from math import *
from re import findall, split
from typing import *


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().splitlines()
        pass


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()
        pass


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true',
                    help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
