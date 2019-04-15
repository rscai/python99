from python99.misc.p706 import identifier


def test_identifier():
    assert identifier('abc') == True
    assert identifier('ab-12') == True
    assert identifier('ab-') == False
    assert identifier('-ab12') == False
