from python99.btree.p402 import cbal_tree

def test_cbal_tree():
    assert cbal_tree(4) == [
        ['E', ['E', ['E', None, None], None], ['E', None, None]],
        ['E', ['E', None, ['E', None, None]], ['E', None, None]],
        ['E', ['E', None, None], ['E', ['E', None, None], None]],
        ['E', ['E', None, None], ['E', None, ['E', None, None]]]
    ]