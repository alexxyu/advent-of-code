import argparse

import utils


def hash_word(word):
    h = 0
    for c in word:
        h += ord(c)
        h *= 17
        h %= 256
    return h


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        seq = f.read().splitlines()[0]
        s = sum(hash_word(word) for word in seq.split(","))
        print(s)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        seq = f.read().splitlines()[0]
        boxes = [[] for _ in range(256)]
        lenses = set()
        for word in seq.split(","):
            if "=" in word:
                label = word[: word.index("=")]
                h = hash_word(label)
                fp = int(word[-1])

                if label in lenses:
                    box = boxes[h]
                    for i, (b, _) in enumerate(box):
                        if b == label:
                            box[i] = (label, fp)
                            break
                else:
                    boxes[h].append((label, fp))
                    lenses.add(label)
            else:
                label = word[:-1]
                h = hash_word(label)
                box = boxes[h]

                for i, (b, _) in enumerate(box):
                    if b == label:
                        boxes[h] = box[:i] + box[i + 1:]
                        lenses.remove(b)
                        break

        s = 0
        for i, box in enumerate(boxes):
            for j, (_, fp) in enumerate(box):
                s += (i + 1) * (j + 1) * fp

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
    filename = utils.get_real_input(15)

part_a(filename)
if not args.skip_b:
    part_b(filename)
