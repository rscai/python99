def construct(nums):
    tree = None
    for num in nums:
        tree = add(tree, num)
    return tree


def add(tree, e):
    if tree is None:
        return [e, None, None]
    if e < tree[0]:
        return[tree[0], add(tree[1], e), tree[2]]
    else:
        return [tree[0], tree[1], add(tree[2], e)]
