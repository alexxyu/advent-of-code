import argparse


rocks = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
    [(0, 2), (1, 2), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],
]


def top_down_view(grid):
    view = [len(grid) for _ in range(7)]
    for c in range(7):
        n = 0
        for r in grid:
            if r[c] == '.':
                n += 1
            else:
                break
        view[c] = n
    return tuple(view)


def simulate(n, moves):
    grid = []
    cache = dict()
    state_after_rock = dict()

    i, k, N = 0, 0, 0
    while i < n:
        prev_height = len(grid)
        t = i % len(rocks)
        rock = [(r, c+2) for r, c in rocks[t]]

        # Add rows to the grid to fit the next rock
        h = max(rock, key=lambda x: x[0])[0] + 1
        for _ in range(3 + h):
            grid.insert(0, list('.......'))

        # Simulate where the rock ends up on the grid
        can_move_vertically = True
        while can_move_vertically:
            dc = 1 if (moves[k % len(moves)] == '>') else -1

            # Try to move the rock horizontally based on the jet stream
            rock_updated = []
            can_move_horizontally = True
            for (r, c) in rock:
                c += dc
                if c < 0 or c >= 7 or grid[r][c] == '#':
                    can_move_horizontally = False
                    break
                rock_updated.append((r, c))
            if can_move_horizontally:
                rock = rock_updated

            # Try to move the rock vertically
            rock_updated = []
            can_move_vertically = True
            for (r, c) in rock:
                r += 1
                if r >= len(grid) or grid[r][c] == '#':
                    can_move_vertically = False
                    break
                rock_updated.append((r, c))
            if can_move_vertically:
                rock = rock_updated

            k += 1

        # Update the grid with the new rock
        for (r, c) in rock:
            grid[r][c] = '#'

        # Remove any empty rows at the top of the grid
        while len(grid) > 0 and all([c == '.' for c in grid[0]]):
            grid.pop(0)

        state_after_rock[i] = (k, len(grid))
        state = top_down_view(grid)
        curr_height = len(grid)

        # A cycle is detected when we end up with the same top-down view of the board,
        # along with the same rock and index into the moves
        if (t, k % len(moves), state) in cache:
            j = cache[(t, k % len(moves), state)]
            k_j, h = state_after_rock[j]

            dd = i - j              # how many rocks are in the cycle
            dh = curr_height - h    # the change in height over one cycle
            dk = k - k_j            # the change in k over one cycle
            p = (n - 1 - j) // dd   # the number of cycles

            # Now, we can skip over the cycles and resume simulation after the last full cycle.
            N = h + p*dh
            i = j + p*dd
            k += (p-1) * dk

            cache.clear()           # clear the cache so another cycle isn't detected
        else:
            N += (curr_height - prev_height)
            cache[(t, k % len(moves), state)] = i
        i += 1

    print(N)


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().splitlines()
        simulate(2022, lines[0])


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()
        simulate(1000000000000, lines[0])


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true',
                    help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
