import argparse
from collections import *
from typing import *

from utils import get_real_input


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        stones = [int(x) for x in lines[0].split()]

        for _ in range(25):
            sim = []
            for stone in stones:
                stonestr = str(stone)
                if stone == 0:
                    sim.append(1)
                elif len(stonestr) % 2 == 0:
                    sim.append(int(stonestr[:len(stonestr) // 2]))
                    sim.append(int(stonestr[len(stonestr) // 2:]))
                else:
                    sim.append(stone * 2024)
            stones = sim
        print(len(stones))



def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()

        stones = Counter([int(x) for x in lines[0].split()])
        for _ in range(75):
            sim = Counter()
            for stone, count in stones.items():
                stonestr = str(stone)
                if stone == 0:
                    sim[1] += count
                elif len(stonestr) % 2 == 0:
                    a = int(stonestr[:len(stonestr) // 2])
                    b = int(stonestr[len(stonestr) // 2:])
                    sim[a] += count
                    sim[b] += count
                else:
                    sim[stone * 2024] += count
            stones = sim

        print(sum(stones.values()))


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
    filename = get_real_input(11)

part_a(filename)
if not args.skip_b:
    part_b(filename)
