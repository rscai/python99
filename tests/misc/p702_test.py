from python99.misc.p702 import knight_tour


def test_knight_tour():
    n = 5
    paths = knight_tour(n)
    for index, path in enumerate(paths, start=1):
        print(index, 'path:')
        printPath(path, n)
    assert len(paths) == 304


def printPath(path, n):
    chess = [[0 for x in range(0, n)] for y in range(0, n)]
    for index, value in enumerate(path, start=1):
        # path is 1-based, list is 0-based
        x = value[0]-1
        y = value[1]-1
        chess[y][x] = index
    for row in chess:
        print(row)
