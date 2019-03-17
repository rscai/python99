def internals(t):
    if t is None:
        return []
    if t[1] is None and t[2] is None:
        return []
    return [t[0]] + internals(t[1]) + internals(t[2])
