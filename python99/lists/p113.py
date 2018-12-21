# Run-length encoding of a list (direct solution)
# Implement the so-called run-length encoding data compression method directly.
# I.e. don't explicitly create the sublists containing the duplicates,
# as in problem 1.09, but only count them. As in problem 1.11,
# simplify the result list by replacing the singleton terms [1,X] by X.

def encode_direct(l):
    if len(l) == 0:
        return []
    if len(l) == 1:
        return l
    element = l[0]
    remain = l[1:len(l)]
    encoded_remain = encode_direct(remain)
    if len(encoded_remain) == 0:
        return [element]
    if isinstance(encoded_remain[0], list):
        if encoded_remain[0][1] == element:
            encoded_remain[0][0]+=1
            return encoded_remain
        else:
            return [element] + encoded_remain
    else:
        if encoded_remain[0] == element:
            encoded_remain[0] = [2,element]
            return encoded_remain
        else:
            return [element] + encoded_remain
    