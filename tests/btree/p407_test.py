from python99.btree.p407 import minNodes, minHeight, maxHeight, hbal_tree_nodes


def test_minNides():
    assert minNodes(2) == 2
    assert minNodes(3) == 4
    assert minNodes(4) == 7


def test_minHeight():
    assert minHeight(4) == 3
    assert minHeight(7) == 3


def test_maxHeight():
    assert maxHeight(7) == 4
    assert maxHeight(12) == 5


def test_hbal_tree_nodes():
    assert hbal_tree_nodes(4) == [
        ['E', ['E', ['E', None, None], None], ['E', None, None]],
        ['E', ['E', None, ['E', None, None]], ['E', None, None]],
        ['E', ['E', None, None], ['E', ['E', None, None], None]],
        ['E', ['E', None, None], ['E', None, ['E', None, None]]]
    ]
