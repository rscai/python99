from python99.lists.p126 import combination
import itertools


def test_combination():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    k = 2
    actual = combination(l, k)
    assert actual == [list(e) for e in itertools.combinations(l, k)]
