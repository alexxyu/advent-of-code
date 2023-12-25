import argparse

import utils


def get_pairwise_distances_after_expansion(lines, d=1):
    empty_rows = []
    for i, line in enumerate(lines):
        if all(c == "." for c in line):
            empty_rows.append(i)
    empty_cols = []
    for j in range(len(lines[0])):
        if all(line[j] == "." for line in lines):
            empty_cols.append(j)
    galaxies = [(r, c) for (r, c), g in utils.iter_grid_with_pos(lines) if g == "#"]

    new_galaxies = []
    for r, c in galaxies:
        dr = 0
        for er in empty_rows:
            if er < r:
                dr += d
        dc = 0
        for ec in empty_cols:
            if ec < c:
                dc += d
        new_galaxies.append((r + dr, c + dc))

    d = 0
    for i, (r1, c1) in enumerate(new_galaxies):
        for r2, c2 in new_galaxies[i + 1:]:
            d += abs(c1 - c2) + abs(r1 - r2)
    return d


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().splitlines()
        print(get_pairwise_distances_after_expansion(lines))


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().splitlines()
        print(get_pairwise_distances_after_expansion(lines, d=999999))


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
    filename = utils.get_real_input(11)

part_a(filename)
if not args.skip_b:
    part_b(filename)
