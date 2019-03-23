from python99.mtree.p501 import istree


def test_istree():
    assert istree(('a', [])) == True
    assert istree(('a', [('b', []), ('c', []), ('d', [])])) == True
    assert istree(('a', 'b', [])) == False
