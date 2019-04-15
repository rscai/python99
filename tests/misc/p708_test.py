from python99.misc.p708 import nonograms, isNotViolate

def test_nonograms():
    assert nonograms([
        [1],
        [1]
    ],[
        [1],
        [1]
    ]) == [
        [
            True, False, 
            False, True
        ], [
            False, True, 
            True, False
        ]
    ]
    assert nonograms([
        [3],
        [2,1],
        [3],
        [2]
    ],[
        [1],
        [3],
        [1,2],
        [4]
    ]) == [
        [
            False,True,True,True,
            True,True,False,True,
            False,True,True,True,
            False,False,True,True
        ]
    ]

def test_isNotViolate():
    assert isNotViolate([
        False,True,
        True,False
    ], [
        [1],
        [1]
    ],[
        [1],
        [1]
    ]) == True