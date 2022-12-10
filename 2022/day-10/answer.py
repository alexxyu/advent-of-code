import argparse


OP_CYCLES = {
    'addx': 2,
    'noop': 1,
}


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().splitlines()
        i, x, signal = 1, 1, 0
        cycles = set([20, 60, 100, 140, 180, 220])
        for line in lines:
            op = line.split()[0]
            for _ in range(OP_CYCLES[op]):
                if i in cycles:
                    signal += i*x
                i += 1
            if op == 'addx':
                x += int(line.split()[1])
        print(signal)


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()
        rows = [['.' for _ in range(40)] for _ in range(6)]
        i, x = 0, 1
        for line in lines:
            op = line.split()[0]
            for _ in range(OP_CYCLES[op]):
                r, c = i // 40, i % 40
                if abs(x - c) <= 1:
                    rows[r][c] = '#'
                i += 1
            if op == 'addx':
                x += int(line.split()[1])

        for r in rows:
            print(''.join(r))


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true',
                    help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
