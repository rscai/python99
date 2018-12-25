## Find the number of elements of a list

def length(list):
    if list is None:
        return 0
    return len(list)

def length_recursive(l):
    if l == []:
        return 0
    return 1 + l[1:]