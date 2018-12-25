from python99.lists.p101 import find_last_one, find_last_one_recursive

def test_find_last_one():
    input = [1,4,6,'s','no','X']
    actual = find_last_one(input)
    assert actual == 'X'

def test_find_last_one_recursive():
    input = [1,4,6,'s','no','X']
    actual = find_last_one_recursive(input)
    assert actual == 'X'