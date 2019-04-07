def traversal(g, start):
    return doTraversal(g, start, [])


def doTraversal(g, start, accessedNodes):
    accessedNodes = accessedNodes + [start]
    nextNode = findNext(g, start, accessedNodes)
    while nextNode is not None:
        accessedNodes = doTraversal(g, nextNode, accessedNodes)
        nextNode = findNext(g, start, accessedNodes)
    return accessedNodes


def findNext(g, start, accessedNodes):
    adjacentNodes = adjacent(g, start)
    availableNodes = [
        node for node in adjacentNodes if node not in accessedNodes]
    if len(availableNodes) == 0:
        return None
    else:
        return availableNodes[0]


def adjacent(g, node):
    for edge in g[1]:
        if edge[0] == node:
            yield edge[1]
        if edge[1] == node:
            yield edge[0]
