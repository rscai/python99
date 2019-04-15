def crossword(puzzle, width, height, words):
    solutions = doCrossword(puzzle, [], words)
    filledSolutions = []
    for solution in solutions:
        table = [[' ' for h in range(0, width)] for v in range(0, height)]
        for wordSolution in solution:
            for index, pos in enumerate(wordSolution[0]):
                letter = wordSolution[1][index]
                table[pos//width][pos%width] = letter
        filledSolutions.append(table)
    return filledSolutions


def doCrossword(puzzle, solution, words):
    if len(puzzle) == 0:
        return [[]]
    firstPuzzle = puzzle[0]
    remainPuzzle = puzzle[1:]
    availableWords = [word for word in words if len(word) == len(firstPuzzle)]
    return [[(firstPuzzle, word)] + remain
            for word in availableWords
            for remain in doCrossword(remainPuzzle,
                                      solution + [(firstPuzzle, word)],
                                      [e for e in words if e != word])
            if isNotViolate(solution + [(firstPuzzle, word)])]


def isNotViolate(solution):
    filledDict = {}
    for fill in solution:
        puzzle = fill[0]
        word = fill[1]
        for index, pos in enumerate(puzzle):
            letter = word[index]
            if pos in filledDict and filledDict[pos] != letter:
                return False
            filledDict[pos] = letter
    return True
