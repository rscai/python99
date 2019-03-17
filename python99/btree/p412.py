def complete_binary_tree(n):
    return construct(1, n)


def construct(n, limit):
    if n > limit:
        return None
    return [n, construct(2*n, limit), construct(2*n+1, limit)]
