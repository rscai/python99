from python99.graph.p607 import degree


def gen_regular(k, n):
    if k*n % 2 != 0:
        return []
    nodes = [e for e in range(1, n+1)]
    allEdges = genEdges(nodes)
    edgeCombinations = combination(allEdges, k*n/2)
    return [(nodes, edges) for edges in edgeCombinations if isRegular((nodes, edges), k)]


def genEdges(nodes):
    if len(nodes) == 2:
        return [(nodes[0], nodes[1])]
    head = nodes[0]
    remain = nodes[1:]
    edges = [(head, end) for end in remain]
    return edges + genEdges(remain)


def combination(l, n):
    if len(l) == n:
        return [l]
    if n == 1:
        return [[e] for e in l]
    if n == 0:
        return []
    return [[head] + remain for head in l for remain in combination(l[l.index(head)+1:], n-1)]


def isRegular(g, k):
    nodes = g[0]
    for node in nodes:
        if degree(g, node) != k:
            return False
    return True
