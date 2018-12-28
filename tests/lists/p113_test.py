from python99.lists.p113 import encode_direct


def test_encode_direct():
    assert encode_direct([]) == []
    assert encode_direct([1, 2, 2, 2, 3, 4, 5, 5]) == [1, [3, 2], 3, 4, [2, 5]]
    assert encode_direct([1, 1, 2, 2, 2, 3, 3, 4, 4, 4]) == [
        [2, 1], [3, 2], [2, 3], [3, 4]]
