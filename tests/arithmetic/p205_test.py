from python99.arithmetic.p205 import goldbach


def test_goldbach():
    assert goldbach(28) == [5, 23]
    assert goldbach(36) == [5, 31]
    assert goldbach(38) == [7, 31]
    assert goldbach(48) == [5, 43]
    assert goldbach(64) == [3, 61]
