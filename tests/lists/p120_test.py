from python99.lists.p120 import remove_at

def test_remove_at():
    assert remove_at([1,2,3,4,5,6],0) == (None,[1,2,3,4,5,6])
    assert remove_at([1,2,3,4,5,6], 2) == (2,[1,3,4,5,6])
    assert remove_at([1,2,3,4,5,6], 6) == (6, [1,2,3,4,5])
    assert remove_at([1,2,3,4,5,6], 7) == (None, [1,2,3,4,5,6])