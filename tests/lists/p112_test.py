from python99.lists.p112 import decode

def test_decode():
    assert decode([1,[3,2],[2,3],4,[2,5]]) == [1,2,2,2,3,3,4,5,5]
    assert decode([1,2,3]) == [1,2,3]
    assert decode([[3, 1], [2, 2], [4, 3]]) == [1, 1, 1, 2, 2, 3, 3, 3, 3]
