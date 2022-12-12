import argparse
from math import prod
from dataclasses import dataclass
from typing import List
import operator


@dataclass
class Monkey:
    op: str             # The operation on the worry level
    x: int              # The first operand in the worry level equation
    y: int              # The second operand in the worry level equation
    k: int              # The divisor used to test divisibility
    a: int              # The monkey to throw to if the divisibility test passes
    b: int              # The monkey to throw to if the divisibility test fails
    items: List[int]    # The monkey's items


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().splitlines()
        i = 0
        monkeys = []
        while i < len(lines):
            i += 1
            items = list(map(int, lines[i].split(': ')[-1].split(', ')))
            i += 1
            _, _, x, op, y = lines[i].split(': ')[-1].split()
            i += 1
            k = int(lines[i].split()[-1])
            i += 1
            a = int(lines[i].split()[-1])
            i += 1
            b = int(lines[i].split()[-1])
            monkeys.append(Monkey(op, x, y, k, a, b, items))
            i += 2

        times_inspected = [0 for _ in range(len(monkeys))]
        for _ in range(20):
            for i, m in enumerate(monkeys):
                for worry in m.items:
                    times_inspected[i] += 1

                    op = operator.add if m.op == '+' else operator.mul
                    worry = op(worry, worry if m.y == 'old' else int(m.y))
                    worry //= 3

                    if worry % m.k == 0:
                        monkeys[m.a].items.append(worry)
                    else:
                        monkeys[m.b].items.append(worry)
                m.items = []

        times_inspected.sort()
        print(times_inspected[-1]*times_inspected[-2])


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()
        i = 0
        monkeys = []
        while i < len(lines):
            i += 1
            items = list(map(int, lines[i].split(': ')[-1].split(', ')))
            i += 1
            _, _, x, op, y = lines[i].split(': ')[-1].split()
            i += 1
            k = int(lines[i].split()[-1])
            i += 1
            a = int(lines[i].split()[-1])
            i += 1
            b = int(lines[i].split()[-1])
            monkeys.append(Monkey(op, x, y, k, a, b, items))
            i += 2

        mod = prod([m.k for m in monkeys])
        times_inspected = [0 for _ in range(len(monkeys))]
        for _ in range(10000):
            for i, m in enumerate(monkeys):
                for worry in m.items:
                    times_inspected[i] += 1

                    op = operator.add if m.op == '+' else operator.mul
                    worry = op(worry, worry if m.y == 'old' else int(m.y))
                    worry %= mod

                    if worry % m.k == 0:
                        monkeys[m.a].items.append(worry)
                    else:
                        monkeys[m.b].items.append(worry)
                m.items = []

        times_inspected.sort()
        print(times_inspected[-1]*times_inspected[-2])


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true',
                    help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
