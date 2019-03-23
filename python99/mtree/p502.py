from functools import reduce
from operator import add


def nnodes(t):
    return reduce(add, [nnodes(e) for e in t[1]], 1)
