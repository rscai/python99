from python99.misc.p701 import eight_queens


def test_eight_queens():
    result = eight_queens()
    assert len(result) == 92
