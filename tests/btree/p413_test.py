from python99.btree.p413 import layout_binary_tree


def test_layout_binary_tree():
    E = 'E'
    assert layout_binary_tree([E, [E, None, None], [E, None, None]]) == E - [
        ('E', 2, 1), [('E', 1, 2), None, None], [('E', 3, 2), None, None]]
