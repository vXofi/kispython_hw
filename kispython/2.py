import math


def main(y):
    if y < 180:
        return math.sqrt(y) ** 5 + y ** 7 + y ** 3
    elif 180 <= y < 263:
        return 61 * (37 + y / 42 + 5 * y ** 2) ** 6
    elif 263 <= y < 336:
        return 66 * (24 * y ** 2 + 75 * y) ** 3 + y ** 6 + y ** 5
    elif y >= 336:
        return math.log2(y)