import argparse

rps = { 'A': 'R', 'B': 'P', 'C': 'S', 'X': 'R', 'Y': 'P', 'Z': 'S' }
m = { 'R': 1, 'P': 2, 'S': 3 }
k = { 'R': { 'R': 3, 'P': 6, 'S': 0 }, 'P': { 'R': 0, 'P': 3, 'S': 6 }, 'S': { 'R': 6, 'P': 0, 'S': 3 } }
p = { 'R': { 'X': 'S', 'Y': 'R', 'Z': 'P' }, 'P': { 'X': 'R', 'Y': 'P', 'Z': 'S' }, 'S': { 'X': 'P', 'Y': 'S', 'Z': 'R' } }

def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().splitlines()
        score = 0
        for line in lines:
            a, b = line.split()
            a, b = rps[a], rps[b]
            score += k[a][b] + m[b]
        print(score)

def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()
        score = 0
        for line in lines:
            a, b = line.split()
            a = rps[a]
            need = p[a][b]
            score += k[a][need] + m[need]
        print(score)

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true', help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
