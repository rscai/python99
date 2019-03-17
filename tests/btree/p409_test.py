from python99.btree.p409 import leaves


def test_leaves():
    E = 'E'
    assert leaves([E, None, None]) == [E]
    assert leaves([E, [E, None, [E, None, None]], [E, None, None]]) == [E,E]
