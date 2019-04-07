from sys import maxsize
from functools import reduce
from operator import add

# return tree, sumOfWeight


def ms_tree(g):
    nodes = g[0]
    initTree = ([nodes[0]], [])
    _, msTree = constructMsTree(g, initTree)
    return msTree, reduce(add, [edge[2] for edge in msTree[1]], 0)


def constructMsTree(remainG, tree):
    nodes = remainG[0]
    remainEdges = remainG[1]
    newNodes = tree[0]
    newEdges = tree[1]
    if set(newNodes) == set(nodes):
        return remainG, tree
    minEdge = (None, None, maxsize)
    newNode = None
    for edge in remainEdges:
        if edge[0] in newNodes and edge[1] not in newNodes and edge[2] < minEdge[2]:
            minEdge = edge
            newNode = edge[1]
        if edge[1] in newNodes and edge[0] not in newNodes and edge[2] < minEdge[2]:
            minEdge = edge
            newNode = edge[0]
    return constructMsTree((nodes, [edge for edge in remainEdges if edge != minEdge]), ([newNode]+newNodes, [minEdge]+newEdges))
