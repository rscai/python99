from python99.btree.p418 import tree_dotstring


def test_tree_dotstring():
    assert tree_dotstring(['a', ['b', ['d', None, None], ['e', None, None]], [
                          'c', None, ['f', ['g', None, None], None]]]) == 'abd..e..c.fg...'
