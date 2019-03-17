def preorder(t):
    if t is None:
        return ''
    return t[0]+preorder(t[1])+preorder(t[2])


def inorder(t):
    if t is None:
        return ''
    return inorder(t[1])+t[0]+inorder(t[2])


def preorder_to_tree(s):
    if len(s) == 0:
        return [None]
    e = s[0]
    s = s[1:]

    leftAndRights = []
    for i in range(0, len(s)+1):
        leftAndRights.append([s[:i], s[i:]])
    result = []
    for leftAndRight in leftAndRights:
        result = result+[[e, left, right] for left in preorder_to_tree(
            leftAndRight[0]) for right in preorder_to_tree(leftAndRight[1])]
    return result


def inorder_to_tree(s):
    if len(s) == 0:
        return [None]
    leftAndEAndRights = []
    for i in range(0, len(s)):
        leftAndEAndRights.append([s[:i], s[i], s[i+1:]])
    result = []
    for (l, e, r) in leftAndEAndRights:
        result = result+[[e, left, right]
                         for left in inorder_to_tree(l) for right in inorder_to_tree(r)]
    return result


def pre_in_tree(p, i):
    ptree = preorder_to_tree(p)
    itree = inorder_to_tree(i)

    trees = [(pt, it) for pt in ptree for it in itree if pt == it]
    return trees[0][0]
