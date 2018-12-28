# Modified run-length encoding.
# Modify the result of problem 1.10 in such a way that if
# an element has no duplicates it is simply copied into the result lists.
# Only elements with duplicates are transferred as [N,E] terms.

from python99.lists.p110 import encode


def encode_modified(l):
    return [simplify(e) for e in encode(l)]


def simplify(term):
    if term[0] == 1:
        return term[1]
    else:
        return term
