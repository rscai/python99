def isomorphic(ga, gb):
    gaNodes = ga[0]
    gaEdges = ga[1]
    gbNodes = gb[0]
    gbEdges = gb[1]
    if len(gaNodes) != len(gbNodes):
        return False
    funs = listAllFun(gaNodes, gbNodes)
    for fun in funs:
        if isIsomorphicFun(fun, gaEdges, gbEdges):
            return True
    return False


def listAllFun(gaNodes, gbNodes):
    if len(gaNodes) == 1:
        return [[(gaNodes[0], gbNodes[0])]]
    gaNode = gaNodes[0]
    gaRemainNodes = gaNodes[1:]
    return [[(gaNode, gbNode)] + remainFun for gbNode in gbNodes for remainFun in listAllFun(gaRemainNodes, listWithoutE(gbNodes, gbNode))]


def isIsomorphicFun(fun, gaEdges, gbEdges):
    funDict = {mapping[0]: mapping[1] for mapping in fun}
    for sourceNode, targetNode in funDict.items():
        sourceAdjacentNodes = adjacentNode(sourceNode, gaEdges)
        sourceMappedAdjacentNodes = [funDict[node] for node in sourceAdjacentNodes]
        actualTargetAdjacentNodes = adjacentNode(targetNode, gbEdges)
        if set(sourceMappedAdjacentNodes) != set(actualTargetAdjacentNodes):
            return False
    return True


def adjacentNode(node, edges):
    for edge in edges:
        if edge[0] == node:
            yield edge[1]
        if edge[1] == node:
            yield edge[0]


def listWithoutE(l, e):
    return [x for x in l if x != e]
