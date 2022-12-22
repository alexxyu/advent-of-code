import argparse
import re
from math import *
from copy import deepcopy
from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class State:
    time: int = 0
    resources: List[int] = field(default_factory=lambda: [0, 0, 0, 0])
    robots: List[int] = field(default_factory=lambda: [1, 0, 0, 0])


def update_state(state: State, dt: int):
    state.time += dt
    for i in range(len(state.resources)):
        state.resources[i] += state.robots[i] * dt


def try_to_create_robot(state: State, costs: List[Tuple[int]], r: int, T: int, max_geodes: int = 0):
    time_left = T - state.time
    if time_left <= 1:
        # Heuristic #1: If there's less than 2 units of time left, there's no point in building anything
        return None
    if r == 3 and state.resources[r] + time_left*state.robots[r] + sum([t for t in range(time_left)]) < max_geodes:
        # Heuristic #2: We shouldn't consider this state if, hypothetically, we were able to create a
        # geode robot every minute but still wouldn't produce as many geodes as the best plan thus far
        return None
    if r < 3 and state.resources[r] + time_left*state.robots[r] >= time_left * max(c[r] for c in costs):
        # Heuristic #3: For any non-geode robots for resource R, there isn't any point in creating more
        # of these robots if, hypothetically, we would have enough to spend as much R as possible to build
        # robots in the remaining time
        return None

    cost = costs[r]
    next_state = deepcopy(state)

    if all([rsc >= cst for rsc, cst in zip(state.resources, cost)]):
        # Case 1: We have the necessary amount of resources to build the robot
        update_state(next_state, 1)
    elif all([rbt > 0 for rbt, cst in zip(state.robots, cost) if cst > 0]):
        # Case 2: We can wait for our existing robots to produce the resources needed to build the robot
        needed_time = max(
            [ceil((cst - rsc) / rbt) for rsc, rbt,
             cst in zip(state.resources, state.robots, cost) if cst > 0]
        )
        update_state(next_state, needed_time + 1)
        if next_state.time > T:
            return None
    else:
        # Case 3: We have to build other robots to produce the necessary resources first
        return None

    for i, c in enumerate(cost):
        next_state.resources[i] -= c
    next_state.robots[r] += 1
    return next_state


def simulate(costs, T):
    q = [State()]
    max_geodes = 0
    while q:
        curr_state = q.pop()
        time_left = T - curr_state.time
        if time_left == 0:
            max_geodes = max(max_geodes, curr_state.resources[-1])
            continue

        # Option 1: Don't make any new robots
        next_state = deepcopy(curr_state)
        update_state(next_state, time_left)
        q.append(next_state)

        # Options 2-5: Wait and try to make a robot
        for i in range(len(costs)):
            if next_state := try_to_create_robot(curr_state, costs, i, T, max_geodes):
                q.append(next_state)

    return max_geodes


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().splitlines()
        N = 0
        for blueprint in lines:
            i, a, b, c, d, e, f = map(int, re.findall(r'\d+', blueprint))
            costs = [
                (a, 0, 0, 0),
                (b, 0, 0, 0),
                (c, d, 0, 0),
                (e, 0, f, 0),
            ]
            N += i * simulate(costs, 24)
        print(N)


def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()
        k = []
        for blueprint in lines[:3]:
            _, a, b, c, d, e, f = map(int, re.findall(r'\d+', blueprint))
            costs = [
                (a, 0, 0, 0),
                (b, 0, 0, 0),
                (c, d, 0, 0),
                (e, 0, f, 0),
            ]
            k.append(simulate(costs, 32))
        print(k, '=>', prod(k))


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true',
                    help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
