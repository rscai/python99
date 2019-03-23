from functools import reduce
from operator import concat


def tree_ltl(tree):
    e = tree[0]
    subtrees = tree[1]
    if len(subtrees) == 0:
        return [e]
    return ['(', e] + reduce(concat, [tree_ltl(subtree) for subtree in subtrees], []) + [')']


def ltl_tree(ltl):
    tree, _ = parse_tree(ltl)
    return tree


def parse_tree(s):
    if len(s) == 0:
        return None, s
    e = s[0]
    remain = s[1:]
    if e not in ['(', ')']:
        return (e, []), remain
    if e == ')':
        return None, remain
    if e == '(':
        e = remain[0]
        remain = remain[1:]
    subtrees = []
    subtree, remain = parse_tree(remain)
    while subtree is not None:
        subtrees.append(subtree)
        subtree, remain = parse_tree(remain)
    return (e, subtrees), remain
