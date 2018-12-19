from python99.lists.p110 import encode

def test_encode():
    assert encode([]) == []
    assert encode([1]) == [[1,1]]
    assert encode([1,1,2,3,3,4,4,4,4,5,6,6,6]) == [[2,1],[1,2],[2,3],[4,4],[1,5],[3,6]]