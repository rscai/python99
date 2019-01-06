# Determine the prime factors of a given positive integer(2)
# Construct a list containing the prime factors and their multiplicity
from python99.arithmetic.p202 import prime_factors
from python99.lists.p109 import pack


def prime_factors_mult(n):
    return [(group[0], len(group)) for group in pack(prime_factors(n))]
