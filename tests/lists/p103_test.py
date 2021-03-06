from python99.lists.p103 import find_kth, find_kth_recursive


def test_find_kth():
    input = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    assert find_kth(input, 4) == 'd'
    assert find_kth(input, 9) == None


def test_find_kth_recursive():
    input = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    assert find_kth(input, 4) == 'd'
    assert find_kth(input, 9) == None
