from python99.lists.p101 import find_last_one

def test_find_last_one():
    input = [1,4,6,'s','no','X']
    actual = find_last_one(input)
    assert actual == 'X'