SEG_COUNT_TO_DIGIT = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [6, 9],
    7: [8]
}

with open('day8.txt', 'r') as f:
    lines = f.read().splitlines()

    # seg_map = dict({c: set(j for j in range(10)) for c in ['a', 'b', 'c', 'd', 'e', 'f', 'g']})
    seg_map = dict({c: set() for c in ['a', 'b', 'c', 'd', 'e', 'f', 'g']})
    for line in lines:
        lhs, rhs = line.split(' | ')

        digits = lhs.split()
        for digit in digits:
            seg_count = len(digit)
            if seg_count in SEG_COUNT_TO_DIGIT:
                for seg in digit:
                    seg_map[seg].add(SEG_COUNT_TO_DIGIT[seg_count])
            else:


    print(res)
