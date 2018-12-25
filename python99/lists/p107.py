## Flatten a nested list structure


def flatten(l):
    if l is None:
        return []
    if len(l) == 0:
        return []
    element = l[0]
    remain = l[1:len(l)]
    if isinstance(element, list):
        return flatten(element)+flatten(remain)
    else:
        return [element]+flatten(remain)
