from python99.graph.p601 import arc_to_graph, adj_to_graph, graph_to_arc, graph_to_adj


def test_arc_to_graph():
    result = arc_to_graph(
        [('b', 'c'), ('b', 'f'), ('c', 'f'), ('f', 'k'), ('g', 'h')])
    assert len(result) == 2
    assert set(result[0]) == set(['b', 'c', 'f', 'c', 'k', 'g', 'h'])
    assert result[1] == [('b', 'c'), ('b', 'f'),
                         ('c', 'f'), ('f', 'k'), ('g', 'h')]


def test_adj_to_graph():
    result = adj_to_graph([('b', ['c', 'f']), ('c', ['b', 'f']), ('d', []), ('f', [
                          'b', 'c', 'k']), ('g', ['h']), ('h', ['g']), ('k', ['f'])])
    assert len(result) == 2
    assert set(result[0]) == set(['b', 'c', 'd', 'f', 'g', 'h', 'k'])
    assert result[1] == [('b', 'c'), ('b', 'f'),
                         ('c', 'f'), ('f', 'k'), ('g', 'h')]


def test_graph_to_arc():
    assert graph_to_arc((['b', 'c', 'd', 'f', 'k', 'g', 'h'], [('b', 'c'), ('b', 'f'), ('c', 'f'), ('f', 'k'), ('g', 'h')])) == [
        ('b', 'c'), ('b', 'f'), ('c', 'f'), ('f', 'k'), ('g', 'h')]


def test_graph_to_adj():
    assert graph_to_adj((['b', 'c', 'd', 'f', 'k', 'g', 'h'], [('b', 'c'), ('b', 'f'), ('c', 'f'), ('f', 'k'), ('g', 'h')])) == [('b', ['c', 'f']), ('c', ['b', 'f']), ('d', []), ('f', [
        'b', 'c', 'k']), ('k', ['f']), ('g', ['h']), ('h', ['g'])]
