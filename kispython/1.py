import math


def main(x, y):
    return (x - y ** 6) / (
            (87 * y ** 3 - 0.01) ** 2 - x) + math.sqrt(
        (x ** 6 - 62 * (1 - 32 * y ** 3 - 72 * y) ** 7) / (
                (1 - 39 * y - x ** 2) ** 4 + math.sin(x) ** 3))