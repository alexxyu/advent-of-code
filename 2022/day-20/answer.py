from __future__ import annotations
import argparse
from dataclasses import dataclass


@dataclass
class Node:
    n: int
    next_node: Node = None
    prev_node: Node = None


def decrypt(nums: Node, t: int = 1, decrypt_key: int = 1) -> int:
    N = len(nums)
    nums = [n * decrypt_key for n in nums]

    # Construct a linked list representing the numbers
    ptr = head = Node(n=nums[0])
    to_visit = [head]
    for n in nums[1:]:
        node = Node(n=n, prev_node=ptr)
        to_visit.append(node)
        ptr.next_node = node
        ptr = node
    ptr.next_node = head
    head.prev_node = ptr

    for _ in range(t):
        # Update the ordering of the nodes according to the order seen
        for curr_node in to_visit:
            n = curr_node.n
            if n == 0:
                continue

            is_forwards = (n > 0)
            n = abs(n)

            # Move the node to its correct position
            ptr = curr_node
            ptr.next_node.prev_node = ptr.prev_node
            ptr.prev_node.next_node = ptr.next_node
            ptr = ptr.next_node
            if is_forwards:
                for _ in range((n-1) % (N-1)):
                    ptr = ptr.next_node
            else:
                for _ in range((n+1) % (N-1)):
                    ptr = ptr.prev_node
            curr_node.prev_node = ptr
            curr_node.next_node = ptr.next_node
            ptr.next_node.prev_node = curr_node
            ptr.next_node = curr_node

    # Find the node with value 0 and calculate the grove coordinates
    ptr = head
    while ptr.n != 0:
        ptr = ptr.next_node

    k = 0
    for _ in range(3):
        for _ in range(1000):
            ptr = ptr.next_node
        k += ptr.n

    return k


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().splitlines()
        nums = list(map(int, lines))
        print(decrypt(nums))


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()
        nums = list(map(int, lines))
        print(decrypt(nums, t=10, decrypt_key=811589153))


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true',
                    help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
