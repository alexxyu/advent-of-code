import os
import subprocess
from dataclasses import dataclass
from enum import Enum

import requests


@dataclass(frozen=True)
class Position2D:
    row: int
    col: int

    def is_inside_grid(grid, pos):
        r, c = pos.row, pos.col
        return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[r])

    def __neg__(self):
        return Position2D(-self.row, -self.col)

    def __add__(self, other):
        p0 = self if not isinstance(self, Direction) else self.value
        r0, c0 = p0.row, p0.col

        p1 = other if not isinstance(other, Direction) else other.value
        r1, c1 = p1.row, p1.col

        return Position2D(r0 + r1, c0 + c1)

    def __lt__(self, other):
        return self.col < other.col if self.row == other.row else self.row < other.row

    def __sub__(self, other):
        return self + (-other)


class Direction(Enum):
    LEFT = Position2D(0, -1)
    RIGHT = Position2D(0, 1)
    UP = Position2D(-1, 0)
    DOWN = Position2D(1, 0)

    def rot90(direction, k=1):
        if k == 0:
            return direction

        k %= 4
        match direction:
            case Direction.LEFT:
                return Direction.rot90(Direction.UP, k - 1)
            case Direction.UP:
                return Direction.rot90(Direction.RIGHT, k - 1)
            case Direction.RIGHT:
                return Direction.rot90(Direction.DOWN, k - 1)
            case Direction.DOWN:
                return Direction.rot90(Direction.LEFT, k - 1)
            case _:
                raise ValueError("invalid direction provided")

    def __lt__(self, other):
        return self.value < other.value


def print_grid(grid):
    return [print("".join(r)) for r in grid]


def iter_grid_with_pos(grid):
    for i, r in enumerate(grid):
        for j, c in enumerate(r):
            yield (i, j), c


def iter_grid(grid):
    for _, g in iter_grid_with_pos(grid):
        yield g


def iter_grid_neighbors_with_pos(grid, r, c):
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= len(grid):
                continue
            if nc < 0 or nc >= len(grid[nr]):
                continue
            yield (nr, nc), grid[nr][nc]


def iter_grid_neighbors(grid, r, c):
    for _, n in iter_grid_neighbors_with_pos(grid, r, c):
        yield n


def parse_list_nums(line, sep=None):
    line_split = line.split() if sep is None else line.split(sep)
    return list(map(int, line_split))


def parse_grid_digits(grid):
    return [[int(c) for c in r] for r in grid]


def ans(response):
    # Note: this is a MacOS-specific implementation to copy to clipboard
    print(response)
    subprocess.run("pbcopy", text=True, input=str(response).strip())


def get_real_input(day, year=2023):
    filepath = os.path.join(
        os.path.expanduser("~"), ".cache", "advent-of-code", str(year), f"{day}.in"
    )
    if os.path.exists(filepath):
        return filepath

    session_cookie = os.environ["ADVENT_OF_CODE_KEY"]
    if session_cookie is None:
        print(
            "WARNING: AOC session cookie is not set. Check value of ADVENT_OF_CODE_KEY."
        )

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {"Cookie": f"session={session_cookie}"}
    response = requests.get(url, headers=headers, timeout=5)

    if response.status_code != 200:
        raise ValueError(
            f"Got non-ok response from Advent of Code: {response.status_code} {response.reason}."
        )

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        f.write(response.text)

    return filepath
