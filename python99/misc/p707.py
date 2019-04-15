from functools import reduce
from operator import concat, and_
import copy
import numpy as np

def sudoku(puzzle):
    squares = puzzleToSquares(puzzle)
    solutions = resolveSudoku(squares, [])
    return [squaresToPuzzle(solution) for solution in solutions]

def puzzleToSquares(puzzle):
    squares = []
    d = 3
    array = np.array(puzzle)
    for v in range(0, d):
        for h in range(0, d):
            squares.append((array[v*d:v*d+d,h*d:h*d+d]).tolist())
    return squares

def resolveSudoku(squares, solution):
    if len(squares) == 0:
        return [[]]
    square = squares[0]
    remainSquares = squares[1:]
    return [[squareSolution] + remain
            for squareSolution in resolveSquare(square)
            for remain in resolveSudoku(remainSquares, solution+[squareSolution])
            if isValid(solution + [squareSolution])]


def isValid(solutions):
    puzzleSolution = squaresToPuzzle(solutions)
    for row in puzzleSolution:
        nums = [num for num in row if num is not None]
        if len(nums) != len(set(nums)):
            return False
    for y in range(0, 9):
        nums = [puzzleSolution[x][y]
                for x in range(0, 9) if puzzleSolution[x][y] is not None]
        if len(nums) != len(set(nums)):
            return False
    return True


def squaresToPuzzle(squares):
    d = 3
    puzzle = [[None for h in range(0, 9)] for v in range(0, 9)]
    for i in range(0, len(squares)):
        hOffset = (i % d)*d
        vOffset = (i // d)*d
        square = squares[i]
        for v in range(0, len(square)):
            for h in range(0, len(square[v])):
                puzzle[vOffset+v][hOffset+h] = square[v][h]
    return puzzle


def resolveSquare(square):
    if isCompleted(square):
        return [square]
    nums = availableNums(square)
    return reduce(concat,
                  [resolveSquare(fill(square, num)) for num in nums],
                  [])


def isCompleted(square):
    return reduce(and_,
                  [(lambda x:x is not None)(e)
                   for e in reduce(concat, square, [])],
                  True)


def availableNums(square):
    all = [num for num in range(1, 10)]
    used = [num for num in reduce(concat, square, []) if num is not None]
    return [num for num in all if num not in used]


def fill(square, num):
    newSquare = copy.deepcopy(square)
    for v in range(0, len(newSquare)):
        for h in range(0, len(newSquare[v])):
            if newSquare[v][h] is None:
                newSquare[v][h] = num
                return newSquare
    return newSquare
