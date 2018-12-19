from python99.lists.p105 import reverse_inplace, reverse_immutable

def test_reverse_inplace():
    input = [1,2,3,4,5,6]
    actual = reverse_inplace(input)
    assert actual == None
    assert input == [6,5,4,3,2,1]

def test_reverse_immutable():
    input = [1,2,3,4,5,6]
    actual = reverse_immutable(input)
    assert actual == [6,5,4,3,2,1]
    assert input == [1,2,3,4,5,6]