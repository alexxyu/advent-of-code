import argparse
import itertools

import utils
from sympy import Symbol, solve_poly_system


# https://stackoverflow.com/a/41798064
def intersect(pa, va, pb, vb):
    (xa0, ya0), (vxa, vya) = pa, va
    (xb0, yb0), (vxb, vyb) = pb, vb

    try:
        u = (vya * (xa0 - xb0) - vxa * (ya0 - yb0)) / (vxb * vya - vxa * vyb)
        t = (vyb * (xb0 - xa0) - vxb * (yb0 - ya0)) / (vxa * vyb - vxb * vya)
    except ZeroDivisionError:
        return None

    if u < 0 or t < 0:
        return None
    return (xa0 + vxa * t, ya0 + vya * t)


# MIN_VAL = 7
MIN_VAL = 200000000000000
# MAX_VAL = 27
MAX_VAL = 400000000000000


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()
        stones = []
        for line in lines:
            pos, vel = line.split(" @ ")
            pos = tuple(utils.parse_list_nums(pos, ", "))[:2]
            vel = tuple(utils.parse_list_nums(vel, ", "))[:2]
            stones.append((pos, vel))

        in_test_area = 0
        for (p1, v1), (p2, v2) in itertools.combinations(stones, 2):
            p = intersect(p1, v1, p2, v2)
            if p and all(c >= MIN_VAL and c <= MAX_VAL for c in p):
                in_test_area += 1

        print(in_test_area)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().strip().splitlines()

        xm = Symbol("xm")
        ym = Symbol("ym")
        zm = Symbol("zm")
        vxm = Symbol("vxm")
        vym = Symbol("vym")
        vzm = Symbol("vzm")

        equations = []
        symbols = [xm, ym, zm, vxm, vym, vzm]

        # We only need to check the first 3 hailstones. There are 6+x unknowns and 3*x equations
        # provided, where x is the number of hailstones we look at. That means that we just need
        # x=3 hailstones to get 9 equations for 9 unknowns.
        for i, line in enumerate(lines[:3]):
            pos, vel = line.split(" @ ")
            x0, y0, z0 = tuple(utils.parse_list_nums(pos, ", "))
            vx, vy, vz = tuple(utils.parse_list_nums(vel, ", "))

            t = Symbol(f"t{i}")

            # xm + vxm*t = x0 + vx*t
            xt = vx * t + x0 - (xm + vxm * t)
            yt = vy * t + y0 - (ym + vym * t)
            zt = vz * t + z0 - (zm + vzm * t)

            symbols.append(t)
            equations.extend([xt, yt, zt])

        s = solve_poly_system(equations, symbols)
        print(s)
        print(sum(s[0][:3]))


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
    filename = utils.get_real_input(24)

part_a(filename)
if not args.skip_b:
    part_b(filename)
