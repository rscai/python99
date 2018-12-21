# Insert an element at a given  position into a list

# index is 1-based
def insert_at(l,index, value):
    if index <= 1:
        return [value] + l
    if index > len(l):
        return l + [value]
    return l[:index-1] + [value] + l[index-1:]

def insert_at_mutable(l, index, value):
    l.insert(index-1, value)
    return l
