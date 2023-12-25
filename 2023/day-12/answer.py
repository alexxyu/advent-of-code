import argparse
import itertools
from functools import lru_cache

import utils


def matches(pattern, counts):
    splits = [len(p) for p in pattern.split(".") if len(p) != 0]
    return splits == counts


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().splitlines()
        s = 0
        for line in lines:
            pattern, counts = line.split()
            counts = utils.parse_list_nums(counts, sep=",")

            questions = []
            for i, c in enumerate(pattern):
                if c == "?":
                    questions.append(i)

            test = list(pattern)
            combinations = itertools.product(".#", repeat=len(questions))
            for combo in combinations:
                for i, c in zip(questions, combo, strict=False):
                    test[i] = c
                if matches("".join(test), counts):
                    s += 1
        print(s)


@lru_cache
def count(pattern, counts):
    if len(counts) == 0:
        return all(c in ".?" for c in pattern)

    s = 0
    curr, rem = counts[0], counts[1:]
    min_len_of_rem = sum(rem) + len(rem) + curr - 1
    for offset in range(len(pattern) - min_len_of_rem):
        test = f"{'.' * offset}{'#' * curr}."
        if all(a == "?" or a == b for a, b in zip(pattern[: len(test)], test, strict=False)):
            s += count(pattern[len(test):], rem)

    return s


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().splitlines()
        s = 0
        for line in lines:
            pattern, counts = line.split()
            counts = utils.parse_list_nums(counts, sep=",")

            pattern = "?".join([pattern] * 5)
            counts *= 5

            s += count(tuple(pattern), tuple(counts))
        print(s)


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
args = parser.parse_args()

filename = args.filename
if not args.filename:
    filename = utils.get_real_input(12)

if not args.skip_a:
    part_a(filename)
if not args.skip_b:
    part_b(filename)
