from python99.lists.p115 import duplicate, duplicate_mutable

def test_duplicate():
    assert duplicate([], 2) == []
    assert duplicate([1,2], 3) == [1,1,1,2,2,2]
    assert duplicate([1,2,3,4,5],1) == [1,2,3,4,5]

def test_duplicate_mutable():
    assert duplicate_mutable([], 2) == []
    assert duplicate_mutable([1,2], 3) == [1,1,1,2,2,2]
    assert duplicate_mutable([1,2,3,4,5],1) == [1,2,3,4,5]