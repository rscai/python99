from python99.lists.p114 import duplicate


def test_duplicate():
    assert duplicate([]) == []
    assert duplicate([1]) == [1, 1]
    assert duplicate([1, 1, 2, 3]) == [1, 1, 1, 1, 2, 2, 3, 3]
