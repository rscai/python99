from python99.graph.p609 import connected_components


def is_bipartite(g):
    components = connected_components(g)
    nodeColorDicts = [binaryColoring(component) for component in components]
    allNodeColors = mergeDicts(nodeColorDicts)
    for edge in g[1]:
        startColor = allNodeColors[edge[0]]
        endColor = allNodeColors[edge[1]]
        if startColor == endColor:
            return False
    return True


def binaryColoring(component):
    nodes = component[0]
    start = nodes[0]
    coloredNodes = {}
    _, coloredNodes = binaryColoringTree(
        component, start, True, set(), coloredNodes)
    return coloredNodes


def binaryColoringTree(t, start, color, accessedNodes, coloredNodes):
    coloredNodes[start] = color
    accessedNodes.add(start)
    linkedNodes = set(getLinkedNodes(start, t))
    childNodes = linkedNodes - accessedNodes
    for node in childNodes:
        accessedNodes, coloredNodes = binaryColoringTree(
            t, node, not color, accessedNodes, coloredNodes)
    return accessedNodes, coloredNodes


def getLinkedNodes(node, graph):
    edges = graph[1]
    for edge in edges:
        if edge[0] == node:
            yield edge[1]
        if edge[1] == node:
            yield edge[0]


def mergeDicts(dicts):
    mergedDict = {}
    for dict in dicts:
        for k, v in dict.items():
            mergedDict[k] = v
    return mergedDict
