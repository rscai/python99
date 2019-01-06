# Calculate Euler's totient function phi(m)
from python99.arithmetic.p203 import prime_factors_mult
import functools
import operator


def totient_phi(n):
 return functools.reduce(operator.mul, 
            [int((factor-1)*factor**(exp-1)) 
                for factor, exp in prime_factors_mult(n)], 
            1)
