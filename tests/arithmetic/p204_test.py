from python99.arithmetic.p204 import prime

def test_prime():
    assert prime(2,7) == [2, 3, 5, 7]
    assert prime(10, 20) == [11, 13, 17, 19]