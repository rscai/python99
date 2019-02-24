from python99.logic_codes.p302 import evaluate, buildTreeFrom, postOrderTraversal, tokenize,table


def test_table():
    assert table([True, False], [True, False], 'A and B') == [
        (True, True, True),
        (True, False, False),
        (False, True, False),
        (False, False, False)
    ]
    assert table([True, False], [True, False], 'A and (A or not B)') == [
        (True, True, True),
        (True, False, True),
        (False, True, False),
        (False, False, False)
    ]


def test_evaluate():
    assert evaluate([True, 'not']) == False
    assert evaluate([False, 'not', True, 'or', False, 'and']) == False
    assert evaluate([False, False, True, 'not', 'or', 'and']) == False


def test_buildTreeFrom():
    treeA = buildTreeFrom(['A', 'and', 'B'])
    assert treeA is not None
    assert treeA.value[0] == 'and'
    assert len(treeA._children) == 2
    assert treeA._children[0].value[0] == 'A'
    assert treeA._children[1].value[0] == 'B'

    treeB = buildTreeFrom(['A', 'and', '(', 'A', 'or', 'not', 'B', ')'])
    assert treeB is not None
    assert treeB.value[0] == 'and'
    assert len(treeB._children) == 2
    assert treeB._children[0].value[0] == 'A'
    assert treeB._children[1].value[0] == 'or'
    assert len(treeB._children[1]._children) == 2
    assert treeB._children[1]._children[0].value[0] == 'A'
    assert treeB._children[1]._children[1].value[0] == 'not'
    assert len(treeB._children[1]._children[1]._children) == 1
    assert treeB._children[1]._children[1]._children[0].value[0] == 'B'


def test_postOrderTraversal():
    assert postOrderTraversal(buildTreeFrom(['A', 'and', 'B'])) == [
        'A', 'B', 'and']
    assert postOrderTraversal(buildTreeFrom(['A', 'and', '(', 'A', 'or', 'not', 'B', ')'])) == [
        'A', 'A', 'B', 'not', 'or', 'and']


def test_tokenize():
    assert tokenize('A and B') == ['A', 'and', 'B']
    assert tokenize('A and (A or not B)') == [
        'A', 'and', '(', 'A', 'or', 'not', 'B', ')']
