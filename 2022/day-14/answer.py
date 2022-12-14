import argparse


def parse_grid(lines):
    blocked = set()
    for line in lines:
        s = line.split(' -> ')
        x_p, y_p = map(int, s[0].split(','))
        for p in s[1:]:
            x, y = map(int, p.split(','))
            if x_p == x:
                a, b = min(y_p, y), max(y_p, y)
                for i in range(a, b+1):
                    blocked.add((x, i))
            elif y_p == y:
                a, b = min(x_p, x), max(x_p, x)
                for j in range(a, b+1):
                    blocked.add((j, y))
            x_p, y_p = x, y
    return blocked


def simulate_sand_grain(blocked, max_y):
    (x, y) = (500, 0)
    while y <= max_y:
        if (x, y+1) not in blocked:
            y += 1
            blocked.add((x, y))
        elif (x-1, y+1) not in blocked:
            x -= 1
            y += 1
            blocked.add((x, y))
        elif (x+1, y+1) not in blocked:
            x += 1
            y += 1
            blocked.add((x, y))
        else:
            blocked.add((x, y))
            break
        blocked.remove((x, y))
    return (x, y)

def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().splitlines()
        blocked = parse_grid(lines)

        s = 0
        y, max_y = 0, max(blocked, key=lambda x: x[1])[1]
        while y <= max_y:
            s += 1
            (_, y) = simulate_sand_grain(blocked, max_y)
        print(s-1)


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()
        blocked = parse_grid(lines)

        min_x = min(blocked, key=lambda x: x[0])[0]
        max_x = max(blocked, key=lambda x: x[0])[0]
        y, max_y = -1, max(blocked, key=lambda x: x[1])[1]+2
        for x in range(min_x//2, max_x*2):
            blocked.add((x, max_y))

        s = 0
        while y != 0:
            s += 1
            (x, y) = simulate_sand_grain(blocked, max_y)
        print(s)


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true',
                    help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
