def read_hex(filename):
    with open(filename, 'r') as file:
        return file.read().replace('\n', '')

def to_bin(hex):
    h_size = len(hex) * 4
    return (bin(int(hex, 16))[2:] ).zfill(h_size)

def to_dec(binary):
    return int(binary, 2)

def log(message, indentation):
  print("  "*indentation + message)
  pass

def apply_value(left, op_type_id, value):
    if left is None:
        return value
    if op_type_id == 0:
        return left + value
    elif op_type_id == 1:
        if left == 0 or value == 0:
            return 0
        return left * value
    elif op_type_id == 2:
        return min(left, value)
    elif op_type_id == 3: 
        return max(left, value)
    elif op_type_id == 5:
        return 1 if left > value else 0
    elif op_type_id == 6:
        return 1 if left < value else 0
    elif op_type_id == 7:
        return 1 if left == value else 0

def get_literal_value(packet, level):
    payload = packet[6:]
    offset = 0
    value = ""

    value += payload[offset + 1:offset + 5]
    log("Extracted value part from literal: " + value, level)
    while payload[offset] == "1":
        offset += 5
        value += payload[offset + 1:offset + 5]
        log("Extended value part from literal to: " + value, level)
    log("Literal consumed: " + str(6 + offset + 5), level)
    return to_dec(value), 6 + offset + 5

def parse_packet(data, level):
    version = to_dec(data[:3])
    log("Packet version: " + str(version), level)
    version_sum = version
    type_id = to_dec(data[3:6])
    log("Packet type id: " + str(type_id), level)

    if type_id == 4:
        [value, length] = get_literal_value(data, level)
    else:
        [value, length, part_version_sum] = handle_operator(data, level)
        version_sum += part_version_sum
    return length, version_sum, value

def op_log(operands, op_type_id, value):
    operands = [str(op) for op in operands]
    value = str(value)
    if op_type_id == 0:
        print('+'.join(operands) + ' = ' + value)
    if op_type_id == 1:
        print('*'.join(operands) + ' = ' + value)
    if op_type_id == 2:
        print('min(' + ','.join(operands) + ') = ' + value)
    if op_type_id == 3:
        print('max(' + ','.join(operands) + ') = ' + value)
    if op_type_id == 5:
        print(operands[0] + '>' + operands[1] + ' = ' + value)
    if op_type_id == 6:
        print(operands[0] + '<' + operands[1] + ' = ' + value)
    if op_type_id == 7:
        print(operands[0] + '==' + operands[1] + ' = ' + value)

def handle_operator(payload, level):
    op_type_id = to_dec(payload[3:6])
    log("Operator type_id: " + str(op_type_id), level)
    length_type_id = payload[6]
    log("Handling operator, length type id: " + str(length_type_id), level)
    payload = payload[7:]

    data_length = 15
    nbr_of_sub = float('inf')
    total_length_in_bits = float('inf')
    if length_type_id == "0":
        total_length_in_bits = to_dec(payload[:data_length])
        log("Total length in bits: " + str(total_length_in_bits), level)
    if length_type_id == "1":
        data_length = 11
        nbr_of_sub = to_dec(payload[:data_length])
        log("Nbr sub packages: " + str(nbr_of_sub), level)

    offset = data_length
    consumed_packages = 0
    consumed_length = 0
    part_version_sum = 0
    left = None
    operands = []
    while total_length_in_bits > consumed_length and nbr_of_sub > consumed_packages:
        [length, packet_version_sum, value] = parse_packet(payload[offset:], level + 1)
        operands.append(value)
        part_version_sum += packet_version_sum
        consumed_length += length
        consumed_packages += 1
        offset += length
        left = apply_value(left, op_type_id, value)
#    op_log(operands, op_type_id, left)
    return left, 6 + 1 + data_length + consumed_length, part_version_sum

def run(filename):
    _, version_sum, value = parse_packet(to_bin(read_hex(filename)), 1)
    print("Version sum: " + str(version_sum))
    print("Value: " + str(value))
    return version_sum, value

def test_version(filename, expected_length):
    log("Testing version for: " + filename, 0)
    version_sum, _ = run(filename)
    assert version_sum == expected_length

def test_value(filename, expected_value):
    log("Testing value for: " + filename, 0)
    _, value = run(filename)
    assert value == expected_value

#test_version('./examples/version/operator-9.txt', 9)
#test_version('./examples/version/operator-14.txt', 14)
#test_version('./examples/version/literal-6.txt', 6)
#test_version('./examples/version/operator-16.txt', 16)
#test_version('./examples/version/operator-12.txt', 12)
#test_value('./examples/value/1-3.txt', 3)
#test_value('./examples/value/2-54.txt', 54)
#test_value('./examples/value/3-7.txt', 7)
#test_value('./examples/value/4-9.txt', 9)
#test_value('./examples/value/5-1.txt', 1)
#test_value('./examples/value/6-0.txt', 0)
#test_value('./examples/value/7-0.txt', 0)
#test_value('./examples/value/8-1.txt', 1)
run('./input.txt')
