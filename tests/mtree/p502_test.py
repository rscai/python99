from python99.mtree.p502 import nnodes


def test_nnodes():
    assert nnodes(('a', [('b', [('c', []), ('d', [])])])) == 4
