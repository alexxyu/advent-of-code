import argparse


def calculate_priority(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().splitlines()
        s = 0
        for line in lines:
            l = len(line)
            a, b = line[:l//2], line[l//2:]
            shared = set(a).intersection(set(b))
            s += calculate_priority(list(shared)[0])
        print(s)


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()
        s = 0
        for i in range(len(lines)//3):
            a, b, c = lines[3*i:3*(i+1)]
            shared = set(a).intersection(set(b)).intersection(set(c))
            c = list(shared)[0]
            s += calculate_priority(list(shared)[0])
        print(s)


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true',
                    help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
