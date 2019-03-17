def atlevel(t, l):
    if t is None:
        return []
    if l == 1:
        return [t[0]]
    return atlevel(t[1], l-1)+atlevel(t[2], l-1)
