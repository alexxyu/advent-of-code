import argparse
from tqdm import tqdm


def distance(a, b):
    return (abs(a[0] - b[0])) + (abs(a[1] - b[1]))


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().splitlines()
        sensors = dict()
        for line in lines:
            s, b = line.split(': ')
            _, _, s_x, s_y = s.split()
            s_x, s_y = int(s_x[:-1][2:]), int(s_y[2:])

            _, _, _, _, b_x, b_y = b.split()
            b_x, b_y = int(b_x[:-1][2:]), int(b_y[2:])
            sensors[(s_x, s_y)] = (b_x, b_y)

        p = set()
        beacons = set(sensors.values())
        target_y = 2000000
        for s, b in sensors.items():
            d = distance(s, b)
            dy = abs(s[1] - target_y)
            dx = d - dy
            for di in range(-dx, dx+1):
                x = s[0] + di
                if (x, target_y) not in beacons:
                    p.add(x)
        print(len(p))


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()
        sensors = dict()
        min_x, max_x, min_y, max_y = float('inf'), float('-inf'), float('inf'), float('-inf')
        for line in lines:
            s, b = line.split(': ')
            _, _, s_x, s_y = s.split()
            s_x, s_y = int(s_x[:-1][2:]), int(s_y[2:])

            _, _, _, _, b_x, b_y = b.split()
            b_x, b_y = int(b_x[:-1][2:]), int(b_y[2:])
            sensors[(s_x, s_y)] = (b_x, b_y)

            min_x, max_x = min(min_x, s_x), max(max_x, s_x)
            min_y, max_y = min(min_y, s_y), max(max_y, s_y)

        min_x, min_y = max(min_x, 0), max(min_y, 0)
        max_x, max_y = min(max_x, 4e6), min(max_y, 4e6)
        def check(p):
            if p[0] < min_x or p[1] < min_y or p[0] > max_x or p[1] > max_y:
                return False
            for s, b in sensors.items():
                d1 = distance(s, b)
                d2 = distance(s, p)
                if d2 <= d1:
                    return False
            return True

        for s, b in tqdm(sensors.items(), leave=False):
            d = distance(s, b)

            # upper left diagonal
            x, y = s
            x = x-d-1
            while x+1 <= s[0]:
                if check((x, y)):
                    print(x, y, int(x*4e6 + y))
                    return
                x += 1
                y -= 1

            # upper right diagonal
            while y+1 <= s[1]:
                if check((x, y)):
                    print(x, y, int(x*4e6 + y))
                    return
                x += 1
                y += 1

            # lower right diagonal
            while x-1 >= s[1]:
                if check((x, y)):
                    print(x, y, int(x*4e6 + y))
                    return
                x -= 1
                y += 1

            # lower left diagonal
            while y-1 >= s[0]:
                if check((x, y)):
                    print(x, y, int(x*4e6 + y))
                    return
                x -= 1
                y -= 1


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true',
                    help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
