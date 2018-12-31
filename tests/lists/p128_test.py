from python99.lists.p128 import lsort, ifsort


def test_lsort():
    assert lsort([[1, 2, 3], ['a', 'b'], [4]]) == [[4], ['a', 'b'], [1, 2, 3]]


def test_ifsort():
    assert ifsort([[1, 2, 3], [4, 5, 6], [7, 8, 9], ['a'], ['b'], ['c', 'd']]) == [
        ['c', 'd'], ['a'], ['b'], [1, 2, 3], [4, 5, 6], [7, 8, 9]]
