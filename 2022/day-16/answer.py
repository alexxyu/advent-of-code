import argparse


def part_a(filename):
    print('Trying part a...')
    with open(filename) as f:
        lines = f.read().splitlines()

        valve_rates = dict()
        tunnels = dict()
        for line in lines:
            a, b = line.split('; ')
            src = a[6:8]
            rate = int(a.split('=')[-1])
            valve_rates[src] = rate

            dst = b.split(', ')
            dst[0] = dst[0][-2:]
            tunnels[src] = dst

        mem = dict()
        queue = [('AA', 0, set())]
        for t in range(29, -1, -1):
            N = len(queue)
            for _ in range(N):
                (v, p, s) = queue.pop(0)
                if mem.get(v, -1) >= p:
                    continue
                mem[v] = p

                # I may choose to open the current valve
                if v not in s:
                    queue.append((v, p + (valve_rates[v]*t), s | { v }))

                # Or, I could move to a different valve
                for d in tunnels[v]:
                    queue.append((d, p, s))

        print(max([x[1] for x in queue]))


# My answer to part b is janky but it works... I would clean this up
# if I had the motivation.
def part_b(filename):
    print('Trying part b...')
    with open(filename) as f:
        lines = f.read().splitlines()

        valve_to_idx = dict()
        valve_rates = dict()
        tunnels = dict()
        for line in lines:
            a, b = line.split('; ')
            src = a[6:8]
            rate = int(a.split('=')[-1])
            valve_rates[src] = rate
            valve_to_idx[src] = len(valve_to_idx)

            dst = b.split(', ')
            dst[0] = dst[0][-2:]
            tunnels[src] = dst

        def set_bitmask(n, i):
            return n | (1 << i)

        def is_set(n, i):
            return (n >> i) & 1 == 1

        max_p = 0
        queue = [('AA', 'AA', 0, 0)]
        for t in range(25, -1, -1):
            N = len(queue)
            mem = dict()
            for _ in range(N):
                (v, w, p, s) = queue.pop(0)
                max_p = max(max_p, p)

                # Case 1: Elephant and I both open our valves.
                if v != w and not is_set(s, valve_to_idx[v]) and not is_set(s, valve_to_idx[w]) and valve_rates[v] > 0 and valve_rates[w] > 0:
                    p_t = p + (valve_rates[v] * t) + (valve_rates[w] * t)
                    if mem.get((v, w, s), -1) < p:
                        queue.append((v, w, p_t, set_bitmask(set_bitmask(s, valve_to_idx[v]), valve_to_idx[w])))
                        mem[(v, w, s)] = p

                # Case 2: I open my valve; Elephant moves.
                if not is_set(s, valve_to_idx[v]) and valve_rates[v] > 0:
                    p_t = p + (valve_rates[v] * t)
                    for w_n in tunnels[w]:
                        if mem.get((v, w_n, s), -1) < p:
                            queue.append((v, w_n, p_t, set_bitmask(s, valve_to_idx[v])))
                            mem[(v, w_n, s)] = p

                # Case 3: Elephant opens its valve; I move.
                if not is_set(s, valve_to_idx[w]) and valve_rates[w] > 0:
                    p_t = p + (valve_rates[w] * t)
                    for v_n in tunnels[v]:
                        if mem.get((v_n, w, s), -1) < p:
                            queue.append((v_n, w, p_t, set_bitmask(s, valve_to_idx[w])))
                            mem[(v_n, w, s)] = p

                # Case 4: Elephant and I both move.
                for v_n in tunnels[v]:
                    for w_n in tunnels[w]:
                        if mem.get((v_n, w_n, s), -1) < p:
                            queue.append((v_n, w_n, p, s))
                            mem[((v_n, w_n, s))] = p

            print(t, N, max_p)

        print(max_p)


parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the input file')
parser.add_argument('-b', '--part_b', action='store_true',
                    help='whether to try part B (default: try part A)')
args = parser.parse_args()

filename = args.filename
(part_b if args.part_b or filename[0] == 'b' else part_a)(filename)
