import argparse
from collections import *
from functools import lru_cache
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from itertools import *
from math import *

def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().splitlines()
        crates = []
        for line in lines:
            if line.strip()[0] == '1':
                break

            j = 0
            row = []
            while j < len(line):
                c = line[j]
                spaces = 0
                while j < len(line) and line[j] == ' ':
                    spaces += 1
                    j += 1

                row.extend([' '] * (spaces // 4))
                if c == '[':
                    row.append(line[j+1])
                    j += 3

            crates.append(row)

        i = lines.index('')
        k = int(lines[i-1].split()[-1])
        columns = [[] for _ in range(k)]
        for row in crates:
            for j, r in enumerate(row):
                if r != ' ':
                    columns[j].append(r)
        columns = [c[::-1] for c in columns]

        for line in lines[i+1:]:
            _, n, _, a, _, b = line.split()
            n, a, b = map(int, [n, a, b])
            
            for _ in range(n):
                columns[b-1].append(columns[a-1][-1])
                columns[a-1].pop()

        print(''.join([c[-1] for c in columns]))

def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()
        crates = []
        for line in lines:
            if line.strip()[0] == '1':
                break

            j = 0
            row = []
            while j < len(line):
                c = line[j]
                spaces = 0
                while j < len(line) and line[j] == ' ':
                    spaces += 1
                    j += 1

                row.extend([' '] * (spaces // 4))
                if c == '[':
                    row.append(line[j+1])
                    j += 3

            crates.append(row)

        i = lines.index('')
        k = int(lines[i-1].split()[-1])
        columns = [[] for _ in range(k)]
        for row in crates:
            for j, r in enumerate(row):
                if r != ' ':
                    columns[j].append(r)
        columns = [c[::-1] for c in columns]

        for line in lines[i+1:]:
            _, n, _, a, _, b = line.split()
            n, a, b = map(int, [n, a, b])
            
            columns[b-1].extend(columns[a-1][-n:])
            for _ in range(n):
                columns[a-1].pop()

        print(''.join([c[-1] for c in columns]))

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true', help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
