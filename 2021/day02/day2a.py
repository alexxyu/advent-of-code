with open('day2.txt', 'r') as f:
    lines = f.readlines()
    hor_pos, depth = 0, 0

    for line in lines:
        cmd, amt = line.split()
        if cmd == 'forward':
            hor_pos += int(amt)
        elif cmd == 'up':
            depth -= int(amt)
        elif cmd == 'down':
            depth += int(amt)
        else:
            print(f'invalid command: {cmd}')

    print(hor_pos * depth)
