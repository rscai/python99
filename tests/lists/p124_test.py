from python99.lists.p124 import lotto
import functools
import operator


def test_lotto():
    m = 46
    n = 6
    l = [e for e in range(1, m+1)]
    actual = lotto(n, m)
    assert len(actual) == n
    assert functools.reduce(
        operator.and_, [e in l for e in actual], True) == True
    assert len(actual) == len(set(actual))
