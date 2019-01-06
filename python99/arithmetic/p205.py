# Goldbach's conjecture
from python99.arithmetic.p201 import is_prime
from python99.arithmetic.p204 import prime_generator


def goldbach(n):
    for first_prime in prime_generator(2, n//2):
        if is_prime(n-first_prime):
            return [first_prime, n-first_prime]
    return []
