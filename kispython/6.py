import math


def main(i_):
    i_ = set(i_)
    si_ = set([abs(e) for e in i_ if -54 < e < 52])
    Y_ = i_.union((si_))
    h_ = set([abs(e) + abs(e) for e in Y_ if e < -96 or e >= 54])
    t_ = set([w * v for w in si_ for v in Y_ if w <= v])
    return len(t_) + math.prod(n for n in h_)
