from python99.arithmetic.p209 import totient_phi

def test_totient_phi():
    assert totient_phi(10) == 4
    assert totient_phi(10090) == 4032