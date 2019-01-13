from python99.logic_codes.p301 import table, and_, or_, nand, nor, xor, impl, equ


def test_table():
    la = [True, False]
    lb = [True, False]
    assert table(la, lb, lambda a, b: and_(a, b)) == [
        (True, True, True),
        (True, False, False),
        (False, True, False),
        (False, False, False)
    ]
    assert table(la, lb, lambda a, b: or_(a, b)) == [
        (True, True, True),
        (True, False, True),
        (False, True, True),
        (False, False, False)
    ]
    assert table(la, lb, lambda a, b: nand(a, b)) == [
        (True, True, False),
        (True, False, True),
        (False, True, True),
        (False, False, True)
    ]
    assert table(la, lb, lambda a, b: xor(a, b)) == [
        (True, True, False),
        (True, False, True),
        (False, True, True),
        (False, False, False)
    ]
    assert table(la, lb, lambda a, b: nor(a, b)) == [
        (True, True, False),
        (True, False, False),
        (False, True, False),
        (False, False, True)
    ]
    assert table(la, lb, lambda a, b: impl(a, b)) == [
        (True, True, True),
        (True, False, False),
        (False, True, True),
        (False, False, True)
    ]
    assert table(la, lb, lambda a, b: equ(a, b)) == [
        (True, True, True),
        (True, False, False),
        (False, True, False),
        (False, False, True)
    ]
    assert table(la, lb, lambda a, b: nand(and_(a, b), or_(a, b))) == [
        (True, True, False),
        (True, False, True),
        (False, True, True),
        (False, False, True)
    ]
