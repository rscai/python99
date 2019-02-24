from python99.logic_codes.p303 import table


def test_table():
    assert table({'A': [True, False], 'B': [True, False], 'C': [True, False]}, 'A and B or C') == [
        (True, True, True, True),
        (True, True, False, True),
        (True, False, True, True),
        (True, False, False, False),
        (False, True, True, True),
        (False, True, False, False),
        (False, False, True, True),
        (False, False, False, False)
    ]
