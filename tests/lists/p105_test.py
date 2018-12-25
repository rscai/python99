from python99.lists.p105 import reverse, reverse_recursively


def test_reverse():
    input = [1, 2, 3, 4, 5, 6]
    actual = reverse(input)
    assert actual == None
    assert input == [6, 5, 4, 3, 2, 1]


def test_reverse_immutable():
    assert reverse_recursively([1, 2, 3, 4, 5, 6]) == [6, 5, 4, 3, 2, 1]
