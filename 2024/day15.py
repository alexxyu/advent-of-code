import argparse
from collections import *
from typing import *

import utils
from utils import Direction, Position2D

MOVES = {
    "<": Direction.LEFT,
    ">": Direction.RIGHT,
    "v": Direction.DOWN,
    "^": Direction.UP
}


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        grid, moves = f.read().strip().split("\n\n")
        grid = [list(r) for r in grid.splitlines()]

        curr = None
        for (r, c), p in utils.iter_grid_with_pos(grid):
            if p == "@":
                curr = Position2D(r, c)
                break

        def apply_move(pos, move):
            new_pos = pos + move
            if not new_pos.is_inside_grid(grid):
                return pos

            match grid[new_pos.row][new_pos.col]:
                case ".":
                    grid[new_pos.row][new_pos.col] = grid[pos.row][pos.col]
                    grid[pos.row][pos.col] = "."
                    return new_pos
                case "#":
                    return pos
                case "O":
                    if apply_move(new_pos, move) != new_pos:
                        grid[new_pos.row][new_pos.col] = grid[pos.row][pos.col]
                        grid[pos.row][pos.col] = "."
                        return new_pos
                    return pos
                case _:
                    return pos

        moves = moves.replace("\n", "")
        for move in moves:
            curr = apply_move(curr, MOVES[move])

        s = 0
        for (r, c), p in utils.iter_grid_with_pos(grid):
            if p == "O":
                s += 100*r + c
        print(s)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        grid, moves = f.read().strip().split("\n\n")
        grid = [list("".join({"#": "##", "O": "[]", ".": "..", "@": "@."}[x] for x in r)) for r in grid.splitlines()]

        curr = None
        for (r, c), p in utils.iter_grid_with_pos(grid):
            if p == "@":
                curr = Position2D(r, c)
                break

        def apply_move(pos, move):
            seen = {}
            def can_move(pos, move):
                if not pos.is_inside_grid(grid):
                    return False

                p = grid[pos.row][pos.col]
                match p:
                    case ".":
                        return True
                    case "#":
                        return False
                    case "@":
                        seen[pos] = "@"
                        return can_move(pos + move, move)
                    case "[" | "]":
                        pair = {"[": "]", "]": "["}[p]
                        pairdir = {"[": Direction.RIGHT, "]": Direction.LEFT}[p]
                        seen[pos] = p
                        seen[pos + pairdir] = pair

                        new_pos = pos + move
                        if move == pairdir:
                            return can_move(new_pos + pairdir, move)
                        return can_move(new_pos, move) and can_move(new_pos + pairdir, move)

            if can_move(pos, move):
                for p in seen:
                    grid[p.row][p.col] = "."

                for p, v in seen.items():
                    new_pos = p + move
                    grid[new_pos.row][new_pos.col] = v
                return pos + move
            return pos

        moves = moves.replace("\n", "")
        for move in moves:
            curr = apply_move(curr, MOVES[move])

        s = 0
        for (r, c), p in utils.iter_grid_with_pos(grid):
            if p == "[":
                s += 100*r + c
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
    filename = utils.get_real_input(15)

part_a(filename)
if not args.skip_b:
    part_b(filename)
