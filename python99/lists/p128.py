# Sorting a list of lists according to length of sublists
# a) We suppose that a list (Inlist) contains elements that are lists themselves.
# The objective is to sort the elements of InList according to their length.
# E.g. short lists first, longer lists later, or vice versa.
import functools


def lsort(l):
    return [l_and_length[0] for l_and_length in sorted([(e, len(e)) for e in l], key=lambda x: x[1])]

# b) Again, we suppose that a list (InList) contains elements that are lists themselves.
# But this time the objective is to sort the elements of InList according to their length frequency;
# i.e. in the default, where sorting is done ascendingly, lists with rare lengths are placed first,
# others with a more frequent length come later.


def ifsort(l):
    list_with_length = [(e, len(e)) for e in l]
    lengths = [e[1] for e in list_with_length]
    length_frequency = functools.reduce(accum_to_dict, lengths, {})
    list_with_length_frequency = [
        (e[0], length_frequency[e[1]]) for e in list_with_length]
    return [e[0] for e in sorted(
        list_with_length_frequency, key=lambda x: x[1])]


def accum_to_dict(d, value):
    if value not in d:
        d[value] = 1
    else:
        d[value] = d[value]+1
    return d
