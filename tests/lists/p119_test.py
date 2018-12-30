from python99.lists.p119 import rotate


def test_rotate():
    assert rotate([1, 2, 3, 4, 5, 6], 2) == [3, 4, 5, 6, 1, 2]
    assert rotate([1, 2, 3, 4, 5, 6], 5) == [6, 1, 2, 3, 4, 5]
    assert rotate([1, 2, 3, 4, 5, 6], -2) == [5, 6, 1, 2, 3, 4]
