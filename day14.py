N_BITS = 36

# Part 1
with open('input/day14.txt', 'r') as f:
    lines = f.read().splitlines()

    mask = ""
    arr = dict()

    for line in lines:
        if 'mask' in line:
            mask = line.split(' = ')[1]
        else:
            parts = line.split(' = ')

            addr = parts[0]
            addr = int(addr[addr.find('[')+1:addr.find(']')])
            val = int(parts[1])

            bits = [(val >> b) & 1 for b in range(N_BITS)]
            bits = bits[::-1]

            new_val = 0
            for i in range(N_BITS):
                new_val <<= 1
                bitop = mask[i]
                if bitop == 'X':
                    new_val += bits[i]
                elif bitop == '1':
                    new_val += 1
                elif bitop == '0':
                    pass

            arr[addr] = new_val

    s = sum(arr.values())
    print(s)

# Part 2
def decode(s: set, bits, mask, curr, i):
    if i == N_BITS:
        s.add(curr)
        return
    
    curr <<= 1
    bitop = mask[i]
    if bitop == 'X':
        decode(s, bits, mask, curr, i+1)
        decode(s, bits, mask, curr+1, i+1)
    elif bitop == '1':
        decode(s, bits, mask, curr+1, i+1)
    elif bitop == '0':
        decode(s, bits, mask, curr+bits[i], i+1)

with open('input/day14.txt', 'r') as f:
    lines = f.read().splitlines()

    mask = ""
    arr = dict()

    for line in lines:
        if 'mask' in line:
            mask = line.split(' = ')[1]
        else:
            parts = line.split(' = ')

            addr = parts[0]
            addr = int(addr[addr.find('[')+1:addr.find(']')])
            val = int(parts[1])

            bits = [(addr >> b) & 1 for b in range(N_BITS)]
            bits = bits[::-1]

            all_vals = set()
            decode(all_vals, bits, mask, 0, 0)

            for decoded_addr in list(all_vals):
                arr[decoded_addr] = val

    s = sum(arr.values())
    print(s)
