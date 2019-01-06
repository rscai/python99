from python99.arithmetic.p202 import prime_factors


def test_prime_factors():
    assert prime_factors(2) == [2]
    assert prime_factors(3) == [3]
    assert prime_factors(315) == [3, 3, 5, 7]
