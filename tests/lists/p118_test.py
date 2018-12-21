from python99.lists.p118 import slice

def test_slice():
    assert slice([1,2,3,4,5,6],-1,3) == [1,2,3]
    assert slice([1,2,3,4,5,6],-1,7) == [1,2,3,4,5,6]
    assert slice([1,2,3,4,5,6], 2,9) == [2,3,4,5,6]
    assert slice([1,2,3,4,5,6], 2,4) == [2,3,4]