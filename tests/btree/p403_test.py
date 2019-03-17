from python99.btree.p403 import symmetric


def test_symmetric():
    assert symmetric([
        1, [1, None, None], [1, None, None]
    ]) == True
    assert symmetric([
        1, [1, None, None], [1, [1, None, None], [1, None, None]]
    ]) == False
