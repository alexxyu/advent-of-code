import argparse
from enum import Enum

import utils


class Direction(Enum):
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP = (-1, 0)
    DOWN = (1, 0)


STATE_MACHINE = {
    Direction.RIGHT: {"/": Direction.UP, "\\": Direction.DOWN},
    Direction.LEFT: {"\\": Direction.UP, "/": Direction.DOWN},
    Direction.UP: {"/": Direction.RIGHT, "\\": Direction.LEFT},
    Direction.DOWN: {"/": Direction.LEFT, "\\": Direction.RIGHT},
}


def get_pos_in_direction(pos, direction):
    r, c = pos
    nr, nc = r + direction.value[0], c + direction.value[1]
    return nr, nc


def simulate(grid, r, c, d):
    energized = {(r, c)}
    states_seen = set()
    q = [((r, c), d)]

    while len(q) > 0:
        ((r, c), d), q = q[0], q[1:]

        if (
            r < 0
            or c < 0
            or r >= len(grid)
            or c >= len(grid[r])
            or ((r, c), d) in states_seen
        ):
            continue
        states_seen.add(((r, c), d))
        energized.add((r, c))

        if grid[r][c] in "/\\":
            nd = STATE_MACHINE[d][grid[r][c]]
            q.append((get_pos_in_direction((r, c), nd), nd))
        elif grid[r][c] == "|" and (d == Direction.LEFT or d == Direction.RIGHT):
            nd = Direction.UP
            q.append((get_pos_in_direction((r, c), nd), Direction.UP))
            nd = Direction.DOWN
            q.append((get_pos_in_direction((r, c), nd), Direction.DOWN))
        elif grid[r][c] == "-" and (d == Direction.UP or d == Direction.DOWN):
            nd = Direction.RIGHT
            q.append((get_pos_in_direction((r, c), nd), Direction.RIGHT))
            nd = Direction.LEFT
            q.append((get_pos_in_direction((r, c), nd), Direction.LEFT))
        else:
            nd = d
            q.append((get_pos_in_direction((r, c), nd), nd))

    return len(energized)


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().splitlines()
        print(simulate(lines, 0, 0, Direction.RIGHT))


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().splitlines()

        candidates = []
        for i in range(len(lines)):
            candidates.append(((i, 0), Direction.RIGHT))
            candidates.append(((i, len(lines[i]) - 1), Direction.LEFT))

        for j in range(len(lines[0])):
            candidates.append(((0, j), Direction.DOWN))
            candidates.append(((len(lines) - 1, j), Direction.UP))

        s = max(simulate(lines, r, c, d) for ((r, c), d) in candidates)
        print(s)


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
