def decode_literal(content):
    literal = ""
    while True:
        first_bit = content[0]
        literal += content[1:5]
        content = content[5:]

        if first_bit == '0':
            break
    return int(literal, 2), content

def decode_packet(packet):
    version = int(packet[:3], 2)
    type_id = int(packet[3:6], 2)

    if type_id == 4:
        _, next = decode_literal(packet[6:])
    else:
        length_type_id = packet[6]
        if length_type_id == 0:
            pass
        elif length_type_id == 1:
            pass
    

with open('day16.txt', 'r') as f:
    line = f.readline().strip()
    packet = bin(int(line, 16))[2:]
    
    print(packet)
