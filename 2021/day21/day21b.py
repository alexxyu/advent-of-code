from functools import lru_cache

with open('day21.txt', 'r') as f:
    lines = f.read().splitlines()
    _, p1 = lines[0].split(': ')
    _, p2 = lines[1].split(': ')

    p1, p2 = int(p1), int(p2)

    @lru_cache(maxsize=None)
    def find_wins(p1, p2, p1_score, p2_score):
        if p2_score >= 21:
            return 0, 1
        
        p1_wins, p2_wins = 0, 0
        for move, ways in [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]:
            p1_next = (p1 + move - 1) % 10 + 1
            w2, w1 = find_wins(p2, p1_next, p2_score, p1_score + p1_next)
            p1_wins += w1 * ways
            p2_wins += w2 * ways
        return p1_wins, p2_wins

    print(max(find_wins(p1, p2, 0, 0)))
