from functools import reduce
from operator import concat, add


def arc_to_graph(arcs):
    nodes = reduce(concat, [(lambda x:[x[0], x[1]])(e) for e in arcs], [])
    nodes = list(set(nodes))
    edges = arcs
    return (nodes, edges)


def adj_to_graph(adj):
    nodes = reduce(add, [[term[0]] for term in adj], [])
    edges = [(lambda term: [(term[0], otherNode)
                            for otherNode in term[1]])(term) for term in adj]
    edges = reduce(add, edges, [])
    edges = [(lambda edge: tuple(sorted(list(edge))))(edge) for edge in edges]
    edges = [x for i, x in enumerate(edges) if i == edges.index(x)]
    return (nodes, edges)


def graph_to_arc(graph):
    return graph[1]


def graph_to_adj(graph):
    nodes = graph[0]
    edges = graph[1]

    return [(node, adjacencyList(node, edges)) for node in nodes]


def adjacencyList(node, edges):
    nodes = []
    for edge in edges:
        if edge[0] == node:
            nodes.append(edge[1])
        elif edge[1] == node:
            nodes.append(edge[0])
    return nodes
