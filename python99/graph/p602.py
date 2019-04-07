def path(g, start, end):
    paths = listPath(g, [start], start, end)
    return [[start] + e for e in paths]


def listPath(g, path, current, end):
    # it reach destination when current node is end one
    if current == end:
        return [[]]
    nodes = nextNodes(g, path, current)
    return [[nextNode]+remainPath for nextNode in nodes for remainPath in listPath(g, path+[nextNode], nextNode, end)]


def nextNodes(g, path, start):
    for edge in g[1]:
        if edge[0] == start and edge[1] not in path:
            yield edge[1]
        elif edge[1] == start and edge[0] not in path:
            yield edge[0]
