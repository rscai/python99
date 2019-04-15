def knight_tour(n):
    return [[(1, 1)]+path for path in doTour(n, n*n-1, (1, 1), [(1, 1)])]


def doTour(n, m, start, path):
    if m == 0:
        return [[]]
    availableMoves = getAvailableMoves(n, path, start)
    return [[moveTo(start, move)]+remainPath
            for move in availableMoves
            for remainPath in doTour(n, m-1, moveTo(start, move), path+[moveTo(start, move)])]


def moveTo(start, move):
    return (start[0]+move[0], start[1]+move[1])


def getAvailableMoves(n, path, start):
    moveRules = [
        (2, 1),
        (1, 2),
        (-1, 2),
        (-2, 1),
        (-2, -1),
        (-1, -2),
        (1, -2),
        (2, -1)
    ]
    for move in moveRules:
        newPos = moveTo(start, move)
        if newPos[0] > 0 and newPos[0] <= n and newPos[1] > 0 and newPos[1] <= n and newPos not in path:
            yield move
