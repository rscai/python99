# Duplicate the elements of a list

from python99.lists.p107 import flatten

def duplicate(l):
    return flatten([ [e] * 2 for e in l])

def duplicate_mutable(l):
    result = []
    for e in l:
        result.append(e)
        result.append(e)
    return result