# An n-bit Gray code is a sequence of n-bit strings constructed according to certain rules. For example,
# n = 1: C(1) = ['0','1'].
# n = 2: C(2) = ['00','01','11','10'].
# n = 3: C(3) = ['000','001','011','010','110','111','101','100'].
#
# Find out the construction rules and write a predicate with the following specification:
#
# % gray(N,C) :- C is the N-bit Gray code


def gray(n):
    if n == 1:
        return ['0', '1']
    return ['0'+e for e in gray(n-1)] + ['1'+e for e in reversed(gray(n-1))]
