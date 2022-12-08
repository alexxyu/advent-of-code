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
        grid = []
        for line in lines:
            grid.append(list(map(int, line)))
        
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                h = grid[i][j]

                if (all(grid[ii][j] >= h for ii in range(0, i-1)) or
                    all(grid[ii][j] >= h for ii in range(i+1, len(grid))) or
                    all(grid[i][jj] >= h for jj in range(0, j-1)) or
                    all(grid[i][jj] >= h for jj in range(j+1, len(grid[i])))):
                    c += 1
        print(c)

def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()
        grid = []
        for line in lines:
            grid.append(list(map(int, line)))
        
        c = 1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                h = grid[i][j]

                k = 1
                p = 0
                for ii in range(i-1, -1, -1):
                    p += 1
                    if grid[ii][j] >= h:
                        break
                k *= p

                p = 0
                for ii in range(i+1, len(grid)):
                    p += 1
                    if grid[ii][j] >= h:
                        break
                k *= p

                p = 0
                for jj in range(j-1, -1, -1):
                    p += 1
                    if grid[i][jj] >= h:
                        break
                k *= p

                p = 0
                for jj in range(j+1, len(grid[i])):
                    p += 1
                    if grid[i][jj] >= h:
                        break
                k *= p
                c = max(c, k)
        print(c)

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true', help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
