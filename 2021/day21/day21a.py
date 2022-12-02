with open('day21.txt', 'r') as f:
    lines = f.read().splitlines()
    _, p1 = lines[0].split(': ')
    _, p2 = lines[1].split(': ')

    p1, p2 = int(p1), int(p2)

    p1_score, p2_score = 0, 0
    rolls = 0
    die = 0
    while p1_score < 1000 and p2_score < 1000:
        for _ in range(3):
            die = (die % 100) + 1
            p1 += die
            rolls += 1

        p1 = (p1 - 1) % 10 + 1
        p1_score += p1

        if p1_score >= 1000:
            break

        for _ in range(3):
            die = (die % 100) + 1
            p2 += die
            rolls += 1

        p2 = (p2 - 1) % 10 + 1
        p2_score += p2

    print(min(p1_score, p2_score) * rolls)
