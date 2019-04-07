from python99.graph.p611 import gen_regular


def test_gen_regular():
    assert gen_regular(2, 3) == [
        ([1, 2, 3], [(1, 2), (1, 3), (2, 3)])
    ]
    assert gen_regular(2, 4) == [
        ([1, 2, 3, 4], [(1, 2), (1, 3), (2, 4), (3, 4)]),
        ([1, 2, 3, 4], [(1, 2), (1, 4), (2, 3), (3, 4)]),
        ([1, 2, 3, 4], [(1, 3), (1, 4), (2, 3), (2, 4)])
    ]
    assert len(gen_regular(3, 6)) == 70
