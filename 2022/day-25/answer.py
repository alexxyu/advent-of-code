import argparse


SNAFU_TO_DECIMAL = {
    '=': -2,
    '-': -1,
    '0': 0,
    '1': 1,
    '2': 2,
}

DECIMAL_TO_SNAFU = {
    0: '0',
    1: '1',
    2: '2',
    3: '=',
    4: '-',
    5: '0',
}


def to_base(n, b):
    # Adapted from https://stackoverflow.com/a/28666223
    if n == 0:
        return 0
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    n = 0
    for i, d in enumerate(digits):
        n += d * 10**i
    return n


def to_snafu(n):
    (n, m, s) = (to_base(n, 5), 0, '')
    while n > 0:
        k = (m + n % 10)
        m = 1 if k >= 3 else 0
        s += DECIMAL_TO_SNAFU[k]
        n //= 10
    return s[::-1]


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().splitlines()
        s = 0
        for line in lines:
            n = 0
            for i, c in enumerate(reversed(line)):
                n += SNAFU_TO_DECIMAL[c] * 5**i
            s += n
        print(to_snafu(s))


def part_b(_):
    print('Merry Christmas!')


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true',
                    help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
