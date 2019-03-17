def count_leaves(t):
    if t is None:
        return 0
    if t[1] is None and t[2] is None:
        return 1
    return count_leaves(t[1]) + count_leaves(t[2])
