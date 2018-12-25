## find the K'th element of a list. The first element in the list is number 1

def find_kth(list, k):
    if len(list) < k:
        return None
    return list[k-1]


def find_kth_recursive(l, k):
    if k == 1:
        return l[0]
    return find_kth_recursive(l[1:], k-1)
