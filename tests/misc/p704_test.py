from python99.misc.p704 import puzzle

def test_puzzel():
    assert puzzle([2,3,5,7,11])==[
        '2==3-5-7+11',
        '2==(3*5+7)/11',
        '2*(3-5)==7-11',
        '2-3+5+7==11']