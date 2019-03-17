def layout_binary_tree(t):
    markedTree,_ = markXY(t, depth(t), 0, 1)
    return markedTree


def markXY(t, d, x, y):
    selfX = x
    e = ()
    if t is None:
        return (None, x)
    if t[1] is None and x == 0:
        # this node is the most left one
        selfX = 1
        e = (t[0], selfX, y)
    if selfX == 0:
        leftX = selfX
    else:
        leftX = selfX - int(2**(d-y-1))
    left, leftX = markXY(t[1], d, leftX, y+1)
    selfX = leftX + int(2**(d-y-1))
    e = (t[0], selfX, y)
    rightX = selfX + int(2**(d-y-1))
    right, _ = markXY(t[2], d, rightX, y+1)
    return [e, left, right], selfX


def depth(t):
    if t is None:
        return 0
    return max(depth(t[1]), depth(t[2])) + 1
