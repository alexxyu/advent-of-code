import os
import re
import subprocess
from dataclasses import dataclass
from enum import Enum

import requests


@dataclass(frozen=True)
class Position2D:
    row: int
    col: int

    def is_inside_grid(self, grid):
        r, c = self.row, self.col
        return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[r])

    def iter_cardinal_neighbors(self):
        for d in Direction:
            yield self + d

    def iter_all_neighbors(self):
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr != 0 or dc != 0:
                    yield self + Position2D(dr, dc)

    def __neg__(self):
        return Position2D(-self.row, -self.col)

    def __add__(self, other):
        r0, c0 = self if not isinstance(self, Direction) else self.value
        r1, c1 = other if not isinstance(other, Direction) else other.value
        return Position2D(r0 + r1, c0 + c1)

    def __mul__(self, other):
        if isinstance(other, float | int):
            return Position2D(self.row * other, self.col * other)
        r0, c0 = self if not isinstance(self, Direction) else self.value
        r1, c1 = other if not isinstance(other, Direction) else other.value
        return Position2D(r0 * r1, c0 * c1)

    def __rmul__(self, other):
        return self * other

    def __lt__(self, other):
        return self.col < other.col if self.row == other.row else self.row < other.row

    def __sub__(self, other):
        return self + (-other)

    def __iter__(self):
        return iter((self.row, self.col))

    def __getitem__(self, index):
        return (self.row, self.col)[index]


class Direction(Enum):
    RIGHT = Position2D(0, 1)
    UP = Position2D(-1, 0)
    LEFT = Position2D(0, -1)
    DOWN = Position2D(1, 0)

    def rot90(self, k=1):
        if k == 0:
            return self

        k %= 4
        match self:
            case Direction.LEFT:
                return Direction.UP.rot90(k - 1)
            case Direction.UP:
                return Direction.RIGHT.rot90(k - 1)
            case Direction.RIGHT:
                return Direction.DOWN.rot90(k - 1)
            case Direction.DOWN:
                return Direction.LEFT.rot90(k - 1)
            case _:
                msg = "Invalid direction provided"
                raise ValueError(msg)

    def __neg__(self):
        return -self.value

    def __pos__(self):
        return self.value

    def __add__(self, other):
        return self.value + other

    def __sub__(self, other):
        return self + (-other)

    def __lt__(self, other):
        return self.value < other.value


def print_grid(grid):
    return [print("".join(r)) for r in grid]


def find_grid_pos_with_value(grid, value):
    positions = []
    for (r, c), p in iter_grid_with_pos(grid):
        if p == value:
            positions.append(Position2D(r, c))
    return positions


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


def parse_nums(line):
    return [int(n) for n in re.findall(r"\d+", line)]


def parse_grid_digits(grid):
    return [[int(c) for c in r] for r in grid]


def ans(response):
    # Note: this is a MacOS-specific implementation to copy to clipboard
    print(response)
    subprocess.run("/usr/bin/pbcopy", text=True, input=str(response).strip(), check=False)


def get_real_input(day, year=2024):
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
        msg = f"Got non-ok response from Advent of Code: {response.status_code} {response.reason}."
        raise ValueError(msg)

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        f.write(response.text)

    return filepath
