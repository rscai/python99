# Duplicate the elements of a list
import functools
import operator


def duplicate(l):
    return functools.reduce(operator.concat, [[e] * 2 for e in l], [])
