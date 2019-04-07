from python99.graph.p606 import isomorphic


def test_isomorphic():
    assert isomorphic((['a', 'b', 'c'],
                       [('a', 'b'),
                        ('b', 'c'),
                        ('c', 'a')]
                       ), (
                           [1, 2, 3],
                           [(1, 2),
                            (2, 3),
                            (3, 1)])) == True
    assert isomorphic((['a', 'b', 'c'],
                       [('a', 'b'),
                        ('b', 'c'),
                        ('c', 'a')]
                       ), (
                           [1, 2, 3],
                           [(1, 2),
                            (2, 3)])) == False
