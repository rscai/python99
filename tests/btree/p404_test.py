from python99.btree.p404 import construct


def test_construct():
    assert construct([3, 2, 5, 7, 1]) == [
        3, [2, [1, None, None], None], [5, None, [7, None, None]]
    ]
