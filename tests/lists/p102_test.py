from python99.lists.p102 import find_last_but_one, find_last_but_one_recursive

def test_p102_find_last_but_one():
    input = ['a', 2, 3, 'Z', 9]
    actual = find_last_but_one(input)
    assert actual == 'Z'

def test_p102_find_last_but_one_recursive():
    input = ['a', 2, 3, 'Z', 9]
    actual = find_last_but_one_recursive(input)
    assert actual == 'Z'