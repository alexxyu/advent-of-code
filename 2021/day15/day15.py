from heapq import heappush, heappop

SIZE_MULT = 1

with open('day15.txt', 'r') as f:
    lines = f.read().splitlines()
    N = len(lines)

    def manhattan_dist(r, c):
        return (SIZE_MULT*N - r) + (SIZE_MULT*N - c)

    grid = [[int(c) for c in line] for line in lines]
    
    heap = [(0, 0, 0)]
    visited = set()
    while True:
        f, r, c = heappop(heap)
        
        if (r, c) in visited:
            continue
        visited.add((r, c))

        if r == SIZE_MULT*len(lines)-1 and c == SIZE_MULT*len(lines)-1:
            print(f)
            break

        for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            r_new = r + i
            c_new = c + j
            if 0 <= r_new < SIZE_MULT*N and 0 <= c_new < SIZE_MULT*N:
                rdiv, cdiv = r_new // N, c_new // N
                f_new = f + ((grid[r_new % N][c_new % N]) + rdiv + cdiv - 1) % 9 + 1
                heappush(heap, (f_new, r_new, c_new))
