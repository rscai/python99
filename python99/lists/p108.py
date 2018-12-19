# Eliminate consecutive duplicates of list elements.
# If a list contains repeated elements they should be replaced with a single copy of the elements.
# The order of the elements should not be changed.

def compress(l):
    if l is None:
        return []
    if len(l) == 0:
        return []
    if len(l) == 1:
        return l
    first = l[0]
    remain = l[1:len(l)]
    if first == remain[0]:
        return compress(remain)
    else:
        return [first]+compress(remain)