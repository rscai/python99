## find the K'th element of a list. The first element in the list is number 1

def find_kth(list, k):
    if len(list) < k:
        return None
    return list[k-1]