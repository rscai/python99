# Truth tables for logical expressions


def table(la, lb, expr):
    return [(a, b, expr(a, b)) for a in la for b in lb]


def and_(a, b):
    return a and b


def or_(a, b):
    return a or b


def nand(a, b):
    return not (a and b)


def nor(a, b):
    return not (a or b)


def xor(a, b):
    return nand(nand(a, nand(a, b)), nand(b, nand(a, b)))


def impl(a, b):
    return (not a) or b


def equ(a, b):
    return a == b
