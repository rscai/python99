from python99.graph.p609 import connected_components


def test_connected_components():
    components = connected_components((['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], [
        ('a', 'b'),
        ('c', 'd'),
        ('d', 'e'),
        ('e', 'c'),
        ('f', 'g'),
        ('f', 'h'),
        ('g', 'h'),
        ('h', 'i'),
        ('i', 'j'),
        ('j', 'h')
    ]))
    assert len(components) == 3
    assert set(components[0][0]) == set(['a', 'b'])
    assert set(components[1][0]) == set(['d', 'e', 'c'])
    assert set(components[2][0]) == set(['g', 'h', 'f', 'i', 'j'])
