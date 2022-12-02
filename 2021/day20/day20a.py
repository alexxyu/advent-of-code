with open('day20.txt', 'r') as f:
    lines = f.read().splitlines()
    algo = list(lines[0])

    lines = lines[2:]
    w, h = len(lines[0]), len(lines)

    pic = []
    for line in lines:
        pic.append((['.'] * 4) + list(line) + (['.'] * 4))
    pic = ([['.'] * (w+8)] * 4) + pic + ([['.'] * (w+8)] * 4)
    
    # for p in pic:
    #     print(p)

    new_pic1 = []
    for i in range(1, len(pic)-1):
        new_pic1.append([])
        for j in range(1, len(pic[i])-1):
            algo_idx = 0
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    algo_idx <<= 1
                    if pic[i+x][j+y] == '#':
                        algo_idx |= 1
            if algo[algo_idx] == '#':
                new_pic1[-1].append('#')
            else:
                new_pic1[-1].append('.')

    new_pic2 = []
    res = 0
    for i in range(1, len(new_pic1)-1):
        new_pic2.append([])
        for j in range(1, len(new_pic1[i])-1):
            algo_idx = 0
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    algo_idx <<= 1
                    if new_pic1[i+x][j+y] == '#':
                        algo_idx |= 1
            if algo[algo_idx] == '#':
                res += 1
                new_pic2[-1].append('#')
            else:
                new_pic2[-1].append('.')

    # for p in new_pic2:
    #     print(p)

    print(res)
