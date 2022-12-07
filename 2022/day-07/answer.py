import argparse
from collections import *

def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().splitlines()

        curr_dir = '/'
        dir_to_parent = { '/': '/' }
        dir_sizes = defaultdict(int)
        i = 0
        while i < len(lines):
            line = lines[i]
            command = line.split()
            if command[1] == 'cd':
                d = command[-1]
                if d == '..':
                    curr_dir = dir_to_parent[curr_dir]
                elif d == '/':
                    curr_dir = '/'
                else:
                    old_dir = curr_dir
                    curr_dir = f'{curr_dir}{d}/'
                    dir_to_parent[curr_dir] = old_dir
                i += 1
            elif command[1] == 'ls':
                i += 1
                while i < len(lines) and lines[i][0] != '$':
                    listing = lines[i]
                    if listing[0] != 'd':
                        size = int(listing.split()[0])
                        k = curr_dir
                        dir_sizes[k] += size
                        while k != '/':
                            k = dir_to_parent[k]
                            dir_sizes[k] += size
                    i += 1
        print(sum([v for v in dir_sizes.values() if v <= 100000]))

def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()

        curr_dir = '/'
        dir_to_parent = { '/': '/' }
        dir_sizes = defaultdict(int)
        i = 0
        while i < len(lines):
            line = lines[i]
            command = line.split()
            if command[1] == 'cd':
                d = command[-1]
                if d == '..':
                    curr_dir = dir_to_parent[curr_dir]
                elif d == '/':
                    curr_dir = '/'
                else:
                    old_dir = curr_dir
                    curr_dir = f'{curr_dir}{d}/'
                    dir_to_parent[curr_dir] = old_dir
                i += 1
            elif command[1] == 'ls':
                i += 1
                while i < len(lines) and lines[i][0] != '$':
                    listing = lines[i]
                    if listing[0] != 'd':
                        size = int(listing.split()[0])
                        k = curr_dir
                        dir_sizes[k] += size
                        while k != '/':
                            k = dir_to_parent[k]
                            dir_sizes[k] += size
                    i += 1
        free_space = 7e7 - dir_sizes['/']
        need_space = 3e7 - free_space
        print(next(x for x in sorted(dir_sizes.values()) if x >= need_space))

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true', help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
