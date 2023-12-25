import argparse

from regex import findall


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().splitlines()
        s = 0
        for line in lines:
            d = list(filter(lambda x: x.isdigit(), line))
            s += int(d[0] + d[-1])
        print(s)


WORD_TO_NUM = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().splitlines()
        ok = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        ] + [str(x) for x in range(1, 10)]
        s = 0
        for line in lines:
            matches = findall("|".join(ok), line, overlapped=True)
            d = [WORD_TO_NUM[x] for x in matches]
            s += d[0] * 10 + d[-1]
        print(s)


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
