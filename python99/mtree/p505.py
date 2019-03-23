from functools import reduce
from operator import concat


def bottom_up(t_or_s):
    if type(t_or_s) is tuple:
        return bottom_up_t(t_or_s)
    else:
        return bottom_up_s(t_or_s)


def bottom_up_t(tree):
    e = tree[0]
    subtrees = tree[1]
    return reduce(concat, [bottom_up_t(subtree) for subtree in subtrees], '') + e


def bottom_up_s(s):
    e = s[-1]
    remain = s[:-1]
    return (e, [(x, []) for x in remain])
