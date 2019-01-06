from python99.arithmetic.p203 import prime_factors_mult


def test_prime_factors_mult():
    assert prime_factors_mult(315) == [(3, 2), (5, 1), (7, 1)]
