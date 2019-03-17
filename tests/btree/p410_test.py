from python99.btree.p410 import internals


def test_internals():
    E = 'E'
    assert internals([E, [E, None, [E, None, None]],
                      [E, None, None]]) == [E, E]
    assert internals([E, [E, None, None], [E, None, None]]) == [E]
