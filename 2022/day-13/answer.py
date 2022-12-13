import argparse
from functools import cmp_to_key


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(right, list) and isinstance(left, int):
        return compare([left], right)
    else:
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if (r := compare(left[i], right[j])) != 0:
                return r
            i += 1
            j += 1

        if i >= len(left) and j < len(right):
            return -1
        if i < len(left) and j >= len(right):
            return 1
        return 0


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().splitlines()
        s = 0
        for i in range(0, len(lines), 3):
            l1 = eval(lines[i])
            l2 = eval(lines[i+1])
            if compare(l1, l2) < 0:
                s += (i//3 + 1)
        print(s)


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()

        packets = [[[2]], [[6]]]
        packets.extend([eval(line) for line in lines if line != ''])
        packets.sort(key=cmp_to_key(compare))

        a = packets.index([[2]]) + 1
        b = packets.index([[6]]) + 1
        print(a*b)


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true',
                    help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
