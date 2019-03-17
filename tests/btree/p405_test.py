from python99.btree.p405 import sym_cbal_trees

def test_sym_cbal_trees():
    assert sym_cbal_trees(5) == [
        ['E', ['E', ['E', None, None], None], ['E', None, ['E', None, None]]],
        ['E', ['E', None, ['E', None, None]], ['E', ['E', None, None], None]]
    ]