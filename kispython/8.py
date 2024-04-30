def encode_bitfields(bitfields, shifts):
    result = 0
    for field, value in bitfields:
        shift, length = shifts[field]
        mask = (1 << length) - 1
        result |= (value & mask) << shift
    return result


def main(bitfields):
    shifts = {'Y1': (0, 1), 'Y2': (1, 3), 'Y3': (4, 10), 'Y4': (14, 3)}
    return encode_bitfields(bitfields, shifts)
