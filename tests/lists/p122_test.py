from python99.lists.p122 import create_range

def test_create_range():
    assert create_range(1, 4) == [1, 2, 3, 4]
    assert create_range(2, 2) == [2]
    assert create_range(4, 9) == [4, 5, 6, 7, 8, 9]
