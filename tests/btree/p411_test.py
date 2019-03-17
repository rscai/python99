from python99.btree.p411 import atlevel


def test_atlevel():
    E = 'E'
    assert atlevel(
        [E, [E, None, None], [E, None, [E, None, None]]], 2) == [E, E]
    assert atlevel([E, [E, [E, [E, None, None], None], None],
                    [E, None, None]], 3) == [E]
