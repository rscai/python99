from python99.graph.p604 import s_tree, is_tree


def test_s_tree():
    assert s_tree((['a', 'b', 'c', 'd', 'e'],
                   [
        ('a', 'b'),
        ('a', 'd'),
        ('b', 'c'),
        ('b', 'e'),
        ('c', 'e'),
        ('d', 'e')
    ])) == [
        [('a', 'b'), ('a', 'd'), ('b', 'c'), ('b', 'e')],
        [('a', 'b'), ('a', 'd'), ('b', 'c'), ('c', 'e')],
        [('a', 'b'), ('a', 'd'), ('b', 'c'), ('d', 'e')],
        [('a', 'b'), ('a', 'd'), ('b', 'e'), ('c', 'e')],
        [('a', 'b'), ('a', 'd'), ('c', 'e'), ('d', 'e')],
        [('a', 'b'), ('b', 'c'), ('b', 'e'), ('d', 'e')],
        [('a', 'b'), ('b', 'c'), ('c', 'e'), ('d', 'e')],
        [('a', 'b'), ('b', 'e'), ('c', 'e'), ('d', 'e')],
        [('a', 'd'), ('b', 'c'), ('b', 'e'), ('c', 'e')],
        [('a', 'd'), ('b', 'c'), ('b', 'e'), ('d', 'e')],
        [('a', 'd'), ('b', 'c'), ('c', 'e'), ('d', 'e')],
        [('a', 'd'), ('b', 'e'), ('c', 'e'), ('d', 'e')]
    ]


def test_is_tree():
    assert is_tree((['a', 'b', 'c', 'd', 'e'], [('a', 'b'),
                                                ('a', 'd'), ('b', 'c'), ('b', 'e')])) == True
