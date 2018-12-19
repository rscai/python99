# Pack consecutive duplicates of list elements into sublists.
# If a list contains repreated elements they should be placed in separate sublists

def pack(l):
    if l is None:
        return []
    if len(l) == 0:
        return []
    if len(l) == 1:
        return [l]
    first = l[0]
    remain = l[1:len(l)]
    remain_pack = pack(remain)
    if len(remain_pack) == 0:
        return [[first]]
    elif first in remain_pack[0]:
        remain_pack[0].append(first)
        return remain_pack
    else:
        return [[first]]+remain_pack
