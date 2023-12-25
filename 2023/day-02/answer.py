import argparse
from re import search


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().splitlines()
        k = 0
        for i, line in enumerate(lines):
            _, sets = line.split(": ")
            is_sat = True
            for s in sets.split("; "):
                r = search(r"(\d+) red", s) or 0
                if r:
                    r = int(r.group(1))
                g = search(r"(\d+) green", s) or 0
                if g:
                    g = int(g.group(1))
                b = search(r"(\d+) blue", s) or 0
                if b:
                    b = int(b.group(1))
                if not (r <= 12 and g <= 13 and b <= 14):
                    is_sat = False
                    break
            if is_sat:
                k += i + 1
        print(k)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().splitlines()
        k = 0
        for line in lines:
            _, sets = line.split(": ")
            rmax, gmax, bmax = 0, 0, 0
            for s in sets.split("; "):
                r = search(r"(\d+) red", s) or 0
                if r:
                    r = int(r.group(1))
                    rmax = max(rmax, r)
                g = search(r"(\d+) green", s) or 0
                if g:
                    g = int(g.group(1))
                    gmax = max(gmax, g)
                b = search(r"(\d+) blue", s) or 0
                if b:
                    b = int(b.group(1))
                    bmax = max(bmax, b)
            k += rmax * gmax * bmax
        print(k)


parser = argparse.ArgumentParser()
parser.add_argument("filename", help="the input file")
parser.add_argument(
    "-b",
    "--part_b",
    action="store_true",
    help="whether to try part B (default: try part A)",
)
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == "b" else part_a)(filename)
