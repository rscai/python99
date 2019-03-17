from python99.btree.p406 import hbal_tree


def minNodes(h):
    if h == 0:
        return 0
    if h == 1:
        return 1
    return 1 + minNodes(h-1) + minNodes(h-2)


def minHeight(n):
    if n == 0:
        return 0
    return 1 + minHeight(n//2)


def maxHeight(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 2
    for hLeft in range(1, n):
        nLeft = minNodes(hLeft)
        hRight = maxHeight(n-1-nLeft)
        if hLeft == hRight + 1 or hLeft == hRight:
            return 1 + max(hLeft, hRight)


def nodes(t):
    if t is None:
        return 0
    return 1 + nodes(t[1])+nodes(t[2])


def hbal_tree_nodes(n):
    trees = []
    for h in range(minHeight(n), maxHeight(n)+1):
        trees = trees + hbal_tree(h)
    return [tree for tree in trees if nodes(tree) == n]
