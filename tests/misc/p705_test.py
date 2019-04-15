from python99.misc.p705 import full_word


def test_full_word():
    assert full_word(175) == 'one-seven-five'
    assert full_word(1230) == 'one-two-three-zero'
