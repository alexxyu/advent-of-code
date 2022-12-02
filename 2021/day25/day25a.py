import copy

with open('day25.txt', 'r') as f:
    state = f.read().splitlines()
    state = [list(s) for s in state]
    M, N = len(state), len(state[0])

    turn = 0
    while True:
        orig_state = copy.deepcopy(state)
        next_state = copy.deepcopy(state)
        for r in range(M):
            for c in range(N):
                if state[r][c] == '>':
                    c_next = (c+1) % N
                    if state[r][c_next] == '.':
                        next_state[r][c_next] = '>'
                        next_state[r][c] = '.'
                    
        state = next_state
        next_state = copy.deepcopy(next_state)
        for r in range(M):
            for c in range(N):
                if state[r][c] == 'v':
                    r_next = (r+1) % M
                    if state[r_next][c] == '.':
                        next_state[r_next][c] = 'v'
                        next_state[r][c] = '.'

        turn += 1

        if next_state == orig_state:
            break
        state = next_state

    print(turn)
