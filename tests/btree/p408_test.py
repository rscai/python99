from python99.btree.p408 import count_leaves


def test_count_leaves():
    E = 'E'
    assert count_leaves([E, None, None]) == 1
    assert count_leaves([E, [E, None, [E, None, None]], [E, None, None]]) == 2
