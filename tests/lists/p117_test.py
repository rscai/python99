from python99.lists.p117 import split

def test_split():
    assert split([1,2,3,4,5,6],0) == ([],[1,2,3,4,5,6])
    assert split([1,2,3,4,5,6],-1) == ([], [1,2,3,4,5,6])
    assert split([1,2,3,4,5,6],2) == ([1,2],[3,4,5,6])
    assert split([1,2,3,4,5,6],5) == ([1,2,3,4,5],[6])
    assert split([1,2,3,4,5,6],6) == ([1,2,3,4,5,6],[])
    assert split([1,2,3,4,5,6],7) == ([1,2,3,4,5,6],[])