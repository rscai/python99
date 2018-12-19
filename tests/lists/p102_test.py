from python99.lists.p102 import find_last_but_one

def test_p102_find_last_but_one():
    input = ['a', 2, 3, 'Z', 9]
    actual = find_last_but_one(input)
    assert actual == 'Z'