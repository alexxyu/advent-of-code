import argparse
from collections import *
from typing import *

import utils
import z3


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        registersStr, instructionsStr = f.read().strip().split("\n\n")
        registers = utils.parse_nums(registersStr)
        instructions = utils.parse_nums(instructionsStr)

        def combo_operand(n):
            if 0 <= n <= 3:
                return n
            return registers[n-4]

        i = 0
        output = []
        while i < len(instructions):
            jump = 2

            operation = instructions[i]
            operand = instructions[i+1]
            match operation:
                case 0: # adv
                    numer = registers[0]
                    denom = 2 ** combo_operand(operand)
                    registers[0] = numer // denom
                case 1: # bxl
                    registers[1] = registers[1] ^ operand
                case 2: # bst
                    registers[1] = combo_operand(operand) % 8
                case 3: # jnz
                    if registers[0] != 0:
                        i = operand
                        jump = 0
                case 4: # bxc
                    registers[1] = registers[1] ^ registers[2]
                case 5: # out
                    output.append(combo_operand(operand) % 8)
                case 6: # bdv
                    numer = registers[0]
                    denom = 2 ** combo_operand(operand)
                    registers[1] = numer // denom
                case 7: # cdv
                    numer = registers[0]
                    denom = 2 ** combo_operand(operand)
                    registers[2] = numer // denom
            i += jump

        print(",".join(map(str, output)))


def build(solver, a, b, c, instructions):
    def combo_operand(n):
        if 0 <= n <= 3:
            return n
        if n == 4:
            return a
        if n == 5:
            return b
        if n == 6:
            return c
        raise ValueError

    i = 0
    output = []
    while True:
        jump = 2

        operation = instructions[i]
        operand = instructions[i+1]
        match operation:
            case 0: # adv
                numer = a
                denom = 1 << combo_operand(operand)
                a = numer / denom
            case 1: # bxl
                b = b ^ operand
            case 2: # bst
                b = combo_operand(operand) % 8
            case 3: # jnz
                if len(output) < len(instructions):
                    solver.add(a != 0)
                    i = operand
                    jump = 0
                else:
                    solver.add(a == 0)
                    break
            case 4: # bxc
                b = b ^ c
            case 5: # out
                out = combo_operand(operand) % 8
                solver.add(out == instructions[len(output)])
                output.append(out)
            case 6: # bdv
                numer = a
                denom = 1 << combo_operand(operand)
                b = numer / denom
            case 7: # cdv
                numer = a
                denom = 1 << combo_operand(operand)
                c = numer / denom
        i += jump


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        registersStr, instructionsStr = f.read().strip().split("\n\n")
        _, B, C = utils.parse_nums(registersStr)
        instructions = utils.parse_nums(instructionsStr)

        s = z3.Solver()
        A = z3.BitVec("a", 64)
        build(s, A, B, C, instructions)

        ans = float("inf")
        while s.check() == z3.sat:
            curr = s.model()[A].as_long()
            ans = min(ans, curr)
            s.add(curr > A)

        print(ans)

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
    filename = utils.get_real_input(17)

part_a(filename)
if not args.skip_b:
    part_b(filename)
