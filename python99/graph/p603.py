def cycle(g, start):
    cycles = listPath(g, [start], start, start)
    return [[start] + e for e in cycles]


def listPath(g, path, current, end):
    # it reach destination when current node is end one
    if current == end and len(path) > 1:
        return [[]]
    nodes = nextNodes(g, path, current)
    return [[nextNode]+remainPath 
                for nextNode in nodes 
                for remainPath in listPath(g, path+[nextNode], nextNode, end)]


def nextNodes(g, path, start):
    for edge in g[1]:
        if edge[0] == start and edge[1] not in path[1:]:
            yield edge[1]
        elif edge[1] == start and edge[0] not in path[1:]:
            yield edge[0]
