TARGET_TURN = 2020

with open('input/day15.txt', 'r') as f:
    line = f.read().splitlines()[0]
    nums = [int(n) for n in line.split(',')]

    d = {}
    for i, n in enumerate(nums[:-1]):
        d[n] = i+1

    last_num = nums[-1]
    for i in range(len(nums)+1, TARGET_TURN+1):
        if last_num not in d.keys():
            # Last num was spoken for the first time
            d[last_num] = (i-1)
            last_num = 0
        else:
            # Last num was not spoken for the first time
            age = (i-1) - d[last_num]
            d[last_num] = (i-1)
            last_num = age

    print(last_num)
