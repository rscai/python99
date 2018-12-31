from python99.lists.p125 import rnd_permu
import functools
import operator


def test_rnd_permu():
    l = [e for e in range(1, 11)]
    actual = rnd_permu(l)
    assert len(actual) == len(l)
    assert set(actual) == set(l)
    assert functools.reduce(operator.and_, [e in l for e in actual], True)
