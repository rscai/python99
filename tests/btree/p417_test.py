from python99.btree.p417 import preorder, inorder, preorder_to_tree, inorder_to_tree, pre_in_tree


def test_preorder():
    assert preorder(['a', ['b', None, None], ['c', None, None]]) == 'abc'


def test_inorder():
    assert inorder(['a', ['b', None, None], ['c', None, None]]) == 'bac'


def test_preorder_to_tree():
    assert preorder_to_tree('abc') == [['a', None, ['b', None, ['c', None, None]]],
                                       ['a', None, ['b', ['c', None, None], None]],
                                       ['a', ['b', None, None], ['c', None, None]],
                                       ['a', ['b', None, ['c', None, None]], None],
                                       ['a', ['b', ['c', None, None], None], None]]


def test_inorder_to_tree():
    assert inorder_to_tree('abc') == [['a', None, ['b', None, ['c', None, None]]],
                                      ['a', None, ['c', ['b', None, None], None]],
                                      ['b', ['a', None, None], ['c', None, None]],
                                      ['c', ['a', None, ['b', None, None]], None],
                                      ['c', ['b', ['a', None, None], None], None]]


def test_pre_in_tree():
    assert pre_in_tree('abc', 'bac') == [
        'a', ['b', None, None], ['c', None, None]]
