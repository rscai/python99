from functools import reduce
from operator import concat, add


def ipl(tree):
    return reduce(add, [x[1] for x in pl(tree)], 0)


def pl(tree):
    nodesOfSubtrees = reduce(concat, [pl(subtree) for subtree in tree[1]], [])
    return reduce(concat, [[(x[0], x[1]+1)] for x in nodesOfSubtrees], [(tree[0], 0)])
