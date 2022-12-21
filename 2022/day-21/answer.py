import argparse
import operator
from typing import Dict, Union
from sympy import Symbol, solve


ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}


def calculate(monkeys: Dict[str, str], m: str, human: str = '') -> Union[int, Symbol]:
    if m == human:
        return Symbol('x')
    if monkeys[m].isnumeric():
        return int(monkeys[m])

    a, op, b = monkeys[m].split()
    x, y = calculate(monkeys, a, human), calculate(monkeys, b, human)
    return ops[op](x, y)


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().splitlines()
        monkeys = dict(line.split(': ') for line in lines)
        print(int(calculate(monkeys, 'root')))


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()
        monkeys = dict(line.split(': ') for line in lines)

        a, _, b = monkeys['root'].split()
        x, y = calculate(monkeys, a, 'humn'), calculate(monkeys, b, 'humn')

        print(x, '=', y)
        print(round(solve(x - y)[0]))


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true',
                    help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
