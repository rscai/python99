# Run-length encoding of a list (direct solution)
# Implement the so-called run-length encoding data compression method directly.
# I.e. don't explicitly create the sublists containing the duplicates,
# as in problem 1.09, but only count them. As in problem 1.11,
# simplify the result list by replacing the singleton terms [1,X] by X.


def encode_direct(l):
    return [simplify(term) for term in encode_internal(l)]


def encode_internal(l):
    if len(l) == 0:
        return []
    element = l[0]
    remain = l[1:len(l)]
    encoded_remain = encode_internal(remain)
    if len(encoded_remain) == 0:
        return [[1, element]]
    if encoded_remain[0][1] == element:
        encoded_remain[0][0] += 1
        return encoded_remain
    return [[1, element]] + encoded_remain


def simplify(term):
    if term[0] == 1:
        return term[1]
    return term
