import argparse
from collections import *
from typing import *

import numpy as np
import tqdm
import utils


class UnionFind:
    def __init__(self, n):
        self.m = {i: i for i in range(n)}

    def find(self, pt):
        if self.m[pt] != pt:
            self.m[pt] = self.find(self.m[pt])
        return self.m[pt]

    def union(self, pt1, pt2):
        self.m[self.find(pt1)] = self.find(pt2)

    def groups(self):
        result = defaultdict(list)
        for k in self.m:
            result[self.find(k)].append(k)
        return result


def distance(a: Tuple[int, int, int], b: Tuple[int, int, int]):
    return sum((r - q) ** 2 for r, q in zip(a, b, strict=True))


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        points = []
        for line in lines:
            a, b, c = line.split(",")
            points.append((int(a), int(b), int(c)))

        uf = UnionFind(len(points))
        pairs = {(i, j) for i in range(len(points)) for j in range(i+1, len(points))}

        memo = defaultdict(lambda: defaultdict(int))
        for pair in pairs:
            memo[pair[0]][pair[1]] = distance(points[pair[0]], points[pair[1]])

        for _ in tqdm.tqdm(range(1000)):
            closest_pair, closest_dist = None, np.inf

            for (i, j) in pairs:
                dist = memo[i][j]
                if dist < closest_dist:
                    closest_dist = dist
                    closest_pair = (i, j)

            pairs.remove(closest_pair)
            uf.union(closest_pair[0], closest_pair[1])

        group_sizes = sorted([len(g) for g in uf.groups().values()], reverse=True)
        print(np.prod(group_sizes[:3]))

def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        points = []
        for line in lines:
            a, b, c = line.split(",")
            points.append((int(a), int(b), int(c)))

        uf = UnionFind(len(points))
        pairs = {(i, j) for i in range(len(points)) for j in range(i+1, len(points))}

        memo = defaultdict(lambda: defaultdict(int))
        for pair in pairs:
            memo[pair[0]][pair[1]] = distance(points[pair[0]], points[pair[1]])

        last_pair = None
        while len(uf.groups()) > 1:
            closest_pair, closest_dist = None, np.inf

            for (i, j) in pairs:
                if uf.find(i) == uf.find(j):
                    continue

                dist = memo[i][j]
                if dist < closest_dist:
                    closest_dist = dist
                    closest_pair = (i, j)

            pairs.remove(closest_pair)
            last_pair = closest_pair
            uf.union(closest_pair[0], closest_pair[1])

        print(points[last_pair[0]][0] * points[last_pair[1]][0])


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
    filename = utils.get_real_input(8)

part_a(filename)
if not args.skip_b:
    part_b(filename)
