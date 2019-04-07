from python99.graph.p605 import ms_tree

def test_ms_tree():
    tree, sumOfWeight = ms_tree((['a','b','c','d','e','f','g','h'],
                    [
                        ('a','b',5),
                        ('a','d',3),
                        ('b','c',2),
                        ('b','e',4),
                        ('c','e',6),
                        ('d','e',7),
                        ('d','f',4),
                        ('d','g',3),
                        ('e','h',5),
                        ('f','g',4),
                        ('g','h',1)
                    ])) 
    assert tree == (['e', 'c', 'b', 'f', 'h', 'g', 'd', 'a'],
                            [('b', 'e', 4),
                            ('b', 'c', 2),
                            ('a', 'b', 5),
                            ('d', 'f', 4),
                            ('g', 'h', 1),
                            ('d', 'g', 3),
                            ('a', 'd', 3)])
    assert sumOfWeight == 22