# Remove the K'th element from a list.

def remove_at(l, k):
    if k <=0:
        return (None, l)
    if k > len(l):
        return (None,l)
    return (l[k-1],l[0:k-1]+l[k:len(l)])