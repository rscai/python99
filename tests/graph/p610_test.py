from python99.graph.p610 import is_bipartite


def test_is_bipartite():
    assert is_bipartite((['a', 'b', 'c', 'd'], [
        ('a', 'c'),
        ('a', 'd'),
        ('b', 'c'),
        ('b', 'd')
    ])) == True
    assert is_bipartite((['a', 'b', 'c', 'd'], [
        ('a', 'c'),
        ('a', 'b'),
        ('a', 'd'),
        ('b', 'c'),
        ('b', 'd')
    ])) == False
