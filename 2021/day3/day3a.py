with open('day3.txt', 'r') as f:
    lines = f.readlines()

    word_length = len(lines[0].strip())
    gamma, epsilon = 0, 0
    for i in range(word_length):
        count_0, count_1 = 0, 0
        for line in lines:
            if line[i] == '0':
                count_0 += 1
            elif line[i] == '1':
                count_1 += 1
        
        if count_0 > count_1:
            gamma = gamma << 1
            epsilon = (epsilon << 1) ^ 1
        elif count_1 > count_0:
            gamma = (gamma << 1) ^ 1
            epsilon = epsilon << 1

    print(epsilon * gamma)
