from python99.lists.p107 import flatten


def test_flatten():
    assert flatten([1, [2, 3], 4]) == [1, 2, 3, 4]
    assert flatten([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert flatten([1, [2, [3, 4]]]) == [1, 2, 3, 4]
    assert flatten([]) == []
    assert flatten([[1, 2, 3, 4], 5, 6, [[7, 8], [9, 10]]]) == [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
