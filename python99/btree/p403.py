def symmetric(tree):
    return mirror(tree[1], tree[2])


def mirror(a, b):
    if a is None and b is None:
        return True
    if a is None and b is not None:
        return False
    if a is not None and b is None:
        return False
    aleft = a[1]
    aright = a[2]
    bleft = b[1]
    bright = b[2]
    return mirror(aleft, bright) and mirror(aright, bleft)
