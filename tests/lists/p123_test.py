from python99.lists.p123 import rnd_select
import functools
import operator


def test_rnd_select():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    actual = rnd_select(l, 3)
    assert len(actual) == 3
    assert functools.reduce(
        operator.and_, [e in l for e in actual], True) == True
