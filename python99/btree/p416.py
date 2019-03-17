def tree_string(ts):
    if type(ts) is str:
        return string_to_tree(ts)
    else:
        return tree_to_string(ts)


def tree_to_string(t):
    if t is None:
        return ''
    if t[1] is None and t[2] is None:
        return t[0]
    return t[0]+'('+tree_to_string(t[1])+','+tree_to_string(t[2])+')'


def string_to_tree(s):
    e = s[0]
    s = s[1:]
    if e == ')':
        return None, s
    if len(s) == 0:
        return [e, None, None], s
    if s[0] == ',':
        return [e, None, None], s
    if s[0] == ')':
        return [e, None, None], s
    s = s[1:]
    left, s = string_to_tree(s)
    s = s[1:]
    right, s = string_to_tree(s)
    s = s[1:]
    return [e, left, right], s
