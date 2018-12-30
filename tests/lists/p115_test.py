from python99.lists.p115 import duplicate


def test_duplicate():
    assert duplicate([], 2) == []
    assert duplicate([1, 2], 3) == [1, 1, 1, 2, 2, 2]
    assert duplicate([1, 2, 3, 4, 5], 1) == [1, 2, 3, 4, 5]
