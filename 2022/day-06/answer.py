import argparse


def find_marker(msg, n):
    k = list(msg[:n])

    if len(set(k)) == len(k):
        return n

    for i, c in enumerate(msg[n:]):
        k = k[1:]
        k.append(c)
        if len(set(k)) == len(k):
            return i+n+1

    return None


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().splitlines()
        print(find_marker(lines[0], 4))


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()
        print(find_marker(lines[0], 14))


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true',
                    help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
