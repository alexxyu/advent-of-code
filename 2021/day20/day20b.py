n = 50

def enhance(pic, algo):
    enhanced_pic = []

    for i in range(1, len(pic)-1):
        enhanced_pic.append([])
        for j in range(1, len(pic[i])-1):
            algo_idx = 0
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    algo_idx <<= 1
                    if pic[i+x][j+y] == '#':
                        algo_idx |= 1
            if algo[algo_idx] == '#':
                enhanced_pic[-1].append('#')
            else:
                enhanced_pic[-1].append('.')

    return enhanced_pic

with open('day20.txt', 'r') as f:
    lines = f.read().splitlines()
    algo = list(lines[0])

    lines = lines[2:]
    w, h = len(lines[0]), len(lines)

    pic = []
    for line in lines:
        pic.append((['.'] * (2*n)) + list(line) + (['.'] * (2*n)))
    pic = ([['.'] * (w+(4*n))] * (2*n)) + pic + ([['.'] * (w+(4*n))] * (2*n))
    
    for _ in range(n):
        enhanced_pic = enhance(pic, algo)
        pic = enhanced_pic

    res = 0
    for p in pic:
        for c in p:
            if c == '#':
                res += 1

    print(res)
