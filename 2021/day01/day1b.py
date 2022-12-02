with open('day1.txt', 'r') as f:
    lines = f.readlines()
    prev_readings = [int(lines[0]), int(lines[1]), int(lines[2])]
    res = 0

    for line in lines[3:]:
        reading = int(line)
        next_readings = prev_readings[1:] + [reading]
        if sum(next_readings) > sum(prev_readings):
            res += 1

        prev_readings = next_readings

    print(res)
