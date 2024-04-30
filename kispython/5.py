from math import ceil, floor


def main(y, z):
    s = 0
    for i in range(1, len(y) + 1):
        s += floor(z[i - 1] ** 3 - 29 * y[len(y) + 1 - ceil(i / 3) - 1]
                   - y[len(y) + 1 - ceil(i / 4) - 1] ** 2) ** 6
    return s * 85 / 32
