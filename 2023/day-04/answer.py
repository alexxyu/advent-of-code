import argparse

import utils


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().splitlines()
        s = 0
        for line in lines:
            _, nums = line.split(": ")
            win, act = nums.split(" | ")

            win = {int(x) for x in win.split()}
            act = [int(x) for x in act.split()]

            m = 0
            for a in act:
                if a in win:
                    m += 1

            if m > 0:
                s += 2 ** (m - 1)
        print(s)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().splitlines()
        c = [1] * len(lines)
        for i, line in enumerate(lines):
            _, nums = line.split(": ")
            win, act = nums.split(" | ")

            win = {int(x) for x in win.split()}
            act = [int(x) for x in act.split()]

            m = 0
            for a in act:
                if a in win:
                    m += 1

            if m > 0:
                for j in range(1, m + 1):
                    c[i + j] += c[i]
        print(sum(c))


parser = argparse.ArgumentParser()
parser.add_argument(
    "filename",
    help="the input file, will default to actual AoC input if omitted",
    type=str,
    nargs="?",
    default=None,
)
parser.add_argument("--skip-b", help="skip running part b", action="store_true")
args = parser.parse_args()

filename = args.filename
if not args.filename:
    filename = utils.get_real_input(4)

part_a(filename)
if not args.skip_b:
    part_b(filename)
