def tree_dotstring(t):
    if t is None:
        return '.'
    return t[0] + tree_dotstring(t[1]) + tree_dotstring(t[2])
