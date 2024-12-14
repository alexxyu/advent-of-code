import argparse
from collections import *
from copy import deepcopy
from typing import *

import utils


def generate_rules(rules: list[str]) -> defaultdict[str, set[str]]:
    deps = defaultdict(set)
    for rule in rules:
        lhs, rhs = rule.split("|")
        deps[rhs].add(lhs)
    return deps


def is_valid(deps: defaultdict[str, set[str]], pages: list[str]) -> bool:
    seen = set()
    for p in pages:
        seen.add(p)
        if any(n in pages and n not in seen for n in deps[p]):
            return False

    return True

def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        rules, updates = f.read().strip().split("\n\n")
        deps = generate_rules(rules.split("\n"))

        s = 0
        for update in updates.split("\n"):
            pages = update.split(",")
            if is_valid(deps, pages):
                s += int(pages[len(pages) // 2])
        print(s)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        rules, updates = f.read().strip().split("\n\n")
        deps = generate_rules(rules.split("\n"))

        s = 0
        for update in updates.split("\n"):
            pages = update.split(",")

            if not is_valid(deps, update.split(",")):
                depscopy = deepcopy(deps)
                for n in depscopy:
                    r = [p for p in depscopy[n] if p not in pages]
                    for k in r:
                        depscopy[n].remove(k)

                b = []
                while len(b) < len(pages):
                    for p in pages:
                        if p not in b and len(depscopy[p]) == 0:
                            b.append(p)
                            for n in depscopy:
                                if p in depscopy[n]:
                                    depscopy[n].remove(p)

                s += int(b[len(b) // 2])

        print(s)



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
    filename = utils.get_real_input(5)

part_a(filename)
if not args.skip_b:
    part_b(filename)
