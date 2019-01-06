# Determine the prime factors of a given positive integer
# Construct a flat list containing the prime factors in ascending order
from python99.arithmetic.p201 import is_prime


def prime_factors(n):
    return prime_factors_internal(n, 2)


def prime_factors_internal(n, prime):
    if is_prime(n):
        return [n]
    if n % prime == 0:
        return [prime]+prime_factors_internal(n/prime, prime)
    else:
        return prime_factors_internal(n, next_prime(prime))

# Bertrand's postulate


def next_prime(n):
    for i in range(n+1, 2*n):
        if is_prime(i):
            return i
    return None
