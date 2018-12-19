# Run-length encoding of a list.
# Use the result of problem 1.09 to implement the so-called run-length encoding data compression method.
# Consecutive duplicates of elements are encoded as terms [N,E]
# where N is the number of duplictes of the element E.

from python99.lists.p109 import pack

def encode(l):
    packed_list = pack(l)
    return [[len(group),group[0]] for group in packed_list]