import copy

with open('day3.txt', 'r') as f:
    lines = f.read().splitlines()
    word_length = len(lines[0].strip())
    
    o2_group = copy.deepcopy(lines)
    co2_group = copy.deepcopy(lines)
    for i in range(word_length):
        o2_group0, o2_group1 = [], []
        for r in o2_group:
            if r[i] == '0':
                o2_group0.append(r)
            elif r[i] == '1':
                o2_group1.append(r)
        o2_group = max(o2_group1, o2_group0, key=lambda x: len(x))
        # print(o2_group)

        co2_group0, co2_group1 = [], []
        for r in co2_group:
            if r[i] == '0':
                co2_group0.append(r)
            elif r[i] == '1':
                co2_group1.append(r)

        if co2_group0 == []:
            co2_group = co2_group1
        elif co2_group1 == []:
            co2_group = co2_group0
        else:
            co2_group = min(co2_group0, co2_group1, key=lambda x: len(x))
        
    print(int(o2_group[0], 2) * int(co2_group[0], 2))
