# Determine whether two positive integer numbers are coprime
from python99.arithmetic.p207 import gcd


def coprime(a, b):
    return gcd(a, b) == 1
