with open('day1.txt', 'r') as f:
    lines = f.readlines()
    prev_reading = int(lines[0])
    res = 0

    for line in lines[1:]:
        reading = int(line)
        if reading > prev_reading:
            res += 1

        prev_reading = reading

    print(res)
