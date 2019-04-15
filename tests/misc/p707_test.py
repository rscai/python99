from python99.misc.p707 import sudoku, resolveSquare, puzzleToSquares, squaresToPuzzle
from functools import reduce
from operator import concat
import pytest

#@pytest.mark.skip(reason="it is very slow")
def test_puzzle():
    assert sudoku([
        [None, None, 4, 8, None, None, None, 1, 7],
        [6, 7, None, 9, None, None, None, 5, None],
        [5, None, 8, None, 3, 7, 9, None, 4],
        [3, 2, 5, 7, 4, 8, 1, 6, 9],
        [4, 6, 9, 1, 5, None, 7, 8, 2],
        [None, 8, 1, 2, 6, 9, None, 3, 5],
        [1, 9, 7, 5, 8, None, 3, 4, 6],
        [8, 5, 3, 4, 7, 6, 2, 9, 1],
        [2, 4, None, 3, 9, 1, 5, None, 8]
    ]) == [
        [
            [9, 3, 4, 8, 2, 5, 6, 1, 7],
            [6, 7, 2, 9, 1, 4, 8, 5, 3],
            [5, 1, 8, 6, 3, 7, 9, 2, 4],
            [3, 2, 5, 7, 4, 8, 1, 6, 9],
            [4, 6, 9, 1, 5, 3, 7, 8, 2],
            [7, 8, 1, 2, 6, 9, 4, 3, 5],
            [1, 9, 7, 5, 8, 2, 3, 4, 6],
            [8, 5, 3, 4, 7, 6, 2, 9, 1],
            [2, 4, 6, 3, 9, 1, 5, 7, 8]
        ]
    ]


def test_resolveSquare():
    result = resolveSquare([
        [3, None, 6],
        [None, 7, 1],
        [5, None, 8]
    ])
    assert len(result) == 6
    for solution in result:
        assert set(reduce(concat, solution, [])) == set(
            [num for num in range(1, 10)])
