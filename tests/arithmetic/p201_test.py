from python99.arithmetic.p201 import is_prime


def test_is_prime():
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(8191) == True
    assert is_prime(524287) == True
    assert is_prime(6700417) == True
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(100) == False
