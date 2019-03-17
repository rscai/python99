from python99.btree.p401 import istree


def test_istree():
    assert istree([1, [2, None, None], None]) == True
    assert istree([1, [2, None], 3]) == False
