def layout_binary_tree(t):
    tree, _ = markX(t, 0)
    return markY(tree, 1)


def markX(t, p):
    if t is None:
        return (t, p)
    left, p = markX(t[1], p)
    p = p+1
    e = (t[0], p)
    right, p = markX(t[2], p)
    return [e, left, right],p


def markY(t, h):
    if t is None:
        return None
    return [(t[0][0], t[0][1], h), markY(t[1], h+1), markY(t[2], h+1)]
