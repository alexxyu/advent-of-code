import argparse
import itertools
from collections import Counter
from dataclasses import dataclass
from enum import Enum
from functools import cmp_to_key

import utils

CARD_VALUES = "AKQJT987654321"


class Hand(Enum):
    HighCard = 1
    OnePair = 2
    TwoPair = 3
    ThreeKind = 4
    FullHouse = 5
    FourKind = 6
    FiveKind = 7


def cmp_val(a, b):
    if a == b:
        return 0
    return CARD_VALUES.index(b) - CARD_VALUES.index(a)


def get_hand(hand):
    counts = dict(Counter(hand)).values()
    if len([x for x in counts if x == 5]) > 0:
        return Hand.FiveKind
    if len([x for x in counts if x == 4]) > 0:
        return Hand.FourKind
    if (
        len([x for x in counts if x == 3]) > 0
        and len([x for x in counts if x == 2]) > 0
    ):
        return Hand.FullHouse
    if len([x for x in counts if x == 3]) > 0:
        return Hand.ThreeKind
    if len([x for x in counts if x == 2]) > 1:
        return Hand.TwoPair
    if len([x for x in counts if x == 2]) > 0:
        return Hand.OnePair
    return Hand.HighCard


def cmp_hand(hand1: str, hand2: str):
    v1 = get_hand(hand1)
    v2 = get_hand(hand2)

    if v1 == v2:
        for a, b in zip(hand1, hand2, strict=False):
            if (c := cmp_val(a, b)) != 0:
                return c
        return 0
    return v1.value - v2.value


def part_a(filename):
    print("Trying part a...")
    with open(filename) as f:
        lines = f.read().splitlines()
        hands = {}
        for line in lines:
            h, v = line.split()
            hands[h] = int(v)

        w = 0
        sorted_hands = sorted(hands.keys(), key=cmp_to_key(cmp_hand))
        for i, h in enumerate(sorted_hands):
            w += (i + 1) * hands[h]
        print(w)


@dataclass(frozen=True)
class HandWithJoker:
    best_hand: str
    orig_hand: str


def cmp_val_with_joker(a, b):
    if a == b:
        return 0
    if a == "J":
        return -1
    if b == "J":
        return 1

    return CARD_VALUES.index(b) - CARD_VALUES.index(a)


def cmp_hand_with_jokers(hand1: HandWithJoker, hand2: HandWithJoker):
    v1 = get_hand(hand1.best_hand)
    v2 = get_hand(hand2.best_hand)

    if v1 == v2:
        for a, b in zip(hand1.orig_hand, hand2.orig_hand, strict=False):
            if (c := cmp_val_with_joker(a, b)) != 0:
                return c
        return 0
    return v1.value - v2.value


def get_best_hand(hand: str):
    if "J" not in hand:
        return HandWithJoker(hand, hand)

    js = [i for i in range(len(hand)) if hand[i] == "J"]
    k = itertools.product(CARD_VALUES.replace("J", ""), repeat=len(js))

    hand_arr = list(hand)
    best_hand = "".join(hand_arr)
    for combo in k:
        for i, c in zip(js, combo, strict=False):
            hand_arr[i] = c
        curr_hand = "".join(hand_arr)
        if (
            cmp_hand_with_jokers(
                HandWithJoker(curr_hand, hand), HandWithJoker(best_hand, hand)
            )
            > 0
        ):
            best_hand = curr_hand
    return HandWithJoker(best_hand, hand)


def part_b(filename):
    print("Trying part b...")
    with open(filename) as f:
        lines = f.read().splitlines()
        hands = {}
        for line in lines:
            h, v = line.split()
            hands[get_best_hand(h)] = int(v)

        w = 0
        sorted_hands = sorted(hands.keys(), key=cmp_to_key(cmp_hand_with_jokers))
        for i, h in enumerate(sorted_hands):
            w += (i + 1) * hands[h]
        print(w)


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
    filename = utils.get_real_input(7)

part_a(filename)
if not args.skip_b:
    part_b(filename)
