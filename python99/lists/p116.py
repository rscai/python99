# Drop every N'th element from a list


def drop(l, n):
    return [e for i, e in enumerate(l) if (i+1) % n != 0]
