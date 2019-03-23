from functools import reduce
from operator import and_


def istree(t):
    if type(t) is not tuple:
        return False
    if len(t) != 2:
        return False
    if type(t[1]) is not list:
        return False
    return reduce(and_, [istree(e) for e in t[1]], True)
