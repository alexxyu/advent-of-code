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
        workflows, ratings = f.read().strip().split('\n\n')

        parsed = dict()
        for w in workflows.split('\n'):
            name, v = w[:w.find('{')], w[w.find('{'):]
            parsed[name] = v[1:-1].split(',')

        def judge(w, r):
            if w == 'A':
                return True
            if w == 'R':
                return False

            workflow = parsed[w]
            for rule in workflow:
                if ':' not in rule:
                    return judge(rule, r)

                cond, x = rule.split(':')

                # This used to be way more convoluted, but I dumbed it down...
                if eval(str(r[cond[0]]) + cond[1:]):
                    return judge(x, r)
            return None

        s = 0
        for r in ratings.split('\n'):
            t = r[1:-1].split(',')

            vals = {}
            for g in t:
                k, v = g.split('=')
                v = int(v)
                vals[k] = v

            if judge('in', vals):
                s += sum(vals.values())

        print(s)


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        workflows, _ = f.read().strip().split('\n\n')
        parsed = dict()
        for w in workflows.split('\n'):
            name, v = w[:w.find('{')], w[w.find('{'):]
            parsed[name] = v[1:-1].split(',')

        def combinations(w, r):
            if w == 'A':
                return math.prod([b - a + 1 for (a, b) in r.values()])
            if w == 'R':
                return 0

            s = 0
            workflow = parsed[w]
            for k in workflow:
                if ':' not in k:
                    s += combinations(k, r)
                else:
                    cond, n = k.split(':')
                    if '>' in cond:
                        k, v = cond.split('>')
                        a, b = r[k]
                        v = int(v)
                        if b > v:
                            nr = deepcopy(r)
                            nr[k] = (max(a, v+1), b)
                            s += combinations(n, nr)

                            r[k] = (a, min(b, v))
                    elif '<' in cond:
                        k, v = cond.split('<')
                        a, b = r[k]
                        v = int(v)
                        if a < v:
                            nr = deepcopy(r)
                            nr[k] = (a, min(b, v-1))
                            s += combinations(n, nr)

                            r[k] = (max(a, v), b)

            return s

        r = {c: (1, 4000) for c in 'xmas'}
        print(combinations('in', r))


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file, will default to actual AoC input if omitted', type=str, nargs='?', default=None)
parser.add_argument('--skip-b', help='skip running part b', action='store_true')
args = parser.parse_args()

filename = args.filename
if not args.filename:
    filename = utils.get_real_input(19)

part_a(filename)
if not args.skip_b:
    part_b(filename)
