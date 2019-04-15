from python99.misc.p703 import conjecture

def test_conjecture():
    assert conjecture((['a','b','c'],
                        [('a','b'),('a','c')])) == [
                            ([('a', 1), ('b', 2), ('c', 3)], [('a', 'b', 1), ('a', 'c', 2)]),
                            ([('a', 1), ('b', 3), ('c', 2)], [('a', 'b', 2), ('a', 'c', 1)]),
                            ([('a', 3), ('b', 1), ('c', 2)], [('a', 'b', 2), ('a', 'c', 1)]),
                            ([('a', 3), ('b', 2), ('c', 1)], [('a', 'b', 1), ('a', 'c', 2)])
                        ]
    sevenNodeResult = conjecture((['a','b','c','d','e','f','g'],
                        [
                            ('a','d'),
                            ('a','g'),
                            ('a','b'),
                            ('b','e'),
                            ('b','c'),
                            ('e','f')
                        ]))
    assert len(sevenNodeResult) == 52