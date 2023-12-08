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
        dirs, nodes = f.read().strip().split('\n\n')
        nodes = nodes.split('\n')

        tree = dict()
        for n in nodes:
            curr, neighbors = n.split(" = ")
            a, b = neighbors[1:-1].split(", ")
            tree[curr] = (a, b)

        i = 0
        curr = 'AAA'
        while curr != 'ZZZ':
            d = dirs[i % len(dirs)]
            if d == 'L':
                curr = tree[curr][0]
            else:
                curr = tree[curr][1]
            i += 1
        print(i)


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        dirs, nodes = f.read().strip().split('\n\n')
        nodes = nodes.split('\n')

        tree = dict()
        ends_with_a = set()
        for n in nodes:
            curr, neighbors = n.split(" = ")
            a, b = neighbors[1:-1].split(", ")
            tree[curr] = (a, b)

            if curr[-1] == 'A':
                ends_with_a.add(curr)

        t = []
        for curr in ends_with_a:
            i = 0
            while curr[-1] != 'Z':
                d = dirs[i % len(dirs)]
                if d == 'L':
                    curr = tree[curr][0]
                else:
                    curr = tree[curr][1]
                i += 1
            t.append(i)
        print(math.lcm(*t))


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file, will default to actual AoC input if omitted', type=str, nargs='?', default=None)
parser.add_argument('--skip-b', help='skip running part b', action='store_true')
args = parser.parse_args()

filename = args.filename
if not args.filename:
    filename = utils.get_real_input(8)

part_a(filename)
if not args.skip_b:
    part_b(filename)
