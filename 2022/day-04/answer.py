import argparse

def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().splitlines()
        c = 0
        for line in lines:
            a, b = line.split(',')
            a_s, a_e = map(int, a.split('-'))
            b_s, b_e = map(int, b.split('-'))

            if a_s <= b_s and a_e >= b_e or b_s <= a_s and b_e >= a_e:
                c += 1
        print(c)

def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()
        c = 0
        for line in lines:
            a, b = line.split(',')
            a_s, a_e = map(int, a.split('-'))
            b_s, b_e = map(int, b.split('-'))

            if b_s < a_s:
                a_s, b_s = b_s, a_s
                a_e, b_e = b_e, a_e
            if a_e >= b_s:
                c += 1
        print(c)

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true', help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
