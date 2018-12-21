# Sorting a list of lists according to length of sublists
# a) We suppose that a list (Inlist) contains elements that are lists themselves.
# The objective is to sort the elements of InList according to their length.
# E.g. short lists first, longer lists later, or vice versa.
import functools

def lsort(l):
    list_with_length = [ (e, len(e)) for e in l]
    sorted_list_with_length = insert_sort(list_with_length,length_comparator)
    return [e[0] for e in sorted_list_with_length]

def insert_sort(l,comparator):
    if len(l) == 1:
        return l
    first_element = l[0]
    remain = insert_sort(l[1:],comparator)
    for index, value in enumerate(remain):
        if comparator(first_element,value) <0:
            return remain[:index]+[first_element]+remain[index:]
    return remain+[first_element]

def length_comparator(left, right):
    (_,left_length) = left
    (_,right_length) = right
    if left_length < right_length:
        return -1
    if left_length > right_length:
        return 1
    return 0

# b) Again, we suppose that a list (InList) contains elements that are lists themselves.
# But this time the objective is to sort the elements of InList according to their length frequency;
# i.e. in the default, where sorting is done ascendingly, lists with rare lengths are placed first,
# others with a more frequent length come later.

def ifsort(l):
    list_with_length = [(e,len(e)) for e in l]
    lengths = [e[1] for e in list_with_length]
    length_frequency = functools.reduce(accum_to_dict,lengths,{})
    list_with_length_frequency = [(e[0],length_frequency[e[1]]) for e in list_with_length]
    sorted_list_with_length_frequency = insert_sort(list_with_length_frequency, length_comparator)
    return [e[0] for e in sorted_list_with_length_frequency]

def accum_to_dict(d,value):
    if value not in d:
        d[value]=1
    else:
        d[value]=d[value]+1
    return d