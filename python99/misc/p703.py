from python99.graph.p608 import traversal


def conjecture(g):
    nodes = g[0]
    edges = g[1]
    markedNodes = []
    remainNos = [no for no in range(1, len(nodes)+1)]
    markedNodes = doConjecture(nodes, edges, markedNodes, remainNos)
    return [markEdge((nodesWithNo, edges)) for nodesWithNo in markedNodes]

def doConjecture(nodes, edges, markedNodes, remainNos):
    if len(nodes) == 0:
        return [[]]
    v = nodes[0]
    remainNodes = nodes[1:]
    return [[(v,no)]+remain 
            for no in remainNos
            for remain in doConjecture(remainNodes, edges, markedNodes + [(v, no)], [remainNo for remainNo in remainNos if remainNo != no]) 
            if isValid(markedNodes+[(v, no)], edges)]


def isValid(markedNodes, edges):
    maxEdgeNo = len(edges)
    minEdgeNo = 1
    usedEdgeNos = set()
    nodeNoDict = {}
    for markedNode in markedNodes:
        nodeNoDict[markedNode[0]] = markedNode[1]
    for edge in edges:
        start = edge[0]
        end = edge[1]
        if start in nodeNoDict and end in nodeNoDict:
            diff = abs(nodeNoDict[start]-nodeNoDict[end])
            if diff < minEdgeNo or diff > maxEdgeNo:
                return False
            elif diff in usedEdgeNos:
                return False
            else:
                usedEdgeNos.add(diff)
    return True

def markEdge(g):
    nodeNoDict = {}
    for markedNode in g[0]:
        nodeNoDict[markedNode[0]] = markedNode[1]
    edges = g[1]
    markedEdges = []
    for edge in edges:
        start = edge[0]
        end = edge[1]
        diff = abs(nodeNoDict[start]-nodeNoDict[end])
        markedEdges.append((start,end,diff))
    return (g[0],markedEdges)
