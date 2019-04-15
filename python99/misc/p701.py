def eight_queens():
    return queens(8, 8, [])


def queens(m, n, allocatedQueens):
    if n == 0:
        return [[]]
    availablePostions = allocate(m, allocatedQueens)
    return [[queen] + remain 
            for queen in availablePostions 
            for remain in queens(m, n-1, allocatedQueens + [queen])]


def allocate(m, allocatedQueens):
    for pos in range(1, m+1):
        if isAvailable(pos, allocatedQueens):
            yield pos


def isAvailable(pos, allocatedQueens):
    if pos in allocatedQueens:
        return False
    for index in range(1, len(allocatedQueens)+1):
        if allocatedQueens[-index]+index == pos:
            return False
        if allocatedQueens[-index]-index == pos:
            return False
    return True
