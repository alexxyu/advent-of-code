import numpy as np

# Part 1
k = 25
p1_ans = 0

nums = np.loadtxt('input/day9.txt', dtype=int)
for i in range(k, len(nums)):
    target = nums[i]

    s = set()
    is_valid = False
    for j in range(i-k, i):
        if target - nums[j] in s:
            is_valid = True
            break
        s.add(nums[j])

    if not is_valid:
        print(target)
        p1_ans = target
        break

# Part 2
curr = nums[0]
start = 0
for i in range(1, len(nums)):
    while curr > p1_ans and start < i-1:
        curr -= nums[start]
        start += 1

    if curr == p1_ans:
        sum_subarray = nums[start:i]
        print(min(sum_subarray) + max(sum_subarray))
        break

    curr += nums[i]