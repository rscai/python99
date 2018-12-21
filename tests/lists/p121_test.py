from python99.lists.p121 import insert_at, insert_at_mutable

def test_insert_at():
    assert insert_at([1, 2, 3, 4, 5, 6], 2, 'a') == [1, 'a', 2, 3, 4, 5, 6]
    assert insert_at([1, 2, 3, 4, 5, 6], 1, 'a') == ['a', 1, 2, 3, 4, 5, 6]
    assert insert_at([1, 2, 3, 4, 5, 6], 7, 'a') == [1, 2, 3, 4, 5, 6, 'a']

def test_insert_at_mutable():
    assert insert_at([1, 2, 3, 4, 5, 6], 2, 'a') == [1, 'a', 2, 3, 4, 5, 6]
    assert insert_at([1, 2, 3, 4, 5, 6], 1, 'a') == ['a', 1, 2, 3, 4, 5, 6]
    assert insert_at([1, 2, 3, 4, 5, 6], 7, 'a') == [1, 2, 3, 4, 5, 6, 'a']
