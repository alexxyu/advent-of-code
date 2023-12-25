import argparse
from enum import Enum

import utils
from matplotlib.path import Path


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


PIPES = {
    Direction.UP: ["|", "7", "F"],
    Direction.DOWN: ["|", "J", "L"],
    Direction.RIGHT: ["-", "7", "J"],
    Direction.LEFT: ["-", "F", "L"],
}


NEXT_DIRECTION = {
    Direction.LEFT: {
        "-": Direction.LEFT,
        "F": Direction.DOWN,
        "L": Direction.UP,
    },
    Direction.RIGHT: {
        "-": Direction.RIGHT,
        "J": Direction.UP,
        "7": Direction.DOWN,
    },
    Direction.DOWN: {
        "|": Direction.DOWN,
        "J": Direction.LEFT,
        "L": Direction.RIGHT,
    },
    Direction.UP: {
        "|": Direction.UP,
        "7": Direction.LEFT,
        "F": Direction.RIGHT,
    },
}


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().splitlines()
        start = None
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == "S":
                    start = (i, j)

        loop = [start]
        next_pos, next_dir = None, None
        for d in Direction:
            dr, dc = d.value
            np = (start[0] + dr, start[1] + dc)
            if lines[np[0]][np[1]] in PIPES[d]:
                next_pos = np
                next_dir = d
                break

        loop.append(next_pos)
        while next_pos != start:
            nd = NEXT_DIRECTION[next_dir][lines[next_pos[0]][next_pos[1]]]
            np = (next_pos[0] + nd.value[0], next_pos[1] + nd.value[1])
            loop.append(np)
            next_pos, next_dir = np, nd

        print(len(loop) // 2)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().splitlines()
        start = None
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == "S":
                    start = (i, j)

        loop = [start]
        next_pos, next_dir = None, None
        for d in Direction:
            dr, dc = d.value
            np = (start[0] + dr, start[1] + dc)
            if lines[np[0]][np[1]] in PIPES[d]:
                next_pos = np
                next_dir = d
                break

        loop.append(next_pos)
        while next_pos != start:
            nd = NEXT_DIRECTION[next_dir][lines[next_pos[0]][next_pos[1]]]
            np = (next_pos[0] + nd.value[0], next_pos[1] + nd.value[1])
            loop.append(np)
            next_pos, next_dir = np, nd

        s = 0
        pts = []
        hull_path = Path(loop[::-1])
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if (i, j) not in loop and hull_path.contains_point((i, j)):
                    pts.append((i, j))
                    s += 1

        # visualize_grid(lines, loop, pts)
        print(s)


def visualize_grid(grid, loop, enclosed):
    g = [["." for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for p in loop:
        g[p[0]][p[1]] = "*"
    for e in enclosed:
        g[e[0]][e[1]] = "I"
    for r in g:
        print("".join(r))


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
    filename = utils.get_real_input(10)

part_a(filename)
if not args.skip_b:
    part_b(filename)
