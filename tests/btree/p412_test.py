from python99.btree.p412 import complete_binary_tree


def test_complete_binary_tree():
    assert complete_binary_tree(
        4) == [1, [2, [4, None, None], None], [3, None, None]]
    assert complete_binary_tree(
        5) == [1, [2, [4, None, None], [5, None, None]], [3, None, None]]
