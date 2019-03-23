from python99.mtree.p503 import tree_to_string, string_to_tree, tree


def test_tree_to_string():
    assert tree_to_string(('a', [('f', [('g', [])]), ('c', []), ('b', [
                          ('d', []), ('e', [])])])) == 'afg^^c^bd^e^^^'


def test_string_to_tree():
    assert string_to_tree('afg^^c^bd^e^^^') == ('a', [('f', [('g', [])]), ('c', []), ('b', [
        ('d', []), ('e', [])])])


def test_tree():
    assert tree(('a', [('f', [('g', [])]), ('c', []), ('b', [
        ('d', []), ('e', [])])])) == 'afg^^c^bd^e^^^'
    assert tree('afg^^c^bd^e^^^') == ('a', [('f', [('g', [])]), ('c', []), ('b', [
        ('d', []), ('e', [])])])
