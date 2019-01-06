# A list of prime numbers
# Given a range of integers by its lower and upper limit, construct a list of all prime numbers in that range
from python99.arithmetic.p201 import is_prime

def prime(lower, upper):
    return [x for x in prime_generator(lower, upper)]

def prime_generator(lower, upper):
    for num in range(lower, upper+1):
        if is_prime(num):
            yield num