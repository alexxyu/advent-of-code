with open('day8.txt', 'r') as f:
    lines = f.read().splitlines()

    res = 0
    for line in lines:
        _, rhs = line.split(' | ')

        digits = rhs.split()
        for digit in digits:
            if 2 <= len(digit) <= 4 or len(digit) == 7:
                res += 1

    print(res)
