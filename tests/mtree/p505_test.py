from python99.mtree.p505 import bottom_up_t, bottom_up_s, bottom_up


def test_bottom_up():
    assert bottom_up(
        ('a', [('f', [('g', [])]), ('c', []), ('b', [('d', []), ('e', [])])])) == 'gfcdeba'
    assert bottom_up('gfcdeba') == (
        'a', [('g', []), ('f', []), ('c', []), ('d', []), ('e', []), ('b', [])])


def test_bottom_up_t():
    assert bottom_up_t(
        ('a', [('f', [('g', [])]), ('c', []), ('b', [('d', []), ('e', [])])])) == 'gfcdeba'


def test_bottom_up_s():
    assert bottom_up_s('gfcdeba') == (
        'a', [('g', []), ('f', []), ('c', []), ('d', []), ('e', []), ('b', [])])
