from python99.arithmetic.p206 import goldbach_list
from python99.arithmetic.p201 import is_prime


def test_goldbach_list():
    assert goldbach_list(9, 20) == [[3, 7], [5, 7], [
        3, 11], [3, 13], [5, 13], [3, 17]]

def test_goldbach_list2():
    actual = goldbach_list(1, 2000, 50)
    for composition in actual:
        assert len(composition) == 2
        assert composition[0] > 50
        assert is_prime(composition[0]) == True
        assert composition[1] > 50
        assert is_prime(composition[1]) == True
