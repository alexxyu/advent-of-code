import argparse
import re
from enum import Enum
from typing import Tuple


class Direction(Enum):
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)
    UP = (-1, 0)


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        board, path = f.read().split('\n\n')

        board = board.splitlines()
        M, N = len(board), max(len(r) for r in board)
        board = [row.ljust(N) for row in board]
        path = re.split(r'([LR])', path.strip())

        directions = [d.value for d in Direction]
        i, r, c = 0, 0, board[0].find('.')

        def get_next_position(r, c, dr, dc):
            r = (r + M + dr) % M
            c = (c + N + dc) % N
            while board[r][c] == ' ':
                r = (r + M + dr) % M
                c = (c + N + dc) % N
            return r, c

        for p in path:
            if p == 'R':
                i = (i+1) % 4
            elif p == 'L':
                i = (i+3) % 4
            else:
                (dr, dc) = directions[i]
                for _ in range(int(p)):
                    (nr, nc) = get_next_position(r, c, dr, dc)
                    if board[nr][nc] == '#':
                        break
                    (r, c) = (nr, nc)

        print(1000*(r+1) + 4*(c+1) + i)


M = N = 50


def get_next_position(i: int, d: Direction, r: int, c: int) -> Tuple[int, Direction, int, int]:
    """
    This is hard-coded for my specific input because I can't be bothered
    to figure out how to generalize the cube structure.

    My cube is in the following form:
     12
     3
    45
    6
    """

    dr, dc = d.value
    nr, nc = r + dr, c + dc
    if 0 <= nr < M and 0 <= nc < N:
        return (i, d, nr, nc)

    if i == 1:
        if d == Direction.RIGHT:
            return (2, Direction.RIGHT, r, 0)
        elif d == Direction.DOWN:
            return (3, Direction.DOWN, 0, c)
        elif d == Direction.LEFT:
            return (4, Direction.RIGHT, M-1-r, 0)
        elif d == Direction.UP:
            return (6, Direction.RIGHT, c, 0)
    elif i == 2:
        if d == Direction.RIGHT:
            return (5, Direction.LEFT, M-1-r, N-1)
        elif d == Direction.DOWN:
            return (3, Direction.LEFT, c, N-1)
        elif d == Direction.LEFT:
            return (1, Direction.LEFT, r, N-1)
        elif d == Direction.UP:
            return (6, Direction.UP, M-1, c)
    elif i == 3:
        if d == Direction.RIGHT:
            return (2, Direction.UP, M-1, r)
        elif d == Direction.DOWN:
            return (5, Direction.DOWN, 0, c)
        elif d == Direction.LEFT:
            return (4, Direction.DOWN, 0, r)
        elif d == Direction.UP:
            return (1, Direction.UP, M-1, c)
    elif i == 4:
        if d == Direction.RIGHT:
            return (5, Direction.RIGHT, r, 0)
        elif d == Direction.DOWN:
            return (6, Direction.DOWN, 0, c)
        elif d == Direction.LEFT:
            return (1, Direction.RIGHT, M-1-r, 0)
        elif d == Direction.UP:
            return (3, Direction.RIGHT, c, 0)
    elif i == 5:
        if d == Direction.RIGHT:
            return (2, Direction.LEFT, M-1-r, N-1)
        elif d == Direction.DOWN:
            return (6, Direction.LEFT, c, N-1)
        elif d == Direction.LEFT:
            return (4, Direction.LEFT, r, N-1)
        elif d == Direction.UP:
            return (3, Direction.UP, M-1, c)
    elif i == 6:
        if d == Direction.RIGHT:
            return (5, Direction.UP, M-1, r)
        elif d == Direction.DOWN:
            return (2, Direction.DOWN, 0, c)
        elif d == Direction.LEFT:
            return (1, Direction.DOWN, 0, r)
        elif d == Direction.UP:
            return (4, Direction.UP, M-1, c)


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        board, path = f.read().split('\n\n')
        board = board.splitlines()
        path = re.split(r'([LR])', path.strip())

        offsets = [(0, 50), (0, 100), (50, 50), (100, 0), (100, 50), (150, 0)]
        faces = []
        for (r, c) in offsets:
            rows = board[r:r+M]
            faces.append([row[c:c+N] for row in rows])

        (f, k, r, c) = (1, 0, 0, 0)
        directions = [d for d in Direction]
        for p in path:
            if p == 'R':
                k = (k+1) % 4
            elif p == 'L':
                k = (k+3) % 4
            else:
                for _ in range(int(p)):
                    (nf, nd, nr, nc) = get_next_position(
                        f, directions[k], r, c)
                    if faces[nf-1][nr][nc] == '#':
                        break
                    (f, d, r, c) = (nf, nd, nr, nc)
                    k = directions.index(d)
        print(
            f"face {f}, row: {r+1}, col: {c+1}, direction: {k}")
        print((r+1+offsets[f-1][0])*1000 + (c+1+offsets[f-1][1])*4 + k)


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true',
                    help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
