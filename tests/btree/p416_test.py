from python99.btree.p416 import tree_to_string, string_to_tree, tree_string


def test_tree_string():
    E = 'E'
    assert tree_string(
        [E, [E, None, None], [E, [E, None, None], None]]) == 'E(E,E(E,))'
    r, _ = tree_string('E(E,E(E,))')
    assert r == [E, [E, None, None], [E, [E, None, None], None]]


def test_tree_to_string():
    E = 'E'
    assert tree_to_string(
        [E, [E, None, None], [E, [E, None, None], None]]) == 'E(E,E(E,))'


def test_string_to_tree():
    E = 'E'
    r, _ = string_to_tree('E(E,E(E,))')
    assert r == [E, [E, None, None], [E, [E, None, None], None]]
    r2, _ = string_to_tree('E(E(E,E),E)')
    assert r2 == [E, [E, [E, None, None], [E, None, None]], [E, None, None]]
