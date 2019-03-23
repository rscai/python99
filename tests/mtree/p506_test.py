from python99.mtree.p506 import tree_ltl, ltl_tree


def test_tree_ltl():
    assert tree_ltl(('a', [('f', [('g', [])]), ('c', []), ('b', [('d', []), ('e', [])])])) == [
        '(', 'a', '(', 'f', 'g', ')', 'c', '(', 'b', 'd', 'e', ')', ')']


def test_ltl_tree():
    assert ltl_tree([
        '(', 'a', '(', 'f', 'g', ')', 'c', '(', 'b', 'd', 'e', ')', ')']) == ('a', [('f', [('g', [])]), ('c', []), ('b', [('d', []), ('e', [])])])
