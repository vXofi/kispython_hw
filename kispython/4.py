def main(x):
    if x == 0:
        return -0.63
    if x >= 1:
        return main(x - 1) ** 2 + main(x - 1) + main(x - 1) ** 9