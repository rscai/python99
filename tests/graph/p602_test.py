from python99.graph.p602 import path


def test_path():
    assert path((['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], 
                    [
                        ('a', 'b'), 
                        ('a', 'd'), 
                        ('b', 'c'), 
                        ('b', 'e'),
                        ('c', 'e'), 
                        ('d', 'e'), 
                        ('d', 'f'), 
                        ('d', 'g'), 
                        ('e', 'h'), 
                        ('f', 'g'), 
                        ('g', 'h')
                    ]), 'a', 'e') == [
                                        ['a', 'b', 'c', 'e'], 
                                        ['a', 'b', 'e'], 
                                        ['a', 'd', 'e'], 
                                        ['a', 'd', 'f', 'g', 'h', 'e'], 
                                        ['a', 'd', 'g', 'h', 'e']
                                    ]
