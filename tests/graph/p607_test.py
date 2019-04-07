from python99.graph.p607 import degree, orderNodeByDegreeDesc, coloring


def test_degree():
    assert degree((['a', 'b', 'c', 'd', 'e'],
                   [('a', 'b'),
                    ('a', 'd'),
                    ('b', 'c'),
                    ('b', 'e'),
                    ('c', 'e'),
                    ('d', 'e')
                    ]), 'b') == 3

def test_orderNodeByDegreeDesc():
    assert orderNodeByDegreeDesc((['a', 'b', 'c', 'd', 'e'],
                   [('a', 'b'),
                    ('a', 'd'),
                    ('b', 'c'),
                    ('b', 'e'),
                    ('c', 'e'),
                    ('d', 'e')
                    ])) == ['e', 'd', 'c', 'b', 'a']


def test_coloring():
    coloredG = coloring((['a', 'b', 'c', 'd', 'e'],
                   [('a', 'b'),
                    ('a', 'd'),
                    ('b', 'c'),
                    ('b', 'e'),
                    ('c', 'e'),
                    ('d', 'e')
                    ]))
    assert coloredG[0] == [('a', 1), ('b', 3), ('c', 2), ('d', 2), ('e', 1)]