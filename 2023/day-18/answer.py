import argparse

import utils
from shapely.geometry import Polygon
from utils import Direction, Position2D

DIRECTIONS = {
    "R": Direction.RIGHT,
    "D": Direction.DOWN,
    "L": Direction.LEFT,
    "U": Direction.UP,
    "0": Direction.RIGHT,
    "1": Direction.DOWN,
    "2": Direction.LEFT,
    "3": Direction.UP,
}


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().splitlines()
        curr_pos = Position2D(0, 0)
        vertices = [(0, 0)]
        points = set(vertices)
        for line in lines:
            direction, steps, _ = line.split()
            direction = DIRECTIONS[direction]

            next_pos = curr_pos
            for _ in range(int(steps)):
                next_pos += direction
                points.add((next_pos.row, next_pos.col))
            vertices.append((next_pos.row, next_pos.col))
            curr_pos = next_pos

        p = Polygon(vertices)

        # p.area provides the area of the polygon, but it doesn't tell us how
        # many points consisting of integer coordinates actually lie within the
        # polygon.
        #
        # Pick's theorem says that A = i + b/2 - 1, where A is the area of the
        # polygon, b is the number of points on the polygon's boundary, and i
        # is the number of points enclosed by the polygon. We can calculate
        # i since we know A and b, and our answer is b+i.

        A = p.area
        b = p.length
        i = A - b // 2 + 1
        print(b + i)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().splitlines()
        curr_pos = Position2D(0, 0)
        vertices = [(0, 0)]
        points = set(vertices)
        for line in lines:
            _, _, code = line.split()
            code = code[2:-1]
            hex_steps, direction = code[:5], DIRECTIONS[code[-1]]
            steps = int(hex_steps, base=16)

            next_pos = curr_pos
            for _ in range(int(steps)):
                next_pos += direction
                points.add((next_pos.row, next_pos.col))
            vertices.append((next_pos.row, next_pos.col))
            curr_pos = next_pos

        p = Polygon(vertices)
        A = p.area
        b = p.length
        i = A - b // 2 + 1
        print(b + i)


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
    filename = utils.get_real_input(18)

part_a(filename)
if not args.skip_b:
    part_b(filename)
