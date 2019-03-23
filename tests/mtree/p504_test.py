from python99.mtree.p504 import ipl


def test_ipl():
    assert ipl(('a', [('f', [('g', [])]), ('c', []),
                      ('b', [('d', []), ('e', [])])])) == 9
