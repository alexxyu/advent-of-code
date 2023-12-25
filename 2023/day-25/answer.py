import argparse

import utils
from networkx import Graph, connected_components, minimum_edge_cut
from numpy import prod


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()

        g = Graph()
        for line in lines:
            n, _ = line.split(": ")
            g.add_node(n)

        edges = []
        for line in lines:
            n, x = line.split(": ")
            for k in x.split():
                g.add_edge(n, k)
                edges.append((n, k))

        g.remove_edges_from(minimum_edge_cut(g))
        print(prod([len(c) for c in connected_components(g)]))


parser = argparse.ArgumentParser()
parser.add_argument("filename", help="the input file, will default to actual AoC input if omitted", type=str, nargs="?", default=None)
args = parser.parse_args()

filename = args.filename
if not args.filename:
    filename = utils.get_real_input(25)

part_a(filename)
