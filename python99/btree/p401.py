# P401: Check whether a given term represents a binary tree


def istree(tree):
    SIZE_SELF_CHILDREN = 3
    if tree is None:
        return True
    if type(tree) is not list:
        return False
    if len(tree) is not SIZE_SELF_CHILDREN:
        return False
    if tree[0] is None:
        return False
    return istree(tree[1]) and istree(tree[2])
