from python99.logic_codes.p305 import huffman, constructTree


def test_huffman():
    assert huffman([
        ('a', 45), 
        ('b', 13), 
        ('c', 12), 
        ('d', 16), 
        ('e', 9), 
        ('f', 5)
        ]) == [
        ('a', '11'),
        ('b', '011'),
        ('c', '010'),
        ('d', '10'),
        ('e', '001'),
        ('f', '000')
    ]

def test_constructTree():
    assert constructTree([
        ('f', 5),
        ('e', 9),
        ('c', 12),
        ('b', 13), 
        ('d', 16), 
        ('a', 45)
        ]) == [[
                [
                    [('f',5),('e',9)],
                    [('c',12),('b',13)]
                ],[
                    ('d',16),('a',45)
                ]
            ]]