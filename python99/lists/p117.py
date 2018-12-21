# Split a list into two parts; the length of the first part is given.

def split(l, n):
    if n <0:
        return ([],l)
    if n> len(l):
        return (l,[])
    return (l[0:n],l[n:len(l)])