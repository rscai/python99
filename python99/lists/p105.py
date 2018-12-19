## Reverse a list

def reverse_inplace(list):
    if list is None:
        return []
    return list.reverse()

def reverse_immutable(list):
    if list is None:
        return []
    return [list[i] for i in range(len(list)-1,-1,-1)]