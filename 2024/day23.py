import argparse
import itertools
from collections import *
from typing import *

import utils


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        graph = defaultdict(set)
        for line in lines:
            a, b = line.split("-")
            graph[a].add(b)
            graph[b].add(a)

        s = 0
        visited = set()
        for n in graph:
            if n in visited:
                continue

            component = set()

            q = deque([n])
            while q:
                node = q.popleft()
                if node in visited:
                    continue
                visited.add(node)
                component.add(node)
                q.extend(graph[node])

            for a, b, c in itertools.combinations(component, 3):
                if b in graph[a] and c in graph[a] and c in graph[b] and any(x[0] == "t" for x in [a, b, c]):
                    s += 1

        print(s)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        graph = defaultdict(set)
        for line in lines:
            a, b = line.split("-")
            graph[a].add(b)
            graph[b].add(a)

        max_clique = []
        cliques = [{key} for key in graph]
        while cliques != []:
            new_cliques = []
            for clique in cliques:
                for n in sorted(graph):
                    if all(x in graph[n] and x < n for x in clique):
                        c = clique | {n}
                        new_cliques.append(c)
                        if len(c) > len(max_clique):
                            max_clique = c
            cliques = new_cliques

        print(",".join(max_clique))


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
    filename = utils.get_real_input(23)

part_a(filename)
if not args.skip_b:
    part_b(filename)
