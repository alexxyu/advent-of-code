with open('day2.txt', 'r') as f:
    lines = f.readlines()
    hor_pos, depth, aim = 0, 0, 0

    for line in lines:
        cmd, amt = line.split()
        if cmd == 'forward':
            hor_pos += int(amt)
            depth += int(amt) * aim
        elif cmd == 'up':
            aim -= int(amt)
        elif cmd == 'down':
            aim += int(amt)
        else:
            print(f'invalid command: {cmd}')

    print(hor_pos * depth)
