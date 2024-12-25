import argparse
import random
from collections import *
from typing import *

import utils

# Add pairs to swap as you find them via inspection.
SWAP_PAIRS = [
    ("bjm", "z07"),
    ("z13", "hsw"),
    ("z18", "skf"),
]

SWAPS = dict(SWAP_PAIRS) | {b: a for a, b in SWAP_PAIRS}

# Use the --random-flip flag to randomly flip bits in the input value. This is a hacky way to find any further swaps
# that don't appear in the original input.
ENABLE_RANDOM_FLIP = False


def filter_bits(regs: Dict[str, int], prefix: str) -> Dict[str, int]:
    return {k: v for k, v in regs.items() if k.startswith(prefix)}


def bits_to_str(regs: Dict[str, int], prefix: str) -> str:
    bits = filter_bits(regs, prefix)
    return "".join(str(v) for _, v in sorted(bits.items(), reverse=True))


def calculate_sum(regs: Dict[str, int], equations: List[str], swaps=None) -> str:
    left = set(equations)
    while len(left) > 0:
        done = set()
        for eq in left:
            lhs, rhs = eq.split(" -> ")
            a, op, b = lhs.split()
            if a not in regs or b not in regs:
                continue
            if swaps and rhs in swaps:
                rhs = swaps[rhs]

            match op:
                case "AND":
                    regs[rhs] = regs[a] & regs[b]
                case "OR":
                    regs[rhs] = regs[a] | regs[b]
                case "XOR":
                    regs[rhs] = regs[a] ^ regs[b]
                case _:
                    pass
            done.add(eq)
        left -= done

    return bits_to_str(regs, "z")


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        inputs, eqs = [s.splitlines() for s in f.read().strip().split("\n\n")]
        regs = {}
        for i in inputs:
            lhs, rhs = i.split(": ")
            regs[lhs] = int(rhs)

        s = calculate_sum(regs, eqs)
        print(int(s, 2))


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        """
        *********************
        * Half-adder design *
        *********************
        z[i] = x[i] ^ y[i]
        c[i] = x[i] & y[i]

        *********************
        * Full-adder design *
        *********************
        - xor[i] = x[i] ^ y[i]
        - tmp[i] = xors[i] & c[i-1]
        - and[i] = x[i] & y[i]
        - c[i] = tmp[i] | and[i]
        - z[i] = xor[i] ^ c[i-1]
        """

        random.seed(0)
        inputs, equations = [s.splitlines() for s in f.read().strip().split("\n\n")]
        regs = {}
        for i in inputs:
            lhs, rhs = i.split(": ")

            r = int(rhs)
            if ENABLE_RANDOM_FLIP and lhs.startswith("x") and random.random() < 0.5:  # noqa: S311
                r = 1 - r
            regs[lhs] = r

        x = bits_to_str(regs, "x")
        y = bits_to_str(regs, "y")
        ztarget = str(bin(int(x, 2) + int(y, 2)))[2:]

        zreal = calculate_sum(regs, equations, swaps=SWAPS)

        mlen = max(len(zreal), len(ztarget))
        zreal = zreal.zfill(mlen)
        ztarget = ztarget.zfill(mlen)
        diffs = {i for i, (a, b) in enumerate(zip(reversed(ztarget), reversed(zreal), strict=True)) if a != b}

        # No closed form solution for today. Instead, we'll create a graph visualization
        # (see https://dreampuf.github.io/GraphvizOnline) of the given equations, and label any z
        # nodes that are differ from the expected bit. We can then manually inspect the graph to
        # determine the correct pairs of gates to swap one by one.
        with open("graph.dot", "w") as g:
            g.write("digraph G {\n")

            for i in range(mlen):
                g.write(f'\t"z{str(i).zfill(2)}" [color="{"red" if i in diffs else "green"}",style="filled"];\n')
            g.write("\n")

            for eq in equations:
                lhs, rhs = eq.split(" -> ")
                a, op, b = lhs.split()
                res = f"{a} {op} {b}"

                if rhs in SWAPS:
                    rhs = SWAPS[rhs]

                g.write(f'\t"{a}" -> "{res}";\n')
                g.write(f'\t"{b}" -> "{res}";\n')
                g.write(f'\t"{res}" [shape="diamond", label="{op}"];\n')
                g.write(f'\t"{res}" -> "{rhs}";\n')

            g.write("}")

        print(",".join(sorted(SWAPS.keys())))


parser = argparse.ArgumentParser()
parser.add_argument(
    "filename",
    help="the input file, will default to actual AoC input if omitted",
    type=str,
    nargs="?",
    default=None,
)
parser.add_argument("--skip-a", help="skip running part a", action="store_true")
parser.add_argument("--skip-b", help="skip running part b", action="store_true")
parser.add_argument("--random-flip", help="randomly flip bits in input value", action="store_true")
args = parser.parse_args()

ENABLE_RANDOM_FLIP = args.random_flip

filename = args.filename
if not args.filename:
    filename = utils.get_real_input(24)

if not args.skip_a:
    part_a(filename)
if not args.skip_b:
    part_b(filename)
