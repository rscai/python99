# Duplicate the elements of a list a given number of times

from python99.lists.p107 import flatten

def duplicate(l, n):
    return flatten([ [e] * n for e in l])

def duplicate_mutable(l, n):
    result = []
    for e in l:
        for i in range(0,n):
            result.append(e)
    return result