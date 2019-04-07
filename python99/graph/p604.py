from functools import reduce
from operator import add


def s_tree(graph):
    nodes = graph[0]
    edges = graph[1]
    minEdgeNum = len(nodes) - 1
    combinations = combination(edges, minEdgeNum)
    return [comb for comb in combinations if is_connected((nodes, comb))]


def combination(l, n):
    if len(l) == n:
        return [l]
    if n == 1:
        return [[e] for e in l]
    elements = l.copy()
    return [[e] + remain for e in elements for remain in combination(l[l.index(e)+1:], n-1)]


def is_connected(graph):
    nodes = graph[0]
    edges = graph[1]
    return len(edges) >= len(nodes) - 1 and set(nodes) == set(reduce(add, [[edge[0], edge[1]] for edge in edges], []))


def is_tree(graph):
    nodes = graph[0]
    edges = graph[1]
    return len(edges) == len(nodes) - 1 and set(nodes) == set(reduce(add, [[edge[0], edge[1]] for edge in edges], []))
