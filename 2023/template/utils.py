import os
import requests
import subprocess


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


def parse_grid_digits(grid):
    return [[int(c) for c in r] for r in grid]


def ans(response):
    # Note: this is a MacOS-specific implementation to copy to clipboard
    print(response)
    subprocess.run('pbcopy', text=True, input=str(response).strip())


def get_real_input(day, year=2023):
    filepath = os.path.join(
        os.path.expanduser('~'),
        '.cache',
        'advent-of-code',
        str(year),
        f'{day}.in')
    if os.path.exists(filepath):
        return filepath

    session_cookie = os.environ['ADVENT_OF_CODE_KEY']
    if session_cookie is None:
        print("WARNING: AOC session cookie is not set. Check value of ADVENT_OF_CODE_KEY.")

    url = f'https://adventofcode.com/{year}/day/{day}/input'
    headers = {'Cookie': f'session={session_cookie}'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise ValueError(f"Got non-ok response from Advent of Code: {response.status_code} {response.reason}.")

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(response.text)

    return filepath
