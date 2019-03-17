def leaves(t):
    if t is None:
        return []
    if t[1] is None and t[2] is None:
        return [t[0]]
    return leaves(t[1])+leaves(t[2])
