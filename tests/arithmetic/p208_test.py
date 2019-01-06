from python99.arithmetic.p208 import coprime


def test_coprime():
    assert coprime(35, 64) == True
    assert coprime(36, 63) == False
