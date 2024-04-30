import math


def main(m, a, n):
    temp = 0
    for k in range(1, a+1):
        for j in range(1, m+1):
            temp += math.ceil(j ** 3 / 30 + k)
    for i in range(1, n+1):
        for k in range(1, a+1):
            temp += 43 * i + math.cos(k) ** 4
    return temp