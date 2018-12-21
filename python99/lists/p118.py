# Extract a slice from a list.
# Given two indices, I and K, the slice is the list containing
# the elements between the I'th and K'th element of the original list
# (both limits included). Start counting the elements with 1.

def slice(l, i, k):
    return l[max(0,i-1):min(len(l),k)]