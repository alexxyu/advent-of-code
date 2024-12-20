import argparse
from collections import *
from typing import *

import utils
from utils import Position2D


def distance_from_position(grid, pos):
    t, q = 1, [pos]
    dists = defaultdict(lambda: float("inf"))
    while q != []:
        for _ in range(len(q)):
            curr, q = q[0], q[1:]
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = curr.row + dr, curr.col + dc
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[nr]) or grid[nr][nc] == "#":
                    continue
                if t < dists[Position2D(nr, nc)]:
                    dists[Position2D(nr, nc)] = t
                    q.append(Position2D(nr, nc))
        t += 1
    return dists


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        grid = [str(x) for x in f.read().strip().splitlines()]
        start = utils.find_grid_pos_with_value(grid, "S")[0]
        end = utils.find_grid_pos_with_value(grid, "E")[0]

        dist_to_end = distance_from_position(grid, end)
        t_end = dist_to_end[start]

        save, seen = set(), set()
        t, q = 1, [(start, None)]
        while q != []:
            for _ in range(len(q)):
                (curr, skip), q = q[0], q[1:]
                if curr == end:
                    continue

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = curr.row + dr, curr.col + dc
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[nr]) or Position2D(nr, nc) in seen:
                        continue

                    if grid[nr][nc] == "#":
                        if skip is None:
                            seen.add(Position2D(nr, nc))
                            q.append((Position2D(nr, nc), curr))
                    elif skip is not None:
                        tt = t + dist_to_end[Position2D(nr, nc)]
                        if t_end - tt >= 100:
                            save.add((skip, nr, nc))
                    else:
                        seen.add(Position2D(nr, nc))
                        q.append((Position2D(nr, nc), skip))
            t += 1

        print(len(save))


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        grid = [str(x) for x in f.read().strip().splitlines()]
        start = utils.find_grid_pos_with_value(grid, "S")[0]
        end = utils.find_grid_pos_with_value(grid, "E")[0]

        dist_to_end = distance_from_position(grid, end)
        t_end = dist_to_end[start]

        save = set()
        dist_from_start = distance_from_position(grid, start)
        for pos, t_start in dist_from_start.items():
            for dr in range(-20, 21):
                for dc in range(-20, 21):
                    cheat = abs(dr) + abs(dc)
                    if cheat > 20:
                        continue
                    nr, nc = pos.row + dr, pos.col + dc
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[nr]):
                        continue
                    if grid[nr][nc] != "#":
                        tt = t_start + cheat + dist_to_end[Position2D(nr, nc)]
                        if t_end - tt >= 100:
                            save.add((pos, nr, nc))

        print(len(save))


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
    filename = utils.get_real_input(20)

part_a(filename)
if not args.skip_b:
    part_b(filename)
