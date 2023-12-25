import argparse
from collections import defaultdict

import utils
from utils import Direction, Position2D


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        start = Position2D(0, 1)

        memo = defaultdict(lambda: -1)

        q = [(start, set(), 0)]
        while q != []:
            curr, q = q[0], q[1:]
            pos, visited, s = curr

            memo[pos] = s

            r, c = pos
            directions = list(Direction)
            match lines[r][c]:
                case ">":
                    directions = [Direction.RIGHT]
                case "^":
                    directions = [Direction.UP]
                case "<":
                    directions = [Direction.LEFT]
                case "v":
                    directions = [Direction.DOWN]

            for nd in directions:
                nr, nc = np = pos + nd
                if (
                    np not in visited
                    and np.is_inside_grid(lines)
                    and lines[nr][nc] != "#"
                    and memo[pos] < s + 1
                ):
                    q.append((np, visited | {pos}, s + 1))

        print(memo[Position2D(len(lines) - 1, len(lines[-1]) - 2)])


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        start = Position2D(0, 1)
        end = Position2D(len(lines) - 1, len(lines[-1]) - 2)

        parsed_graph = {}
        for r, row in enumerate(lines):
            for c, ch in enumerate(row):
                if ch != "#":
                    p = Position2D(r, c)
                    neighbors = defaultdict(int)
                    for np in p.iter_neighbors():
                        if np.is_inside_grid(lines) and lines[np.row][np.col] != "#":
                            neighbors[np] = 1
                    parsed_graph[p] = neighbors

        for p in list(parsed_graph.keys()):
            neighbors = parsed_graph[p]
            if len(neighbors) == 2:
                a, b = neighbors.keys()
                del parsed_graph[a][p]
                del parsed_graph[b][p]
                parsed_graph[b][a] = parsed_graph[a][b] = max(
                    parsed_graph[a][b], neighbors[a] + neighbors[b]
                )
                del parsed_graph[p]

        # Note: I found it much faster to run DFS instead of the BFS approach in part A, probably
        # because backtracking here doesn't require copying the dict every iteration.
        visited = {start: 0}

        def dfs(p):
            if p == end:
                return sum(visited.values())
            max_steps = 0
            for np in parsed_graph[p]:
                if np not in visited:
                    visited[np] = parsed_graph[p][np]
                    max_steps = max(max_steps, dfs(np))
                    del visited[np]
            return max_steps

        print(dfs(start))


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
    filename = utils.get_real_input(23)

# part_a(filename)
if not args.skip_b:
    part_b(filename)
