import struct


def parse_data(data):
    signature = data[:4]
    if signature != b'UBX\n':
        raise ValueError("Invalid signature")

    result = {}

    # Parse Structure A
    result['A1'] = parse_structure_b(data, struct.unpack('<H', data[4:6])[0])
    result['A2'] = struct.unpack('<B', data[6:7])[0]
    result['A3'] = parse_structure_c(data, struct.unpack('<H', data[7:9])[0])
    result['A4'] = struct.unpack('<h', data[9:11])[0]
    size_a5, addr_a5 = struct.unpack('<II', data[11:19])
    result['A5'] = list(struct.unpack(
        f'<{size_a5}i', data[addr_a5:addr_a5 + size_a5 * 4]))
    result['A6'] = parse_structure_e(data, 19)

    return result


def parse_structure_b(data, offset):
    result = {}
    result['B1'] = struct.unpack('<5s', data[offset:offset + 5])[0].decode()
    result['B2'] = struct.unpack('<h', data[offset + 5:offset + 7])[0]
    result['B3'] = struct.unpack('<I', data[offset + 7:offset + 11])[0]
    result['B4'] = struct.unpack('<i', data[offset + 11:offset + 15])[0]
    result['B5'] = struct.unpack('<Q', data[offset + 15:offset + 23])[0]
    return result


def parse_structure_c(data, offset):
    result = {}
    result['C1'] = struct.unpack('<d', data[offset:offset + 8])[0]
    size_c2, addr_c2 = struct.unpack('<HH', data[offset + 8:offset + 12])
    result['C2'] = [parse_structure_d(data, addr) for addr in
                    struct.unpack(
                        f'<{size_c2}I', data[addr_c2:addr_c2 + size_c2 * 4])]
    result['C3'] = struct.unpack('<d', data[offset + 12:offset + 20])[0]
    size_c4, addr_c4 = struct.unpack('<IH', data[offset + 20:offset + 26])
    result['C4'] = list(struct.unpack(
        f'<{size_c4}B', data[addr_c4:addr_c4 + size_c4]))
    result['C5'] = struct.unpack('<q', data[offset + 26:offset + 34])[0]
    return result


def parse_structure_d(data, offset):
    result = {}
    result['D1'] = struct.unpack('<i', data[offset:offset + 4])[0]
    result['D2'] = struct.unpack('<I', data[offset + 4:offset + 8])[0]
    return result


def parse_structure_e(data, offset):
    result = {}
    size_e1, addr_e1 = struct.unpack('<IH', data[offset:offset + 6])
    result['E1'] = list(struct.unpack(
        f'<{size_e1}h', data[addr_e1:addr_e1 + size_e1 * 2]))
    result['E2'] = struct.unpack('<H', data[offset + 6:offset + 8])[0]
    return result


def main(in_data):
    out_data = parse_data(in_data)
    return out_data
