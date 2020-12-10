import numpy as np

adapters = list(np.loadtxt('input/day10.txt', dtype=int))
adapters.sort()
adapters.append(adapters[-1]+3)

# Part 1
cnt_1 = 0
cnt_3 = 0

curr = 0
for n in adapters:
    if n - curr == 1:
        cnt_1 += 1
    elif n - curr == 3:
        cnt_3 += 1

    curr = n

print(cnt_1 * cnt_3)

# Part 2
adapters.insert(0, 0)
dp = [0] * (len(adapters))
dp[0] = 1
for i in range(1, len(adapters)):
    adapter_i = adapters[i]

    for j in range(max(i-3, 0), i):
        adapter_j = adapters[j]
        diff = adapter_i - adapter_j
        if diff >= 1 and diff <= 3:
            dp[i] += dp[j]

print(dp[-1])
