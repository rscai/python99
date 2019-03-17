from python99.btree.p414 import layout_binary_tree


def test_layout_binary_tree():
    E = 'E'
    assert layout_binary_tree([E, [E, None, [E, None, None]], [E, [E, None, None], None]]) == [('E', 3, 1),
                                                                                               [('E', 1, 2), None, [
                                                                                                   ('E', 2, 3), None, None]],
                                                                                               [('E', 5, 2), [('E', 4, 3), None, None], None]]
