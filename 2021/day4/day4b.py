import numpy as np

def update_board(board, n):
    bingo = False
    for board_set in board:
        if n in board_set:
            board_set.remove(n)
        if len(board_set) == 0:
            bingo = True
    return bingo

with open('day4.txt', 'r') as f:
    lines = f.read().splitlines()

    numbers = lines[0].split(',')
    numbers = [int(n) for n in numbers]

    lines = lines[2:]
    boards = []
    while len(lines) >= 5:
        board = lines[:5]
        board = [[int(c) for c in row.split()] for row in board]

        board_sets = [set(row) for row in board]
        board_sets.extend([set(col) for col in np.transpose(board)])

        boards.append(board_sets)
        lines = lines[6:]

    i = 0
    last_board = None
    while len(boards) > 0:
        n = numbers[i]
        next_boards = []
        for board in boards:
            bingo = update_board(board, n)
            if not bingo:
                next_boards.append(board)
            else:
                last_board = board
        boards = next_boards
        i += 1

    s = set()
    for board_set in last_board:
        for k in board_set:
            s.add(k)

    print(sum(s) * numbers[i-1])
    