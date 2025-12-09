import argparse
from collections import *
from typing import *

import utils
from shapely.geometry import Polygon


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        points = []
        for line in lines:
            a, b = line.split(",")
            points.append((int(a), int(b)))


        max_size = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                a1, b1 = points[i]
                a2, b2 = points[j]

                area = (abs(a1 - a2) + 1) * (abs(b1 - b2) + 1)
                max_size = max(max_size, area)

        print(max_size)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        points = []
        for line in lines:
            a, b = line.split(",")
            points.append((int(a), int(b)))

        polygon = Polygon(points)
        max_size = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                a1, b1 = points[i]
                a2, b2 = points[j]

                left = min(a1, a2)
                bottom = min(b1, b2)
                right = max(a1, a2)
                top = max(b1, b2)
                rectangle = Polygon([(left, bottom), (right, bottom), (right, top), (left, top)])

                if polygon.covers(rectangle):
                    area = (abs(a1 - a2) + 1) * (abs(b1 - b2) + 1)
                    max_size = max(max_size, area)

        print(max_size)


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
    filename = utils.get_real_input(9)

part_a(filename)
if not args.skip_b:
    part_b(filename)
