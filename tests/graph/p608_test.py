from python99.graph.p608 import traversal

def test_traversal():
    assert traversal((['a', 'b', 'c', 'd', 'e'],
                   [('a', 'b'),
                    ('a', 'd'),
                    ('b', 'c'),
                    ('b', 'e'),
                    ('c', 'e'),
                    ('d', 'e')
                    ]), 'b') == ['b', 'a', 'd', 'e', 'c']