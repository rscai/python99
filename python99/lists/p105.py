## Reverse a list

def reverse(list):
    if list is None:
        return []
    return list.reverse()

def reverse_recursively(l):
    if l == []:
        return l
    return reverse_recursively(l[1:]) + [l[0]]