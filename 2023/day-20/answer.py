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


class ModuleType(Enum):
    BROADCAST = 0
    FF = 1
    CONJ = 2
    TEST = 3


class ModuleState(Enum):
    LO = -1
    HI = 1


def press_button(modules, conj_to_ins, np=1, ns_in_presses={}):
    lo, hi = 1, 0

    q = []
    _, _, deps = modules['broadcaster']
    lo += len(deps)
    for d in deps:
        q.append((d, ModuleState.LO))

    while q != []:
        (curr, signal), q = q[0], q[1:]
        t, s, deps = modules[curr]

        out = None
        if t == ModuleType.FF:
            if signal == ModuleState.LO:
                out = s = ModuleState(-s.value)
                modules[curr][1] = out
        elif t == ModuleType.CONJ:
            out = ModuleState.LO if all(modules[x][1] == ModuleState.HI for x in conj_to_ins[curr]) else ModuleState.HI

        if out:
            modules[curr][1] = out
            if out == ModuleState.LO:
                lo += len(deps)
            elif out == ModuleState.HI:
                hi += len(deps)

            for d in deps:
                q.append((d, out))

        if curr in conj_to_ins['ns'] and out == ModuleState.HI and curr not in ns_in_presses:
            ns_in_presses[curr] = np

    return lo, hi


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        modules = defaultdict(lambda: [ModuleType.TEST, None, None])

        conjs = set()
        for line in lines:
            a, b = line.split(' -> ')
            deps = set(b.split(', '))

            t = ModuleType.BROADCAST
            if a[0] == '%':
                t = ModuleType.FF
                a = a[1:]
            elif a[0] == '&':
                t = ModuleType.CONJ
                a = a[1:]
                conjs.add(a)

            modules[a] = [t, ModuleState.LO, deps]

        ins = defaultdict(list)
        for x, (_, _, deps) in modules.items():
            for d in deps & conjs:
                ins[d].append(x)

        lo, hi = 0, 0
        for _ in range(1000):
            a, b = press_button(modules, ins)
            lo += a
            hi += b
        print(lo * hi)


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()
        modules = defaultdict(lambda: [ModuleType.TEST, None, None])

        conjs = set()
        for line in lines:
            a, b = line.split(' -> ')
            deps = set(b.split(', '))

            t = ModuleType.BROADCAST
            if a[0] == '%':
                t = ModuleType.FF
                a = a[1:]
            elif a[0] == '&':
                t = ModuleType.CONJ
                a = a[1:]
                conjs.add(a)

            modules[a] = [t, ModuleState.LO, deps]

        ins = defaultdict(list)
        for x, (_, _, deps) in modules.items():
            for d in deps & conjs:
                ins[d].append(x)

        i, ns_in = 0, {}
        while len(ns_in) < 4:
            i += 1
            press_button(modules, ins, i, ns_in)

        print(math.lcm(*ns_in.values()))


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file, will default to actual AoC input if omitted', type=str, nargs='?', default=None)
parser.add_argument('--skip-b', help='skip running part b', action='store_true')
args = parser.parse_args()

filename = args.filename
if not args.filename:
    filename = utils.get_real_input(20)

part_a(filename)
if not args.skip_b:
    part_b(filename)
