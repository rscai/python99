def nonograms(rowBitmaps, columnBitmaps):
    rowCount = len(rowBitmaps)
    columnCount = len(columnBitmaps)
    count = rowCount * columnCount
    return resolveNonograms(count, [], rowBitmaps, columnBitmaps)


def resolveNonograms(n, solution, rowBitmaps, columnBitmaps):
    if n == 0:
        return [[]]
    result = [[mark]+remain
            for mark in [True, False]
            for remain in resolveNonograms(n-1, solution + [mark], rowBitmaps, columnBitmaps)
            if isNotViolate(solution+[mark], rowBitmaps, columnBitmaps)]
    return result


def isNotViolate(partialSolution, rowBitmaps, columnBitmaps):
    nRow = len(rowBitmaps)
    nCol = len(columnBitmaps)
    for rowIndex, bitmaps in enumerate(rowBitmaps):
        if len(partialSolution) >= (rowIndex+1) * nCol:
            if bitmaps != countBitmaps(partialSolution[rowIndex*nCol:(rowIndex+1)*nCol]):
                return False
    for columnIndex, bitmaps in enumerate(columnBitmaps):
        cellOfColumn = []
        for index, value in enumerate(partialSolution):
            if index % nRow == columnIndex:
                cellOfColumn.append(value)
        if len(partialSolution) >= (nRow-1)*nCol +columnIndex +1:
            if bitmaps != countBitmaps(cellOfColumn):
                return False
    return True


def countBitmaps(l):
    trueCount = 0
    bitmaps = []
    for v in l:
        if v is False and trueCount != 0:
            bitmaps.append(trueCount)
            trueCount = 0
        if v is True:
            trueCount = trueCount + 1
    if trueCount != 0:
        bitmaps.append(trueCount)
    return bitmaps
