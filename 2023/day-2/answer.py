import argparse
from collections import *
from copy import deepcopy
from dataclasses import dataclass
from enum import Enum
from functools import cmp_to_key, lru_cache, reduce
from heapq import *
from itertools import *
from math import *
from re import findall, split, search
from typing import *


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().splitlines()
        k = 0
        for i, line in enumerate(lines):
            _, sets = line.split(": ")
            isSat = True
            for s in sets.split("; "):
                r = search("(\d+) red", s) or 0
                if r:
                    r = int(r.group(1))
                g = search("(\d+) green", s) or 0
                if g:
                    g = int(g.group(1))
                b = search("(\d+) blue", s) or 0
                if b:
                    b = int(b.group(1))
                if not (r <= 12 and g <= 13 and b <= 14):
                    isSat = False
                    break
            if isSat:
                k += i+1
        print(k)


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()
        k = 0
        for i, line in enumerate(lines):
            _, sets = line.split(": ")
            maxR, maxG, maxB = 0, 0, 0
            for s in sets.split("; "):
                r = search("(\d+) red", s) or 0
                if r:
                    r = int(r.group(1))
                    maxR = max(maxR, r)
                g = search("(\d+) green", s) or 0
                if g:
                    g = int(g.group(1))
                    maxG = max(maxG, g)
                b = search("(\d+) blue", s) or 0
                if b:
                    b = int(b.group(1))
                    maxB = max(maxB, b)
            k += maxR * maxG * maxB
        print(k)


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true',
                    help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
