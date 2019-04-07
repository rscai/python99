from python99.graph.p608 import traversal


def connected_components(g):
    nodes = g[0]
    connectedNodeSets = [set(traversal(g, node)) for node in nodes]
    uniqueConnectedNodeSets = []
    for nodeSet in connectedNodeSets:
        if nodeSet not in uniqueConnectedNodeSets:
            uniqueConnectedNodeSets.append(nodeSet)
    return [(list(nodeSet), linkedEdges(g, list(nodeSet))) for nodeSet in uniqueConnectedNodeSets]


def linkedEdges(g, nodes):
    allEdges = g[1]
    edges = []
    for edge in allEdges:
        if edge[0] in nodes or edge[1] in nodes:
            edges.append(edge)
    return edges