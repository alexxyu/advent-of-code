import numpy as np

data = np.loadtxt('input/day1.txt')

# Part 1
entries = set()
for n in data:
    if (2020 - n) in entries:
        print(n * (2020 - n))
        break
    entries.add(n)

# Part 2
data.sort()
for i in range(len(data)-2):
    j = i+1
    k = len(data)-1
    while j < k and j < len(data):
        sum = data[i] + data[j] + data[k]
        if sum == 2020:
            print(data[i] * data[j] * data[k])
            break
        elif sum > 2020:
            k -= 1
        else:
            j += 1
