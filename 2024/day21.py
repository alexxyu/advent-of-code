import argparse
from collections import *
from functools import cache
from typing import *

import utils
from utils import Direction, Position2D


def key_to_pos(pad: List[List[str]]) -> Dict[str, Position2D]:
    return {key: Position2D(r, c) for (r, c), key in utils.iter_grid_with_pos(pad)}


NUMPAD = key_to_pos([
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"],
])

DIRPAD = key_to_pos([
    [None, "^", "A"],
    ["<", "v", ">"],
])


DIR_TO_DIFF = {
    "^": Direction.UP,
    "v": Direction.DOWN,
    "<": Direction.LEFT,
    ">": Direction.RIGHT
}


def construct_paths(start: Position2D, end: Position2D, padpos: Dict[str, Position2D]) -> List[str]:
    diff = end - start
    dr, dc = diff.row, diff.col

    path = ""
    path += ("v" if dr > 0 else "^") * abs(dr)
    path += (">" if dc > 0 else "<") * abs(dc)

    def can_traverse(moves: str) -> bool:
        curr = start
        for m in moves:
            curr = curr + DIR_TO_DIFF[m]
            pos_to_key = {v: k for k, v in padpos.items()}
            if pos_to_key[curr] is None:
                return False
        return True

    return list(set(filter(can_traverse, [path, path[::-1]])))


@cache
def dirpad_presses(path: str, layer: int) -> int:
    if layer == 0:
        return len(path) + 1

    s = 0
    curr = DIRPAD["A"]
    for p in (path + "A"):
        target = DIRPAD[p]
        s += min(
            dirpad_presses(path, layer-1) for path in construct_paths(curr, target, DIRPAD)
        )
        curr = target
    return s


def presses(code: str, layers: int) -> int:
    s = 0
    curr = NUMPAD["A"]
    for c in code:
        target = NUMPAD[c]
        s += min(
            dirpad_presses(path, layers) for path in construct_paths(curr, target, NUMPAD)
        )
        curr = target
    return s


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        codes = f.read().strip().splitlines()
        s = sum(presses(code, 2) * int(code[:-1]) for code in codes)
        print(s)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        codes = f.read().strip().splitlines()
        s = sum(presses(code, 25) * int(code[:-1]) for code in codes)
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
    filename = utils.get_real_input(21)

part_a(filename)
if not args.skip_b:
    part_b(filename)
