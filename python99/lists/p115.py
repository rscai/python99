# Duplicate the elements of a list a given number of times
import functools
import operator


def duplicate(l, n):
    return functools.reduce(operator.concat, [[e] * n for e in l], [])
