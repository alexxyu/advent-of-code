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
        s = 0
        for line in lines:
            history = utils.parse_list_nums(line)

            histories = [history]
            curr_history = history
            while any(x for x in curr_history if x != 0):
                next_history = []
                for i in range(1, len(curr_history)):
                    next_history.append(curr_history[i] - curr_history[i-1])
                curr_history = next_history
                histories.append(curr_history)

            for i in range(len(histories)-2, -1, -1):
                next_history = histories[i+1]
                histories[i].append(next_history[-1] + histories[i][-1])
            s += histories[0][-1]

        print(s)


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()
        s = 0
        for line in lines:
            history = utils.parse_list_nums(line)

            histories = [history]
            curr_history = history
            while any(x for x in curr_history if x != 0):
                next_history = []
                for i in range(1, len(curr_history)):
                    next_history.append(curr_history[i] - curr_history[i-1])
                curr_history = next_history
                histories.append(curr_history)

            for i in range(len(histories)-2, -1, -1):
                next_history = histories[i+1]
                histories[i] = [histories[i][0] - next_history[0]] + histories[i]
            s += histories[0][0]

        print(s)


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file, will default to actual AoC input if omitted', type=str, nargs='?', default=None)
parser.add_argument('--skip-b', help='skip running part b', action='store_true')
args = parser.parse_args()

filename = args.filename
if not args.filename:
    filename = utils.get_real_input(9)

part_a(filename)
if not args.skip_b:
    part_b(filename)
