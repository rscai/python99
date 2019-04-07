def degree(g, node):
    d = 0
    for edge in g[1]:
        if edge[0] == node:
            d = d+1
        if edge[1] == node:
            d = d+1
    return d


def orderNodeByDegreeDesc(g):
    nodes = g[0]
    nodesWithDegree = [(node, degree(g, node)) for node in nodes]
    return [e[0] for e in sorted(nodesWithDegree, key=lambda x:x, reverse=True)]


def coloring(g):
    nodesOrderByDegree = orderNodeByDegreeDesc(g)
    # color represent in int, start from 1
    usedColors = []
    nodeWithColors = {}
    edges = g[1]
    for node in nodesOrderByDegree:
        nodeWithColors, usedColors = doColor(
            nodeWithColors, usedColors, edges, node)
    nodes = [(node, nodeWithColors[node]) for node in g[0]]
    return (nodes, g[1])


def doColor(nodeWithColors, usedColors, edges, node):
    adjacentNodes = adjacent(node, edges)
    adjacentColors = [nodeWithColors[node]
                      for node in adjacentNodes if node in nodeWithColors]
    availableColors = list(set(usedColors)-set(adjacentColors))
    newColor = 1
    if len(availableColors) > 0:
        newColor = availableColors[0]
    elif len(usedColors) > 0:
        newColor = usedColors[-1]+1
        usedColors.append(newColor)
    else:
        newColor = 1
        usedColors.append(newColor)
    nodeWithColors[node] = newColor
    return nodeWithColors, usedColors


def adjacent(node, edges):
    for edge in edges:
        if edge[0] == node:
            yield edge[1]
        if edge[1] == node:
            yield edge[0]
