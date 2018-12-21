# Rotate a list N places to the left.

def rotate(l, n):
    return l[n:len(l)]+l[0:n]