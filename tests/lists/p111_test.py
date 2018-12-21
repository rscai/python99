from python99.lists.p111 import encode_modified

def test_encode_modified():
    assert encode_modified([]) == []
    assert encode_modified([1,2,2,2,3,4,5,5]) == [1,[3,2],3,4,[2,5]]
    assert encode_modified([1,1,2,2,2,3,3,4,4,4]) == [[2,1],[3,2],[2,3],[3,4]]
