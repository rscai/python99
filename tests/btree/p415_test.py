from python99.btree.p415 import countour, layout_binary_tree


def test_layout_binary_tree():
    assert layout_binary_tree(['a', ['b', None, ['d', None, None]], ['c', None, None]]) == [
        ('a', 2, 1),
        [('b', 1, 2), None, [('d', 2, 3), None, None]],
        [('c', 3, 2), None, None]
    ]


def test_countour():
    assert countour(['a', ['b', None, ['d', None, None]], ['c', None, None]]) == [
        ('a', [(-1, 1), (-1, 1)]),
        [('b', [(0, 1)]), None, [('d', []), None, None]],
        [('c', []), None, None]
    ]
