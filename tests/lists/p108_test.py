from python99.lists.p108 import compress

def test_compress():
    assert compress(None) == []
    assert compress([]) == []
    assert compress([1]) == [1]
    assert compress([1,1,2,3,4,4,5,6,6,6,6]) == [1,2,3,4,5,6]
    assert compress([2,3]) == [2,3]