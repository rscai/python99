from python99.btree.p406 import hbal_tree


def test_hbal_tree():
    E = 'E'
    assert hbal_tree(2) == [
        [E, [E, None, None], [E, None, None]],
        [E, [E, None, None], None],
        [E, None, [E, None, None]]
    ]
    assert hbal_tree(3) == [
        ['E',
            ['E', ['E', None, None], ['E', None, None]],
            ['E', ['E', None, None], ['E', None, None]]
         ],
        ['E',
         ['E', ['E', None, None], ['E', None, None]],
         ['E', ['E', None, None], None]],
        ['E',
         ['E', ['E', None, None], ['E', None, None]],
         ['E', None, ['E', None, None]]],
        ['E',
         ['E', ['E', None, None], None],
         ['E', ['E', None, None], ['E', None, None]]],
        ['E', ['E', ['E', None, None], None],
         ['E', ['E', None, None], None]],
        ['E', ['E', ['E', None, None], None],
         ['E', None, ['E', None, None]]],
        ['E',
         ['E', None, ['E', None, None]],
         ['E', ['E', None, None], ['E', None, None]]],
        ['E', ['E', None, ['E', None, None]],
         ['E', ['E', None, None], None]],
        ['E', ['E', None, ['E', None, None]],
         ['E', None, ['E', None, None]]],
        ['E', ['E', ['E', None, None], ['E', None, None]],
         ['E', None, None]],
        ['E', ['E', ['E', None, None], None], ['E', None, None]],
        ['E', ['E', None, ['E', None, None]], ['E', None, None]],
        ['E', ['E', None, None], [
            'E', ['E', None, None], ['E', None, None]]],
        ['E', ['E', None, None], ['E', ['E', None, None], None]],
        ['E', ['E', None, None], ['E', None, ['E', None, None]]]]
