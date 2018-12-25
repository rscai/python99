from python99.lists.p104 import length, length_recursive


def test_length():
    assert length([1, 3, 4, 5, 'Apple', 'Orange']) == 6
    assert length(None) == 0


def test_length_recursive():
    assert length([1, 3, 4, 5, 'Apple', 'Orange']) == 6
    assert length(None) == 0
