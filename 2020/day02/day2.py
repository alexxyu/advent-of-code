n_valid = 0

# Part 1
with open('input/day2.txt', 'r') as f:
    for entry in f:
        parts = entry.split(' ')

        range_low, range_hi = parts[0].split('-')
        range_low = int(range_low)
        range_hi = int(range_hi)

        letter = parts[1][0]
        password = parts[2]

        cnt = 0
        for c in password:
            if c == letter:
                cnt += 1

        if cnt >= range_low and cnt <= range_hi:
            n_valid += 1

print(n_valid)

# Part 2
n_valid = 0

with open('input/day2.txt', 'r') as f:
    for entry in f:
        parts = entry.split(' ')

        pos_lo, pos_hi = parts[0].split('-')
        pos_lo = int(pos_lo)-1
        pos_hi = int(pos_hi)-1

        letter = parts[1][0]
        password = parts[2]

        if (password[pos_lo] == letter and password[pos_hi] != letter) or (password[pos_hi] == letter and password[pos_lo] != letter):
            n_valid += 1

print(n_valid)