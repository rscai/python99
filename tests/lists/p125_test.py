from python99.lists.p125 import rnd_permu


def test_rnd_permu():
    l = [e for e in range(1, 11)]
    actual = rnd_permu(l)
    assert len(actual) == len(l)
    assert set(actual) == set(l)
