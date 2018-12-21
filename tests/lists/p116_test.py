from python99.lists.p116 import drop

def test_drop():
    assert drop([1,2,3,4,5,6],2) == [1,3,5]
    assert drop([1,2,3,4,5,6], 3) == [1,2,4,5]
    assert drop([1,2,3,4,5,6], 4) == [1,2,3,5,6]