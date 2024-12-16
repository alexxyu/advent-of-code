import argparse
import heapq
from collections import *
from typing import *

import utils
from utils import Direction, Position2D


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        grid = [list(x) for x in f.read().strip().splitlines()]

        curr, end = None, None
        for (r, c), p in utils.iter_grid_with_pos(grid):
            if p == "E":
                end = Position2D(r, c)
            elif p == "S":
                curr = Position2D(r, c)

        lowest_score = None
        seen = set()
        pq = [(0, curr, Direction.RIGHT)]

        while pq != []:
            s, p, d = heapq.heappop(pq)
            if (p, d) in seen:
                continue
            seen.add((p, d))

            if not p.is_inside_grid(grid) or grid[p.row][p.col] == "#":
                continue
            if p == end:
                lowest_score = s
                break

            heapq.heappush(pq, (s + 1000, p, d.rot90(k=1)))
            heapq.heappush(pq, (s + 1000, p, d.rot90(k=-1)))
            heapq.heappush(pq, (s + 1, p + d, d))

        print(lowest_score)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        grid = [list(x) for x in f.read().strip().splitlines()]

        curr, end = None, None
        for (r, c), p in utils.iter_grid_with_pos(grid):
            if p == "E":
                end = Position2D(r, c)
            elif p == "S":
                curr = Position2D(r, c)

        lowest_score = None
        seen = set()
        backtrack = defaultdict(list)
        pq = [(0, curr, Direction.RIGHT)]

        while pq != []:
            s, p, d = heapq.heappop(pq)
            if (p, d) in seen:
                continue
            seen.add((p, d))

            if not p.is_inside_grid(grid) or grid[p.row][p.col] == "#":
                continue
            if p == end:
                lowest_score = s
                break

            for new_state in [
                (s + 1000, p, d.rot90(k=1)),
                (s + 1000, p, d.rot90(k=-1)),
                (s + 1, p + d, d),
            ]:
                backtrack[new_state].append((s, p, d))
                heapq.heappush(pq, new_state)

        on_best_path = set()
        q = [(lowest_score, end, d) for d in Direction]
        while q != []:
            s, p, d = q.pop()
            on_best_path.add(p)
            for b in backtrack[(s, p, d)]:
                q.append(tuple(b))

        print(len(on_best_path))


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
    filename = utils.get_real_input(16)

part_a(filename)
if not args.skip_b:
    part_b(filename)
