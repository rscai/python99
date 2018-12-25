from python99.lists.p109 import pack


def test_pack():
    assert pack([]) == []
    assert pack([1]) == [[1]]
    assert pack([1, 1, 2, 3, 3, 4]) == [[1, 1], [2], [3, 3], [4]]
