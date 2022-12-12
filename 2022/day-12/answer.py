import argparse


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().splitlines()
        grid = [[c for c in line] for line in lines]

        s_i, s_j = 0, 0
        e_i, e_j = 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 'S':
                    s_i, s_j = i, j
                    grid[i][j] = 'a'
                elif grid[i][j] == 'E':
                    e_i, e_j = i, j
                    grid[i][j] = 'z'

        steps = 0
        q = [(s_i, s_j)]
        visited = set(q)
        while q != []:
            N = len(q)
            for _ in range(N):
                i, j = q.pop(0)

                if (i, j) == (e_i, e_j):
                    print(steps)
                    q = []
                    break

                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ii = i+di
                    jj = j+dj
                    if ii >= 0 and jj >= 0 and ii < len(grid) and jj < len(grid[ii]) and (ii, jj) not in visited and ord(grid[ii][jj]) <= ord(grid[i][j])+1:
                        visited.add((ii, jj))
                        q.append((ii, jj))
            steps += 1


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()
        grid = [[c for c in line] for line in lines]

        q = []
        visited = set()
        e_i, e_j = 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 'S' or grid[i][j] == 'a':
                    q.append((i, j))
                    grid[i][j] = 'a'
                elif grid[i][j] == 'E':
                    e_i, e_j = i, j
                    grid[i][j] = 'z'

        steps = 0
        visited = set(q)
        while q != []:
            N = len(q)
            for _ in range(N):
                i, j = q.pop(0)

                if (i, j) == (e_i, e_j):
                    print(steps)
                    q = []
                    break

                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ii = i+di
                    jj = j+dj
                    if ii >= 0 and jj >= 0 and ii < len(grid) and jj < len(grid[ii]) and (ii, jj) not in visited and ord(grid[ii][jj]) <= ord(grid[i][j])+1:
                        visited.add((ii, jj))
                        q.append((ii, jj))
            steps += 1


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true',
                    help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
