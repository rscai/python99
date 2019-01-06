# Determine the greatest common divisor of two positive integer numbers
# Use Euclid's algorithm


def gcd(a, b):
    return euclid(max(a, b), min(a, b))


def euclid(a, b):
    # expect a > b
    r0 = a % b
    if r0 ==0:
        return b
    r1 = b % r0
    if r1 == 0:
        return r0
    else:
        return euclid(r0, r1)
