from functools import reduce
from operator import concat


def tree(t_or_s):
    if type(t_or_s) is tuple:
        return tree_to_string(t_or_s)
    else:
        return string_to_tree(t_or_s)


def tree_to_string(t):
    return t[0] + reduce(concat, [tree_to_string(subtree) for subtree in t[1]], '') + '^'


def string_to_tree(s):
    tree, _ = do_string_to_tree(s)
    return tree


def do_string_to_tree(s):
    e = s[0]
    remain = s[1:]
    if e == '^':
        return None, remain
    subtrees = []
    subtree, remain = do_string_to_tree(remain)
    while subtree is not None:
        subtrees.append(subtree)
        subtree, remain = do_string_to_tree(remain)
    return (e, subtrees), remain
