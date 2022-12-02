# Part 1
with open('input/day8.txt', 'r') as f:
    seen = set()
    lines = f.read().splitlines()

    i = 0
    acc = 0
    while i not in seen:
        seen.add(i)

        line = lines[i]
        instr, val = line.split(' ')
        
        if val[0] == '+':
            val = int(val[1:])
        else:
            val = -int(val[1:])

        if instr == 'jmp':
            i += val
        elif instr == 'acc':
            acc += val
            i += 1
        else:
            i += 1

    print(acc)

# Part 2
with open('input/day8.txt', 'r') as f:
    lines = f.read().splitlines()

    for k in range(len(lines)):
        l = lines[k]
        if 'acc' in l:
            continue
        
        instr, val = l.split(' ')
        if instr == 'jmp':
            instr = 'nop'
        else:
            instr = 'jmp'

        lines[k] = instr + ' ' + val

        i = 0
        acc = 0
        seen = set()

        while i not in seen and i < len(lines):
            seen.add(i)

            line = lines[i]
            instr, val = line.split(' ')
            
            if val[0] == '+':
                val = int(val[1:])
            else:
                val = -int(val[1:])

            if instr == 'jmp':
                i += val
            elif instr == 'acc':
                acc += val
                i += 1
            else:
                i += 1

        lines[k] = l
        if i == len(lines):
            print(acc)
            break
