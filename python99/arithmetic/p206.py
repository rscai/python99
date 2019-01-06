# A list of Goldbach compositions
from python99.arithmetic.p201 import is_prime
from python99.arithmetic.p204 import prime_generator
import math


def goldbach_list(lower, upper, min_prime_factor=0):
    return [x for x in
            [goldbach(even, min_prime_factor) for even in
             even_nums(lower, upper, min_prime_factor*2)]
            if x != None]


def even_nums(lower, upper, min_even):
    for num in range(lower, upper+1):
        if num > min_even and num % 2 == 0:
            yield num


def goldbach(n, min_prime_factor):
    for first_prime in prime_generator(max(2, min_prime_factor+1), n//2):
        if n-first_prime < min_prime_factor:
            return None
        if is_prime(n-first_prime):
            return [first_prime, n-first_prime]
    return None
